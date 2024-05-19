# jsonFile need to be in triple quotation
# Serialize or Encode= pythonObj to jsonFile => dumps,dump 
# Deserialize or Decode= jsonFile to pythonObj => loads,load 
# dupms and loads are used in VS but dump converts to a file and load bring a file to VS
#----------------------------------------------------------------------------------------------------
import json
import jmespath


pyobj={"Employees":[
            {"First_Name":"Negin","Last_Name":"Sarlak","Age":26,"Occupation":"Lawyer"},
            {"First_Name":"Najmeh","Last_Name":"Golestan","Age":34,"Occupation":"Psychologist"},
            {"First_Name":"Omid","Last_Name":"Hashemi","Age":32,"Occupation":"Saler"},
            {"First_Name":"Tara","Last_Name":"Ochizi","Age":37,"Occupation":"Architecture"}],
        "Employers":[
            {"First_Name":"Soheil","Last_Name":"Daliri","Age":31,"Occupation":"Programmer"},
            {"First_Name":"Mathew","Last_Name":"Blackwell","Age":35,"Occupation":"Programmer"}]}


# jobj=json.dumps(pyobj)
# print(pyobj)

# with open("JsonFiles/myJsonFile.json","w") as file1:
#     jfobj=json.dump(pyobj,file1,indent=4)

#-----------------------------------------------------------------------------------------------------

jsonFile="""{"Employees":[
            {"First_Name":"Negin","Last_Name":"Sarlak","Age":26,"Occupation":"Lawyer"},
            {"First_Name":"Najmeh","Last_Name":"Golestan","Age":34,"Occupation":"Psychologist"},
            {"First_Name":"Omid","Last_Name":"Hashemi","Age":32,"Occupation":"Saler"},
            {"First_Name":"Tara","Last_Name":"Ochizi","Age":37,"Occupation":"Architecture"}],
        "Employers":[
            {"First_Name":"Soheil","Last_Name":"Daliri","Age":31,"Occupation":"Programmer"},
            {"First_Name":"Mathew","Last_Name":"Blackwell","Age":35,"Occupation":"Programmer"}]}"""


# jobj=json.loads(jsonFile)
# print(jobj)

# with open("JsonFiles/myJsonFile.json","r") as file2:
#     jfobj=json.load(file2)
#     print(jfobj)

#-----------------------------------------------------------------------------------------------------