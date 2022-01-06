import os
import pandas as pd
import xgboost as xgb
import pickle
from flask import Flask, request, Response
from rossmann.Rossmann import Rossmann
from xgboost import Booster, XGBRegressor


# loading model
model = pickle.load( open('model/model_rossmann_xgb142.pkl', 'rb' ) )
# model = xgb.XGBRegressor()
# model.load_model('model/model_rossmann_xgb142.json')


# initialize API
app = Flask(__name__)

@app.route( '/rossmann/predict', methods=['POST'] )
def rossmann_predict():
    test_json = request.get_json()
    
    if test_json: # there is data
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else: # multiple example
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
        
        # Instantiate Rossmann Class
        pipeline = Rossmann()
        
        # Data Cleaning
        df1 = pipeline.data_cleaning( test_raw )
        
        # Feature Engineering
        df2 = pipeline.feature_engineering( df1 )
        
        # Data Preparation
        df3 = pipeline.data_preparation( df2 )
        
        # Prediction
        df_response = pipeline.get_prediction( model, test_raw, df3 )
        
        return df_response
        
    else:
        return Response( '{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    port = int( os.environ.get('PORT', 5000) )
    app.run('0.0.0.0', port=port, debug=True)
