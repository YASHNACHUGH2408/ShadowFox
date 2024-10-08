# 1. Write a function that takes two arguments, 145 and 'o', and
# uses the `format` function to return a formatted string. Print the
# result. Try to identify the representation used.


def format_function(num, char):
    return "{0:{1}^10}".format(num, char)

result = format_function(145, 'o')
print("Formatted String:", result)
print("Representation used:", type(result).__name__)