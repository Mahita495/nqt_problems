conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 
                    5: '5', 6: '6', 7: '7', 
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 
                    13: 'D', 14: 'E', 15: 'F'}

def convert(dec):
    hex=""
    while dec>0:
        rem=dec%16
        hex= conversion_table[rem]+hex
        dec=dec//16
    return hex

def ascii_to_hex(input_string):
    decimal=[]
    hexa=[]
    for char in input_string:
        decimal.append(ord(char))
    for i in decimal:
        hexa.append(convert(i))
    return hexa
        
        

# Example usage:
input_str = "Hello, world!"
print(ascii_to_hex(input_str))