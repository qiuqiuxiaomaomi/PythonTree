from pymongo import MongoClient

con = MongoClient('&&', 27100)

db = con.material
myset = db.ponaparte
item = {
    "name":"xiaoxiao",
    "description":"good",
}
object_id =myset.insert_one(item).inserted_id
print object_id