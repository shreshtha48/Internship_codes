#this is the code to set hierarchies for the dummy dataset
#the dataset in question is the customers dataset which contains the name, age, email id, the zipcodes and the amount spent for a customer
#according to the convention, the name will be sensitive since once the name gets out all of the information can be traced back to the user
#the email is also a sensitive case since once the name gets out, the information can also be traced directly back to the user as the users often have their own names as email
#the amount spent is an insensitive column here since a lot of people can spend the same amount and the amount spent can not directly be traced back to the user
#the zipcodes is a quasidentifying column since it alone will not lead to tracing the user back but combining it with other columns can lead to identification of the users
#the gender column is also a quasiidentifying column
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
#starting up the arx instance:
arxaas = ARXaaS("http://localhost:8080/")
#reading in the data from the local file
data=pd.read_csv("/home/shreshtha/customer_data.csv")
    #creating a dataset according to the pyarxaas guideline
dataset = Dataset.from_pandas(data)
    #setting the attribute type from arxaas
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'Age','Email','zipcode','Gender','Amount_spent')
dataset.set_attribute_type(AttributeType.SENSITIVE,'Name')
#creating the column for the age hierarchy
age = data["Age"].tolist()
#creating interval based hierarchy for age
interval_based=IntervalHierarchyBuilder()
#adding the groupings for the interval
interval_based.add_interval(0,18, "child")
interval_based.add_interval(18,30, "young-adult")
interval_based.add_interval(30,60, "adult")
interval_based.add_interval(60,120, "old")
#adding the gropuings based on the intervals
interval_based.level(0)\
    .add_group(2, "young")\
    .add_group(2, "adult")
#creating the hierarchy
interval_hierarchy = arxaas.hierarchy(interval_based, age)
#making sure that the hierarchy works succesfully
print(interval_hierarchy)
#setting the interval hierarchy to the data
dataset.set_hierarchy('Age',interval_hierarchy)
#creating an order based hierarchy for gender
gender_cols=data['Gender'].to_list()
#reading the set hierarchies for the gender
gender=pd.read_csv("/home/shreshtha/Documents/gender.csv")
#setting the hierarchies for the gender
dataset.set_hierarchy('Gender',gender)
#creating a custom hierarchy for zipcode
hierarchy=pd.read_csv("/home/shreshtha/Documents/zipcode.csv")
hierarchy_var=hierarchy
#setting the hierarchy for zipcode
dataset.set_hierarchy('zipcode',hierarchy_var)
#creating an reduction based hierarchy for email 
mail=data['Email'].to_list()
#building the redaction builder instance
reduction_builder=RedactionHierarchyBuilder()
#building the redaction hierarchy
redaction_hierarchy = arxaas.hierarchy(reduction_builder, mail) 
#making sure that the hierarchy is set correctly
print(redaction_hierarchy)
#setting the email hierarchy
dataset.set_hierarchy('Email',redaction_hierarchy)
#creating an interval based hierarchy for the amount spent
#getting the values for the amount to set the hierarchy on
amount=data['Amount_spent'].to_list()
#building the interval builder instance
amountspent_intervals = IntervalHierarchyBuilder()
#grouping values on the intervals based on the values
amountspent_intervals.add_interval(0,50, "low")
amountspent_intervals.add_interval(50,200, "high_low")
amountspent_intervals.add_interval(200,550,"mid")
amountspent_intervals.add_interval(550,1000, "high")
#creating the hierarchy
amount_hierarchy = arxaas.hierarchy(amountspent_intervals,amount )
#making sure that the hierarchy is working as desired
print(amount_hierarchy)
#setting the hierarchy
dataset.set_hierarchy("Amount_spent",amount_hierarchy)
