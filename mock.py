#importing the neccesary modules and functions
import numpy as np
import pandas as pd
import pyarxaas
from pyarxaas import ARXaaS
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder
from pyarxaas import AttributeType
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import Dataset
#creating a local arx instance, can be created using running the docker image locally
arxaas = ARXaaS("http://localhost:8080/")
#print(data)
#loading the data which contains the zipcodes
data=pd.read_csv("/home/shreshtha/Documents/zipcode.csv",header=None,usecols=[0],names=['zipcode'])
dataset = Dataset.from_pandas(data)
#loading the zipcode hierarchies present in the csv files, if dont want to define manually then can be done automatically with arx
zipcode_hierarchy=pd.read_csv("/home/shreshtha/Documents/zipcode.csv",header=None,usecols=[1,2,3,4,5])
#print(zipcode_hierarchy.head)
#setting the attribute types for the dataset column
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING)
#creating a risk profile
risk_profile = arxaas.risk_profile(dataset)
#reidentification risk states how much the data is at the risk of reidentifying
#print(risk_profile.re_identification_risk)
#attacker success rate tells you how much the data can be attacked by which model of attacking
#print(risk_profile.attacker_success_rate)
print(risk_profile.population_model)
#setting the hierarchies for the datset
dataset.set_hierarchy('zipcode',zipcode_hierarchy)
#creating an object which displays the level of anonmity per model for the privacy of the data
kanon = KAnonymity(2)
#privatizing the data using privacy models
#the given below chunk of code does not work somehow but will work through it
request = arxaas.create_anonymization_request(dataset, KAnonymity)
request.set_data(dataset.values.tolist())
result = request.get_result()
anonymized_df = pd.DataFrame(result.get_data(), columns=dataset.columns)
print(anonymized_df)
#anonymize_result = arxaas.anonymize(dataset, kanon)
#anonymized_dataset = anonymize_result.dataset
#anon_dataframe = anonymized_dataset.to_dataframe()
