#user input

to_units = 24
name_of_unit = "hours"

def days_of_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days*to_units} {name_of_unit}")
    print("All Good!")

#user_input = input("enter num of days :\n")
#print(user_input)


#function with return values

def days_of_units(num_of_days):
    return f"{num_of_days} days are {num_of_days*to_units} {name_of_unit}"

my_var = days_of_units(35)
print(my_var)

################################

def days_of_units(num_of_days):
    return f"{num_of_days} days are {num_of_days*to_units} {name_of_unit}"

user_input = input("enter num of days :\n")
user_input_num = int(user_input)

calculate_value = days_of_units(user_input_num)
print(calculate_value)