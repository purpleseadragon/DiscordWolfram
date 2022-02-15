import wolframalpha

with open('token.txt') as token:
    TOKEN = token.readlines()[1]

client = wolframalpha.Client(TOKEN)


def result_from_WolframAlpha(question):
    """scrapes answer from Wolfram Alpha"""
    res = client.query(question)
    return next(res.results).text

if __name__ == '__main__':
    # for testing
    print(result_from_WolframAlpha('derivative x^4 / 3'))
