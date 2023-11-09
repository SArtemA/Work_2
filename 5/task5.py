import csv
import numpy as np
import json
import pickle
import msgpack
import os

def most_common(spis):
    slov ={}
    for cri in spis:
        if cri in slov:
            slov[cri] += 1
        else:
            slov[cri] = 1
    return [(key,value) for key, value in slov.items() if value == max(slov.values())][0]

def saver(stat):
    with open("Crime_Data.json", "w") as r_json:
        r_json.write(json.dumps(stat))

    with open("Crime_Data.pkl", "wb") as f:
        f.write(pickle.dumps(stat))

    with open('Crime_Data.csv', 'w', encoding="utf-8", newline='') as result:
        writer = csv.writer(result, delimiter=',', quotechar='*', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(stat.keys())
        writer.writerow(stat.values())

    with open("Crime_Data.msgpack", "wb") as r_msgpack:
        r_msgpack.write(msgpack.dumps(stat))
    print("Size:")
    print(f"csv        = {os.path.getsize('Crime_Data.csv')}")
    print(f"json       = {os.path.getsize('Crime_Data.json')}")
    print(f"msgpack    = {os.path.getsize('Crime_Data.msgpack')}")
    print(f"pickle     = {os.path.getsize('Crime_Data.pkl')}")


crime_stat = {}

sex = []
sex_n = []

age=[]
age_n = []

crimes = []

weapons = []
weapons_n = []

with open("Crime_Data_TOP_100.csv", encoding='utf-8') as r_file:
    file_reader = list(csv.reader(r_file, delimiter = ","))
    lines_amount = 100
    first_100 = file_reader[1:lines_amount+1:]
    headers = file_reader[0]
    for line in first_100:
        sex.append(line[12])
        age.append(line[11])
        crimes.append(line[9])
        weapons.append(line[17])

    for rec in age:
        try:
            if len(rec)<=3 and rec.isdigit():
                age_n.append(int(rec))
        except:
            print("e")

    for rec in weapons:
        try:
            if rec!= '':
                weapons_n.append(rec)
        except:
            print("e")

    for rec in sex:
        try:
            if len(rec)<=2 and rec.isalpha() and rec!="X":
                sex_n.append(rec)
        except:
            print("e")


    crime_stat["Max age of victim"] = max(age_n)
    crime_stat["Min age of victim"] = min(age_n)

    crime_stat["Average age of victim"] = sum(age_n)/len(age_n)
    crime_stat["Standard deviation of age of victim"] = np.std(age_n)

    crime_stat["Most common victim's sex"] = most_common(sex_n)[0]
    crime_stat["Most common victim's sex,%"] = most_common(sex_n)[1]/lines_amount * 100

    crime_stat["Most common victim's age"] = most_common(age_n)[0]
    crime_stat["Most common victim's age,%"] = most_common(age_n)[1] / lines_amount * 100

    crime_stat["Most common crime"] = most_common(crimes)[0]
    crime_stat["Most common crime,%"] = most_common(crimes)[1] / lines_amount * 100

    crime_stat["Most used weapon"] = most_common(weapons_n)[0]
    crime_stat["Most used weapon,%"] = most_common(weapons_n)[1] / lines_amount * 100


    saver(crime_stat)







