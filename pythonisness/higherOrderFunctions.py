# Higher Order Function = a function that either:
#                        1. accepts a function as an argument
#                               or
#                        2. returns a function 
#                         (In python, functions are also treated as objects)

#---------------------------------------------------------------------------------------
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

#----------------------------------------------------------------------------------------

def divisor(x):
    def dividend(y):
        return y / x
    return dividend


division = divisor(2)
print(division(10))

