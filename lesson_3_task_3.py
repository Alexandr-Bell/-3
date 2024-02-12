from address import Address
from mailing import Mailing


to_address = Address("11243", "Murmansk", "Gagarina", "7", "10")
from_address = Address ("234234", "Санкт-Петербург", "Невский проспект", "2", "20")
mailing = Mailing(to_address, from_address, 156, "ABB777")


print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
