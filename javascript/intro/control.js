const age = 19

//if statement 
if (age >= 18) {
    console.log("Adult")
} else if (age >= 13) {
    console.log("teen")
} else {
    console.log("Child")
}

// ternary if statement
const message = age >= 18 ? "Allowed" : "not allowed"

//Match case

switch (message) {
    case "Allowed":
        console.log("Go through")
        break // you need to break or it will go through every block after this as well
    case "not allowed":
        console.log("Go Home!!!")
        break
    default:
        console.log("I don;t knoiw who I am anyMoRE!!!!")
}