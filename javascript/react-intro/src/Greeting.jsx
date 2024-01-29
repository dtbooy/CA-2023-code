// function Greeting(props){
//// 1. you can deconstruct props into variables. This also alows you to set a default 
    // const {name="None", age} = props
// 2. or destructure props in-situ
function Greeting({name="None", age}){
    return(
      <>
        <p>Greetings {name}!!</p>
        <p>There is {age} things strange in your neighbourhood.</p>
      </>
    )
  }

  export default Greeting