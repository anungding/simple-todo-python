
students = []

def add_student():
    name = input("NAMA MAHASISWA:")
    major = input("JURUSAN:")
    students.append({"name": name, "major": major})

def show_students():
    if len(students) > 0:
        print(students)
    else:
        print("Data tidak ada!")
       


def show_menu():
    print("----------- MENU ----------")
    print("[1] Show Data")
    print("[2] Add Data")
    
    menu = input("PILIH MENU> ")
    if menu == "1":
        show_students()
    elif menu == "2":
        add_student()
    elif menu == "3":
        exit()
    else:
        print("Salah pilih!")

if __name__ == "__main__":

    while(True):
        show_menu()