import config
from cake_schema import CakeSchema
from transform.transform_model import TransformModel
from transform.transform_processing import TransformProcessing
from flask import Flask, jsonify, request
from marshmallow import ValidationError
import pandas as pd


app = Flask(__name__)
schema = CakeSchema()
transform = TransformProcessing(config)
model = TransformModel(config)


@app.route('/predict', methods=['POST'])
def predict():
   request_data = request.json


   try:
       # Validate request body against schema data types
       request_body = schema.load(request_data)
   except ValidationError as err:
       # Return a nice message if validation fails
       return jsonify(err.messages), 400


   dataset = pd.DataFrame([[
                            request_body['Layers'],
                            request_body['Topping'],
                            request_body['Price']]], columns=config.MODEL_COLUMNS)


   # transform
   dataset_transform = transform.transform(dataset)


   # predict
   result = model.predict(dataset_transform)


   # post processing
   result_value = int(result[0])


   return jsonify({"predict_result": result_value}, 200)




if __name__ == '__main__':
   app.run(port=8000)
