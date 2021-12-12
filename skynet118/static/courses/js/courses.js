let changeCourse = (selection) =>{
    const xhr = new XMLHttpRequest();
    const url = '/'
    let success = ()=>{
        let info = document.querySelector('#intro');
        info.innerHTML = selection
    }
    let error = (err)=> console.log("Request Failed", err);
    xhr.onload = success 
    xhr.onerror = error
    xhr.open("POST", url);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    xhr.send(selection);
}




