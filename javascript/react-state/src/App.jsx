import React, { useState } from 'react'
import "./App.css"

const App = () => {
  // useState creates an internal variable in React. 
  // contains an array of 2 values. The first element  is the current value, 
  // the second element is a setter function that updates the first element. 
  let [ count, setCount ]  = useState(0) // pass Use State the initial calue of count
  

  return (
    <>
      <h1>State</h1>
      <p>You have clicked {count} times!</p>
      {/* need to use React "on" attribute instead of event listener */}
      <button onClick={()=> {setCount(count + 1)} }>Click Me!</button>
    </>
  )
}

export default App