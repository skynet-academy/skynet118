const form = document.getElementById('course_selection')

const image = document.getElementById('img-course')



let changeCourse = (selection) =>{
    const xhr = new XMLHttpRequest();
    const url = "" 
    let success = ()=>{
        let info = document.querySelector('#intro');
        info.innerHTML = selection
    }
    let error = (err)=> console.log("Request Failed", err);
    xhr.onload = success 
    xhr.onerror = error
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.send(JSON.stringify({"hello": "ok"}));
}




