import math

from rover_dynamics.arm_kinematics import ArmKinematics


arm = ArmKinematics(
    link1_length=0.40,
    link2_length=0.36
)


# Test 1: both links horizontal
q1 = 0.0
q2 = 0.0

x, z = arm.forward_kinematics(
    q1,
    q2
)

print("Test 1")
print("q1 =", q1, "rad")
print("q2 =", q2, "rad")
print("Camera x =", x, "m")
print("Camera z =", z, "m")

print()


# Test 2:
# shoulder = 90 degrees
# elbow = 0 degrees

q1 = math.pi / 2
q2 = 0.0

x, z = arm.forward_kinematics(
    q1,
    q2
)

print("Test 2")
print("q1 =", q1, "rad")
print("q2 =", q2, "rad")
print("Camera x =", x, "m")
print("Camera z =", z, "m")