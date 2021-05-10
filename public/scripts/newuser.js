//data set
let sphoto;


// Configure a few settings and attach camera 
Webcam.set({
    width: 320,
    height: 240,
    image_format: 'jpeg',
    jpeg_quality: 90
});
Webcam.attach('#my_camera');

function take_snapshot() {
    // take snapshot and get image data
    Webcam.snap(function (data_uri) {

        let imgNode=document.createElement('IMG')
        imgNode.setAttribute("id", "sphoto");
        imgNode.setAttribute("src", data_uri)
        document.getElementById('results').appendChild(imgNode)


        
    });
}

function submitUser(e){
    e.preventDefault();

    [studentPhoto,studentName,studentID,studentDepartment,studentSchool]=[
        document.getElementById('sphoto').src,
        document.getElementById('sname').value,
        document.getElementById('sid').value,
        document.getElementById('sdepartment').value,
        document.getElementById('sschool').value
    ]
   
    console.log(studentPhoto,studentName,studentID,studentDepartment,studentSchool)
    eel.addNewUser(studentPhoto,studentName,studentID,studentDepartment,studentSchool)
}

function successMessage(message) {
    document.getElementById('addsuccess').style.display='block'
    document.getElementById('addsuccess').innerText='sucess'+message

}
function errorMessage(message) {
    document.getElementById('adderror').style.display='block'
    document.getElementById('adderror').innerText='error'+message
}

eel.expose(submitUser);
eel.expose(errorMessage);
eel.expose(successMessage)