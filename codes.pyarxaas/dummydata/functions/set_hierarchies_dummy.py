
import pyarxaas
from pyarxaas import ARXaaS
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder,RedactionHierarchyBuilder
from pyarxaas import AttributeType
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import Dataset
import pandas as pd
import pandas as pd

def set_hierarchy(data=pd.DataFrame):
    name_hierarchy = pd.read_csv("/home/shreshtha/Hiearchies/namehier.csv")
    age_hierarchy = pd.read_csv("/home/shreshtha/Hiearchies/agehier.csv")
    mail_hierarchy = pd.read_csv("/home/shreshtha/Hiearchies/emailhier.csv")
    gender_hierarchy = pd.read_csv("/home/shreshtha/Hiearchies/gender.csv")
    zip_hierarchy = pd.read_csv("/home/shreshtha/Hiearchies/zipcode.csv")
    amount_spent_hierarchy = pd.read_csv("/home/shreshtha/Hiearchies/amounthier.csv")

    dataset = Dataset.from_pandas(data)
    arxaas = ARXaaS("http://localhost:8080/")
    dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'Age', 'Email', 'zipcode', 'Amount_spent', 'Gender', 'Name')
    for column in ['Age', 'Email', 'zipcode', 'Amount_spent', 'Gender', 'Name']:
        if column not in data.columns:
            raise ValueError(f"{column} column not found in data")
        if column == 'Name':
            dataset.set_hierarchy('Name', name_hierarchy)
        elif column == 'Age':
            dataset.set_hierarchy('Age', age_hierarchy)
        elif column == 'Email':
            dataset.set_hierarchy('Email', mail_hierarchy)
        elif column == 'Gender':
            dataset.set_hierarchy('Gender', gender_hierarchy)
        elif column == 'Zipcode':
            dataset.set_hierarchy('zipcode', zip_hierarchy)
        else:
            dataset.set_hierarchy('Amount_spent', amount_spent_hierarchy)
    return dataset
