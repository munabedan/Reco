# import all the necessary libraries
import time
import cv2
import numpy
import numpy as np
import face_recognition
import os
from datetime import datetime
import eel
import DB
import utils
import face
import time



# # convert the images to rgb and encode them
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodedImg = face_recognition.face_encodings(img)[0]

        print(encodedImg)
        encodeList.append(encodedImg)
    return encodeList


# # record the attendace
def recordAttendance(name):
    with open('records.csv', 'w+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dateTimeString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dateTimeString}')


# initialise execution

# initialise eel files
eel.init('public', allowed_extensions=['.js', '.html'])
DB.connectToDB()



# load known encodings
#DB.queryAllEncodingsFromDB()
#print(len(encodedListOfKnownImages))



#stop face recognition
@eel.expose()
def stopAppLoop():
    global appLoopStatus
    appLoopStatus='stop'
    print('stop reading media ')

@eel.expose
def appLoop():
    encodedListOfKnownImages, studentIdList = DB.queryAllEncodingsFromDB()
    print(encodedListOfKnownImages)
    print(studentIdList)
    # start webacam media stream
    mediaStream = cv2.VideoCapture(0)
    global appLoopStatus
    appLoopStatus = 'run'
    # start app loop
    while(appLoopStatus == 'run' ):
        print(appLoopStatus)

        #read mediaframes webcam media stream
        success, mediaFrame = mediaStream.read()
        print("read media")
        #send mediaframe to ui client
        eel.updateVideoStream(utils.mediaConversion(mediaFrame))()

        #optimization: resize image frame
        resizedImg=face.formatImageFrame(mediaFrame)

        #search for faces in frame
        facesInFrame=face.getFacesInFrame(resizedImg)

        #generate encodings for all faces in frame
        encodedFacesInFrame=face.encodeFaceInFrame(resizedImg,facesInFrame)

        #loop through the faces in frame
        for encodeFace, faceLoc in zip(encodedFacesInFrame, facesInFrame):

            #query for matching faces
            matches = face_recognition.compare_faces(encodedListOfKnownImages, encodeFace)
            faceDis = face_recognition.face_distance(encodedListOfKnownImages, encodeFace)
            matchIndex = numpy.argmin(faceDis)

            if matches[matchIndex]:
                print("match found")

                studentIdMatch = studentIdList[matchIndex]

                studentRecords=DB.queryOneRecordFromDB(studentIdMatch)

                eel.showContent(studentRecords['_id'], studentRecords['Name'], studentRecords['School'], studentRecords['Department'])
                time.sleep(3)
                eel.clearContent()
        #eel.sleep(0.0001)
        if appLoopStatus == 'stop':
            break
    mediaStream.release()
    print("camera released")

# start the eel web server
print("start webserver")
eel.start('index.html')#, block=False)
