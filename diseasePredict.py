import io
import pymysql
# STEPS:
# data from DB(bridge table);
# populate that data in List of Array;
# check most match with symptoms;
# Match it to doctor profile
# display doctor

## fetch data from junction table
## connection work
conn = pymysql.connect(host='localhost', user='root', password='', db='HealthSystem')
a = conn.cursor()
##end connection work
## Query
# sql = 'SELECT D.disease_name, S.symptom_name FROM diseases AS D JOIN disease_symptoms_bridgetable AS DC ON D.disease_id = DC.disease_id JOIN symptoms AS S ON S.symptom_id = DC.symptom_id'
# a.execute(sql)
# data = a.fetchall()
# print(data)
data = (('Influenza', 'fever'), ('Influenza', 'cough'), ('Influenza', 'headache'), ('Influenza', 'sore throat'), ('FoodPoisoning', 'vomiting'), ('FoodPoisoning', 'weakness'), ('FoodPoisoning', 'fever'), ('Food Poisoning', 'V'), ('Food Poisoning', 'W'), ('Food Poisoning', 'F'))
print()
# OR
inputValueArr = ['fever','weakness','headache'] # input by patient

## list = [disease, symptom1, symptom2....]
list = [['Influenza', 'cough', 'headache', 'sore throat'],
        ['FoodPoisoning', 'weakness', 'fever','sore throat','headache'],
        ['Cancer', 'W', 'fever']]

val = 0
thisdoctor = "General"
percentArr = []
inputVal = 0

for i in range(3):
    for inputVal in inputValueArr:
        # print(inputVal)
        if inputVal in list[i]:
            val = val + 1
    percentArr.append(val)
    val = 0

# percentArr.sort()
highestPerValueFound = max(percentArr)
mostSuitableDisease = percentArr.index(highestPerValueFound)

# # Data fetch from doctor table
# doctor, disease1,disease2,disease3
doctorDisease = [['Dr Sattar','Influenza','d2','d3'],
                 ['Dr Fahad','Food Poisoning','d4','d5'],
                 ['Dr Maaz','d1','d2','d5']]
thisdoctor = doctorDisease[mostSuitableDisease][0]
print("inputval ",inputValueArr)
print("\n",thisdoctor)
