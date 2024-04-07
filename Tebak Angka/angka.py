import random

# Mendefinisikan angka yang harus ditebak
target_number = random.randint(1, 100)

# Fungsi untuk memeriksa tebakan
def check_guess(guess):
    try:
        guess = int(guess)
        if guess < 1 or guess > 100:
            return "Silakan masukkan angka antara 1 dan 100."
        elif guess < target_number:
            return "Tebakan Anda terlalu rendah. Coba lagi!"
        elif guess > target_number:
            return "Tebakan Anda terlalu tinggi. Coba lagi!"
        else:
            return "Selamat! Tebakan Anda benar!"
    except ValueError:
        return "Mohon masukkan angka yang valid."

# Main loop permainan
while True:
    guess_input = input("Masukkan angka antara 1 dan 100: ")
    message = check_guess(guess_input)
    print(message)
    if message == "Selamat! Tebakan Anda benar!":
        break
