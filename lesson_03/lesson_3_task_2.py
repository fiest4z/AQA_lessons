from smartphone import Smartphone

catalog = []

iPhone17 = Smartphone("iPhone", "17", "+79991111111")
iPhoneAir = Smartphone("iPhone", "Air", "+79992222222")
galaxy16 = Smartphone("Samsung", "Galaxy 16", "+79993333333")
nokia3310 = Smartphone("Nokia", "3310", "+79994444444")
poco = Smartphone("Poco", "XProMaxUltra", "+79995555555")
catalog.append(iPhone17)
catalog.append(iPhoneAir)
catalog.append(galaxy16)
catalog.append(nokia3310)
catalog.append(poco)
for element in catalog:
    print(f"{element.brand} - {element.model}. {element.phonenumber}")
