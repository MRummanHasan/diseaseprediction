import io

# data from DB(bridge table);
# populate that data in List of Array;
# check most match with symptoms;
# Match it to doctor profile
# display doctor

objects = []

Influenza = {"cough", "fever", "headache"}
Diarrhea = {"motion", "stomach pain"}
objects.sort()
objects.insert(1,Influenza)
objects.insert(2,Diarrhea)

# objects.append(Influenza)
print(objects)
# [disese, s1, s2]