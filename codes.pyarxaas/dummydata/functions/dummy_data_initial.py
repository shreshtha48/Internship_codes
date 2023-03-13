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
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'Age','Email','zipcode','Amount_spent','Gender','Name')
#before setting up the hierarchy and anonymizing the data, it wise to analyze the risk of the data
#the risk profile for the dataset can be created by calling the risk profile class of the arxaas module
risk_profile = arxaas.risk_profile(dataset)
#the risk profile has various columns and now we are looking at some of the terms in the risk profile such as reidentification risk
risk_profile.re_identification_risk
#let us now look at the success rate of the attackers
risk_profile.attacker_success_rate
#there are several attacker models such as journalist, prosecuter and the arxaas tells us the risk of all of them
#we are now looking at the distribution of the risk for vatious intervals
risk_profile.distribution_of_risk
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
#print(interval_hierarchy)
#saving the hierarchy for reuse
age_hierarchy=pd.DataFrame(interval_hierarchy)
age_hierarchy.to_csv('/home/shreshtha/Downloads/agehier.csv')
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
email_hierarchy=pd.DataFrame(mail)
email_hierarchy.to_csv("/home/shreshtha/Downloads/emailhier.csv")
#making sure that the hierarchy is set correctly
#print(redaction_hierarchy)
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
amount_spent=pd.DataFrame(amount_hierarchy)
amount_spent.to_csv("/home/shreshtha/Downloads/amountspend.hier.csv")
#making sure that the hierarchy is working as desired
#print(amount_hierarchy)
#setting the hierarchy
dataset.set_hierarchy("Amount_spent",amount_hierarchy)
#setting redaction based hierarchy for the name
name=data['Name'].to_list()
redaction_hierarchy = arxaas.hierarchy(reduction_builder, name) 
dataset.set_hierarchy('Name',redaction_hierarchy)
name_hier=pd.DataFrame(redaction_hierarchy)
name_hier.to_csv("/home/shreshtha/Downloads/namehier.csv")
print(dataset.describe())
#now that we have set the hierarchies for the data, we can go about anonymizing them
#I will not be setting the same privacy models for all the columns in the dataset, rather i will choose different models for different columns of the dataset depending on values
from pyarxaas.privacy_models import KAnonymity,LDiversityDistinct,TClosenessEqualDistance
kanon = KAnonymity(2)
anon_result = arxaas.anonymize(dataset,[kanon],0.002)
anon_result.dataset.to_dataframe()

    
