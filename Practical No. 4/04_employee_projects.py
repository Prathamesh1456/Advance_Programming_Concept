# Employee Involvement in Two Projects

project1 = set(input("Enter employees in Project 1: ").split())
project2 = set(input("Enter employees in Project 2: ").split())

# Employees working on both projects
both_projects = project1.intersection(project2)

# Employees working only on Project 1
only_project1 = project1.difference(project2)

# Employees working only on Project 2
only_project2 = project2.difference(project1)

# Total unique employees
all_employees = project1.union(project2)

print("\nEmployees working on both projects:", both_projects)
print("Employees only on Project 1:", only_project1)
print("Employees only on Project 2:", only_project2)
print("Total unique employees:", all_employees)