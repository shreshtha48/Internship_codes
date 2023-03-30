import pandas as pd
import pickle
import pyarxaas
from pyarxaas import ARXaaS
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder,RedactionHierarchyBuilder
from pyarxaas import AttributeType
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import Dataset
import pandas as pd
import pandas as pd
#instead of reading the csv files multiple times on their own, it makes a lot more sense to store that as pickle objects
import pickle
from pandas.api.types import CategoricalDtype

class HierarchySetter:
    def __init__(self, data=pd.DataFrame()):
        self.data = data
        self.name_hier_file = "/home/shreshtha/Hiearchies/namehier.csv"
        self.age_hier_file = "/home/shreshtha/Hiearchies/agehier.csv"
        self.mail_hier_file = "/home/shreshtha/Hiearchies/emailhier.csv"
        self.gender_hier_file = "/home/shreshtha/Hiearchies/gender.csv"
        self.zip_hier_file = "/home/shreshtha/Hiearchies/zipcode.csv"
        self.amount_hier_file = "/home/shreshtha/Hiearchies/amounthier.csv"
        self.name_hierarchy = None
        self.age_hierarchy = None
        self.mail_hierarchy = None
        self.gender_hierarchy = None
        self.zip_hierarchy = None
        self.amount_spent_hierarchy = None
    
    def load_hierarchy_files(self):
        try:
            # Load pickled hierarchy files
            with open('name_hier.pkl', 'rb') as f:
                self.name_hierarchy = pickle.load(f)
            with open('age_hier.pkl', 'rb') as f:
                self.age_hierarchy = pickle.load(f)
            with open('mail_hier.pkl', 'rb') as f:
                self.mail_hierarchy = pickle.load(f)
            with open('gender_hier.pkl', 'rb') as f:
                self.gender_hierarchy = pickle.load(f)
            with open('zip_hier.pkl', 'rb') as f:
                self.zip_hierarchy = pickle.load(f)
            with open('amount_hier.pkl', 'rb') as f:
                self.amount_spent_hierarchy = pickle.load(f)
        except FileNotFoundError:
            # Load hierarchy files from CSV and pickle for future use
            self.name_hierarchy = pd.read_csv(self.name_hier_file)
            with open('name_hier.pkl', 'wb') as f:
                pickle.dump(self.name_hierarchy, f)
            self.age_hierarchy = pd.read_csv(self.age_hier_file)
            with open('age_hier.pkl', 'wb') as f:
                pickle.dump(self.age_hierarchy, f)
            self.mail_hierarchy = pd.read_csv(self.mail_hier_file)
            with open('mail_hier.pkl', 'wb') as f:
                pickle.dump(self.mail_hierarchy, f)
            self.gender_hierarchy = pd.read_csv(self.gender_hier_file)
            with open('gender_hier.pkl', 'wb') as f:
                pickle.dump(self.gender_hierarchy, f)
            self.zip_hierarchy = pd.read_csv(self.zip_hier_file)
            with open('zip_hier.pkl', 'wb') as f:
                pickle.dump(self.zip_hierarchy, f)
            self.amount_spent_hierarchy = pd.read_csv(self.amount_hier_file)
            with open('amount_hier.pkl', 'wb') as f:
                pickle.dump(self.amount_spent_hierarchy, f)
    
    def set_attribute_types(self, dataset):
        dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'Age', 'Email', 'zipcode', 'Amount_spent', 'Gender', 'Name')
    
    def set_hierarchy(self, dataset, column):
        if column not in self.data.columns:
            raise ValueError(f"{column} column not found in data")
        if column == 'Name':
            dataset.set_hierarchy('Name', self.name_hierarchy)
        elif column == 'Age':
            dataset.set_hierarchy('Age', self.age_hierarchy)
        elif column == 'Email':
            dataset.set_hierarchy('Email', self.mail_hierarchy)
        elif column == 'Gender':
            dataset.set_hierarchy('Gender', self.gender_hierarchy)
        elif column=='zipcode':
            dataset.set_hierarchy('zipcode',zip_hierarchy)
        else:
            dataset.set_hierarchy('Amount_spent',amount_spent_hierarchy)
            #function ends
        return dataset



