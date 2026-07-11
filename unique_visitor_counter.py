visitors = set()

while True:
    name = input("Enter visitor name: ")
    visitors.add(name)

    choice = input("Add another visitor? (yes/no): ")

    if choice == "no":
        break

print("\n===== UNIQUE VISITORS =====")

for visitor in visitors:
    print(visitor)

print("Total Unique Visitors:", len(visitors))
