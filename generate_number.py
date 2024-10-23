# generate_number.py

from luhn import generate_luhn_number

def generate_number():
    """
    Kullanıcıdan bir kısmı numara alır ve geçerli bir Luhn numarası oluşturur.
    """
    partial = input("Geçerli bir numara oluşturmak için numaranın kısmını girin: ").strip()
    if not partial.isdigit():
        print("Hata: Numara sadece rakamlardan oluşmalıdır.")
        return
    full_number = generate_luhn_number(partial)
    print(f"Oluşturulan geçerli numara: {full_number}")
