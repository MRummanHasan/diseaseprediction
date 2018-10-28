import io
import pymysql
# STEPS:
# data from DB(bridge table);
# populate that data in List of Array;
# check most match with symptoms;

## fetch data from junction table
## connection work
# conn = pymysql.connect(host='localhost', user='root', password='', db='HealthSystem')
# a = conn.cursor()
##end connection work
inputValueArr = ['fever','weakness','headache'] # input by patient

## Query
# sql = 'SELECT D.disease_name, S.symptom_name FROM diseases AS D JOIN disease_symptoms_bridgetable AS DC ON D.disease_id = DC.disease_id JOIN symptoms AS S ON S.symptom_id = DC.symptom_id'
# a.execute(sql)
# data = a.fetchall()
# data = (('Influenza', 'fever'), ('Influenza', 'cough'), ('Influenza', 'headache'), ('Influenza', 'sore throat'), ('FoodPoisoning', 'vomiting'), ('FoodPoisoning', 'weakness'), ('FoodPoisoning', 'fever'), ('Food Poisoning', 'V'), ('Food Poisoning', 'W'), ('Food Poisoning', 'F'))
        ####### OR #######
## list = [disease, symptom1, symptom2....]
list = [['Influenza', 'cough', 'headache', 'sore throat'],
        ['Food Poisoning', 'weakness', 'fever','sore throat','headache'],
        ['eating or weight problems', 'W', 'fever']
        ['lung problems','cough with blood','shortness of breath']
        ['skin problems','redness of face','moles on skin']
        ['Diarrhea','watery stool','vomiting','abdominal cramps','belly pain']]

val = 0
thisdisease = ""
percentArr = []
inputVal = 0

for i in range(3):
    for inputVal in inputValueArr:
        # print(inputVal)
        if inputVal in list[i]:
            val = val + 1
    percentArr.append(val)
    val = 0

highestPerValueFound = max(percentArr)
mostSuitableDiseasecount = percentArr.index(highestPerValueFound)

thisdisease = list[mostSuitableDiseasecount][0]
print("Symptoms by user: ",inputValueArr)
print("\nYou might be suffering from: ",thisdisease)
