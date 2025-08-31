names = ["sara", "ali", "reza"]

def capitalized_names():
    return list(map(str.capitalize , names))
print(capitalized_names())


#2
temperatures_celsius = []

while True:
    try:
        user_input = input("Enter a temp (or 'stop' to finish): ")
        if user_input.lower() == 'stop':
            break   
        temperatures_celsius.append(float(user_input))
    except ValueError:
        print("Invalid input. Please enter a valid number or 'stop'.")
        pass    

print("Celsius to Fahrenheit:", list(map(lambda c: (c * 9/5) + 32, temperatures_celsius)))

#3

def is_integer(s):
    try:
        int(s)
        return True 
    except ValueError:
        return None

list_of_strings = ["3", "5", "2", "0", "-4", "hasan"]
list_of_integers = list(filter(is_integer, list_of_strings))
list_of_integers = list(map(int, list_of_integers))

print(list_of_integers)
