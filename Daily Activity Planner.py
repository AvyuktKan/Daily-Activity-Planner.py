homework_time = int(input("How many minutes of homework do you have today? "))

if homework_time > 60:
    plan = "start homework now"
    print("That is a long homework session.")

free_time = input("Is there free time after homework? (yes/no): ")
if free_time.lower() == "yes":
    print("Remember to pick a hobby during your free time!")

print("===== DAILY PLAN =====")

print(f"Homework time: {homework_time} minutes")
print(f"Plan: {plan}")
print(f"Free time: {free_time}")