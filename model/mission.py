class Mission:
    def __init__(self, target_city, priority, pilot, aircraft, distance, weather,
                 pilot_skill, aircraft_speed, fuel_capacity, mission_score):
        self.target_city = target_city
        self.priority = priority,
        self.pilot = pilot,
        self.aircraft = aircraft,
        self.distance = distance,
        self.weather = weather,
        self.pilot_skill = pilot_skill,
        self.aircraft_speed = aircraft_speed,
        self.fuel_capacity = fuel_capacity,
        self.mission_score = mission_score

    def __repr__(self):
        return (f"Target city: {self.target_city}, "
                f"priority: {self.priority}, "
                f"pilot: {self.pilot}, "
                f"aircraft: {self.aircraft}, "
                f"distance: {self.distance}, "
                f"weather: {self.weather}, "
                f"pilot_skill: {self.pilot_skill}, "
                f"aircraft_speed: {self.aircraft_speed}, "
                f"fuel_capacity: {self.fuel_capacity}, "
                f"mission_score: {self.mission_score} "
                )