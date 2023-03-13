#this function sets the hierarchy for the datasetto get it ready for the anonymization
#load the data and the neccesary libraries
#we will start by importing the neccesarry libraries
import pyarxaas
from pyarxaas import ARXaaS
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder,RedactionHierarchyBuilder
from pyarxaas import AttributeType
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import Dataset
import pandas as pd
import pandas as pd
import pickle
from pandas.api.types import CategoricalDtype

def set_hierarchy(data=pd.DataFrame):
    # Check if hierarchy files exist and load the neccesarry files
    name_hier_file = "/home/shreshtha/Hiearchies/namehier.csv"
    age_hier_file = "/home/shreshtha/Hiearchies/agehier.csv"
    mail_hier_file = "/home/shreshtha/Hiearchies/emailhier.csv"
    gender_hier_file = "/home/shreshtha/Hiearchies/gender.csv"
    zip_hier_file = "/home/shreshtha/Hiearchies/zipcode.csv"
    amount_hier_file = "/home/shreshtha/Hiearchies/amounthier.csv"
    
    try:
        # Load pickled hierarchy files
        with open('name_hier.pkl', 'rb') as f:
            name_hierarchy = pickle.load(f)
        with open('age_hier.pkl', 'rb') as f:
            age_hierarchy = pickle.load(f)
        with open('mail_hier.pkl', 'rb') as f:
            mail_hierarchy = pickle.load(f)
        with open('gender_hier.pkl', 'rb') as f:
            gender_hierarchy = pickle.load(f)
        with open('zip_hier.pkl', 'rb') as f:
            zip_hierarchy = pickle.load(f)
        with open('amount_hier.pkl', 'rb') as f:
            amount_spent_hierarchy = pickle.load(f)
    except FileNotFoundError:
        # Load hierarchy files from CSV and pickle for future use
        name_hierarchy = pd.read_csv(name_hier_file)
        with open('name_hier.pkl', 'wb') as f:
            pickle.dump(name_hierarchy, f)
        age_hierarchy = pd.read_csv(age_hier_file)
        with open('age_hier.pkl', 'wb') as f:
            pickle.dump(age_hierarchy, f)
        mail_hierarchy = pd.read_csv(mail_hier_file)
        with open('mail_hier.pkl', 'wb') as f:
            pickle.dump(mail_hierarchy, f)
        gender_hierarchy = pd.read_csv(gender_hier_file)
        with open('gender_hier.pkl', 'wb') as f:
            pickle.dump(gender_hierarchy, f)
        zip_hierarchy = pd.read_csv(zip_hier_file)
        with open('zip_hier.pkl', 'wb') as f:
            pickle.dump(zip_hierarchy, f)
        amount_spent_hierarchy = pd.read_csv(amount_hier_file)
        with open('amount_hier.pkl', 'wb') as f:
            pickle.dump(amount_spent_hierarchy, f)

    # Set attribute types and hierarchies
    dataset = Dataset.from_pandas(data)
    arxaas = ARXaaS("http://localhost:8080/")
    dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'Age', 'Email', 'zipcode', 'Amount_spent', 'Gender', 'Name')
    for column in ['Age', 'Email', 'zipcode', 'Amount_spent', 'Gender', 'Name']:
        if column not in data.columns:
            raise ValueError(f"{column} column not found in data")
        if column == 'Name':
            dataset.set_hierarchy('Name', name_hierarchy)
        elif column == 'Age':
            dataset.set_hierarchy('Age', age_hierarchy)
        elif column == 'Email':
            dataset.set_hierarchy('Email', mail_hierarchy)
        elif column == 'Gender':
            dataset.set_hierarchy('Gender', gender_hierarchy)
        elif column=='zipcode':
            dataset.set_hierarchy('zipcode',zip_hierarchy)
        else:
            dataset.set_hierarchy('Amount_spent',amount_spent_hierarchy)
        return


data=pd.read_csv("/home/shreshtha/Downloads/customer_data.csv")
set_hierarchy(data=data)
