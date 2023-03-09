#this is the final version of the updated code
#importing the neccesary stuff
import numpy as np
import pandas as pd
import pyarxaas
from pyarxaas import ARXaaS
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder
from pyarxaas import AttributeType
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import Dataset
arxaas = ARXaaS("http://localhost:8080/")
data=pd.read_csv("/home/shreshtha/Documents/zipcode.csv",usecols=[0])
hierarchy=pd.read_csv("/home/shreshtha/Documents/zipcode.csv")
hierarchy_var=hierarchy
dataset = Dataset.from_pandas(data)
#print(dataset)
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING,'zipcode')
risk_profile = arxaas.risk_profile(dataset)
#print(risk_profile.re_identification_risk)
#print(risk_profile.attacker_success_rate)
#print(risk_profile.population_model)
dataset.set_hierarchy('zipcode',hierarchy_var)
kanon = KAnonymity(5)
anonymize_result = arxaas.anonymize(dataset, [kanon],0.02)
print(anonymize_result.dataset.to_dataframe())
risk_profile_final=arxaas.risk_profile(anonymize_result)
print(risk_profile_final.re_identification_risk) 
anon_metrics = anonymize_result.anonymization_metrics
anon_metrics.attribute_generalization
