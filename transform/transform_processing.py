import pickle
import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

class TransformProcessing():
    def __init__(self, config):
        self.config = config
        # load encoder
        with open('extract/OneHotEncoder.pkl', 'rb') as file:
            self.oht = pickle.load(file)

    def __validation(self,dataset):
        pass


    def transform(self, dataset):
        self.__validation(dataset)

        # Separate features and target
        #dataset.columns = dataset.columns.str.strip()

        # # load encoder
        # with open('extract/OneHotEncoder.pkl', 'rb') as file:
        #     oht = pickle.load(file)


        one_hot_encoded = self.oht.transform(dataset[['Topping']])

        # Convert encoded result to DataFrame, reset indices
        one_hot_df = pd.DataFrame(one_hot_encoded,
            columns=self.oht.get_feature_names_out(),
            index=dataset.index  # explicitly set the same index as original dataset
        )

        # Concatenate dataframes (indices now match)
        X = pd.concat([dataset.drop('Topping', axis=1), one_hot_df], axis=1)

        # Identify numeric columns explicitly
        numeric_cols = X.select_dtypes(include=[np.number]).columns
        non_numeric_cols = X.select_dtypes(exclude=[np.number]).columns

        # Impute numeric columns only
        imputer = SimpleImputer(strategy='mean')

        X_numeric_imputed = pd.DataFrame(
            imputer.fit_transform(X[numeric_cols]),
            columns=numeric_cols,
            index=X.index
        )

        # Concatenate back non-numeric columns (if any)
        X_imputed = pd.concat([X_numeric_imputed, X[non_numeric_cols]], axis=1)

        return X_imputed
