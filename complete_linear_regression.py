import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class dataset_analysis():
     def __init__(self, df):
         self.df = df
     def load_data(self):
         loaded_data = pd.read_csv(self.df)
         return dataset_analysis.feature_target_extraction(loaded_data)
     
     def feature_target_extraction(loaded_data):
         binary_cols = [i for i in loaded_data.columns if loaded_data[i].nunique() == 2]
         if binary_cols == []:
            pass
         else:
            return'This must be a logistic regression problem as the target is holding binary values'
         target_value = loaded_data.columns[-1]
         feature_values = loaded_data.columns[:-1]
         return target_value, feature_values
         
     
     def feature_selection():
         pass 
     
     
     def target_feature_corelation():
         pass 
     
     def overall_validation():
         pass
     
     def pass_on():
         pass
     
class Model_implementation():
     def __init__():
        pass
    
     def training():
        pass
    
     def prediction():
        pass
    
     def Z_score_validation():
         pass
     
     def overall_validation():
         pass
     
     def pass_on():
         pass
        
class Plot_mechanics():
     def __init__(self):
         pass
     def Linear_Regression_plot(self):
         pass
     
analysis = dataset_analysis("D:/DS/CSV_files/Advertising.csv")
print(analysis.load_data())