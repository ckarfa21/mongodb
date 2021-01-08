import pymongo
import json
import requests


#La bibliothèque # pprint est utilisée pour rendre la sortie plus jolie

# se connecter à MongoDB, modifier le << MONGODB URL >> pour refléter votre propre chaîne de connexion
client = pymongo.MongoClient ('mongodb://localhost:27017/')

# Emettez la commande serverStatus et imprimez les résultats
#serverStatusResult = db.command ("serverStatus")
#pprint (serverStatusResult)
#Par le biais de l'objet ainsi créé (client), on a accès à la liste des bases de données présentes, avec la fonction database_name().
#client.database_names()
#print(client)
mabase=client["dblp"]
#print(mabase)
mycol=mabase["publis"]

#mydoc=mycol.count()
#print(mydoc)
#Lister tous les livres (type “Book”)
for x in mycol.find({ "type": "Book" }):
    #print(x)


    

#Lister les livres depuis 2014 ;
#for x in mycol.find({ "year" : { "$gt" : 2014}}):
    #print(x)

#Lister les publications de l’auteur “Toru Ishida” ;
#for x in mycol.find({ "authors" : "Toru Ishida"}):
    #print(x)


#Lister tous les auteurs distincts
    #mycol.distinct("authors") 
    #print(x)

#Compter le nombre de publications de Toru Ishida
# nbr_pub = mycol.count({ "authors" : "Toru Ishida" })
# print(nbr_pub)
#OU :
# for nombre_publications in mycol.aggregate([
# {"$match":{"authors" : "Toru Ishida"}}, {"$group":{"_id":"null", "total" : { "$sum" : 1}}}
# ]):
#     print(nombre_publications)

#Compter le nombre de publications depuis 2011 et par type

# for x in mycol.aggregate([{"$match":{"year" : {"$gte" : 2011}}}, {"$group":{"_id":"$type", "total" : { "$sum" : 1}}}]):
#     print(x)
    for nb_publications_auteur in mycol.aggregate([{ "$unwind" : "$authors" }, { "$group" : { "_id" : "$authors", "number" : { "$sum" : 1 } }}, 
    {"$sort" : {"number" : 1}}] ): 
        print(nb_publications_auteur)

  