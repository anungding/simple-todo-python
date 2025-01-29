students = []  # List untuk menyimpan data mahasiswa

# Fungsi untuk menambahkan mahasiswa
def add_student():
    name = input("NAMA MAHASISWA: ")
    major = input("JURUSAN: ")
    students.append({"name": name, "major": major})
    print("Data berhasil ditambahkan!\n")

# Fungsi untuk menampilkan data mahasiswa
def show_students():
    if len(students) > 0:
        print("\n--- DAFTAR MAHASISWA ---")
        for i, student in enumerate(students):
            print(f"[{i}] Nama: {student['name']}, Jurusan: {student['major']}")
        print("------------------------\n")
    else:
        print("\nData tidak ada!\n")

# Fungsi untuk mengedit data mahasiswa
def edit_student():
    show_students()  # Tampilkan daftar mahasiswa terlebih dahulu
    if len(students) > 0:
        try:
            index = int(input("Masukkan indeks mahasiswa yang ingin diedit: "))
            if 0 <= index < len(students):
                name = input("Nama baru: ")
                major = input("Jurusan baru: ")
                students[index] = {"name": name, "major": major}
                print("Data berhasil diperbarui!\n")
            else:
                print("Indeks tidak valid!\n")
        except ValueError:
            print("Masukkan angka yang valid!\n")

# Fungsi untuk menghapus mahasiswa berdasarkan indeks
def delete_student():
    show_students()  # Tampilkan daftar mahasiswa terlebih dahulu
    if len(students) > 0:
        try:
            index = int(input("Masukkan indeks mahasiswa yang ingin dihapus: "))
            if 0 <= index < len(students):
                deleted_student = students.pop(index)
                print(f"Mahasiswa {deleted_student['name']} berhasil dihapus!\n")
            else:
                print("Indeks tidak valid!\n")
        except ValueError:
            print("Masukkan angka yang valid!\n")

# Fungsi untuk menampilkan menu
def show_menu():
    print("----------- MENU ----------")
    print("[1] Show Data")
    print("[2] Add Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    
    menu = input("PILIH MENU> ")
    if menu == "1":
        show_students()
    elif menu == "2":
        add_student()
    elif menu == "3":
        edit_student()
    elif menu == "4":
        delete_student()
    elif menu == "5":
        print("Keluar dari program. Sampai jumpa!")
        exit()
    else:
        print("Menu tidak valid!\n")

# Main program
if __name__ == "__main__":
    while True:
        show_menu()
