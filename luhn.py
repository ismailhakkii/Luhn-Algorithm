# luhn.py

def calculate_luhn_checksum(number: str) -> int:
    """
    Verilen numaranın Luhn checksum değerini hesaplar.

    Args:
        number (str): Sayı dizisi.

    Returns:
        int: Checksum değeri.
    """

    def digits_of(n):
        return [int(d) for d in n]

    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for d in even_digits:
        total += sum(digits_of(str(d * 2)))
    return total % 10


def is_luhn_valid(number: str) -> bool:
    """
    Verilen numaranın Luhn algoritmasına göre geçerli olup olmadığını kontrol eder.

    Args:
        number (str): Sayı dizisi.

    Returns:
        bool: Geçerli ise True, değilse False.
    """
    return calculate_luhn_checksum(number) == 0


def generate_luhn_number(partial_number: str) -> str:
    """
    Verilen kısmı (kontrol basamağı hariç) kullanarak geçerli bir Luhn numarası oluşturur.

    Args:
        partial_number (str): Kısmı sayı dizisi.

    Returns:
        str: Tamamlanmış geçerli Luhn numarası.
    """
    checksum = calculate_luhn_checksum(partial_number + '0')
    check_digit = (10 - checksum) % 10
    return partial_number + str(check_digit)
