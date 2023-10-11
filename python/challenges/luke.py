def relation_to_luke(name):
	relation = {"Darth Vader":	"father", "Leia":	"sister", "Han":	"brother in law", "R2D2":	"droid"}
	return (f"Luke, I am your {relation.get(name)}.")

print(relation_to_luke("Leia"))