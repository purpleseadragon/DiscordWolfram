import requests
import bs4

# Wolfram input conversions
# starts with input?i={first_word}+...
# y^x -> y%5Ex
# y*x -> y*x
# y/x -> y%2Fy
# () -> %28, %29
# sqrt -> sqrt

def convert_to_url(eq_input):
    """takes natural language wolfram alpha input as a string and 
    converts to what should be put in the url"""
    first_part = "https://www.wolframalpha.com/input?i="
    second_part = r''
    conversion_dict = {'^':r'%5E', '(': r'%28', ')': r'%29', '/': r'%2F', '=': r'%3D', '+': r'%2B'}
    for letter in eq_input:
        if letter in conversion_dict.keys():
            second_part += conversion_dict[letter]
        elif letter == ' ':
            second_part += '+'
        else:
            second_part += letter
    return first_part + second_part


if __name__ == '__main__':
    print(convert_to_url('derivative x^4 / 3'))
    print(convert_to_url('solve sqrt(x)+3-5 =y'))
    print('pass')
