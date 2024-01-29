import React, { useState } from 'react'
import "./App.css"
import ShowCount from './components/ShowCount.jsx'
import BitcoinIndex from './components/BitcoinIndex.jsx'



const App = () => {
  // useState creates an internal variable in React. 
  // contains an array of 2 values. The first element  is the current value, 
  // the second element is a setter function that updates the first element. 
  let [ count, setCount ]  = useState(0) // pass Use State the initial calue of count


  return (
    <>
      {/* <ShowCount count={count} setCount={setCount}/> */}
      <h1>Bitcoin Index</h1>
      <BitcoinIndex />
    </>
  )
}

export default App