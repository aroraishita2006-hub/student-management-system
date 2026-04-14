import os
File_name="students.txt"
def load_data():
    students=[]
    if os.path.exists(File_name):
        with open(File_name,"r") as f:
            for line in f:
                name,m1,m2,m3=line.strip().split(",")
                marks=[int(m1),int(m2),int(m3)]
                total=sum(marks)
                percentage=total/3
                students.append({
                    "name":name,
                    "marks":marks,
                    "total":total,
                    "percentage":percentage

                })
    return students
def save_data(students):
    with open(File_name,"w") as f:
        for s in students:
            f.write(f"{s['name']},{s['marks'][0]},{s['marks'][1]},{s['marks'][2]}\n")
def add_data(students):
    name=input("Enter name: ")
    marks=list(map(int,input("Enter marks in 3 subjects: ").split()))
    total=sum(marks)
    percentage=total/3
    students.append({
        "name":name,
        "marks":marks,
        "total":total,
        "percentage":percentage
    })
    save_data(students)
    print("Student added successfully!")

def view_data(students):
    if not students:
        print("No records found!")
        return
    
    print("\n---Student Records---")
    for s in students:
        print(f"{s['name']} -> {s['marks']} | {s['percentage']:.2f}%")

def search_data(students):
    name=input("Enter name to be search: ")
    for s in students:
        if s["name"].lower()==name.lower():
             print(f"Found: {s['name']} -> {s['marks']} | {s['percentage']:.2f}%")
             return
    print("Student not found!")

def update_data(students):
    name = input("Enter name to update: ")
    for s in students:
        if s["name"].lower() == name.lower():
            marks = list(map(int, input("Enter new marks: ").split()))
            s["marks"] = marks
            s["total"] = sum(marks)
            s["percentage"] = s["total"] / 3
            save_data(students)
            print("Updated successfully!")
            return
    print("Student not found!")


def delete_data(students):
    name=input("Enter name to be deleted ")
    for s in students:
        if s["name"].lower()==name.lower():
            students.remove(s)
            save_data(students)
            print("Deleted successfully!")
            return
    print("Student not found!")

def topper(students):
    if not students:
        print("No data available!")
        return
    topper=max(students, key=lambda x: x["percentage"])
    print(f"Topper: {topper['name']} with {topper['percentage']:.2f}%")

def main():
    students = load_data()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_data(students)
        elif choice == "2":
            view_data(students)
        elif choice == "3":
            search_data(students)
        elif choice == "4":
            update_data(students)
        elif choice == "5":
            delete_data(students)
        elif choice == "6":
            topper(students)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()

           

