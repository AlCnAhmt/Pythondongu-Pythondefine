def menu():
         
    print("Seçiminizi Yapınız:")
    print("1. Menü")
    print("2. Çıkış")
    
    choice = input("Seçiminizi Yazınız:")
    
    if choice == "1":
        option1()
    elif choice == "2":
        print("Programdan Çıkılıyor...")
        exit()
    else:
        print("Yanlış Seçenek. LÜtfen Tekrar Deneyiniz.")
        menu()

def option1():
      print("1. Seçenek Seçildi")

      print("""
     1) Menü
     """)
     
      islemno=input("İşlem Numarası Giriniz>:")

      if islemno=="1":
        menu()
      else:
         print("Yanlış Tuşa Bastınız...")
         
      back_to_menu()

def back_to_menu():
    input("Enter'a Basarak Ana Menüye Dönün.")
    menu()

menu()
