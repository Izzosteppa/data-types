def boolean():
    """
    Question 1 - Boolean

    Using the variable below, give it the value 'True', then print it.
    """
    staying_alive = True
    print(staying_alive)


def integer():
    """
    Question 2 - Integer

    Create a program to accept two numbers from a user and multiply them, then print the product.
    """

    num1 = int(input("Enter first number\n"))
    num2 = int(input("Enter second number\n"))

    product = num1 * num2

    print("The product is", product)


def string():
    """
    Question 3 - String

    Assign a name to the variable below and print it.
    """

    your_name = None
    print(your_name)

def convert_to_float():
    """
    Question 4 - Float

    Convert the following integer to a float then print it.
    """

    int_num=60

    int_num = 60
    float_num = float(int_num)
    print(float_num)


def all_data_types():
    """
    Question 5 - All Data Types

    Output the following sentence using the given variables.

    Welcome to the 2023 WeThinkCode_ bootcamp where True learning costs R0.00
    """
   
    string_one = "Welcome to the "
    string_two = " WeThinkCode_ bootcamp where "
    string_3 = " learning costs R"
    bool_condition = True
    int_year = 2023
    float_cost = 0.00

    output_string = f"{string_one}{int_year}{string_two}{bool_condition}{string_3}{float_cost:.2f}"
    

    print(output_string)