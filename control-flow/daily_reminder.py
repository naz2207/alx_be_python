task = input("Enter the task you want to be reminded of: ")
priority = input("Enter the priority level (high/medium/low): ")
time_bound = input("Is this task time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"Reminder: You have a HIGH priority task - '{task}'. Please address it) as soon as possible.")
    case "medium":
        print(f"Reminder: You have a MEDIUM priority task - '{task}'. Try to complete it soon.")
    case "low": 
        print(f"Reminder: You have a LOW priority task - '{task}'. You can attend to it at your convenience.")
    case _: 
        print("Invalid priority level entered.")    
if time_bound.lower() == "yes":
    print(f"Note: This task is  that requires immediate attention today!")
else:
    print("This task is not time-bound.")
    
