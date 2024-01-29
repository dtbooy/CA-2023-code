import './App.css'
import Greeting from "./Greeting.jsx"

function App() {
  return (
    <>
      <Greeting foo="bar" name="Dirk" age={36}/>
      <h1>Do you like pie?</h1>
      <p>
        Pie is great and you should try it, any sort of pie at all;
        cherry pie, apple pie, steak pie!! Any pie is a winner!!!
      </p>
      <Greeting foo="bar" name="Matt" age={51}/>
      <Greeting age={99}/>

    </>
  )
}


export default App
