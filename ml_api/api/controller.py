from flask import Blueprint, request

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return 'ok'

@prediction_app.route('/v1/predict', methods=['POST'])
def predict():
    
