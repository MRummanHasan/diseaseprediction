import io

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

inputVal = "S1" 
# list = [disease, symptom1, symptom2....]
list = [["D1","S1","S2","S3"],
        ["D2","S1","S2","S3"],
        ["D3","S1","S2","S3"]]
highestPer = 0
val = 0
thisDoctor = "General"
for i in range(2):
    for j in range(3):
        if inputVal in list[i][j]:
            val = val + 1
            per=float(val)*(100/10) # divide by avg#OfDisease; Make function for that
        else:
            continue
        
        if (per > highestPer):
            highestPercent = per
            thisDoctor = list[i][0]
        else:
            continue


print(inputVal)
print(highestPer)
print(per)
print(thisDoctor)