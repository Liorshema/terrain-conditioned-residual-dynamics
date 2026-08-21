from rover_dynamics.actuator_model import ActuatorModel
from rover_dynamics.wheel_model import WheelModel
from rover_dynamics.dynamic_model import RoverDynamicModel
from rover_dynamics.slip_model import SlipModel


# -----------------------------
# Physical parameters
# -----------------------------

wheel_radius = 0.15
track_width = 0.60
mass = 20.0
yaw_inertia = 2.0

torque_constant = 0.02
gear_ratio = 50.0
efficiency = 0.80


# -----------------------------
# Models
# -----------------------------

actuator = ActuatorModel(
    torque_constant=torque_constant,
    gear_ratio=gear_ratio,
    efficiency=efficiency
)

wheel = WheelModel(
    wheel_radius=wheel_radius
)

nominal_rover = RoverDynamicModel(
    mass=mass,
    yaw_inertia=yaw_inertia,
    track_width=track_width
)

real_rover = RoverDynamicModel(
    mass=mass,
    yaw_inertia=yaw_inertia,
    track_width=track_width
)


# Slip model
slip = SlipModel(
    slip_ratio=0.30
)


# -----------------------------
# Initial states
# [x, y, theta, v, omega]
# -----------------------------

nominal_state = [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
]

real_state = [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
]


# -----------------------------
# Motor commands
# Same command for both models
# -----------------------------

current_left = 3.0
current_right = 3.0


# Current -> wheel torque

torque_left = actuator.current_to_wheel_torque(
    current_left
)

torque_right = actuator.current_to_wheel_torque(
    current_right
)


# Wheel torque -> ideal force

ideal_force_left = wheel.torque_to_force(
    torque_left
)

ideal_force_right = wheel.torque_to_force(
    torque_right
)


# Apply slip only to "real" rover

real_force_left = slip.apply_slip(
    ideal_force_left
)

real_force_right = slip.apply_slip(
    ideal_force_right
)


print("Ideal left force =", ideal_force_left, "N")
print("Ideal right force =", ideal_force_right, "N")

print("Real left force =", real_force_left, "N")
print("Real right force =", real_force_right, "N")

print()


# -----------------------------
# Simulation
# -----------------------------

dt = 0.1
simulation_time = 5.0

steps = int(simulation_time / dt)


for i in range(steps):

    # Nominal model
    nominal_state = nominal_rover.step(
        nominal_state,
        ideal_force_left,
        ideal_force_right,
        dt
    )

    # "Real" model with slip
    real_state = real_rover.step(
        real_state,
        real_force_left,
        real_force_right,
        dt
    )


# -----------------------------
# Residual
# -----------------------------

residual_x = real_state[0] - nominal_state[0]
residual_y = real_state[1] - nominal_state[1]
residual_theta = real_state[2] - nominal_state[2]
residual_v = real_state[3] - nominal_state[3]
residual_omega = real_state[4] - nominal_state[4]


print("----- FINAL STATES -----")

print(
    "Nominal:",
    nominal_state
)

print(
    "Real with slip:",
    real_state
)

print()

print("----- RESIDUAL -----")

print("x residual =", residual_x, "m")
print("y residual =", residual_y, "m")
print("theta residual =", residual_theta, "rad")
print("v residual =", residual_v, "m/s")
print("omega residual =", residual_omega, "rad/s")