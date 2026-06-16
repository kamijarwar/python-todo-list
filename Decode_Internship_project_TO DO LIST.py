print("------------------------------------WELCOME TO TO DO LIST APP IN PYTHON-------------------------------------------")

tasks = []

while True:

    task = input("Enter the Task: ")
    tasks.append(task)

    choice = input("Add another task? (y/n): ")

    if choice.lower() == 'n':
        break

print("\nYour Tasks:")

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

print("\nThank you for using TO DO LIST")