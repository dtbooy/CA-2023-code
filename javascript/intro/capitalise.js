String.prototype.toJadenCase = function (string) {
    //...
    let words = this.split(" ")
    let capitalString = ""
    for (word of words) {

      capitalString = capitalString + word[0].toUpperCase() + word.slice(1) + " "
    }

    return capitalString.slice(0,-1)
  };

var str = "How can mirrors be real if our eyes aren't real";
console.log(str.toJadenCase())
  