#The file given below takes the dataframe as a column input and sets the data. \
import numpy as np
import pandas as pd
import pyarxaas
from pyarxaas import ARXaaS
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder,RedactionHierarchyBuilder
from pyarxaas import AttributeType
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import Dataset
arxaas = ARXaaS("http://localhost:8080/")
data=pd.read_csv("/home/shreshtha/Downloads/test.csv")
def hierarchies(data):
    data=data.dropna()
    dataset = Dataset.from_pandas(data)
      for column in dataset.columns:
          if column_name == 'Age':
        hierarchy_builder = IntervalHierarchyBuilder()
        hierarchy_builder.add_interval(left=0, right=18, name='0-18')
        hierarchy_builder.add_interval(left=19, right=30, name='19-30')
        hierarchy_builder.add_interval(left=31, right=45, name='31-45')
        hierarchy_builder.add_interval(left=46, right=60, name='46-60')
        hierarchy = hierarchy_builder.build()
        arxaas.set_hierarchy(column_name, hierarchy)

        elif column =='Ticket'or'PaseengerId':
            builder= RedactionHierarchyBuilder()