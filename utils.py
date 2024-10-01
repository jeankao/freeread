from pymongo import MongoClient
def get_db_handle(read, localhost, 27017, jeankao, John5543):

 client = MongoClient(host=localhost,
                      port=int(27017),
                      username=jeankao,
                      password=John5543
                     )
 db_handle = client['read']
 return db_handle, client