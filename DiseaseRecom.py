import io
import pymysql

# data from DB(bridge table);
# populate that data in List of Array;
# check most match with symptoms;
# Match it to doctor profile
# display doctor

# objects = []
# Influenza = {"cough", "fever", "headache"}
# Diarrhea = {"motion", "stomach pain"}
# objects.sort()
# objects.insert(1,Influenza)
# objects.insert(2,Diarrhea)
# objects.append(Influenza)
# print(objects)
# [disese, s1, s2]

# fetch data from junction table
# connection work
conn = pymysql.connect(host='localhost', user='root', password='', db='HealthSystem')
a = conn.cursor()
# end connection work
# Query

# sql = 'SELECT D.*, S.* FROM diseases D JOIN disease_symptoms_bridgetable DC ON D.disease_id = DC.disease_id JOIN symptoms S ON S.symptom_id = DC.symptom_id'
sql = 'SELECT D.disease_name, S.symptom_name FROM diseases D INNER JOIN disease_symptoms_bridgetable DC ON D.disease_id = DC.disease_id INNER JOIN symptoms S ON S.symptom_id = DC.symptom_id'
      # GROUP BY D.disease_name'

# 'SELECT D.disease_name, S.symptom_name FROM diseases D '
#     INNER JOIN disease_symptoms_bridgetable DC
#         ON D.disease_id = DC.disease_id
#     INNER JOIN symptoms S
#         ON S.symptom_id = DC.symptom_id'
a.execute(sql)
data = a.fetchall()
print(data)
print()

# wordcount={}
for d in data:

#     for word in d:
#         if word not in wordcount:
#             wordcount[word] = 1
#         else:
#             wordcount[word] += 1
#     print (word,wordcount)

    wordcount = {}
    for word in d:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    for key in wordcount.keys():
        print("%s %s " % (key, wordcount[key]))


inputVal = "fever"
# list = [disease, symptom1, symptom2....]
list = [["D1","fever","S2","S3"],
        ["D2","S1","S4","S5"],
        ["D3","S1","S2","S5"]]
highestPer = 0
val = 0
thisDisease = "General"
percentArr = []
per = 0
for i in range(2):
    for j in range(3):
        if inputVal in list[i][j]:
            val = val + 1
            per=float(val)*(100/10) # divide by avg#OfDisease; Make function for that
        else:
            continue
        
    if (per > highestPer):
        highestPercent = per
    else:
        continue
    
    percentArr.append(per)

percentArr.sort()

highestPerValueFound = max(percentArr)
mostSuitableDisease = percentArr.index(highestPerValueFound)

# doctor ka table 





print(inputVal)
print(highestPer)
print(per)
print(thisDisease)

print(percentArr)
print(mostSuitableDisease)