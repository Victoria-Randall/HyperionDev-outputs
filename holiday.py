"""PROJECT BRIEFING
Your task will be to
calculate a user’s holiday cost including the plane cost, hotel cost, and
car rental cost.
● First, get the following user inputs:
○ city_flight: The city they will be flying to. (You can create some
options for them. Remember: Each city will have different flight
costs.)
○ num_nights: The number of nights they will be staying at a hotel
○ rental_days: The number of days that they will be hiring a car for.
● Next, create the following four functions:
● hotel_cost: This function will take the num_nights as an argument,
and return a total cost for the hotel stay (You can choose the price
per night charged at the hotel).
● plane_cost: This function will take the city_flight as an argument
and return a cost for the flight (hint: use if/else if statements in the
function to retrieve a price based on the chosen city).
● car_rental: This function will take the rental_days as an argument
and return the total cost of the car rental (you can choose the daily
rental cost.)
● holiday_cost: This function will take the three arguments
hotel_cost, plane_cost, car_rental. Using these three
arguments, you can call all three of the above functions with
respective arguments and finally return a total cost for your
holiday.
● Print out all the details about the holiday in a readable way!"""

# Define cost for car rental and lists for destinations and associated hotel costs.
car = 50
destinations = ["Paris", "Sydney", "Tokyo", "Rome"]
hotel_cost_destination = [150,100,200,120]

# Ask user to choose destination, number of nights for the hotel and number of days for car rental. Data
# validation included to check numbers are added for hotel nights and car rental days and valid location.
city_flight = (input("Where would you like to visit? Your options are Paris, Sydney, Tokyo or Rome: ")).capitalize()
while city_flight not in destinations:
    city_flight = (input("Unfortunately that's not one of our destinations. Please try again. Your options are Paris, Sydney, Tokyo or Rome: ")).capitalize()

while True:
    try: 
        num_nights = int(input("For how many nights do you wish to stay? "))
        break
    except ValueError:
        print("Opps! That was not a valid number. Please try again: ")

while True:
    try: 
        rental_days = int(input("For how many days do you wish to hire a car? "))
        break
    except ValueError:
        print("Opps! That was not a valid number. Please try again: ")

# create function to multiply unit cost by number of units. For use calculating hotel and car rental costs.
def multiply(x,y):
    total = x * y
    return (int(total))

# Create function to merge lists.
def list_merge(keys_list, values_list):
    dict_to_return = {}
    for index, key in enumerate(keys_list):
        dict_to_return[key] = values_list[index]
    return dict_to_return

# Create function for calculating plane costs.
def plane_cost_function(x):
    if x == "Rome":
        y = 360
    if x == "Paris":
        y = 240
    if x == "Sydney":
        y = 4500
    if x == "Tokyo":
        y = 3600
    return(int(y))

# Create function for total cost adding costs for hotel, plane and car rental.
def holiday_cost_function(x,y,z):
    total = x + y + z
    description = "Holiday:\t£"
    return (description + str(total))

# Call functions for hotel cost dictionary and hotel, plane, car rental and total holiday costs. 
hotel_cost_dictionary = list_merge(destinations, hotel_cost_destination)
hotel_cost = multiply(hotel_cost_dictionary[city_flight],num_nights)
plane_cost = plane_cost_function(city_flight) 
car_rental = multiply(car,rental_days)
holiday_cost = holiday_cost_function(hotel_cost,plane_cost,car_rental)

# Print summary of costs for user.
print(f"\nA summary of the costs associated with this package is as follows:\nHotel:\t\t£{hotel_cost}\nPlane:\t\t£{plane_cost}\nCar rental:\t£{car_rental}\n----------------------\n{holiday_cost}\n----------------------")
