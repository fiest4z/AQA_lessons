class Address:
    def __init__(self, index, city, street, housenumber, flatnumber):
        self.index = index
        self.city = city
        self.street = street
        self.housenumber = housenumber
        self.flatnumber = flatnumber

    def __str__(self):
        return f"{self.index}, {self.city}, {self.street}, {self.housenumber} - {self.flatnumber}"
