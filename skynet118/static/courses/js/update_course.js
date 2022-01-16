let course_name = document.getElementById("id_course_name")
course_name.placeholder = " Course Name"

let date_pub = document.getElementById("id_date_pub")
date_pub.type = "datetime-local"

let id_price = document.getElementById("id_price")
id_price.placeholder = " Price per lesson"

let id_nro_lessons = document.getElementById("id_nro_lessons")
id_nro_lessons.placeholder = " Number of lessons"

let id_nro_tests = document.getElementById("id_nro_tests")
id_nro_tests.placeholder = " Number of tests"

let details = document.getElementById("id_details")
let description = document.getElementById("id_description")
description.placeholder = " Add a course description"

let image = document.getElementById("id_image")

let topics = document.getElementById("id_topics")

let details_updated = document.getElementById("details_updated") 

let detailsAdded = document.getElementById("detailsAdded")
let topicsAdded = document.getElementById("topicsAdded")

let detailsButtons = document.getElementById("detailsButtons")

let modifyButton = document.getElementById("modifyButton")
let modifyButton2 = document.getElementById("modifyButton2")

details.style.display = "none"
topics.style.display = "none"

let modifyDetails = () => {
    modifyButton.disabled = true
    let myDiv = document.createElement("div")
    let myInp = document.createElement("input")
    let myButton = document.createElement("button")
    myButton.type = "button"
    myButton.innerHTML = "create a detail"
    myInp.placeholder = " Add your detail"
    myDiv.appendChild(myInp)
    myDiv.appendChild(myButton)
    let detailsButtons = document.getElementById("detailButtons")
    detailsButtons.style.display = "initial"
    detailsButtons.appendChild(myDiv)
    myButton.onclick = () => {
        modifyButton.disabled = false
        let li = document.createElement('li')
        li.innerHTML = `${myInp.value}`
        detailsAdded.appendChild(li)
        data = {}
        for(let i = 0; i < detailsAdded.childNodes.length; i++){
            data[i] = detailsAdded.childNodes[i].textContent
        }
        details.value = JSON.stringify(data)
        detailsButtons.innerHTML = ""
    }
}

let modifyTopics = () =>{
    modifyButton2.disabled = true
    let myDiv = document.createElement("div")
    let myInp = document.createElement("input")
    let myButton = document.createElement("button")
    myButton.type = "button"
    myButton.innerHTML = "create a topic"
    myInp.placeholder = " Add your topic"
    myDiv.appendChild(myInp)
    myDiv.appendChild(myButton)
    let topicsButtons = document.getElementById("topicsButtons")
    topicsButtons.style.display = "initial"
    topicsButtons.appendChild(myDiv)
    myButton.onclick = () => {
        modifyButton2.disabled = false
        let li = document.createElement('li')
        li.innerHTML = `${myInp.value}`
        topicsAdded.appendChild(li)
        data = {}
        for(let i = 0; i < topicsAdded.childNodes.length; i++){
            data[i] = topicsAdded.childNodes[i].textContent
        }
        topics.value = JSON.stringify(data)
        detailsButtons2.innerHTML = ""
    }
    
}
