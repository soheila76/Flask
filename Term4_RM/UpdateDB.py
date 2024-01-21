import pymongo
client=pymongo.MongoClient("localhost",27017)
db=client.get_database("poulstar")
coll=db.get_collection("student")
all_data=coll.find({},{'_id':0})
for value in all_data:
    # print(value)
    print(f"name: {value['name']:<15}lastname: {value['lastname']:<20} age: {value['age']:<10} term: {value['term']:<10}")

#اپدیت رو اینجا تمرین کن 
    


    