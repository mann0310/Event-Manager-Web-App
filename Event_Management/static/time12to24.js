const convertTime12to24 = time12h => {
     const [time, modifier] = time12h.split(" ");
    
     let [hours, minutes] = time.split(":");
    
     if (hours === "12") {
       hours = "00";
     }
    
     if (modifier === "PM") {
       hours = parseInt(hours, 10) + 12;
     }
    
     return `${hours}:${minutes}`;
   };
    
function innertext(){
  if(document.getElementById('event_id').value==0)
    document.getElementById('change').innerText="Login";
}
   
