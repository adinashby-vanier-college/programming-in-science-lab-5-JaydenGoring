# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""

    for i in range(n):
        for j in range(n):
            if(i == 0 or i == n - 1 or j == 0 or j == n - 1):
                result += "*"
            else:
                result += " "
        
        result += "\n"

    return result.rstrip()
    
# print(hollow_square(5))

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""

    for i in range(n):
        count = 1
             
        for j in range(i + 1):
            result += str(count)
            count += 1

        result += "\n"

    return result.rstrip()

# print(number_pattern(4))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    count = 1
    sum = 0
    while count <= n:
            sum += count
            count += 1

    return sum

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(n):
        for k in range(n - i - 1):
            result += " "
        for j in range(((i + 1) * 2) - 1):
            result += "*"
        
        result += "\n"

    return result.rstrip()

print(centered_star_pyramid(4))
