
let timer;
//clearing out any timer
clearTimeout(timer);

//defining the comfirm alert function
function confirmalert(){

    //prompting user
    let userselection = confirm("Are you sure you want to logout?");


    //closing the create account modal and sidenav
    $('#create-account').modal('close');

    $('.button-collapse').sideNav('hide');

    //displaying the spinner
    spinnerWrapper.style.display="block";

    //waiting for 2 seconds
    timer = setTimeout(async ()=>{

   
    //checking for user choice
    if (userselection == true){
    
    //making a get request
    const response = await request(logoutURL,'get',formData=null);

        //checking for a successful response
        if(response.data.status.trim("")=="success"){

            const pathname=response.data.redirect;
            //hiding spinner
            spinnerWrapper.style.display="none";
            //alert message to user
            alert(response.data.message);

           //redirecting user
            window.location.href=`${window.location.protocol}//${window.location.host}` +`${pathname}`;
          
            
        }
     
      }

   

    },2000);

    if(userselection == false){

        spinnerWrapper.style.display="none";
       
        return;
       
    }    
    
}