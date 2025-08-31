list_of_integers = input("enter a list of integers separated by spaces: ").split()
list_of_integers = list(map(int, list_of_integers))
list_of_integers = list(filter(lambda x: x>=0, list_of_integers))
print(list_of_integers)
#2-------------------------------------------------------

list_of_words = input("enter a list of words separated by spaces: ").split()
list_of_words = list(filter(lambda x: len(x)>4, list_of_words))
print(list_of_words)