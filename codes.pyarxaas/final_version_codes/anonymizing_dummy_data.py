#this script has a function which takes in the set dataframe and anonymizies it
import pandas as pd
from pyarxaas import ARXaaS
from pyarxaas.privacy_models import KAnonymity, LDiversityDistinct
#creating a class called anonymizer which is used to anonymize the dataset
class Anonymizer:
    def __init__(self, dataset):
        self.dataset = dataset
        #creating a local arx instance
        self.arxaas = ARXaaS("http://localhost:8080/")
        self.privacy_model = None
        #function to anonymize the data using k anonymity
    def set_k_anonymity(self, k):
        self.privacy_model = KAnonymity(k=k)
        #privtaizing the data using l diversity
    def set_l_diversity_distinct(self, column, l):
        self.privacy_model = LDiversityDistinct(column=column, l=l)
    #error handling to handle values not present in the dataset
    def anonymize(self):
        if self.privacy_model is None:
            raise ValueError("Privacy model not set")
         #anonymizing the data
        anonymized = self.arxaas.anonymize(self.dataset, [self.privacy_model],0.002)
        return anonymized



data=pd.read_csv("/home/shreshtha/Downloads/customer_data.csv")
from dummy_function_hierarchy_oops import set_hierarchy
data=set_hierarchy(data=data,risk_profile=True)
anonymizer = Anonymizer(data)
anonymizer.set_k_anonymity(k=5)
anonymized_data = anonymizer.anonymize()
