from rover_dynamics.actuator_model import ActuatorModel


actuator = ActuatorModel(
    torque_constant=0.02,
    gear_ratio=50.0,
    efficiency=0.80
)

current = 5.0

motor_torque = actuator.current_to_motor_torque(
    current
)

wheel_torque = actuator.current_to_wheel_torque(
    current
)

print("Current =", current, "A")
print("Motor torque =", motor_torque, "N*m")
print("Wheel torque =", wheel_torque, "N*m")