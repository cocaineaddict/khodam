import warnings

warnings.filterwarnings("ignore", message="Signature .* for <class 'numpy.longdouble'> does not match any known type")

import numpy as np
import pandas as pd
import random
from datetime import datetime


animals_50 = [
    "Harimau", "Komodo", "Orang Utan", "Anjing Kintamani", "Merak",
    "Badak Bercula Satu", "Garuda", "Macan Dahan", "Banteng", "Ayam Bekisar",
    "Jelarang", "Lumba-lumba", "Cenderawasih", "Tapir", "Elang Jawa",
    "Kucing Sumatera", "Naga Air", "Barong", "Rangda", "Legong",
    "Anoa", "Cendrawasih", "Badak Sumatera", "Gajah Sumatra", "Macan Tutul Jawa",
    "Penyu Belimbing", "Buaya Muara", "Bekantan", "Rusa Timor", "Kalong",
    "Paus Sperma", "Hirola", "Tarsius", "Ular Sanca Kembang", "Ajag",
    "Burung Mandar", "Elang Flores", "Kakatua Raja", "Kuskus", "Monyet Hitam Sulawesi",
    "Kadal Draco", "Kanguru Pohon", "Ikan Arwana", "Ikan Cupang", "Kuda Nil",
    "Gajah Borneo", "Landak Jawa", "Tupai Terbang", "Katak Pohon", "Ular Piton"
]

powers_50 = [
    "Melompat", "Menyala", "Mengambang", "Jentikan", "Gelap",
    "Terangi", "Kilatan", "Lenggok", "Silaukan", "Gemerlap",
    "Bergetar", "Pijarkan", "Terawang", "Bertukar", "Menyatu",
    "Berubah", "Menggulung", "Berputar", "Pecah", "Goyang",
    "Bertahan", "Gesit", "Bringas", "Ngelmu", "Mendung",
    "Berkilau", "Bercahaya", "Berkelebat", "Melayang", "Merayap",
    "Membesar", "Mengecil", "Terbang", "Lari", "Ngedrip",
    "Nglayang", "Nggeblak", "Bledosan", "Nglimpe", "Nglecer",
    "Ceprotan", "Lemes", "Cemeng", "Nyenyet", "Kebak",
    "Nglebur", "Ngemot", "Gumulung", "Berbunyi", "Petir"
]

df_50 = pd.DataFrame({
    "Animals": animals_50,
    "Powers": powers_50
})

csv_path_50 = "/home/cocaine/khodam/Animals_and_Powers_50.csv"
df_50.to_csv(csv_path_50, index=False)

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df['Animals'].tolist(), df['Powers'].tolist()

def calculate_khodamcode(input_string):
    today = datetime.now()
    base_code = sum(ord(char) for char in input_string)
    date_code = today.year + today.month + today.day
    final_code = base_code + date_code
    # 25% chance to set khodamcode to "kosong"
    if random.random() < 0.25:
        return "kosong"
    else:
        return final_code

def select_animal_and_power(animals, powers, code):
    if code == "kosong":
        return "kosong", "kosong"
    index = code % 50
    return animals[index], powers[index]

if __name__ == "__main__":
    animals, powers = load_data(csv_path_50)
    user_input = input("Cek Khodam! tulislah nama anda: ")
    khodamcode = calculate_khodamcode(user_input)
    animal, power = select_animal_and_power(animals, powers, khodamcode)
    print(f"{animal} {power}")
