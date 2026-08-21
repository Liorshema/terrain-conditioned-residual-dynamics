from rover_dynamics.dynamic_model import RoverDynamicModel


model = RoverDynamicModel(
    mass=20.0,
    yaw_inertia=2.0,
    track_width=0.60
)

# state = [x, y, theta, v, omega]
state = [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
]

# Asymmetric left/right forces
force_left = 4.0
force_right = 6.0

dt = 0.1
simulation_time = 5.0

steps = int(simulation_time / dt)

for i in range(steps):

    state = model.step(
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