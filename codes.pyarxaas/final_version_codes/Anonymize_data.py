import pandas as pd
from pyarxaas import ARXaaS
from pyarxaas.privacy_models import KAnonymity, LDiversityDistinct
from pyarxaas.hierarchy import IntervalHierarchyBuilder
from pyarxaas import Dataset, AttributeType

class Anonymizer:
    def __init__(self, data):
        self.dataset = Dataset.from_pandas(data)
        arxaas = ARXaaS("http://localhost:8080/")
        self.privacy_model = None
        try:
    
           amount_spent=pd.read_csv("./hierarchies/amountspend.hier.csv")
           zipcode=pd.read_csv("./hierarchies/zipcode.csv")
        except Exception as error:
            print(error)

    def set_hierarchy( data):
        dataset = Dataset.from_pandas(data)
        def attribute():
            try:
               dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'AGE', 'ZIPCODE', 'AMOUNT_SPENT')
               dataset.set_attribute_type(AttributeType.INSENSITIVE,'GENDER','NAME','EMAIL')
            except Exception as error:
                print(error)
        def age_hierarchy():
            try:
               age=pd.read_csv("./hierarchies/agehier.csv")
               dataset.set_hierarchy('AGE', age)
            except Exception as error:
                print(error)
        def amountspent_hierarchy():
            try:
               amount=pd.read_csv("./hierarchies/amountspend.hier.csv")
               dataset.set_hierarchy('AMOUNT_SPENT', amount)
            except Exception as error:
                print(error)
        def zipcode_hierarchy():
            try:
               zipcode=pd.read_csv("./hierarchies/zipcode.csv")
               dataset.set_hierarchy('ZIPCODE', zipcode)
            except Exception as error:
                print(error)
        attribute()
        age_hierarchy()
        amountspent_hierarchy()
        zipcode_hierarchy()
        arxaas=ARXaaS("http://localhost:8080/")
        kanon = KAnonymity(2)
        anonymize_result = arxaas.anonymize(dataset, [kanon])
        anonymized_dataset = anonymize_result.dataset
        anon_dataframe = anonymized_dataset.to_dataframe()
        return anon_dataframe

    

        

        
      
    
    