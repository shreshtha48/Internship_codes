import snowflake.connector
import pandas as pd
from pyarxaas import ARXaaS
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import AttributeType
from pyarxaas import Dataset
import time
arxToolurl="http://localhost:8080"
#somewhow need to set the regex to create variable names from the file path and set them while iterating thru for loop
Name="/hierarchies/namehier.csv"
Age="/hierarchies/agehier.csv"
Email= "/hierarchies/emailhier.csv"
Gender="hierarchies/gender.csv"
zipcode="/hierarchies/zipcode.csv"
Amount_spent="/hierarchies/amounthier.csv"
data="./customer_data.csv"
""" db_result="db_result.csv" """
def anonymization(dataset):
    try:
        arxaas = ARXaaS(arxToolurl)
        kanon = KAnonymity(4)
        # specify the dataset as the first parameter, and privacy model list as the second paramter
        anonymize_result = arxaas.anonymize(dataset, [kanon])
        # get the new dataset
        anonymized_dataset = anonymize_result.dataset
        #print("Anonymized dataset",anonymized_dataset)
        anon_dataframe = anonymized_dataset.to_dataframe()
        print("Anonymized dataframe: \n",anon_dataframe)
        pd.DataFrame(anon_dataframe).to_csv('annoymize_output.csv',index=False)
        # get the risk profile for the new dataset
        anon_risk_profile = anonymize_result.risk_profile
        # get risk metrics as a dictionary
        re_indentifiation_risk = anon_risk_profile.re_identification_risk
        distribution_of_risk = anon_risk_profile.distribution_of_risk
        # get risk metrivs as pandas.DataFrame
        re_i_risk_df = anon_risk_profile.distribution_of_risk_dataframe()
        dist_risk_df = anon_risk_profile.distribution_of_risk_dataframe()
        # get the anonymiztion metrics
        anon_metrics = anonymize_result.anonymization_metrics
        return True
    except Exception as e:
        pass
        print (e)
