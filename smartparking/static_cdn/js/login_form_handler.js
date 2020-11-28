
//checking for loginform and login button
if(loginButton && loginForm){

//attaching click eventlistener to login button
loginButton.addEventListener("click", function(event){

    //closing the login modal and sidenave
    $('#login').modal('close');
    $('.button-collapse').sideNav('hide');
   

    //displaying spinner
    spinnerWrapper.style.display="block";
    //creating form object
     const formData = new FormData(loginForm);
//delaying for two seconds
     setTimeout(async ()=>{

        //making apost request
        const response = await request(loginURL,'post',formData);
       
       //checking for success response
           if(response.data.status.trim("")==="success"){
            //generating path
            const pathname = window.location.pathname;
             //removing the spinner
             spinnerWrapper.style.display="none";
            //displaying message to user
               alert(response.data.message);
            //redirecting user
               window.location.href=`${window.location.protocol}//${window.location.host}` +`${pathname}`;
            
               } 
               
             //checking for failed response  
            if(response.data.status.trim("")=="failed"){
                //hiding spinner
                spinnerWrapper.style.display="none";
                //displaying message to user
                alert(response.data.message);
            }
       

     },2000)
  

   })

}