var toggled = false;
        function toggle(){
            if(!toggled){
                toggled = true;
                document.querySelector('.main_ul').style.left = "0px";
                return;
            }
            if(toggled){
                toggled = false;
                document.querySelector(".main_ul").style.left = "-60%";
                return;
            }
        }