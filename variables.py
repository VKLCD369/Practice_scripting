#variable code 

to_seconds = 60*60*24
name_of_unit = "seconds"

print(f"20 days are {20*to_seconds} {name_of_unit}")
print(f"31 days are {31*to_seconds} {name_of_unit}")
print(f"60 days are {60*to_seconds} {name_of_unit}")
print(f"90 days are {90*to_seconds} {name_of_unit}")


to_units = 24
name_of_unit = "hours"

print(f"20 days are {20*to_units} {name_of_unit}")
print(f"31 days are {31*to_units} {name_of_unit}")
print(f"60 days are {60*to_units} {name_of_unit}")
print(f"90 days are {90*to_units} {name_of_unit}")

#functions code

to_units = 24
name_of_unit = "hours"

def days_of_units():
    print(f"20 days are {20*to_units} {name_of_unit}")
    print("All Good!")


days_of_units()

#function parameters

to_units = 24
name_of_unit = "hours"

def days_of_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days*to_units} {name_of_unit}")
    print("All Good!")

days_of_units(31)

#########################

to_units = 24
name_of_unit = "hours"

def days_of_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days*to_units} {name_of_unit}")

days_of_units(20)
days_of_units(31)
days_of_units(60)
days_of_units(90)


#scope (global variable and local variable)
#Global variable which are outside of function
#local variable which are within the function

to_units = 24
name_of_unit = "hours"

def days_of_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days*to_units} {name_of_unit}")


def scope_check(num_of_days):
    print(name_of_unit)
    print(num_of_days+20)

scope_check(20)
scope_check(30)
