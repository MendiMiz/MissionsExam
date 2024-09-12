class Target:
    def __init__(self, target_city, priority):
        self.target_city = target_city
        self.priority = priority

    def __repr__(self):
        return f"target_city: {self.target_city}, priority: {self.priority}"