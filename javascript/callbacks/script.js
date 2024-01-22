// function getJoke(){
//     return new Promise((resolve, reject) => {
//         try {
//             // instantiate XHR request object
//             const req = new XMLHttpRequest();
//             //
//             req.addEventListener('load', event => resolve(event.target.response.joke))
//             req.open('GET', 'https://icanhazdadjoke.com/')
//             req.setRequestHeader("Accept", "application/json");
//             req.responseType = "json"
//             // send the request
//             req.send()
//         }
//         catch (e) {
//             reject(e)
//         }
//     })
// }

async function fetchJoke(){
    const res = await fetch('https://icanhazdadjoke.com/', { // configuration object
        headers: {                          
            'Accept': 'application/json'
        }
    }) 
    const data = await res.json()
    return data.joke
        // note teh default value for METHOD is GET - don't need to pass it to fetch
        // .then(res => res.json()) //this returns a promise for the return of the text response
        // .then(data => console.log(data))
}

fetchJoke().then(data => console.log(data))

// const jokePromises = []
// for (let i=0;i<3;i++) {
//     jokePromises.push(getJoke())
// }

// Promise.all waits until all promises in the array are kept, then runs the .then
// Promise.all(jokePromises)
//     .then(jokes=>console.log(jokes))
// // if any promise in the array is rejected the whole array is rejected
//     .catch(err=>console.log(err))

// const jokes = [getJoke().then(joke => jokes.push(joke)),
//         getJoke().then(joke => jokes.push(joke)),
//         getJoke().then(joke => jokes.push(joke)) ]

// getJoke()
//     .then(joke => {
//         jokes.push(joke)
//         return getJoke()
//     })
    // .then(joke => {
    //     jokes.push(joke)
    //     return getJoke()
    // })
    // .then(joke => {
    //     jokes.push(joke)
    //     console.log(jokes)
    // })

    console.log("not waiting for resolve")



let pokemonUrl = "https://pokeapi.co/api/v2/pokemon/"
let pokeFetch = fetch(pokemonUrl)
    .then((response) => response.json()) // returns a promise
    .then((data)=> console.log(data)) // handles the data and runs function
    .catch((error) => console.log("error: " + error)) // handles the errors