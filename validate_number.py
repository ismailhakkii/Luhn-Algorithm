# validate_number.py

from luhn import is_luhn_valid

def validate_number():
    """
    Kullanıcıdan bir numara alır ve Luhn algoritmasına göre doğruluğunu kontrol eder.
    """
    number = input("Doğrulamak istediğiniz numarayı girin: ").strip()
    if not number.isdigit():
        print("Hata: Numara sadece rakamlardan oluşmalıdır.")
        return
    if is_luhn_valid(number):
        print("Numara geçerlidir.")
    else:
        print("Numara geçersizdir.")
