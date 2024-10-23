# main.py

import sys
from validate_number import validate_number
from generate_number import generate_number
2
def print_menu():
    print("Luhn Algoritması Projesi")
    print("1. Numara Doğrulama")
    print("2. Geçerli Numara Oluşturma")
    print("3. Chatbot ile Etkileşim")
    print("4. Çıkış")

def main():
    while True:
        print_menu()
        choice = input("Seçiminizi yapın (1/2/3/4): ").strip()
        if choice == '1':
            validate_number()
        elif choice == '2':
            generate_number()
        elif choice == '3':
            chatbot_main()
        elif choice == '4':
            print("Çıkış yapılıyor...")
            sys.exit()
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
        main()
