# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3

def right_angled_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end='')  # Print '*' without a newline
        print()  # Move to the next line after the inner loop

# Example usage
n = 3
right_angled_triangle(n)

