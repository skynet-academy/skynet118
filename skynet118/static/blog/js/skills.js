let button = document.getElementById('add_skills')
let skills = document.getElementById('skillAdded')
let allSkills = document.getElementById('id_skills') 

let options = ["Basic", "Intermediate", "Advanced"]

let addSkills = () => {
    button.disabled = true
    let myDiv = document.createElement("div")
    let myInp = document.createElement("input")
    let mySelect = document.createElement("select")
    mySelect.id = "mySelection"
    for(let i = 0; i < options.length; i++){
        let option = document.createElement("option")
        option.value = options[i]
        option.text = options[i]
        mySelect.appendChild(option)
    }
    let myButton = document.createElement("button")
    myButton.type = "button"
    myButton.innerHTML = "create skill"
    myInp.placeholder = " Add your skill"
    myDiv.appendChild(myInp)
    myDiv.appendChild(mySelect)
    myDiv.appendChild(myButton)
    let buttonskills = document.getElementById("skillButtons")
    buttonskills.style.display = "initial"
    buttonskills.appendChild(myDiv)
    myButton.onclick = () =>{
        button.disabled = false
        let selected = document.getElementById("mySelection").value
        let li = document.createElement('li')
        console.log(myInp.value)
        console.log(selected)
        li.innerHTML = `${myInp.value} - ${selected}`
        skills.appendChild(li)
        data = {}
        for(let i = 0; i < skills.childNodes.length; i++){
            data[i] = skills.childNodes[i].textContent
            console.log(data[i])
        }
        allSkills.value = JSON.stringify(data)
        buttonskills.innerHTML = ""
    }
}
