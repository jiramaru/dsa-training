# Exercise 1: Reverse a String

string = input('Entrer a string:')

reverse = string[::-1]

print(reverse)


# 2nd method : we convert  string we receive to list

string_to_list = list(string)

reverse_list= string_to_list[::-1]

reverse = ''.join(reverse_list)

print(reverse)