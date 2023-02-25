import pymongo 
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://Hrushikesh:rishi0707@cluster0.hadmu.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = ("/config/workspace/dataset_full.csv")
DATABASE_NAME = "pishing_domain"
COLLECTION_NAME = "pishing_detection"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


