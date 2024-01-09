// // Print to terminal
// console.log("Hello World")
// // variable in JS are declared using camelCase
// const maxTemp = 28 // const enforces a contant - it will not allow you to change this variable once set

// console.log(maxTemp)
// maxTemp = 30
// console.log(maxTemp)

// let x = "Sarah" // implicit variable defined in JS - this makes it a global variable
// {
//     console.log(x)
//     console.log(42)
//     var y = 5
// }
// console.log(y)

// {
//     let str = 'Hello World'

//     // length is a property of a string
//     console.log(str.length) // >>> 11

//     // indexOf returns the index of input, if doesn't exist output is -1
//     console.log(str.indexOf("lo")) // >>> 3

//     // slice - same as python, returns slice of string
//     console.log(str.slice(6, -2)) // >>> "Wor"
//     // note: -1 numbering works in slices but not in indexing:
//     // console.log(str[-1] // >>> error

//     //replace - creates a new string with the replaced chars (first instance only)
//     console.log(str.replace('Hello', "Goodbye"))
//     // replaceAll - replace but for all elements that match
//     console.log(str.replaceAll('o', "---")) // >>> Hell--- W---rld

//     let name = "Jack"
//     //template string - uses backticks ` insteads of quotes ' "
//     console.log(`Hello, ${name}!`) // >>> Hello, Jack!
//     console.log(`Answer: ${5 * 10}!`) // >>> Answer: 50!
// }

// // Operators
// console.log(3 / 2) //>>> 1.5

// // Operators
// console.log(5 % 2) //>>> 1

// //integer division
// console.log(Math.floor(5/2)) //>>> 2

// // incrementing 
// let x = 5
// console.log(x)
// x++ // does the same thing as x+=1
// console.log(x)
// x--// does the same thing as x-=1
// console.log(x)
// console.log(x++) // this prints the value THEN increments it
// console.log(x)
// console.log(++x) // this increments the value THEN prints


// console.log(123 == "123") // >>> true
// console.log(123 === "123") // >>> false
// // use triple === to compare without type coercion

// console.log(typeof x) // >>> number

// // Dictionary!
// let person = { "name" : "Matt", "age" : 37}
// console.log(person.age)


//declare a normal function
// function add(x, y) {
//     return x + y
// }
// console.log(add(10,20))

// ;
// declare an arrow function (equivalent to a lambda function in Python)
// const Utils = {
//     add : (x, y) => x + y,
//     double : x => x * 2,
//     squares : arr => arr.map(x => x **2 )
// }

// console.log(Utils.add(10,20))

// // mapping
// const numbers = [10, 11, 12, 13, 14]

// /// you can add arrow 
// result = Utils.squares(numbers)
// console.log(result)

// Destructuring  (Unpacking)
// const people = ["Jim", "James", "kim", "Sim", "Tim", "Dim"]

// let [, second, third, ...theRest] = people

// console.log(second)
// console.log(theRest)

// const sallyBirds = ["Magpie", "Owl"]
// const bobBirds = ["Robin", "Crow"]

// // concat adds lists together and mamkes a new list - doesn't iompact the original lists
// const allBirds = bobBirds.concat(sallyBirds)
// // Alternative
// const allBirds2 = [ ...bobBirds, ...sallyBirds, "Bin-chicken"]

// console.log(allBirds)
// console.log(allBirds2)

// // expansion operator ... removes element from their list,
// console.log(...bobBirds)

const button = document.querySelector("button");

function greet() {
  const name = prompt("What is your name?");
  const greeting = document.querySelector("#greeting");
  greeting.textContent = `Hello ${name}, nice to see you!`;
}

button.addEventListener("click", greet);
