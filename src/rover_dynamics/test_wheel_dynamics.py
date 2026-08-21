from rover_dynamics.wheel_model import WheelModel
from rover_dynamics.dynamic_model import RoverDynamicModel


# Physical parameters
wheel_radius = 0.15
track_width = 0.60
mass = 20.0
yaw_inertia = 2.0


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


# Total wheel torque produced by each side
torque_left = 0.6
torque_right = 0.9


# Convert wheel torque -> ground force
force_left = wheel.torque_to_force(
    torque_left
)

force_right = wheel.torque_to_force(
    torque_right
)


print("force_left =", force_left, "N")
print("force_right =", force_right, "N")
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