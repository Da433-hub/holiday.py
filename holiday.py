city = {'Miami': 900, 'Cairo': 690, 'Paris': 780, 'Tokyo': 870, 'Milan': 680, 'Ottawa':800} # The dictionary.
for key, value in city.items():# Use the items() method to display to user the key-value pairs as tuples.
    print(key, ":", value)

city_flight = (input("Please enter the name of the city of your choice from the list above: "))
def plane_cost(city_flight):# This function takes the numerical value from the dictionary which corresponds to the city name (the key).
    total = city[city_flight]
    return total
print(f"Plane costs are: £  {plane_cost(city_flight)}") # Call the function.


def hotel_cost(num_nights, hotel_price): # Multiplying function.
    total = num_nights * hotel_price
    return total
num_nights = int(input("The hotel price per night is £50. Please enter the number of nights you will be staying at the hotel: ")) 
hotel_price = 50
print(f"Hotel costs are: £ {hotel_cost(num_nights, hotel_price)}") # Call the function.


def car_rental(rental_days, per_day): # Multiplying function.
    total = rental_days * per_day
    return total
rental_days = int(input("Car-Rental is £40 per day. Please enter the number of days you will be hiring a car: ")) # £40 per day for the car-rental. 
per_day = 40
print(f"Car-rental costs are: £ {car_rental(rental_days,per_day)}.") # Call the function.

def holiday_cost(): # Leave arguments empty for simplicity.
    total = plane_cost(city_flight) + hotel_cost(num_nights, hotel_price) + car_rental(rental_days, per_day) 
    return total
print(f"The total holiday cost is £ {holiday_cost()}.") # Total cost.