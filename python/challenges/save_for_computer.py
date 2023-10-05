weekly_income = int(input("what is your weekly income?"))
living_expenses = int(input("what is your weekly living expenses?"))
comp_cost = int(input("how much is your new computer?"))
	
weeks = comp_cost / (weekly_income - living_expenses)

print(f"it will take {weeks} weeks to save for your computer")