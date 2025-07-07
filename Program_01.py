'''
@author: 22000409 Kaushal Ramoliya
@description: 1. - Write a program in Python to find factorial of a number using a loop. Also find the same using a recursive function. Implement this creating both the function in a class.
'''

class Factorial:
    # Method to calculate factorial using a loop
    def factorial_iterative(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    # Method to calculate factorial using recursion
    def factorial_recursive(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial_recursive(n - 1)

# Main function to test the class methods
if __name__ == "__main__":
    num = int(input("Enter a number to find its factorial: "))
    fact = Factorial()

    print(f"Factorial of {num} using iterative method: {fact.factorial_iterative(num)}")
    print(f"Factorial of {num} using recursive method: {fact.factorial_recursive(num)}")