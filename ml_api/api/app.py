# Flask Extensions
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

# pydata stack
import numpy as np
import joblib

# set up Flask and Flask-Restful
app = Flask(__name__)
api = Api(app)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('pclass', type=float)
parser.add_argument('age', type=float)
# parser.add_argument('petal_length', type=float)
# parser.add_argument('petal_width', type=float)


class TitanicPredict(Resource):
    def get(self):
        # parse arguments
        args = parser.parse_args()
        pclass = args['pclass']
        age = args['age']
        # petal_length = args['petal_length']
        # petal_width = args['petal_width']

        # create numpy ndarray
        pt_to_predict = np.array([[
            pclass,
            age
            # petal_length,
            # petal_width
        ]])

        # load model and predict
        model = joblib.load('model/model.joblib')
        predicted_class = model.predict(pt_to_predict)

        # return answer
        prediction = {
            'predicted_class': predicted_class.tolist()
        }
        result = {'data': dict(prediction)}
        return jsonify(result)


# create endpoint
api.add_resource(TitanicPredict, '/predict/titanic/')


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port='5000',
    )
