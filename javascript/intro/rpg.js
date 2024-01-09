// Character class definitions
class Character{
    constructor(name, race, health, attack){
        this.name = name
        this.race = race
        this.health = health
        this.attack = attack
        this.inv = new Inventory([], 0, 0, 0)
    }
    battle(other){
        console.log(`${this.name} attacks ${other.name}!`)
    }
}
class Ranger extends Character {
    battle(other){
        console.log(`${this.name} launches a brutal melee attack on ${other.name}!`)
    }
}
class Mage extends Character {
    constructor(name, race, health, attack){
        // Call the superclass constructor
        super(name, race, health, attack)
        this.mana = 100
    }
    battle(other){
        console.log(`${this.name} casts a wicked spell at ${other.name}!`)
        this.mana -= 20
    }
}
class Burglar extends Character{
    battle(other){
    console,log(`${this.name} sneaks in a stealth attack on ${other.name}!`)
    }
}

class Wizard extends Character{
    battle(other){
        console.log(`${this.name} summons an orc minion, which attacks ${other.name}!`)
    }
}
class Chest{
    constructor(items, gold, silver, copper){
        this.inv = new Inventory(items, gold, silver, copper)
    }
}
class Inventory{
    constructor(items, gold, silver, copper){
        this.items = items // list
        this.set_currency(gold, silver, copper) // Delegation
    }
    // from_inv and to_inv are instances of Inventory
    transfer(to_inv){
        // Add all the items from from_inv to to_inv
        to_inv.items.push(this.items)
        // # Delete all the items from from_inv
        this.items = []
        // # Add the currency from from_inv to to_inv
        to_inv.copper += this.copper
        // # Set currency of from_inv to 0
        this.copper = 0
    }
    // Setter
    set_currency(gold, silver, copper){
        this.copper = gold * 10000 + silver * 100 + copper
    }
    // # Getter
    get_currency(){
        let gold = Math.floor(this.copper / 10000)
        let silver = Math.floor((this.copper % 10000) / 100)
        let copper = this.copper % 100
        return [gold, silver, copper]
    }
}

let aragorn = new Ranger('Aragorn', 'Human', 100, 50)
let galadriel = new Mage('Galadriel', 'Elf', 120, 75)
let frodo = new Burglar('Frodo', 'Hobbit', 50, 25)
let saruman = new Wizard('Saruman', 'Human', 80, 100)

frodo.inv.set_currency(9, 47, 23)

chest = new Chest(['longsword', 'iron helm'], 2, 25, 99)

galadriel.battle(aragorn)

console.log(chest.inv)
console.log(aragorn)
console.log(frodo)
console.log(galadriel)

// # Frodo loots a chest!
console.log(frodo.inv)
chest.inv.transfer(frodo.inv)
console.log(frodo.inv)
console.log(frodo.inv.get_currency())
