function adder(a,b) {
    return a + b
}

// function adderPromise(x,y) {
//     return new Promise((resolve, reject)=> {
//         if(typeof x === 'number' && typeof y === 'number'){
//             const answer = adder(x,y)
//             resolve(answer)
//         } else {
//             reject("x and y must be numbers")
//         }
//     })
// }

// Syntactic sugar for promises - make the function return a promise
async function adderPromise(x,y) {
    
    if(typeof x === 'number' && typeof y === 'number'){
        const answer = adder(x,y)
        return answer
    } else {
        throw("x and y must be numbers")
    }
}

adderPromise(5,10)
    .then(value => console.log(value))
    .catch(err => console.error(err))

adderPromise(10,10)
    .then(value => console.log(value))
    .catch(err => console.error(err))

adderPromise(5,10)
    .then(value => adderPromise(value, 100))
    .then(value => console.log(value))
    .catch(err => console.error(err))

console.log("not waiting for resolve")