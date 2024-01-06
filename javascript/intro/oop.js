// const person1 = {
//     name:"Matt",
//     age:51
// }
// console.log(person1)
// // we can dynamically add attributes to an object
// const person2 = {}

// person2.name = 'Matt'
// person2.age = 51
// console.log(person2)

// // to create a new object use the new keyword (otherwise it will save the Class object to the variable)
// // creating an empty object (x = {}) is the same as writing:
// const person3 = new Object()


// // // Create a Constructor Function
// // function Person(name, age) {
// //     this.name = name,
// //     this.age = age
// // // you can create class functions: 
// // // NOTE: need to ensure you use the this.variable NOT the input variable 
// // // if the function needs to work dynamically (if it needs to change when the properies are changed)
// //     this.greet = () => (
// //         console.log(`${this.name} is ${this.age} years old`)
// //     )
// // }


// // Create a Class
// class Person{
//     construcor(name, age) {
//         this.name = name
//         this.age = age
//     }
//     greet(){
//         console.log(`${this.name} is ${this.age} years old`)
//     }
// }

// const person4 = new Person("matt", 52)

// // person4.age = 52
// console.log(person4)

// person4.greet()

class Rectangle {
    // declare your private variables
    #width
    #height
    constructor(width, height) {
        this.width = width
        this.height = height
    }

    // setting a getter on a property prevents changes to property (with no getter this will even prevent the constructor it)
    get width() {return this.#width}
    get height() {return this.#height}

    // setters allow validation of inputs
    set width(value) {
        if (typeof value === 'number') {
        return this.#width = value
        } else {
            //raise exception
        }
    }
    set height(value) {
        if (typeof value === 'number') {
        return this.#height = value
        } else {
            //raise exception
        }
    } 
 
    // "get" flags the area function as a getter - it turns the function into a sudo-property
    get area() {return this.#width * this.height}
}

// Class extension (Making a child)
class Square extends Rectangle {
    #width
    #height
    constructor(side=5){
        super(side,side)
    }


}


const rect = new Rectangle(20, 20)

// rect.width = 10
console.log(rect.area)
console.log(rect.width)
console.log(rect)