def anonymizeAll():
    try:
        arxaas = ARXaaS(arxToolurl) # url contains url to AaaS web service
        df = pd.read_csv(dataset,sep=",")
        df = df.fillna('')
        dataset = Dataset.from_pandas(df)
        dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'GENDER','DEPARTMENT','USERROLE','JOBFUNCTION','RACE','ETHNICITY','WORKTYPE','WORKINGZIPCODE')
        dataset.set_attribute_type(AttributeType.IDENTIFYING, 'MANAGER_SAYHII_USER_ID')
        dataset.set_attribute_type(AttributeType.INSENSITIVE, 'ORGID','YEAROFBIRTH','HIREYEARANDMONTH','USERID','ACTIVESTATE','AGEGROUP','GENERATION','SAYHII_USER_ID')
        gender_hierarchy = pd.read_csv(genderHierarchycsv, header=None)
        gender_hierarchy=gender_hierarchy.fillna('')
        department_hierarchy= pd.read_csv(departmentHierarchycsv, header=None)
        department_hierarchy=department_hierarchy.fillna('')
        userrole_hierarchy= pd.read_csv(roleHierarchycsv, header=None)
        userrole_hierarchy=userrole_hierarchy.fillna('')
        jobfunction_hierarchy= pd.read_csv(jobfunctionHierarchycsv, header=None)
        jobfunction_hierarchy=jobfunction_hierarchy.fillna('')
        race_hierarchy= pd.read_csv(raceHierarchycsv, header=None)
        race_hierarchy=race_hierarchy.fillna('')
        ethencity_hierarchy= pd.read_csv(ethencityHierarchycsv, header=None)
        ethencity_hierarchy=ethencity_hierarchy.fillna('')
        worktype_hierarchy= pd.read_csv(worktypeHierarchycsv, header=None)
        worktype_hierarchy=worktype_hierarchy.fillna('')
        zipcode_hierarchy= pd.read_csv(zipcodeHierarchycsv, header=None)
        zipcode_hierarchy=zipcode_hierarchy.fillna('')
        # setting the imported csv file. Specify the column name as the fist parameter, and the hierarchy as the second parameter
        dataset.set_hierarchy('GENDER', gender_hierarchy)
        dataset.set_hierarchy('DEPARTMENT', department_hierarchy)
        dataset.set_hierarchy('USERROLE', userrole_hierarchy)
        dataset.set_hierarchy('JOBFUNCTION', jobfunction_hierarchy)
        dataset.set_hierarchy('RACE', race_hierarchy)
        dataset.set_hierarchy('ETHNICITY', ethencity_hierarchy)
        dataset.set_hierarchy('WORKTYPE', worktype_hierarchy)
        dataset.set_hierarchy('WORKINGZIPCODE', zipcode_hierarchy)
        # creating a privacy_models object
        kanon = KAnonymity(4)
        # specify the dataset as the first parameter, and privacy model list as the second paramter
        anonymize_result = arxaas.anonymize(dataset, [kanon])
        # get the new dataset
        anonymized_dataset = anonymize_result.dataset
        print("Anonymized dataset",anonymized_dataset)
        anon_dataframe = anonymized_dataset.to_dataframe()
        print("Anonymized dataframe: \n",anon_dataframe)
        pd.DataFrame(anon_dataframe).to_csv('annoymize_output.csv',index=False)
        # get the risk profile for the new dataset
        anon_risk_profile = anonymize_result.risk_profile
        # get risk metrics as a dictionary
        re_indentifiation_risk = anon_risk_profile.re_identification_risk
        distribution_of_risk = anon_risk_profile.distribution_of_risk
        # get risk metrivs as pandas.DataFrame
        re_i_risk_df = anon_risk_profile.distribution_of_risk_dataframe()
        dist_risk_df = anon_risk_profile.distribution_of_risk_dataframe()
        # get the anonymiztion metrics
        anon_metrics = anonymize_result.anonymization_metrics
    finally:
        print("Run")
def anonymizeGender():
    try:
        df = pd.read_csv(db_result,sep=",")
        df = df.fillna('')
        dataset = Dataset.from_pandas(df)
        dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'GENDER')
        dataset.set_attribute_type(AttributeType.INSENSITIVE, 'ORGID','SAYHII_USER_ID')
        gender_hierarchy = pd.read_csv(genderHierarchycsv, header=None)
        gender_hierarchy=gender_hierarchy.fillna('')
        dataset.set_hierarchy('GENDER', gender_hierarchy)
        if(anonymization(dataset)):
            return True
        return False
    except Exception as e:
        pass
        logMessage = "An error occurred in anonymizeGender() "+e
        cw.sendLog('anonymizationLogs','{}-{}'.format(time.strftime('%Y-%m-%d'),'logstream'),logMessage)
        print ("An error occurred in anonymizeGender() :",e)
        return False
def anonymizeDepartmentFunction():
    try:
        df = pd.read_csv(db_result,sep=",")
        df = df.fillna('')
        dataset = Dataset.from_pandas(df)
        dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'DEPARTMENT','JOBFUNCTION','USERROLE')
        dataset.set_attribute_type(AttributeType.INSENSITIVE, 'ORGID','SAYHII_USER_ID')
        department_hierarchy= pd.read_csv(departmentHierarchycsv, header=None)
        department_hierarchy=department_hierarchy.fillna('')
        userrole_hierarchy= pd.read_csv(roleHierarchycsv, header=None)
        userrole_hierarchy=userrole_hierarchy.fillna('')
        jobfunction_hierarchy= pd.read_csv(jobfunctionHierarchycsv, header=None)
        jobfunction_hierarchy=jobfunction_hierarchy.fillna('')
        dataset.set_hierarchy('DEPARTMENT', department_hierarchy)
        dataset.set_hierarchy('USERROLE', userrole_hierarchy)
        dataset.set_hierarchy('JOBFUNCTION', jobfunction_hierarchy)
        if(anonymization(dataset)):
            return True
        return False
    except Exception as e:
        pass
        logMessage = "An error occurred in anonymizeDepartmentFunction() "+e
        cw.sendLog('anonymizationLogs','{}-{}'.format(time.strftime('%Y-%m-%d'),'logstream'),logMessage)
        print ("An error occurred in anonymizeDepartmentFunction() :",e)
        return False
