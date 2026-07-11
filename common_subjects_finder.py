student1 = set()
student2 = set()

for i in range(3):
    subject = input("Enter Student 1 subject: ")
    student1.add(subject)

for i in range(3):
    subject = input("Enter Student 2 subject: ")
    student2.add(subject)

print("\n===== RESULT =====")

print("Common Subjects:")
print(student1.intersection(student2))

print("\nAll Subjects:")
print(student1.union(student2))

print("\nSubjects only Student 1 likes:")
print(student1.difference(student2))
