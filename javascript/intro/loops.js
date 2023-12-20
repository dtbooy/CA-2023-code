let count = 3

// While loops
while (count>0){
    console.log(count--)
}

// 3 part for loop
//  innitialiser runs once, berfore the first iteration
// condition is tested before every iteration
// post-iteration executes after every iteration

// for (initialiser ; condition; post-iteration ){ }

// for (let i =0 ; i < 10 ; i++) {
//     console.log(i)
// }

// // More complex example of loop
// let numbers = [1,5,6,7,8,9]
// let res=[]
// for (let i =0, x = 1 ; i < numbers.length ; i++, x +=2) {
//     res.push(`${x}.${numbers[i]}`)
// }
// console.log(res)

// // fibonacci sequence
// for (let prev=1, next=1; next <= 1000; tmp=next, next =prev+next, prev=tmp) {console.log(next)}


// Iterate throgh an array
const food = ["pizza", "tacos", "pasta"]
for (let item of food) {
    console.log(item)
    } //>>> pizza \n tacos \n pasta

food.forEach((food) => {
    console.log(food)
})

// NOTE: (let item in food) in is the index of 

food.forEach((food, index) => {
    console.log(`${index+1}. ${food}`)
})