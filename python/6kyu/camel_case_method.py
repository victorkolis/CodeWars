# Link: https://www.codewars.com/kata/587731fda577b3d1b0001196
# Description:
#
# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings.
# All words must have their first letter capitalized without spaces.
#
# For instance:
#
# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord

def camel_case(string):
    return ''.join([word.capitalize() for word in string.split()])


print(camel_case('camel case kata'))
