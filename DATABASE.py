

import mysql.connector as conn

# import os untuk melakukan perulangan pada output menu
import os

# =======================================
# bagian untuk connect ke localHost

class Connection:
  def __init__(self):
    self.con = conn.connect(
      host="localhost",
      user="root",
      database="",
      password="1409"
    )
    if self.con.is_connected():
      print("berhasil")
    else:
      print("gagal")

# ========================================

class CRUD(Connection):
  def __init__(self):
    super().__init__()
    self.cursor = self.con.cursor()
    self.tablename = None

# jika hasil input = 1, maka akan menghasilkan output database
  def showDB(self):
    try:
      query = "SHOW DATABASES"
      self.cursor.execute(query)
      result = self.cursor.fetchall()
      for data in result:
        print(data)
        
    except Exception as e:
      print(e, "warning gagal")

# ============================================================

# jika hasil input = 2, maka akan membuat data base dan hasilnya akan muncul di SHOW DATABASES
  def createDB(self):
      print("ANDA SEDANG BERADA DI PAGE CREATE DATABASE")
      try:
        DBname = input("\nSILAHKAN MASUKKAN NAMA DATABASE YANG INGIN ANDA BUAT : ")
        quary = ("CREATE DATABASE IF NOT EXISTS " + DBname)
        self.cursor.execute(quary)
        self.con.commit()
        self.con.database = DBname
        return(self.con.database)
      except Exception as e:
        print(e, "error")

# =============================================================

def menu ():
    print("1. SHOW DATABASES")
    print("2. CREATE DATABASE")
    print("0. KELUAR")    
    imenu = input("Pilih menu> ")
    
# =============================================================

    os.system
    
    if imenu == "1":
        db.showDB()
    elif imenu == "2":
        db.createDB()
    elif imenu == "0":
        imenu = input("apakah anda yakin ingin keluar [y/n]")
        if imenu == "y":
            exit()
        else:
            print("selamat datang kembali di: ")
    else:
      print("menu yang anda pilih tidak tersedia")
      
# =============================================================
      
if __name__ == "__main__":
  
      db = CRUD()
      
      while(True):
        menu()
        continue

