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

        #print(f"dataset = {dataset}")
        one_hot_encoded = self.oht.transform(dataset[['Topping']])

        # Convert encoded result to DataFrame, reset indices
        one_hot_df = pd.DataFrame(one_hot_encoded,
            columns=self.oht.get_feature_names_out(),
            index=dataset.index  # explicitly set the same index as original dataset
        )

        # drop column price if exists
        dataset_features = dataset.drop(columns=['Price'], errors='ignore')
        #print(f"dataset_features = {dataset_features}")


        # If the index is numeric and default (0,1,2,3...), drop it:
        #dataset_new_index = dataset_features.reset_index(drop=False)
        if dataset_features.index.equals(pd.RangeIndex(len(dataset_features))):
            dataset_new_index = dataset_features.reset_index(drop=True)
        else:
            dataset_new_index = dataset_features.reset_index(drop=False)

        #print(f"dataset_new_index = {dataset_new_index}")

        # Concatenate dataframes (indices now match)
        one_hot_df = one_hot_df.reset_index(drop=True)

        X = pd.concat([dataset_new_index.drop('Topping', axis=1), one_hot_df], axis=1)
        #print(f"X.columns = {X.columns}")

        # # Identify numeric columns explicitly
        # numeric_cols = X.select_dtypes(include=[np.number]).columns
        # non_numeric_cols = X.select_dtypes(exclude=[np.number]).columns
        #
        # # Impute numeric columns only
        # imputer = SimpleImputer(strategy='mean')
        #
        # X_numeric_imputed = pd.DataFrame(
        #     imputer.fit_transform(X[numeric_cols]),
        #     columns=numeric_cols,
        #     index=X.index
        # )
        #
        # # Concatenate back non-numeric columns (if any)
        # X_imputed = pd.concat([X_numeric_imputed, X[non_numeric_cols]], axis=1)

        return X #X_imputed
