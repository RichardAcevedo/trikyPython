let tab = new Array(9);
for(let aa=0; aa<tab.length;aa++){
    tab[aa]=0;
}


window.onload = function(){

document.getElementById("block_0").addEventListener("click",movimiento);
document.getElementById("block_1").addEventListener("click",movimiento);
document.getElementById("block_2").addEventListener("click",movimiento);
document.getElementById("block_3").addEventListener("click",movimiento);
document.getElementById("block_4").addEventListener("click",movimiento);
document.getElementById("block_5").addEventListener("click",movimiento);
document.getElementById("block_6").addEventListener("click",movimiento);
document.getElementById("block_7").addEventListener("click",movimiento);
document.getElementById("block_8").addEventListener("click",movimiento);

function movimiento(event){
  


    let idele = event.target.id

    let va = idele.split("_");
    let val = va[1];
    console.log(tab);

    if(tab[val]===0){
        let ele = document.getElementById(idele);
        console.log(val);
        ele.innerHTML = '<ion-icon name="close-outline"></ion-icon>';
        tab[val]=1;
        let data = {celda : val}
        let heads = new Headers();
        heads.append("Accept","application/json");
        heads.append("Content-Type","application/json");
    
        let init= {
            method : 'POST',
            mode: 'cors',
            body:JSON.stringify(data),
            headers: heads
        };
    
        let url = "localhost:3000"
    /*
        fetch(url,init)
        .then((resp)=> resp.json())
        .then(function(data){
    
    
        })
    */

    } 

}


}

