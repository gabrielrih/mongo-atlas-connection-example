'''
    MongoDB Atlas connection test
    References:
        https://www.mongodb.com/docs/drivers/pymongo/
'''
from pymongo import MongoClient
from arguments import get_arguments
from sample import get_sample_json

def errorAndExit(exception):
    print(str(exception))
    exit(1)

# Getting information for connection
endpoint, username, password, database, collection = get_arguments()
conn_str_model = 'mongodb+srv://<username>:<password>@<endpoint>/<database>?retryWrites=true&w=majority'
conn_str = conn_str_model.replace('<username>', username).replace('<password>', password).replace('<endpoint>', endpoint).replace('<database>', database)

print("(+) Trying connection and retrieving server information")
client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())
except Exception as ex:
    errorAndExit(ex)

namespace = database + "." + collection
print("(+) Setting namespace " + namespace)
try:
    db = client[database]
    collection = db[collection]
except Exception as ex:
    errorAndExit(ex)

print("(+) Inserting document on " + namespace)
try:
    collection.insert_one(get_sample_json())
except Exception as ex:
    errorAndExit(ex)

print("(+) Retrieving data on " + namespace)
try: 
    data = collection.find_one()
    print(data)
except Exception as ex:
    errorAndExit(ex)

print("(+) Deleting data on " + namespace)
try:
    collection.delete_one({"_id": data["_id"]})
except Exception as ex:
    errorAndExit(ex)