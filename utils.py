import cv2
import base64
import eel
import DB
from urllib import request
from urllib.parse import urlparse
import numpy
import face_recognition
from bson.binary import Binary
import pickle

#display webcam video stream
def mediaConversion(mediaFrame):
    # send mediaFrame to browser window
    ret, jpeg = cv2.imencode('.jpg', mediaFrame)
    jpegByteStream = jpeg.tobytes()

    # Convert bytes to base64 encoded str, as we can only pass json to frontend
    imgFrameBlob = base64.b64encode(jpegByteStream)
    imgFrameBlob = imgFrameBlob.decode("utf-8")

    return imgFrameBlob


# Add new user
@eel.expose
def addNewUser(studentPhoto,studentName,studentID,studentDepartment,studentSchool):

    data=studentPhoto.split(',')
    print(data[1])
    from binascii import a2b_base64

    data = data[1]
    binary_data = a2b_base64(data)


    fd = open('image.png', 'wb')
    fd.write(binary_data)
    fd.close()
    # get image


    img = cv2.imread('image.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    try:
        imgEncoding = face_recognition.face_encodings(img)[0]
    except IndexError as e:
        print(e)
        message="we could not detect your face"
        eel.errorMessage(message)
        return None

    print(imgEncoding)
    imgEncodingBinary=Binary(pickle.dumps(imgEncoding,protocol=2),subtype=128)

    studentDetails={
        "_id": studentID,
        "Name": studentName,
        "Department": studentDepartment,
        "School": studentSchool,
        "Encoding": imgEncodingBinary
    }
    print(studentDetails)
    DB.insertRecordToDB(studentDetails)

