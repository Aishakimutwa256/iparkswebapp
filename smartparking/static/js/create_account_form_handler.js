
//attaching event listener tp createaccount form
createAccountButton.addEventListener("click",function(event){

    //creating a form object
     const formData = new FormData(createAccountForm);

     //hiding the create-account modal and sidenavebar
    $('#create-account').modal('close');
    $('.button-collapse').sideNav('hide');
   
    // displaying the spinner
    spinnerWrapper.style.display="block";

    //dealaying 2 seconds
    setTimeout(async ()=>{

        //making a post request
        const response = await request(createAccountURL,'post',formData);


        //checking for a successful response
        if(response.data.status.trim("")=="success"){

            //hiding the spinner
            spinnerWrapper.style.display="none";

            //giving feedback to user
            alert(response.data.message);
        

        }
        
        //checking for failed response status
        if(response.data.status.trim("")=="failed"){

            //hiding spinner
            spinnerWrapper.style.display="none";

            //alerting error message
            errorAlert(response);
            
        }
            },2000);  
   
   });



