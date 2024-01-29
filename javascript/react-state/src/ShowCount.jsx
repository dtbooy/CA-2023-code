import React, { useState } from 'react'
import "./App.css"

// NOTE: the incoming props are destructured with { } 
const ShowCount = ({count}) => {
  return <p>You have clicked {count} times!</p>
}

export default ShowCount