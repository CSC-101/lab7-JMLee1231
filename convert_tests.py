
import convert
#asks for number inputs until it recieves the command 'done' and makes a list of floats of those numbers
#input - received during runtime - as many as wanted - expects one digit at a time
#output - list of all the floats entered

def gather_numbers():
    returning = []
    while True:
        inp = input("Enter a number (type 'done' to finish):")
        if inp.upper() == "DONE":
            break

        num = convert.str_to_float(inp)

        if num is not None:
            returning.append(num)
        else :
            print("Invalid input")
    return returning


if __name__ == '__main__':
    numbers = gather_numbers()
    print(numbers)
    total = sum(numbers)
    print(total)
