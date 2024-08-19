'''
    ***** Why Logging Over Print ?
    1. Print statements missing contextual information such as time of occurence, line number, module.
    2. No straight forward way to format the output of print statement.
    3. Writing print statement output to sources other than the terminal is non trivial and requires.
    4. Significant amount of coding for file handling, threading, email sending etc.
'''

def return_sum_of_two_nums(a,b):
    print(f"Inside function to add [a = {a} & b = {b}]")

    try:
        print("There are no checks if the inputs are integer")
        return a + b
    except Exception as e:
        print("%s", e)

print(return_sum_of_two_nums(10, 20))

print(return_sum_of_two_nums(10, 'n'))

print(return_sum_of_two_nums(40, 60))