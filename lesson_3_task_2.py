from smartphone import Smartphone
phones = [Smartphone("Apple", "iPhone 18", "+79098098044"),
    Smartphone("Samsung", "Galaxy S50", "+733333333"),
    Smartphone("Redmy", "Pro 9", "+7699000777"),
    Smartphone("Huawei", "P40 Pro", "+7111111112"),
    Smartphone("Sony", "XPERIA", "+73443444535")]
for phone in phones:
    print(f"{phone.brand} - {phone.model}. {phone.number}")