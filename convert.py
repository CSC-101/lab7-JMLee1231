
#The purpose of the function is to convert a number input into a string
#Input is a string
#output is a float
def str_to_float(str1:str)->[float]:
    try:
        return float(str1)

    except ValueError:
        return None
