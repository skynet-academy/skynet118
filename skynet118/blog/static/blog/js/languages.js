function getCookie(name){
    let cookieValue = null;
    if(document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for(let i = 0; i < cookies.length; i++){
            const cookie = cookies[i].trim();
            if(cookie.substring(0, name.length + 1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break
            }
        }
    }
    return cookieValue;
}

const changeLanguage = (val, url) =>{
    const csrftoken = getCookie('csrftoken')
    //document.getElementById("set-language").submit(); 
    const payload = {
        "name": "nicolas humberto",
        "surname": "sulca vega",
        "age": "33"
    }
    const request = new Request(
        "",
        {
            body: JSON.stringify(payload),
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin'
        }
    )
    fetch(request).then(function(response){
        console.log(`working, the value is ${val}`)
    })
    const request2 = new Request(
        url,
        {
            body: JSON.stringify(val),
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
        }
    ) 
    fetch(request2).then(function(response){
        console.log(`working, the second value is ${val}`)
    })
}

