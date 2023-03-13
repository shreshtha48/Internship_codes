#this function sets the hierarchy for the datasetto get it ready for the anonymization
#load the data and the neccesary libraries
#we will start by importing the neccesarry libraries
import pandas as pd
#we will start by importing the neccesarry libraries
import numpy as np
import pandas as pd
#pyarxaas will allow us to import some functions neccesary for anonymization
import pyarxaas
from pyarxaas import ARXaaS
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder,RedactionHierarchyBuilder
from pyarxaas import AttributeType
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import Dataset
def set_hierarchy(data=pd.DataFrame):
    dataset=Dataset.from_pandas(data)
    #starting up the arx instance:
    arxaas = ARXaaS("http://localhost:8080/")
    #setting the attribute type from arxaas
    dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'Age','Email','zipcode','Amount_spent','Gender','Name')
    #setting the hierarchies
    #the following iterates through the columns of the data and sets the hierarchies based on the same
    for columns in data:
        if columns=='Name':
            name_hierarchy=pd.read_csv("/home/shreshtha/Hiearchies/namehier.csv")
            dataset.set_hierarchy('Name',name_hierarchy)
        elif columns=='Age':
            age_hierarchy=pd.read_csv("/home/shreshtha/Hiearchies/agehier.csv")
            dataset.set_hierarchy('Age',age_hierarchy)
        elif columns=='Email':
            mail_hierarchy=pd.read_csv("/home/shreshtha/Hiearchies/emailhier.csv")
            dataset.set_hierarchy('Email',mail_hierarchy)
        elif columns=='Gender':
            gender_hierarchy=pd.read_csv("/home/shreshtha/Hiearchies/gender.csv")
            dataset.set_hierarchy('Gender',gender_hierarchy)
        elif columns=='Zipcode':
            zip_hierarchy=pd.read_csv("/home/shreshtha/Hiearchies/zipcode.csv")
            dataset.set_hierarchy('zipcode',zip_hierarchy)
        else:
            amount_spent_hierarchy=pd.read_csv("/home/shreshtha/Hiearchies/amounthier.csv")
            dataset.set_hierarchy('Amount_spent',amount_spent_hierarchy)
    return
# a demo of the function
data=pd.read_csv("/home/shreshtha/Downloads/customer_data.csv")
set_hierarchy(data)


