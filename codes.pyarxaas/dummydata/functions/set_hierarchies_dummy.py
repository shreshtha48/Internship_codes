import pyarxaas
from pyarxaas import ARXaaS, Dataset
from pyarxaas import AttributeType
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder, RedactionHierarchyBuilder
from pyarxaas.privacy_models import KAnonymity
import pandas as pd
import pickle

import pyarxaas
from pyarxaas import ARXaaS, Dataset
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder, RedactionHierarchyBuilder
from pyarxaas.privacy_models import KAnonymity
import pandas as pd
import pickle

def set_hierarchy(data=pd.DataFrame, risk_profile=False):
    hierarchy_files = {
        "Name": "/home/shreshtha/Hiearchies/namehier.csv",
        "Age": "/home/shreshtha/Hiearchies/agehier.csv",
        "Email": "/home/shreshtha/Hiearchies/emailhier.csv",
        "Gender": "/home/shreshtha/Hiearchies/gender.csv",
        "zipcode": "/home/shreshtha/Hiearchies/zipcode.csv",
        "Amount_spent": "/home/shreshtha/Hiearchies/amounthier.csv"
    }
    hierarchy_data = {}
    for column, file in hierarchy_files.items():
        try:
            with open(f"{column.lower()}_hier.pkl", "rb") as f:
                hierarchy_data[column] = pickle.load(f)
        except FileNotFoundError:
            hierarchy_data[column] = pd.read_csv(file)
            with open(f"{column.lower()}_hier.pkl", "wb") as f:
                pickle.dump(hierarchy_data[column], f)

    dataset = Dataset.from_pandas(data)
    arxaas = ARXaaS("http://localhost:8080/")
    dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, "Age", "Email", "zipcode", "Amount_spent", "Gender", "Name")
    if risk_profile:
        risk_profile = arxaas.risk_profile(dataset)
        print(risk_profile.re_identification_risk)
        print(risk_profile.attacker_success_rate)
        print(risk_profile.distribution_of_risk)
        return risk_profile
    for column in ["Name", "Age", "Email", "Gender", "zipcode", "Amount_spent"]:
        if column not in data.columns:
            raise ValueError(f"{column} column not found in data")
        dataset.set_hierarchy(column, hierarchy_data[column])
    return dataset
