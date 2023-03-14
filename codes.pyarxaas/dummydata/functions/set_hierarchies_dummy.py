#imported all the neccessary libraries
import pyarxaas
from pyarxaas import ARXaaS, Dataset
from pyarxaas import AttributeType
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder, RedactionHierarchyBuilder
from pyarxaas.privacy_models import KAnonymity
import pandas as pd
import pickle
#making a function that takes in the dataframe as input and also has the choice of generating the risk profile
def set_hierarchy(data=pd.DataFrame, risk_profile=False):
    #files which contain the csv files to the hierarchy, they contain the local path for now but will add the global path once it is figured out
    hierarchy_files = {
        "Name": "/home/shreshtha/Hiearchies/namehier.csv",
        "Age": "/home/shreshtha/Hiearchies/agehier.csv",
        "Email": "/home/shreshtha/Hiearchies/emailhier.csv",
        "Gender": "/home/shreshtha/Hiearchies/gender.csv",
        "zipcode": "/home/shreshtha/Hiearchies/zipcode.csv",
        "Amount_spent": "/home/shreshtha/Hiearchies/amounthier.csv"
    }
    #instead of reading through the csv files again and again, this code turns them into pickle objects hence making sure that the code os faster
    #also added exception handling to check for missing or unavailable files
    hierarchy_data = {}
    for column, file in hierarchy_files.items():
        try:
            with open(f"{column.lower()}_hier.pkl", "rb") as f:
                hierarchy_data[column] = pickle.load(f)
        except FileNotFoundError:
            hierarchy_data[column] = pd.read_csv(file)
            with open(f"{column.lower()}_hier.pkl", "wb") as f:
                pickle.dump(hierarchy_data[column], f)
#creating a dataset object from the dataframe
    dataset = Dataset.from_pandas(data)
    #setting up the local arx instance
    arxaas = ARXaaS("http://localhost:8080/")
    #setting up the attribute types
    dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, "Age", "Email", "zipcode", "Amount_spent", "Gender", "Name")
    #also prints the risk profile if the risk profile is true
    #raising an error to check for the columns in the data, this can be done because the columns  here are defined already
    for column in ["Name", "Age", "Email", "Gender", "zipcode", "Amount_spent"]:
        if column not in data.columns:
            raise ValueError(f"{column} column not found in data")
            #setting the hierarchy for the dataset
        dataset.set_hierarchy(column, hierarchy_data[column])
        
    return dataset
