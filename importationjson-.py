from pymongo import MongoClient
import json


client = MongoClient("mongodb://localhost:27017/")

json_file = input("Fichier .json à insérer ?")

#'C:/Users/utilisateur/Google Drive/brief stephane/covers.json'

list_covers = list(open(json_file, 'r'))

percent_count = 0
absolute_count = 0
error_count = 0

for line in list_covers:
    try:
        client.DBLP.publis.insert_one(json.loads(line))
    except:
        error_count += 1
        print(error_count, "error(s)")
        pass
    absolute_count +=1
    if int((absolute_count / len(list_covers)) * 100) > percent_count:
        percent_count += 1
        print(percent_count, "%")                           