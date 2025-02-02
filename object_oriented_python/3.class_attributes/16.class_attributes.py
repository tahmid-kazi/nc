class SmartDevice:
    # unit 2 done (932pm)
    # looked at ovpn (932-950pm)
    # this chapt done (2/1/25)(950-952pm)(Sat. night)
    # 952-1030pm) ovpn 1st in 4 days + ate cheese rice panda express mushroom chicken
    
    # Add your class attributes here
    total_devices = 0
    active_devices = 0

    def __init__(self, name: str):
        self.name = name
        SmartDevice.total_devices += 1  # Each new device adds to total
        
    # Implement these methods
    def turn_on(self) -> None:
        SmartDevice.active_devices += 1
        
    def turn_off(self) -> None:
        SmartDevice.active_devices -= 1



# Don't change anything below this line
tv = SmartDevice("TV")
lights = SmartDevice("Lights")

# Control devices
tv.turn_on()
lights.turn_on()
tv.turn_off()

print(f"Total Devices: {SmartDevice.total_devices}")    # Shows 2
print(f"Active Devices: {SmartDevice.active_devices}")  # Shows 1
