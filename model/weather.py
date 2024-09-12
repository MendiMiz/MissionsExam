class Weather:
    def __init__(self, location, clouds, clouds_status, wind_speed):
        self.location = location
        self.clouds = clouds
        self.clouds_status = clouds_status
        self.wind_speed = wind_speed

    def __repr__(self):
        return f"clouds: {self.clouds}, clouds_status: {self.clouds_status}, wind_speed: {self.wind_speed}"
