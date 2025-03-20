import re
from enum import Enum

class NumericBase(Enum):
    BI = 2    # Binary
    OCT = 8   # Octal
    DEC = 10  # Decimal
    HEX = 16  # Hexidecimal

def validate_input(input: str, base: NumericBase) -> bool:
    """
    Validates that the input string is appropriate for the given numeric base.
    
    Parameters:
        input (str): The input string to validate.
        base (NumericBase): The numeric base for which to validate the input.
        
    Returns:
        bool: True if the input string is valid for the specified base, False otherwise.
    """
    # Define regex patterns for each numeric base.
    patterns = {
        NumericBase.BI:  r'^[01]+$',           # Only 0's and 1's
        NumericBase.OCT: r'^[0-7]+$',           # Only digits 0 through 7
        NumericBase.DEC: r'^\d+$',              # Only digits 0 through 9
        NumericBase.HEX: r'^[0-9a-fA-F]+$',      # Only 0-9 and A-F (case-insensitive)
    }
    
    pattern = patterns.get(base)
    if pattern is None:
        raise ValueError("Unsupported numeric base")
    
    # Use re.fullmatch to ensure the entire string matches the pattern.
    return re.fullmatch(pattern, input) is not None   

################### BINARY TO ALTERNATE BASE CONVERSIONS ########################    
   
def binary_to_decimal(inp: str, print_result=True) -> int:
    """
    Converts a binary input string to a decimal number after validating the input.
    
    Parameters:
        inp (str): The binary number in string format.
    
    If the input is not valid for binary conversion, it prints an error message.
    Otherwise, it converts the binary input to decimal and prints the result.
    """
    if not validate_input(inp, NumericBase.BI):
        print("Error: Input is not a valid binary number.")
        return
    
    # Convert the binary string to a decimal integer.
    result = int(inp, NumericBase.BI.value)
    if print_result:
        print(result)
    else:
        return result

def binary_to_octal(inp: str):
    """
    Converts a binary input string to an octal number after validating the input.
    
    Parameters:
        inp (str): The binary number in string format.
    
    If the input is not valid for binary conversion, it prints an error message.
    Otherwise, it converts the binary input to octal and prints the result.
    """
    if not validate_input(inp, NumericBase.BI):
        print("Error: Input is not a valid binary number.")
        return
    
    # Convert binary to a decimal integer first
    decimal_value = binary_to_decimal(inp, False)
    
    # Convert decimal to octal (without the '0o' prefix)
    octal_str = format(decimal_value, 'o')
    print(octal_str)

def binary_to_hex(inp: str):
    """
    Converts a binary input string to a hexadecimal number after validating the input.
    
    Parameters:
        inp (str): The binary number in string format.
    
    If the input is not valid for binary conversion, it prints an error message.
    Otherwise, it converts the binary input to hexadecimal and prints the result.
    """
    if not validate_input(inp, NumericBase.BI):
        print("Error: Input is not a valid binary number.")
        return
    
    # Convert binary to a decimal integer first
    decimal_value = binary_to_decimal(inp, False)
    # Convert decimal to hexadecimal (using uppercase letters)
    hex_str = format(decimal_value, 'X')
    print(hex_str)  

################### OCTAL TO ALTERNATE BASE CONVERSIONS ########################   

def octal_to_decimal(inp: str, print_result=True) -> int:
    """
    Converts an octal input string to a decimal number after validating the input.
    
    Parameters:
        inp (str): The octal number in string format.
    
    If the input is not valid for octal conversion, it prints an error message.
    Otherwise, it converts the octal input to decimal and prints the result.
    """
    if not validate_input(inp, NumericBase.OCT):
        print("Error: Input is not a valid octal number.")
        return
    
    result = int(inp, NumericBase.OCT.value)
    if print_result:
        print(result)
    else:    
        return result   

def octal_to_binary(inp: str):
    """
    Converts an octal input string to a binary number after validating the input.
    
    Parameters:
        inp (str): The octal number in string format.
    
    If the input is not valid for octal conversion, it prints an error message.
    Otherwise, it converts the octal input to binary and prints the result.
    """
    if not validate_input(inp, NumericBase.OCT):
        print("Error: Input is not a valid octal number.")
        return
    
    decimal_value = octal_to_decimal(inp, False)
    binary_str = format(decimal_value, 'b')
    print(binary_str)   

def octal_to_hex(inp: str):
    """
    Converts an octal input string to a hexadecimal number after validating the input.
    
    Parameters:
        inp (str): The octal number in string format.
    
    If the input is not valid for octal conversion, it prints an error message.
    Otherwise, it converts the octal input to hexadecimal and prints the result.
    """
    if not validate_input(inp, NumericBase.OCT):
        print("Error: Input is not a valid octal number.")
        return
    
    decimal_value = octal_to_decimal(inp, False)
    hex_str = format(decimal_value, 'X')
    print(hex_str)    
    