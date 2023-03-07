import numpy as np
import pandas as pd
import pyarxaas
from pyarxaas import ARXaaS
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder
from pyarxaas import AttributeType
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import Dataset
arxaas = ARXaaS("http://localhost:8080/")
#print(data)
data=pd.read_csv("/home/shreshtha/Documents/zipcode.csv",header=None,usecols=[0],names=['zipcode'])
dataset = Dataset.from_pandas(data)
zipcode_hierarchy=pd.read_csv("/home/shreshtha/Documents/zipcode.csv",header=None,usecols=[1,2,3,4,5])
#print(zipcode_hierarchy.head)
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING)
#creating a risk profile
risk_profile = arxaas.risk_profile(dataset)
#print(risk_profile.re_identification_risk)
#print(risk_profile.attacker_success_rate)
print(risk_profile.population_model)
dataset.set_hierarchy('zipcode',zipcode_hierarchy)
kanon = KAnonymity(2)
request = arxaas.create_anonymization_request(dataset, KAnonymity)
request.set_data(dataset.values.tolist())
result = request.get_result()
anonymized_df = pd.DataFrame(result.get_data(), columns=dataset.columns)
print(anonymized_df)
#anonymize_result = arxaas.anonymize(dataset, kanon)
#anonymized_dataset = anonymize_result.dataset
#anon_dataframe = anonymized_dataset.to_dataframe()
