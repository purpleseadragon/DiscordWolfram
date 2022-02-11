import requests
import bs4
import wolframalpha

with open('token.txt') as token:
    TOKEN = token.readlines()[1]

client = wolframalpha.Client(TOKEN)
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


def result_from_WolframAlpha(question):
    """scrapes answer from Wolfram Alpha"""
    # html using requests
    # headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    # s = HTMLSession()
    # response = s.get(url)
    #response.html.render(wait=5)
    # creation of soup object for parsing
    res = client.query(question)
    wolf_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # notes
    # class="_3-yT" in div> for title, eg. Result or Derivative
    all_imgs = wolf_soup.find_all('img')
    for element in all_imgs:
        print(type(element))
        print(element)
        print(element.name)
        print(element['class'])
        print(element.attrs)
        print(element.attrs.keys())
        if ('src' in element.attrs.keys()) and ('alt' in element.attrs.keys()) and ('class' in element.attrs.keys()):
            if element['class'] == ['_3c8e']:
                raw_text = element['alt'][0]
                break

    # for actual result
    # nested <div class="_1v3w" <div class="_3fR4"<img alt= {what i want} or src={url of image}.gif
    # image name starts at MSP ends at ?
    # at this point guess i just want first result
    return raw_text

if __name__ == '__main__':
    x = convert_to_url('derivative x^4 / 3')
    y = convert_to_url('solve sqrt(x)+3-5 =y')
    print(x, y)
    result_from_WolframAlpha('derivative x^4 / 3')
    # result_from_WolframAlpha(y)
    print('pass')
