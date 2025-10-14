# main.py - Skrip awal Python yang komprehensif
class Project:
    def __init__(self, name):
        self.name = name
        self.version = "1.0.0"
    def display_info(self):
        print(f"Nama Proyek: {self.name}, Versi: {self.version}")
def main():
    my_project = Project("Proyek Repositori Otomatis GitHub")
    my_project.display_info()
    print("\nFitur yang didemonstrasikan: Class, Fungsi, Perulangan")
    for i in range(5): print(f"  - Iterasi perulangan {i + 1}")
if __name__ == "__main__":
    main()
