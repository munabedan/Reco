import face_recognition
import cv2

# format image
def formatImageFrame(mediaFrame):
    resizedImg = cv2.resize(mediaFrame, (0, 0), None, 0.25, 0.25)
    resizedImg = cv2.cvtColor(resizedImg, cv2.COLOR_BGR2RGB)
    return resizedImg

# get encoding for faces in frame
def encodeFaceInFrame(resizedImg,facesInFrame):
    encodedFacesInFrame = face_recognition.face_encodings(resizedImg, facesInFrame)
    return  encodedFacesInFrame

def getFacesInFrame(resizedImg):
    facesInFrame = face_recognition.face_locations(resizedImg)
    return facesInFrame



