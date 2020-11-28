//making axios requests handler
const request =async (url,reqType,formData)=>{

    //making axios request
    const response= await axios({
        method:reqType,
        url:url, 
        data:formData,
        headers: {                            
        "X-CSRFToken": CSRF_TOKEN, 
         "content-type":"application/json"
        }
    });
//returning response
  return response;
};


//error message helper
const errorAlert=(response)=>{

  const errors = JSON.parse(response.data.errors);
  //converting eeror object to an array
  const fields = Object.keys(errors);
  //iterating through fields array
  const errorMessages =fields.map((fieldname)=>{
      //creating amessage for user
      const errorMessage = errors[fieldname][0].replace(errors[fieldname][0].split(" ")[0],fieldname);
      //returning the error message
      return errorMessage;
      
  });



  const message = errorMessages.reduce((accumulator,item)=>{
  
      return accumulator+=`\n ${item}`;

  }, "");

  alert(message);
}


