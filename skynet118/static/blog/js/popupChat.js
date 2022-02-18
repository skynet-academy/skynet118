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
    let chatPopUp = document.querySelector('.chat-popup')
    let openPopUp = document.querySelector('.open-button')
    openPopUp.style.display = "none"
    chatPopUp.style.display = "block";
}
let closeForm = () =>{
    let closePopUp = document.querySelector('.chat-popup')
    let openPopUp = document.querySelector('.open-button')
    openPopUp.style.display = "block"
    closePopUp.style.display = "none";
}

