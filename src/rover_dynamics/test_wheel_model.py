from rover_dynamics.wheel_model import WheelModel


wheel = WheelModel(
    wheel_radius=0.15
)

wheel_torque = 3.0

force = wheel.torque_to_force(
    wheel_torque
)

print("Wheel torque =", wheel_torque, "N*m")
print("Wheel radius =", wheel.r, "m")
print("Traction force =", force, "N")