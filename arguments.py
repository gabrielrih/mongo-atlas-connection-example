import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='Mongo Atlas Connection Test')
    parser.add_argument('--user', '-u', help='Username', required=True)
    parser.add_argument('--password', '-p', help='Password', required=True)
    parser.add_argument('--endpoint', '-e', help='MongoDB Atlas Endpoint. Ex: nonprod-track-trace-pl-2.vmcki.mongodb.net', required=True)
    parser.add_argument('--database', '-d', help='Database name (OPTIONAL)', required=False)
    parser.add_argument('--collection', '-c', help='Collection name (OPTIONAL)', required=False)
    args = parser.parse_args()
    database = args.database
    if database == None:
        database = 'testing'
    collection = args.collection
    if collection == None:
        collection = 'testing'
    return args.endpoint, args.user, args.password, database, collection