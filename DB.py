import pymongo
import eel
from bson.binary import Binary
import pickle



# create a database connection
def connectToDB():
    print("connecting to database")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["reco"]
    global DBCollection
    DBCollection= mydb["StudentDetails"]



# inser record into database
def insertRecordToDB(student):
    print("inserting record")
    try:
        id = DBCollection.insert_one(student).inserted_id
    except pymongo.errors.DuplicateKeyError as e:
        print(e)
        message="we could not insert your record"
        eel.errorMessage(message)
        return None
    message="student added to database"
    eel.successMessage(message)

    return id


# get all encodings from DB
def queryAllEncodingsFromDB():
    students=list(DBCollection.find({},{"_id":1, "Encoding":1}))
    print(students)
    encodingsList=[]
    encodingIdList=[]
    for st in students:

        npArrayEncoding=pickle.loads(st["Encoding"])
        encodingsList.append(npArrayEncoding)
        encodingIdList.append(st["_id"])

    return encodingsList,encodingIdList

def queryOneRecordFromDB(name):
    # the name should be an ID , get more details from database
    myquery = {"_id": name}
    student = DBCollection.find_one(myquery)
    return student