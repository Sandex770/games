import random 


welcome_message = "WELCOME TO SANZZ GAMES"
tikus_position = random.randint(1, 4)

print("****************************")
print(f"** {welcome_message} **")
print("****************************")

nama_user = input("masukkan nama anda:")
    
print(f'''halo {nama_user}! coba perhatikan goa di bawah ini
|_| |_| |_| |_|
''')

pilihan_user = int(input("menurut mu tikus ada di goa nomor berapa? [1 / 2 / 3 /4] "))
    
    
# print(f"pilihan kamu adalah {pilihan_user}")


if pilihan_user == tikus_position:
    print(f"selamat {nama_user} SELAMAT KAMU MENANG!!! posisi tikus ada di {tikus_position} dan pilihanmu adalah {pilihan_user}.")
else:
    print(f"ALAH SALAH COKK , tikus bukan berada disitu tapi ada di goa nomor {tikus_position} sedangkan kamu memilih goa nomor {pilihan_user}")