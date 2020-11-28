const activeSlotSection = document.querySelector(".table-slots");

if(activeSlotSection){


//structuring slots data
const active_slots =object_data=>{

  const newSlots_object={...object_data};
  
  const slots_arr=Object.keys(newSlots_object).map(key=>{

    const value = newSlots_object[key];
    const newKey = key.split("_").join(" ");
    const capitalizedNewKey = newKey.trim().charAt(0).toUpperCase() + newKey.slice(1);
    const  capitalizedNewValue =value.trim().charAt(0).toUpperCase() + value.slice(1);

    return [capitalizedNewKey,capitalizedNewValue];

  });

  return slots_arr
}

//removing child nodes tablebody

const clearChildnodes=()=>{
  
  Object.values(activeSlotSection.children)
      .map(child=>{
        
        child.remove();
        
      })

      

}


//inserts table nodes/rows
const display_active_slots=data=>{

    const dataArr = active_slots(data);
    clearChildnodes();

    let classname="";

    dataArr.map(function(data){

              
   if(data[1].trim() ==="Parked"){

        classname = "red-text lighten-6";

    }

    if(data[1].trim() === "Not parked"){

        classname = "blue-text lighten-8";

    }


  
      let content =`<tr>
      <td class="blue-text darken-3">${data[0]}</td>
      <td  class=${classname}>${data[1]}</td>
      </tr>`
      activeSlotSection.insertAdjacentHTML('beforeend',content);

    })
    
}


ref.on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {
    var childData = childSnapshot.val();
    display_active_slots(childData);
  
  });

});

}







