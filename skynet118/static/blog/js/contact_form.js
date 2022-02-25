let divForm = document.getElementById('id01')
let openFormCont = document.getElementById('open-form-contact')
let contactUs = document.getElementById('contact-us')

function getCookie(name){
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?••
            if (cookie.substring(0, name.length + 1) === (name + '='))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


const csrftoken = getCookie('csrftoken');


let sendForm = () =>{


}


divForm.addEventListener('submit', function(e){
    let name_parent = document.getElementById('name-contact-parent').value
    let phone = document.getElementById('phone-contact-student').value
    let age_name_student = document.getElementById('age-name-student').value

    e.preventDefault();
    divForm.style.display = 'none';
    let url = ''
    fetch(url,{
        method: 'POST',
        headers: {'Content-type': 'application/json', 'X-CSRFToken': csrftoken},
        body: JSON.stringify({})
        }
    )
)


