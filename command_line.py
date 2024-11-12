
import sys
import convert
#should take each argument in the commnand line script and attempt to convert it to a float. Then return the sum of the floats. Ignore unconvertable datatypes. 
#input - multiple datatype entries separated by a space
#output - a single float sum 
if __name__ == '__main__':
    print(sys.argv)
    total = 0
    for i in range(1, len(sys.argv)):
        if convert.str_to_float(sys.argv[i]) is not None:
            total += convert.str_to_float(sys.argv[i])

    print(total)     

# the program is prompted with: 40 forty 213 2 12.3 asdff
# the program outputs 267.3
