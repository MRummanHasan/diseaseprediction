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
sql = 'SELECT D.disease_name, S.symptom_name FROM diseases AS D JOIN disease_symptoms_bridgetable AS DC ON D.disease_id = DC.disease_id JOIN symptoms AS S ON S.symptom_id = DC.symptom_id'
# GROUP BY D.disease_name'

# 'SELECT D.disease_name, S.symptom_name FROM diseases D '
#     INNER JOIN disease_symptoms_bridgetable DC
#         ON D.disease_id = DC.disease_id
#     INNER JOIN symptoms S
#         ON S.symptom_id = DC.symptom_id'
a.execute(sql)
# data = a.fetchall()
# print(data)
data = (('Influenza', 'fever'), ('Influenza', 'cough'), ('Influenza', 'headache'), ('Influenza', 'sore throat'), ('FoodPoisoning', 'vomiting'), ('FoodPoisoning', 'weakness'), ('FoodPoisoning', 'fever'), ('Food Poisoning', 'V'), ('Food Poisoning', 'W'), ('Food Poisoning', 'F'))
print()
# AVERAGE CALC FUNCTION

# wordcount = {''}
# MAINarr = []
# DS = []
# for word in data:
#     if word[0] not in wordcount:
#         MAINarr.append(DS)
#         print(word[0])
#         DS = [word[0]]
#         wordcount.add(word[0])
#     elif word[0] in wordcount:
#         print(word[1])
#         DS.append(word[1]) # wordcount[word] +=1
#         # print(DS)
# print()
# print(MAINarr)
# print(wordcount)


inputValueArr = ['fever','weakness','other']
## list = [disease, symptom1, symptom2....]
list = [['Influenza', 'cough', 'headache', 'sore throat'],
        ['FoodPoisoning', 'weakness', 'fever','sore throat','other'],
        ['Food Poisoning', 'W', 'fever']]

highestPer = 0
val = 0
thisDisease = "General"
percentArr = []
per = 0
inputVal = 0

# for inp in inputValueArr:
#     inputVal = inp
#     print(inputVal)
for i in range(3):
    for inputVal in inputValueArr:
        # print(inputVal)
        if inputVal in list[i]:
            val = val + 1
    print(val, "finalval")
    # if inputValueArr[0] in list[i]:
    #     val = val + 1
        # per=float(val)*(100/10) # divide by avg#OfDisease; Make function for that
    # if inputValueArr[1] in list[i]:
    #     val = val + 1
    # if inputValueArr[2] in list[i]:
    #     val = val + 1

    # if (val > highestPer): # per > highestPer
    #     highestPercent = val
    percentArr.append(val)
    val = 0

# percentArr.sort()
highestPerValueFound = max(percentArr)
mostSuitableDisease = percentArr.index(highestPerValueFound)

# # doctor ka table
# doctor, disease1,d2,d3
doctorDisease = [['Dr Sattar','Influenza','d2','d3'],
                 ['Dr Fahad','Food Poisoning','d4','d5'],
                 ['Dr Maaz','d1','d2','d5']]

print("inputval ",inputValueArr)
print("val ",val)
print("percentArr ",percentArr)

print(thisDisease)
print(mostSuitableDisease)

print(doctorDisease[mostSuitableDisease][0])

# wordcount={}
# for d in data:
#     for word in d:
#         if word not in wordcount:
#             wordcount[word] = 1
#         else:
#             wordcount[word] += 1
#     print (word,wordcount)

# for key in wordcount.keys():
#     print("%s %s " % (key, wordcount[key]))
# print(wordcount)

# wordcount = {'Influenza'}
# for word in data:
#
#     if word[0] not in wordcount:
#         print(word[0])
#         # wordcount[word] = 1
#     else:
#         print(word[1])
#         # wordcount[word) += 1
#         DS = [word]
#         DS.append(word[1])
#         # wordcount[word]
#         print("asas")
#         print(DS)
# for key in wordcount.keys():
#     print("%s %s " % (key, wordcount[key]))


# for inp in inputValueArr:
#     inputVal = inp
#     for i in range(2):
#         for j in range(3):
#             if inputVal in list[i][j]:
#                 val = val + 1
#                 # per=float(val)*(100/10) # divide by avg#OfDisease; Make function for that
#             else:
#                 continue
#
#             if (val > highestPer): # per > highestPer
#                 highestPercent = val
#             else:
#                 continue
#     percentArr.append(val)
