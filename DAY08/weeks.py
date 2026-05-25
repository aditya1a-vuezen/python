# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

def life_in_weeks(age):
    year_left = 90  - age
    weeks_left = year_left * 52
    print(f"You have {weeks_left} weeks left")
    

life_in_weeks(20)
life_in_weeks(40)
life_in_weeks(70)
