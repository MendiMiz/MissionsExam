class Cities_Cordinates:
    def __init__(self, city, lat1, lat2):
        self.city = city
        self.lat1 = lat1
        self.lat2 = lat2

    def __repr__(self):
        return f"city: {self.city}, lat1: {self.lat1}, lat2: {self.lat2}"

