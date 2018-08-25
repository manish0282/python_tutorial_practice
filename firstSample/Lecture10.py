
arr = [2,3,4,1,-9,8,4]

# Q: WAP to print the maximum of a given array
def print_max(arr):
    max = arr[0]
    for idx in range(1, len(arr)):
        if arr[idx] > max:
            max = arr[idx]
    print("\nMaximum value is " + str(max))

print_max(arr)

# Q: WAP to print the minimum of a given array
def print_min(arr):
    min = arr[0]
    for idx in range(1, len(arr)):
        if arr[idx] < min:
            min = arr[idx]
    print("\nMinimum value is " + str(min))

print_min(arr)

# Q: WAP to print prime numbers from 1-100
def check_if_prime(num):
    if num == 1:
        return True
    if num % 2 == 0:
        return False
    for idx in range(2, int(num / 2)):
        if num % idx == 0:
            return False
    return True

def print_prime_number(min_limit, max_limit):
    for idx in range(min_limit, max_limit):
        if check_if_prime(idx):
            print(str(idx), end=" ")

print_prime_number(1, 100)

# Q: WAP to print student_name-Present/ Absent
def print_studentname_Status(student_state):
    for kii, vii in student_state.items():
        print(kii, vii)
print("\n")

student_state = {"Std1":"Present", "Std2":"Absent"}
print_studentname_Status(student_state)
