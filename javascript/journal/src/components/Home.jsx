// import React from 'react'

const Home = ({entries, categories}) => {
  return (
    <div>
      Home
      {categories.map((cat, index) => (
          <div key={index}>
            <h1>{cat}</h1>
            <ul>
              {entries.map((entry, index) => (
                <>
                {categories[entry.category] === cat ? <li key={index}>{entry.content}</li> : null}
                </>
              ))}
            </ul>
            

          </div>
          )
        )}
      

    </div>

  )
}

export default Home