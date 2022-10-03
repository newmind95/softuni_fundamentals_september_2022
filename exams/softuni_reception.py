employee_efficiency1 = int(input())
employee_efficiency2 = int(input())
employee_efficiency3 = int(input())
students_count = int(input())

total_time_needed = (employee_efficiency1 + employee_efficiency2
                                          + employee_efficiency3)
time_needed = 0

while students_count > 0:
    students_count -= total_time_needed
    time_needed += 1
    if time_needed % 4 == 0:
        time_needed += 1

print(time_needed)
