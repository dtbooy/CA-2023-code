// // temp1.innerText = "Heloo"

// // Old way of getting elements
// const el1 = document.getElementById("Foo")
// el1.innerHTML = "Hello <span style='color: red'>World</span>"

// // Selects the first element
// const el2 = document.querySelector('li')

// // Selects all the elements 
// const el3 = document.querySelectorAll('li')
// console.log(el2)
// console.log(el3)


// // Create element
// const newDiv = document.createElement('div')
// newDiv.innerHTML = "<h3> Hello World </h3>"
// newDiv.style.color = "blue"
// newDiv.id = "spam"

// // assign element to a position in the DOM

// // append to the end of the body
// document.body.appendChild(newDiv)

// // append to the end of another elemnet
// document.querySelector("ul").appendChild(newDiv)

// // append to the end of the body
// document.body.insertBefore(newDiv, document.querySelector('ul'))

// // if you want to add somehting to the end of the document you can just append the body HTML
// const myColor = "blue"
// document.body.innerHTML += `<div id="spam" style="color: ${myColor}><h3>Hello World</h3></div>`

// Lets make dynamic content

const items = [
"Adding to the DOM",
"Querying the DOM",
"Changing the DOM",
"Event listeners"
]

const ul = document.querySelector('ul')

// for (let item of items) {
//     ul.innerHTML += `<li>${item}</li>`
//     // const newLi = document.createElement('li')
//     // newLi.innerText = item
//     // document.body.querySelector("ul").appendChild(newLi)
// }

// or
ul.innerHTML += items.map(item => `<li>${item}</li>`).join("")


// Asyncronous 

// Handle a mouse click on the <h1> element
// document.querySelector("h1").addEventListener("click", (event) => {event.target.innerHTML += "!"});


const newItem = document.querySelector("#newItem")
const btn = document.querySelector("button")

btn.addEventListener("click", () => {
    ul.innerHTML += `<li>${newItem.value}</li>`
    newItem.value = ''
});

