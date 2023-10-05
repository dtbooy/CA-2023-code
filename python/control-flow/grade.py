score = int(input("Score: "))

if score >= 90:
    print("HD")
elif score >= 80:
    print("D")
elif 65 <= score < 80: #how to add a range even though redundant in this instance
    print("C")
elif score >= 50 and score < 65: # can use boolean operators (again in this example it's redundant)
    print("P")
else:
    print("F")
    