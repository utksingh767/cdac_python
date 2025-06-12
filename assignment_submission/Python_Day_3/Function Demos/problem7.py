# 7) Define a function which accepts a string, toggles and returns it.
#    [Hint: use "swapcase()" function of string]

def toggle_string_case(input_string):
    return input_string.swapcase()

string_input_q7 = input("Enter a string to toggle its case: ")
toggled_string = toggle_string_case(string_input_q7)
print(f"Original string: '{string_input_q7}'")
print(f"Toggled string: '{toggled_string}'")
