import React, { useState } from 'react'

// import "../App.css"

// NOTE: the incoming props are destructured with { } 
const ShowCount = ({count, setCount}) => {

  return ( 
    <div>
      <h1>State</h1>
      {/* need to use React "on" attribute instead of event listener */}
      <button onClick={()=> {setCount(count + 1)} }>Click Me!</button>
      <p>You have clicked {count} times!</p>
    </div>
  )
}

export default ShowCount