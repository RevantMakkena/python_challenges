from datetime import time, timedelta
from dateutil.relativedelta import relativedelta


class SpaceAge:
    def __init__(self, seconds):
        self.secs = seconds
        self.earth_days = timedelta(seconds=31557600)
        self.mercury_days = 0.2408467 * 365
        self.venus_days = 0.61519726 * 365
        self.mars_days = 1.8808158*365
        self.jupiter_days = 11.862615*365
        self.saturn_days = 29.447498 * 365
        self.uranus_days = 84.016846 * 365
        self.neptune_days = 164.79132 * 365

    def on_earth(self):
        return round(timedelta(seconds=self.secs)/self.earth_days, 2)

    def on_mercury(self):
        return round(timedelta(seconds=self.secs).days/self.mercury_days, 2)

    def on_venus(self):
        return round(timedelta(seconds=self.secs).days/self.venus_days, 2)

    def on_mars(self):
        return round(timedelta(seconds=self.secs).days/self.mars_days, 2)

    def on_jupiter(self):
        return round(timedelta(seconds=self.secs).days/self.jupiter_days, 2)

    def on_saturn(self):
        return round(timedelta(seconds=self.secs).days/self.saturn_days, 2)

    def on_uranus(self):
        return round(timedelta(seconds=self.secs).days/self.uranus_days, 2)

    def on_neptune(self):
        return round(timedelta(seconds=self.secs).days/self.neptune_days, 2)


x = SpaceAge(189839836)
print(x.on_venus())
