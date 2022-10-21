import sys
import json
import pprint
import schema

class MigrateJson:
    def __init__(self, src_path, dest_path):
        self.src_path = src_path
        self.dest_path = dest_path


    def json_read_file(self):
        with open(self.src_path) as file:
            data = json.load(file)
            del data['attributes']
            # print(data)
        json_object = json.dumps(data, indent=4)
        with open(self.dest_path, "w") as outfile:
            outfile.write(json_object)
            print("schema file updated")

    def getSchema(self):
        with open(self.src_path) as data_file:    
            doc = json.load(data_file.read()) 
            return createSchema(doc)


migrate_object = MigrateJson('data/data_2.json', 'schema/schema_2.json')


migrate_object.json_read_file()

 

 
 





