import pickle
import json
import config
import numpy as np

class Estate():
    def __init__(self, X1_transaction_date, X2_house_age, X3_distance_to_the_nearest_MRT_station, X4_number_of_convenience_stores, X5_latitude, X6_longitude):
        self.X1_transaction_date = X1_transaction_date
        self.X2_house_age = X2_house_age
        self.X3_distance_to_the_nearest_MRT_station = X3_distance_to_the_nearest_MRT_station
        self.X4_number_of_convenience_stores = X4_number_of_convenience_stores
        self.X5_latitude = X5_latitude
        self.X6_longitude = X6_longitude

    def __load_model(self):

        with open(config.KNN_REG_FILE_PATH, "rb") as f:
            self.knn_reg = pickle.load(f)
            print("KNN Reg ::",self.knn_reg)

        with open(config.NORMALIZED_FILE_PATH, "rb") as f:
            self.normal_scaler = pickle.load(f)


        with open(config.JSON_FILE_PATH, "r") as f:
            self.project_data = json.load(f)
            print("Project Data :: ",self.project_data)

    def get_price_prediction(self):
        self.__load_model()
        test_array = np.zeros((1,self.knn_reg.n_features_in_))
        test_array[0][0] = self.X1_transaction_date
        test_array[0][1] = self.X2_house_age
        test_array[0][2] = self.X3_distance_to_the_nearest_MRT_station
        test_array[0][3] = self.X4_number_of_convenience_stores
        test_array[0][4] = self.X5_latitude
        test_array[0][5] = self.X6_longitude

        print("Test Array",test_array)
        scaled_test_array = self.normal_scaler.transform(test_array)

        price_pred = np.around(self.knn_reg.predict(scaled_test_array)[0],3)
        print("Price of house ::",price_pred)
        return price_pred
