from rover_dynamics.kinematic_model import RoverKinematicModel


model = RoverKinematicModel(
    wheel_radius=0.15,
    track_width=0.60
)

# Initial state: x, y, theta
state = [0.0, 0.0, 0.0]

# Both sides rotate at the same speed
omega_left = -2.0
omega_right = 2.0

# Simulation settings
dt = 0.1
simulation_time = 10.0

steps = int(simulation_time / dt)

for i in range(steps):
    state = model.step(
        state,
        omega_left,
        omega_right,
        dt
    )

    print(
        f"time = {(i + 1) * dt:.1f} s, "
        f"x = {state[0]:.3f} m, "
        f"y = {state[1]:.3f} m, "
        f"theta = {state[2]:.3f} rad"
    )