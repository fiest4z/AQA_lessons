from address import Address
from mailing import Mailing

address_1 = Address(152900, "Rybinsk", "Kirova", 1, 1)
address_2 = Address(152934, "Moscow", "Sumskaya", 2, 2)


new_element = Mailing(address_1, address_2, 777, 4815162342)

print(new_element)
