"""Create a function that takes an integer as an argument 
and returns "Even" for even numbers or "Odd" for odd numbers."""

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"    
    
    

"""We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?"""    

def number_to_string(num):
    return str(num)


"Write a function that removes the spaces from the string, then return the resultant string"""


def no_space(x):   
    return x.replace(" ", "")


"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces."""

def get_count(input_str):
    return sum(char in "aeiou" for char in input_str)

if __name__ == "__main__":
    print("Demo: codewars_solutions.py\n")

    print("1) even_or_odd")
    for n in (2, 7, 0, -3):
        print(f"   even_or_odd({n}) -> {even_or_odd(n)}")

    print("\n2) number_to_string")
    for n in (67, 0, -12):
        print(f"   number_to_string({n}) -> {number_to_string(n)}")

    print("\n3) no_space")
    for s in ("8 j 8   mBliB8g  imjB8B8  jl  B", " no spaces "):
        print(f'   no_space("{s}") -> "{no_space(s)}"')

    print("\n4) get_count")
    for s in ("abracadabra", "hello world", "my pyx"):
        print(f'   get_count("{s}") -> {get_count(s)}')
