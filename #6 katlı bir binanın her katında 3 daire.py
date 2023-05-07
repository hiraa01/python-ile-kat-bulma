#6 katlı bir binanın her katında 3 daire bulunmaktadır girilen dairenoya göre kaçıncı katta olduğunu göster
while True:
    no= int(input("lütfen daire numaranızı giriniz: "))
    if no<=3:
        print("1.kattasınız")
    elif no<=6 and no>3:
        print("2.kattasınız")
    elif no<=9 and no>6:
        print("3.kattasınız")
    elif no<=12 and no>9:
        print("4.kattasınız")
    elif no<=15 and no>12:
        print("5.kattasınız")
    elif no<=18 and no>15:
        print("6.kattasınız")
    else:
        print("böyle bir daire bulunmamaktadır.")


              