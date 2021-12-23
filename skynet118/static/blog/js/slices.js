let stack = 0;
let len = document.querySelectorAll('.course').length;

let carrusel = (stack, len) => {
    resetCarrusel(len)
    let container = document.querySelector('.course-' + stack)
    let checkbutton = document.getElementById('radio' + stack)
    checkbutton.checked = true;
    container.style.display = "initial";
    container.style.zIndex = stack;
    container.style.left = "0%";
} 


let resetCarrusel = (len) => {
    for(let i = 1; i <= len; i++){
        let container = document.querySelector('.course-' + (len - i + 1));
        container.style.display = "none";
        container.style.zIndex = -i; 
        container.style.left = "100%";
    }
}
let valueInput = (value) =>{ 
    resetCarrusel(stack)
    stack = value.target.value
    carrusel(stack, len)

}
radioButtons = document.getElementsByName('radio-btn')
radioButtons.forEach(item => item.addEventListener('click', valueInput))

document.querySelector('.left-arrow').onclick = () =>{ 
    let radiosArray1 = document.getElementsByName('radio-btn');
    let lenArray1 = radiosArray1.length;
    let before;
    for(let i = 0; i < radiosArray1.length; i++){
        if(radiosArray1[i].checked){
            before = parseInt(radiosArray1[i].value) - 1;
            if(before == 0){
                before = lenArray1;
            }
        }
    }
    resetCarrusel(lenArray1)
    carrusel(before)
}

document.querySelector('.right-arrow').onclick = () =>{ 
    let radiosArray2 = document.getElementsByName('radio-btn');
    let lenArray2 = radiosArray2.length;
    let next;
    for(let i = 0; i < radiosArray2.length; i++){
        if(radiosArray2[i].checked){
            next = parseInt(radiosArray2[i].value) + 1;
            if(next == lenArray2 + 1){
                next = 1;
            }
        }
    }
    resetCarrusel(lenArray2)
    carrusel(next)
}

setInterval(function(){
    stack++; 
    if(stack > len){
        resetCarrusel(len)
        stack = 1
    }
    carrusel(stack, len);
}, 5000);
