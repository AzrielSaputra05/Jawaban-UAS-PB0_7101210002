# ==================================================================
# Terdapat class kendaraan yang terdiri dari( parent class dan child class )
class kendaraan:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def showInfo(self,tipe):
        print("{} health: {}".format(
            self.name,
            self.health
            )
        )

# ==================================================================

# kelas kendaraan sebagai parent class
class kendaraan_parent (kendaraan):
    def __init__(self,name):
        super().__init__(name,100)

    def showInfo(self):
        print("\nSepeda Berjalan ... ")
        
# ==================================================================
        
# kelas mobil sebagai child class
class mobil_child (kendaraan):
    def __init__(self,name):
        super().__init__(name,200)

    def showInfo(self):
        print("{}Sedan Berjalan Dengan Kecepatan {} km/j". format(
            self.name,
            self.health
        )
    )

# ==================================================================

# untuk memanggil parent class
parent = kendaraan_parent ('')

# untuk memanggil child class
child = mobil_child ('')

parent.showInfo()
child.showInfo()

# ==================================================================