#this script has a function which takes in the set dataframe and anonymizies it
#loading the neccessary libraries
import pandas as pd
from pyarxaas import ARXaaS
from pyarxaas.privacy_models import KAnonymity, LDiversityDistinct
#creating a class called anonymizer which is used to anonymize the data
class Anonymizer:
    def __init__(self, dataset):
      #setting up the local arx instance
        self.dataset = dataset
        self.arxaas = ARXaaS("http://localhost:8080/")
        self.privacy_model = None
      #function to set the k anonymity privacy model  
    def set_k_anonymity(self, k):
        self.privacy_model = KAnonymity(k=k)
       #funcyion to set the l diversity model 
    def set_l_diversity_distinct(self, column, l):
        self.privacy_model = LDiversityDistinct(column=column, l=l)
       #raising error if the model is not from the one found in pyarxaas
    def anonymize(self):
        if self.privacy_model is None:
            raise ValueError("Privacy model not set")
            #anonymizing the actual dataset
        anonymized = self.arxaas.anonymize(self.dataset, self.privacy_model)
        return anonymized
