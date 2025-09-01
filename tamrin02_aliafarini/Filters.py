list_of_integers = input("enter a list of integers separated by spaces: ").split()
list_of_integers = list(map(int, list_of_integers))
list_of_positive_integer = list(filter(lambda x: x>=0, list_of_integers))
print(f"your positive number is: {list_of_positive_integer}")
#2-------------------------------------------------------

list_of_words = input("enter a list of words separated by spaces: ").split()
list_of_words_length5 = list(filter(lambda x: len(x)>4, list_of_words))
print(list_of_words_length5)

#3-------------------------------------------------------

list_of_emails = input("enter a list of emails separated by spaces: ").split()
list_of_emails = list(filter(lambda x: "@" in x and "." in x, list_of_emails))
print(list_of_emails)