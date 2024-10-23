# chatbot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from luhn import is_luhn_valid, generate_luhn_number

# Chatbot oluşturma
chatbot = ChatBot('LuhnBot')
trainer = ListTrainer(chatbot)

# Eğitim verisi
trainer.train([
    "Merhaba",
    "Merhaba! Size nasıl yardımcı olabilirim?",
    "Kart numarası doğrulamak istiyorum.",
    "Elbette, kart numaranızı girin.",
    "1234567890123456",
    "Bu kart numarası geçersiz.",
    "Geçerli bir kart numarası girmek için yardımcı olabilir miyim?",
    "Evet, lütfen.",
    "Geçerli bir kart numarası oluşturmak istiyorum.",
    "Tamam, kısmi numaranızı girin.",
    "123456789012345",
    "Oluşturulan geçerli numara: 1234567890123452"
])

def get_response(user_input):
    response = chatbot.get_response(user_input)
    if "geçersiz" in str(response).lower() or "geçerli" in str(response).lower():
        return str(response)
    if user_input.isdigit():
        if len(user_input) in [13, 15, 16, 19]:
            valid = is_luhn_valid(user_input)
            return "Bu kart numarası geçerlidir." if valid else "Bu kart numarası geçersiz."
        else:
            return "Kart numaranızın uzunluğunu kontrol edin."
    if user_input.startswith("Oluşturulan geçerli numara"):
        parts = user_input.split(": ")
        if len(parts) == 2:
            return parts[1]
    return str(response)

def main():
    print("LuhnBot'a Hoşgeldiniz! Kredi kartı numarası doğrulama veya oluşturma işlemleri için buradayım.")
    while True:
        user_input = input("Siz: ")
        if user_input.lower() in ['çıkış', 'exit', 'quit']:
            print("LuhnBot: Görüşmek üzere!")
            break
        response = get_response(user_input)
        print(f"LuhnBot: {response}")

if __name__ == "__main__":
    main()
