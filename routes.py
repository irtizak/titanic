from flask import Flask, render_template
import joblib

app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')

@app.route("/predict"):
def predict():
    model = joblib.load('model/model.joblib')
    return model.predict()

if __name__ == '__main__':
    app.run(debug=True)
