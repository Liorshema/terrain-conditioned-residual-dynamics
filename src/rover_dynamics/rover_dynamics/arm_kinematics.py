import math


class ArmKinematics:
    def __init__(self, link1_length, link2_length):
        self.l1 = link1_length
        self.l2 = link2_length

    def forward_kinematics(self, q1, q2):
        """
        Compute camera position for a planar 2-link arm.

        q1 = shoulder angle [rad]
        q2 = elbow angle [rad]

        Returns:
        x_camera, z_camera
        """

        x_camera = (
            self.l1 * math.cos(q1)
            + self.l2 * math.cos(q1 + q2)
        )

        z_camera = (
            self.l1 * math.sin(q1)
            + self.l2 * math.sin(q1 + q2)
        )

        return x_camera, z_camera