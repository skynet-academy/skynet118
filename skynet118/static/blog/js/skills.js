 let create_skill = () =>{
     let skillAdded = document.getElementById("skill-added")
     let myDiv = document.createElement("div")
     let myInput = document.createElement("input")
     let myButton = document.createElement("button")
     myInput.placeholder = " type your skill"
     myButton.innerHTML = "Add skill"
     myButton.type = "button"
     myButton.onclick = addSkill
     myDiv.appendChild(myInput)
     myDiv.appendChild(myButton)
     skillAdded.appendChild(myDiv)
 }
