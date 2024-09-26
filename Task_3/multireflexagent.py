
class Thermostat:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp

    def check_temperature(self, current_temp):
        if current_temp < self.desired_temp:
            return "Turn On the Heater"
        elif current_temp > self.desired_temp:
            return "Turn On the Air Conditioner"
        else:
            return "Temperature is Fine"

agent = Thermostat(22)
rooms = {
    "living room": 27,
    "bedroom": 20,
    "kitchen": 30
}

for room,temp in rooms.items():
    action = agent.check_temperature(temp)
    print(f"{room}: {temp} --> {action}")
