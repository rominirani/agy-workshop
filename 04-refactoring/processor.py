import math

data = []

def process_calc(type, a, b, c=None):
    global data
    res = 0
    if type == "ADD":
        res = a + b
    elif type == "SUB":
        res = a - b
    elif type == "MUL":
        res = a * b
    elif type == "DIV":
        if b != 0:
            res = a / b
        else:
            print("ERROR: DIVISION BY ZERO")
            return None
    elif type == "POW":
        res = math.pow(a, b)
    elif type == "SQRT":
        if a >= 0:
            res = math.sqrt(a)
        else:
            print("ERROR: NEGATIVE SQRT")
            return None
    
    entry = "Type: " + str(type) + ", Args: (" + str(a) + ", " + str(b) + ", " + str(c) + "), Result: " + str(res)
    data.append(entry)
    print("PROCESSED: " + entry)
    return res

def print_all():
    global data
    print("--- ALL LOGS ---")
    for i in range(len(data)):
        print(str(i) + ": " + data[i])

process_calc("ADD", 10, 20)
process_calc("MUL", 5, 4)
process_calc("DIV", 10, 0)
print_all()
