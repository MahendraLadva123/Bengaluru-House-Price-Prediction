from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

data = pd.read_csv("cleaned_data.csv")

with open("model1.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET"])  
def home():
    locations = sorted(data["location"].unique())
    return render_template("index.html", locations=locations)

@app.route("/predict", methods=["POST"])  # ✅ Ensure POST is explicitly allowed
def predict():
    try:
        location = request.form["location"]
        total_sqft = float(request.form["total_sqft"])
        bath = int(request.form["bath"])
        bhk = int(request.form["bhk"])

        new_data = pd.DataFrame([[location, total_sqft, bath, bhk]], 
                                columns=["location", "total_sqft", "bath", "bhk"])

        prediction = model.predict(new_data)[0]

        return render_template("index.html", locations=sorted(data["location"].unique()),
                               prediction_text=f"Predicted Price: ₹{round(prediction, 2)}")

    except Exception as e:
        return render_template("index.html", locations=sorted(data["location"].unique()),
                               prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
