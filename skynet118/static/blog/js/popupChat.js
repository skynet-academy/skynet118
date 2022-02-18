let openButton = document.querySelector('.open-button')
let createRipples = () =>{
    let ripple = document.createElement('span');
    openButton.appendChild(ripple);
    setTimeout(() =>{
        ripple.remove();
    }, 1000);
}
setInterval(createRipples, 2000);


let openChat = () =>{
    let chatPopUp = document.querySelector('.chat-popup');
    let openPopUp = document.querySelector('.open-button');
    let closeChat = document.querySelector('.close-button');

    closeChat.style.display = "block";
    openPopUp.style.display = "none";
    chatPopUp.style.display = "flex";
}

let closeForm = () =>{
    let openPopUp = document.querySelector('.chat-popup-links');
    let close  = document.querySelector('.form-container');
    close.style.display = "none";
    openPopUp.style.display = "flex";
}

let closeChat =()=>{
    let closeChat = document.querySelector('.close-button');
    let openPopUp = document.querySelector('.open-button');
    let closePopUp = document.querySelector('.chat-popup');

    openPopUp.style.display = "block";
    closeChat.style.display = "none";
    closePopUp.style.display = "none";
}

let openForm = document.getElementById('openForm')
openForm.addEventListener(
    'click',
    function(){
        let chatPopUp = document.querySelector('.chat-popup-links')
        let formContainer = document.querySelector('.form-container')
        chatPopUp.style.display = "none";
        formContainer.style.display = "block";
    }
)
