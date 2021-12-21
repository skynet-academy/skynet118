const getCSRFTokenCookie = (name) =>{
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
    const csrftoken = getCSRFTokenCookie('csrftoken')
    //payload = document.getElementById("set-language").elements; 
	document.getElementById("set-language").submit();
    const request = new Request(
        url,
        {
            //body: payload,
            body: JSON.stringify(val),
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
        }
    ) 
    fetch(request).then(function(response){
        console.log(`working, the second value is ${val}`)
    })
}
