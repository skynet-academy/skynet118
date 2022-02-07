const form = document.getElementById('course_selection')
const image = document.getElementById('img-course')

//const getCookie = (name) =>{
//    let cookieValue = null;
//    if(document.cookie && document.cookie !== ''){
//        const cookies = document.cookie.split(';');
//        for(let i = 0; i < cookies.length; i++){
//            const cookie = cookies[i].trim();
//            if(cookie.substring(0, name.length + 1) === (name + '=')){
//                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
//                break
//            }
//        }
//    }
//    return cookieValue;
//}

let changeCourse = (selection) => {
    const csrftoken = getCookie('csrftoken')
    const request = new Request(
        "",
        {
            body: JSON.stringify(selection),
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
        }
    )
    fetch(request).then(function(response){
        console.log(`Working, the value is: ${selection}`);
    })
}

