# Task 3: Employee Salary Records
employees = {"Alice": 50000, "Brian": 62000, "Cynthia": 58000,
             "David": 45000, "Esther": 70000}

print("Employees and salaries:")
for name, salary in employees.items():
    print(f"  {name}: KSh {salary}")

employees["Brian"] = 65000     # update salary
employees["Felix"] = 48000     # add new employee

total = sum(employees.values())
print(f"Total salary payable: KSh {total}")
