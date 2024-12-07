# from dotenv import load_dotenv
# load_dotenv()
import math

session = dict()

def multiply(a: float, b: float) -> float:
    """useful tool to Multiply two numbers and returns the product
    make sure that both numbers a, b are real numbers and if not try to convert them to real numbers
    args:
        a: float
        b: float    
    requires:
        only_real_numbers
    """
    return float(a) * float(b)


def add(a: float, b: float) -> float:
    """useful tool to Add two numbers and returns the sum, 
    make sure that both numbers a, b are real numbers and if not try to convert them to real numbers
    args:
        a: float
        b: float    

    requires:
        only_real_numbers
    """
    return float(a) + float(b)

# add complex maths tools
def calculate_sin(a: float) -> float:
    """ useful tool to calculate the sin of a number
    IMPORTANT: the value of a will be in degrees, unless user specifically requests it to be in radians
    args: {"a": float}, required: True
    returns: sine of a degrees or radians if user requests
    """
    return math.sin(math.radians(float(a)))

def calculate_cos(a: float) -> float:
    """ useful tool to calculate the cos of a number
    IMPORTANT: the value of a will be in degrees, unless user specifically requests it to be in radians
    args: {"a": float}, required: True
    returns: cosine of a degrees or radians if user requests
    """
    return math.cos(math.radians(float(a)))



# add additional tools

def calculate_log(a: float) -> float:
    """ useful tool to calculate the logarithm of a number, smartly understands expects a float and returns a float and can access any other tools for solving complex problems
    args:
        a: float
    """
    return math.log(float(a))

def calculate_power(a: float, b: float) -> float:
    """ useful tool to calculate the exponential or power of a number a given the power b, smartly understands expects a float and returns a float
    detect cases like a^b and a**b route to this tool
    args:
        a: float
        b: float
    """
    return float(a) ** float(b)

def only_real_numbers(a: float) -> float:
    """ useful tool to verify if the number is real"""
    try: 
        float(a)
    except ValueError: 
        return f"{a} is not a real number so try converting it to a float and try again"

def convert_to_real_number(a: float) -> float:
    """ useful tool to convert a string to a real number"""
    try: 
        return float(a)
    except ValueError: 
        return f"{a} cannot be converted to a real number"    
    
def miscellaneous() -> str:
    """Handle miscellaneous tasks that do not fit into the other tools only returns a string"""
    return "Rephrase and give this answer in words: Hi there, I can't help you with that, if you have any other maths questions please ask them"


def divide(a: float, b: float) -> float:
    """useful tool to divide two numbers and returns the quotient
    make sure that both numbers a, b are real numbers and if not try to convert them to real numbers
    args:
        a: float
        b: float    
    requires:
        only_real_numbers
    """
    return float(a) / float(b)

def subtract(a: float, b: float) -> float:
    """useful tool to subtract two numbers and returns the difference
    make sure that both numbers a, b are real numbers and if not try to convert them to real numbers
    args:
        a: float
        b: float    
    requires:
        only_real_numbers
    """
    return float(a) - float(b)

def ask_name(name: str) -> str:
    """useful tool to ask the name of the user"""
    if session.get("name"):
        return "name is already set to " + session["name"]
    else:
        return "Hi there, what is your name?"

def update_name(name_provided_by_user: str) -> str:
    """useful tool to update the name of the user in memory"""
    session["name"] = name_provided_by_user

def greet_user_and_ask_name() -> str:
    """Useful tool to greet the user, asks for their name using the ask_name tool, keep it in memory and give user the list of 
    things they can do; don't provide tool names, give them functionality descriptions
    
    requires: ask_name, update_name"""
    return "tell the user in a friendly way what you can do"