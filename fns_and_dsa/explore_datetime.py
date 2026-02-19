from datetime import datetime

def display_current_datetime():
    #save current adteand time
    current_date = datetime.now()
    
    #format the date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S") 

    #print result
    print("Current date and time:", formatted_date  )
#call the function
display_current_datetime()


from datetime import datetime, timedelta
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
number_of_days = int(input("Enter the number of days to add: "))
#call the function
calculate_future_date(number_of_days)
