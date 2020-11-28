
//iterating through the nodelist
Object.values(bookButtons).map((button)=>{
    
    //adding event listener to each book button
    button.addEventListener("click", function(event){
         
        //checking for the button trigering the click event 
        if(event.target==button){

            //slot id
            const slot_id =button.getAttribute("data-slot_id");
           
            // const bookingsFormHandler = document.slot-form-slot_id;
            const formId =`#bookings-details-form-${slot_id}`;
            const bookingsFormHandler =document.querySelector(formId);
            
            const start = bookingsFormHandler.elements.start.value;
            console.log(start)
            const end = bookingsFormHandler.elements.end.value;


            //slot identity modal name
            const modal_id =`#slot-${slot_id}`;

            //creating form data object to handle form data for booking details
            const formData = new FormData(bookingsFormHandler);
            
            //appending slot id to formobject
            formData.append("slot_id",slot_id);

            //closing the booking modal
            $(modal_id).modal('close');

           //displaying the spinner
            spinnerWrapper.style.display="block";
            
            //waiting for two seconds
            setTimeout(async()=>{

            //making a post request and waiting for response

            const response = await request(bookingURL,'post',formData);

            //checking for response status
            if(response.data.status.trim("")==="success"){
            
            //hiding the spinner
            spinnerWrapper.style.display="none";

            //getting the pathname
            const pathname = response.data.redirect;
            
            //redirecting the user
            window.location.href= `${window.location.protocol}//${window.location.host}${pathname}`;


}           

    },2000);
            
        }
 

});
})