def anonymizeDepartment():
    try:
        df = pd.read_csv(db_result,sep=",")
        df = df.fillna('')
        dataset = Dataset.from_pandas(df)
        dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'DEPARTMENT')
        dataset.set_attribute_type(AttributeType.INSENSITIVE, 'ORGID','SAYHII_USER_ID')
        department_hierarchy= pd.read_csv(departmentHierarchycsv, header=None)
        department_hierarchy=department_hierarchy.fillna('')
        dataset.set_hierarchy('DEPARTMENT', department_hierarchy)
        if(anonymization(dataset)):
            return True
        return False
    except Exception as e:
        pass
        logMessage = "An error occurred in anonymizeDepartment() "+e
        cw.sendLog('anonymizationLogs','{}-{}'.format(time.strftime('%Y-%m-%d'),'logstream'),logMessage)
        print ("An error occurred in anonymizeDepartment() :",e)
        return False
def anonymizeDemographics():
    try:
        df = pd.read_csv(db_result,sep=",")
        df = df.fillna('')
        dataset = Dataset.from_pandas(df)
        dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'GENDER','RACE','ETHNICITY')
        dataset.set_attribute_type(AttributeType.INSENSITIVE, 'ORGID','SAYHII_USER_ID','GENERATION','AGEGROUP')
        gender_hierarchy= pd.read_csv(genderHierarchycsv, header=None)
        gender_hierarchy=gender_hierarchy.fillna('')
        race_hierarchy= pd.read_csv(raceHierarchycsv, header=None)
        race_hierarchy=race_hierarchy.fillna('')
        ethencity_hierarchy= pd.read_csv(ethencityHierarchycsv, header=None)
        ethencity_hierarchy=ethencity_hierarchy.fillna('')
        dataset.set_hierarchy('GENDER', gender_hierarchy)
        dataset.set_hierarchy('RACE', race_hierarchy)
        dataset.set_hierarchy('ETHNICITY', ethencity_hierarchy)
        if(anonymization(dataset)):
            return True
        return False
    except Exception as e:
        pass
        logMessage = "An error occurred in anonymizeDemographics() "+e
        cw.sendLog('anonymizationLogs','{}-{}'.format(time.strftime('%Y-%m-%d'),'logstream'),logMessage)
        print ("An error occurred in anonymizeDemographics() :",e)
        return False
def anonymizeZipcode():
    try:
        df = pd.read_csv(db_result,sep=",")
        df = df.fillna('')
        dataset = Dataset.from_pandas(df)
        dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'LOCATION')
        dataset.set_attribute_type(AttributeType.INSENSITIVE, 'ORGID','SAYHII_USER_ID')
        location_hierarchy = pd.read_csv(locationHierachycsv, header=None)
        print("hierarchy Colum count :",len(location_hierarchy.columns))
        print(location_hierarchy.columns.tolist())
        location_hierarchy=location_hierarchy.fillna('')
        dataset.set_hierarchy('LOCATION', location_hierarchy)
        if(anonymization(dataset)):
            return True
        return False
    except Exception as e:
        pass
        logMessage = "An error occurred in anonymizeZipcode() "+e
        cw.sendLog('anonymizationLogs','{}-{}'.format(time.strftime('%Y-%m-%d'),'logstream'),logMessage)
        print ("An error occurred in anonymizeZipcode() :",e)
        return False
#anonymizeZipcode()