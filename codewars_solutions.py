"""Codewars practice solutions."""

def even_or_odd(number: int) -> str:
    """Return 'Even' if number is divisible by 2; otherwise return 'Odd'."""
    return "Even" if number % 2 == 0 else "Odd"


def number_to_string(num: int) -> str:
    """Convert an integer to its string representation."""
    return str(num)


def no_space(x: str) -> str:
    """Return the input string with all spaces removed."""
    return x.replace(" ", "")


def get_count(input_str: str) -> int:
    """Count lowercase vowels (a, e, i, o, u) in the input string."""
    vowels = "aeiou"
    return sum(char in vowels for char in input_str)


if __name__ == "__main__":
    print("Demo: codewars_solutions.py\n")

    print("1) even_or_odd")
    for n in (2, 7, 0, -3):
        print(f"   even_or_odd({n}) -> {even_or_odd(n)}")

    print("\n2) number_to_string")
    for n in (67, 0, -12):
        print(f"   number_to_string({n}) -> {number_to_string(n)}")

    print("\n3) no_space")
    for s in ("8 j 8   mBliB8g  imjB8B8  jl  B", " no spaces ", "     "):
        print(f'   no_space("{s}") -> "{no_space(s)}"')

    print("\n4) get_count")
    for s in ("abracadabra", "hello world", "my pyx", "     "):
        print(f'   get_count("{s}") -> {get_count(s)}')


