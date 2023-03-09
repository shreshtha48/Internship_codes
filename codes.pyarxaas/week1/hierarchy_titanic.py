#The file given below takes the dataframe as a column input and sets the data. \
import numpy as np
import pandas as pd
import pyarxaas
from pyarxaas import ARXaaS
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder,RedactionHierarchyBuilder
from pyarxaas import AttributeType
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import Dataset
#running the arx instance locally from the object
arxaas = ARXaaS("http://localhost:8080/")
#loading the dataset
data=pd.read_csv("/home/shreshtha/Downloads/test.csv")
#removing the NaN from the dataset
data=data.dropna()
#age and fare have float values and this will throw error while building hierarchies
data['Age']=data['Age'].astype(int)
data['Fare']=data['Fare'].astype(int)
#data['Fare']=data('Fare').astype(int)
def hierarchies(data):
    #dropping the na's just in case
    data=data.dropna()
    #creating the dataset
    dataset = Dataset.from_pandas(data)
    #setting the attributes as insesntive, sensitive and quasiidentifying based on the values in the column
    #here the fare sex and age and pclass and id are not identifying by themshelves but combining them with other attributes might make them identifying
    dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING,'Fare','Sex','Age','Pclass','PassengerId','Ticket')
    dataset.set_attribute_type(AttributeType.INSENSITIVE,'Embarked')
    #setting the name as sensitive because seeing them on their own can disrupt the user privacy
    dataset.set_attribute_type(AttributeType.SENSITIVE,'Name')
    for column in dataset.columns:
        #setting the hierarchies based on the column values
          if column == 'Age':
            #age can be grouped and shown generalized value as that still keeps the data statistically significant
             hierarchy_builder = IntervalHierarchyBuilder()
             hierarchy_builder.add_interval(left=0, right=18, name='0-18')
             hierarchy_builder.add_interval(left=19, right=30, name='19-30')
             hierarchy_builder.add_interval(left=31, right=45, name='31-45')
             hierarchy_builder.add_interval(left=46, right=60, name='46-60')
             hierarchy = hierarchy_builder.build()
             arxaas.set_hierarchy(column, hierarchy)
#this code would anonymize others based on generalized redaction hierarchy
          elif column =='Ticket'or'PaseengerId': 
            builder= RedactionHierarchyBuilder() 
            if column =='Ticket':
               redaction_hierarchy = arxaas.hierarchy(builder, column)
            else:
                redaction_hierarchy=arxaas.hierarchy(builder, column)
          elif column=='Fare' or 'Name':
