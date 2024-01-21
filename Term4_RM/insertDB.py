import pymongo

def DB_Check():
    client=pymongo.MongoClient("localhost",27017)
    db=client.get_database("poulstar")
    coll=db.get_collection("teacher")
    coll.insert_one({"name":name,"lastname":lastname,"age":age})
    print("done....")

name=input("name:")
lastname=input("last name:")
age=int(input("age:"))
DB_Check()
