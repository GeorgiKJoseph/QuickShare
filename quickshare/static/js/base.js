function app_subtitle_ani(os, device){
    var flag = 0;
    window.setInterval(function(){
        if (flag ==0){
            document.getElementById('subtitle').innerHTML = os;
            flag = 1;
        }
        else{
            document.getElementById('subtitle').innerHTML = device;
            flag = 0;
            document.getElementById('subtitle').style.display='subtitle_ani';
        }
    },3000);
}