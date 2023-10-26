"""
RSA-Factoring Script

This program reads a file containing natural numbers, one number per line,
and factorizes each number into a product of two smaller numbers.
The factorization results are printed in the format 'n = p * q',
where n is the input number, and p and q are its factors.

Usage:
    python factorization.py <file>

Arguments:
    <file>: The path to a file containing natural numbers to factorize. 
    Each number should be on a separate line.

Example:
    python factorization.py numbers.txt

Author: thecodelegion
"""

# Define a function to factorize a number
def factorize(n):
    """
    Factorizes a natural number into two smaller numbers.

    Args:
        n (int): The natural number to be factorized.

    Returns:
        list: A list of tuples representing the factor pairs.
    """
    factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

# Define the main function
def main(file_name):
    """
    Main function to read a file and factorize numbers within it.

    Args:
        file_name (str): The path to the file containing natural numbers.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                n = int(line.strip())  # Parse the natural number from the file
                factor_pairs = factorize(n)
                for pair in factor_pairs:
                    print(f"{n} = {pair[0]} * {pair[1]}")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except ValueError:
        print("Invalid input in the file. All lines should contain valid natural numbers.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python factorization.py <file>")
    else:
        command_line_file_name = sys.argv[1]
        main(command_line_file_name)
