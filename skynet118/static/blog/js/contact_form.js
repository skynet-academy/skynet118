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

openFormCont.addEventListener('click', function(e){
    e.preventDefault();
    divForm.style.display = 'block';
    //let url = '/client_contact/';
    //fetch(url,{
    //    method: "GET",
    //    headers: {"Content-type": "application/json"}
    //})
})


divForm.addEventListener('submit', function(e){
    let name_parent = document.getElementById('name-contact-parent').value
    let phone_number = document.getElementById('phone-contact-student').value
    let age_name_student = document.getElementById('age-name-student').value
    let errors_form = document.getElementById('errors-form')

    e.preventDefault();
    let url = '/client_contact/';
    fetch(url,{
        method: "POST",
        headers: {'Content-type': 'application/json', 'X-CSRFToken': csrftoken},
        body: JSON.stringify({
            'name_parent': name_parent,
            'phone_number': phone_number,
            'age_name_student': age_name_student
        })
    })
        .then(async (response) => {
            const isJson = response.headers.get('content-type')?.includes('application/json');
            data = isJson ? await response.json(): null;
            if(!response.ok){
                const errors = (data  && data.message) || response.status;
                console.log(errors)
            }
            else{
                divForm.style.display = 'none';
            }
            for(let key in data.errors){
                errors_form.innerHTML += `<p>${data.errors[key][0]}</p>`
            }
        })
        .catch((errors) =>{
            console.log(errors)
        })
})


