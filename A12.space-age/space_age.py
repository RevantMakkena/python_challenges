
class SpaceAge:
    def __init__(self, seconds):
        self.given_days = seconds/86400
        self.earth_days = 365.25
        self.mercury_days = self.earth_days * 0.2408467
        self.venus_days = self.earth_days * 0.61519726
        self.mars_days = self.earth_days * 1.8808158
        self.jupiter_days = self.earth_days * 11.862615
        self.saturn_days = self.earth_days * 29.447498
        self.uranus_days = self.earth_days * 84.016846
        self.neptune_days = self.earth_days * 164.79132

    def on_earth(self):
        return self.calculate_days(self.earth_days)

    def on_mercury(self):
        return self.calculate_days(self.mercury_days)

    def on_venus(self):
        return self.calculate_days(self.venus_days)

    def on_mars(self):
        return self.calculate_days(self.mars_days)

    def on_jupiter(self):
        return self.calculate_days(self.jupiter_days)

    def on_saturn(self):
        return self.calculate_days(self.saturn_days)

    def on_uranus(self):
        return self.calculate_days(self.uranus_days)

    def on_neptune(self):
        return self.calculate_days(self.neptune_days)

    def calculate_days(self, days):
        return round(self.given_days/days, 2)


x = SpaceAge(189839836)
print(x.on_venus())
