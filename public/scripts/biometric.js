function startAnalysis() {
    eel.appLoop()
  }
  
  function stopAnalysis(){
    console.log('does this work??')
  
      eel.stopAppLoop()
    
  }
  
  function updateVideoStream(frameVal){
     let videoEL=document.getElementById("videoElement");
      videoEL.src = "data:image/jpeg;base64," + frameVal
  
  }
  function clearContent() {
    console.log("clearContent")
    document.getElementById("userData").innerHTML="";
  }
  
  function showContent(idNumber,name,school,department) {
    console.log("showContent")
      let card = ` 
      <div class="content">
      <div >
        <h3>${idNumber}</h3>
        <h2>${name}</h2>
        <p>${department}</p>
        <p>${school}</p>
  
      </div>
  
    </div>
  
  
    <div class="text-center text-lg-start">
      <a href="#"
        class="btn-read-more d-inline-flex align-items-center justify-content-center align-self-center">
        <span>Access Granted</span>
        <i class="bi bi-check2-square"></i>
      </a>
    </div>
     `;
  
     let spinnerContent=`
     <div class="spinner-border text-primary" id="spinner" role="status">
     <span class="visually-hidden">Loading...</span>
   </div>
     `;
  
     let cardHolder=document.getElementById("userData");
     let spinner=document.getElementById("spinnerHolder");
     cardHolder.innerHTML = cardHolder.innerHTML + card;
      spinner.innerHTML="";
    /* setTimeout(function(){
        cardHolder.innerHTML="";
        spinner.innerHTML=spinner.innerHTML+spinnerContent;
     }, 0);*/
    
  
     
  }
  eel.expose(showContent); // Expose this function to Python*/
  eel.expose(clearContent);
  eel.expose(updateVideoStream);
  //showContent("https://via.placeholder.com/150","muna bedan","smunbe1721","software")
  
  
  