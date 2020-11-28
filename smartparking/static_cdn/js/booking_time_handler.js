const periodSessionEl = document.querySelector("#booking-session");

if(periodSessionEl){
const periodSessionValue = periodSessionEl.value;
const bookingId          =document.querySelector("#booking-id-session").value;
let timerDisplay         =document.querySelector(".duration");
let bookingPeriod =new Date(periodSessionValue).getTime();

 let interval=setInterval(async ()=>{

    //getting current time
    let nowTime =Date.now();

    //gettimg remaining milliseconds
    let millisecondsInterval = bookingPeriod-nowTime;
  
    //getting days,hours,minutes and seconds
    const days =Math.floor(millisecondsInterval/(1000*60*60*24));

    const hours =Math.floor((millisecondsInterval%(1000*60*60*24))/(1000*60*60));

    const minutes =Math.floor((millisecondsInterval%(1000*60*60))/(1000*60));

    const seconds =Math.floor((millisecondsInterval%(1000*60))/(1000));

    //displaying the remaining time
    timerDisplay.innerHTML = ` ${hours}: ${minutes}: ${seconds}`;

    //checking if deadline is less or equal to current time
    if(bookingPeriod<=nowTime){
        clearInterval(interval);
        //updating the timer display to expired
        timerDisplay.innerHTML = "Expired";


        const url = `${window.location.protocol}//${window.location.host}/bookingslot/booking-expired/`;
        
        if(bookingId){
            
            const response = await request(url,'get',formData=null);
        
            if(response.data.status.trim("")=="success") {

                let timer =setTimeout(()=>{
                    timerDisplay.innerHTML = "IPARKS";
                    clearTimeout(timer);
                    return ;
                },80000)
                
            }

        }else{

            timerDisplay.innerHTML = "IPARKS";

        }
 

        return;
        
    }

},1000);




}