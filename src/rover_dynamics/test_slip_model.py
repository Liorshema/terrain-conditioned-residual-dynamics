from rover_dynamics.slip_model import SlipModel


ideal_force = 20.0

no_slip = SlipModel(
    slip_ratio=0.0
)

with_slip = SlipModel(
    slip_ratio=0.30
)


force_no_slip = no_slip.apply_slip(
    ideal_force
)

force_with_slip = with_slip.apply_slip(
    ideal_force
)


print("Ideal force =", ideal_force, "N")

print(
    "Force with 0% slip =",
    force_no_slip,
    "N"
)

print(
    "Force with 30% slip =",
    force_with_slip,
    "N"
)