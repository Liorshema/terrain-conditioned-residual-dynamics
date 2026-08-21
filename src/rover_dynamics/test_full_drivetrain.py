from rover_dynamics.actuator_model import ActuatorModel
from rover_dynamics.wheel_model import WheelModel
from rover_dynamics.dynamic_model import RoverDynamicModel


# Physical parameters
wheel_radius = 0.15
track_width = 0.60
mass = 20.0
yaw_inertia = 2.0

# Actuator parameters
torque_constant = 0.02
gear_ratio = 50.0
efficiency = 0.80


actuator = ActuatorModel(
    torque_constant=torque_constant,
    gear_ratio=gear_ratio,
    efficiency=efficiency
)

wheel = WheelModel(
    wheel_radius=wheel_radius
)

rover = RoverDynamicModel(
    mass=mass,
    yaw_inertia=yaw_inertia,
    track_width=track_width
)


# state = [x, y, theta, v, omega]
state = [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
]


# Motor currents
current_left = 3.0
current_right = 4.0


# Current -> wheel torque
torque_left = actuator.current_to_wheel_torque(
    current_left
)

torque_right = actuator.current_to_wheel_torque(
    current_right
)


# Wheel torque -> ground force
force_left = wheel.torque_to_force(
    torque_left
)

force_right = wheel.torque_to_force(
    torque_right
)


print("Left current =", current_left, "A")
print("Right current =", current_right, "A")

print("Left wheel torque =", torque_left, "N*m")
print("Right wheel torque =", torque_right, "N*m")

print("Left force =", force_left, "N")
print("Right force =", force_right, "N")

print()


dt = 0.1
simulation_time = 5.0

steps = int(simulation_time / dt)


for i in range(steps):

    state = rover.step(
        state,
        force_left,
        force_right,
        dt
    )

    print(
        f"time = {(i + 1) * dt:.1f} s, "
        f"x = {state[0]:.3f} m, "
        f"y = {state[1]:.3f} m, "
        f"theta = {state[2]:.3f} rad, "
        f"v = {state[3]:.3f} m/s, "
        f"omega = {state[4]:.3f} rad/s"
    )