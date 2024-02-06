import React from 'react'

const ShowEntry = ({entry, categories}) => {


  return entry ? (
    <div className="container">
    <h3 className="is-size-4">{entry.content}</h3>
    <p className="is-size-7">posted in {categories[entry.category]}</p>
    </div>
    
  ) : (
    <h3 className="is-size-4">Entry not found!</h3>
  )

}

export default ShowEntry