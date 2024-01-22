CHOICES = ["rock", "paper", "scissors"]

function getComputerChoice(){
    move = Math.floor(Math.random()*3)
    return CHOICES[move]
}

function playRound(playerSelection, computerSelection){
    // Result Matrix for a game of RPS rows = P1, col = P2
    winTable = [[0,-1,1],[-1,1,0],[1,0,-1]]
    result = winTable[CHOICES.indexOf(playerSelection.toLowerCase())][CHOICES.indexOf(computerSelection.toLowerCase())]
    switch (result) {
        case 0: 
            return `Both picked ${computerSelection}, it's a Draw!`
        case -1:
            return `${computerSelection} beats ${playerSelection}. You lose!`
        case 1:
            return `${playerSelection} beats ${computerSelection}. You Win!`
    }
}
