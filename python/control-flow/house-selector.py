name = input("What is your name? ")

if name == "Harry" or "Ron" or "Hermione":
    print("Griffindor")
elif name == "Draco":
    print("Slytherine")
else:
    print("Mudblood")

match name:
    case 'Harry' | "Ron" | "Hermione":
        print("Griffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Mudblood")