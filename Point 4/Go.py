def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

string = input("Enter a string: ")
reversed_string = reverse_string(string)

print("Reversed string:", reversed_string)

with open("results_Go.txt", "w") as f:
    f.write(f"Reversed string: {reversed_string}")




