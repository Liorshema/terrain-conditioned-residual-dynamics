# Stage 1 — ROS 2 & RViz Foundation

## Project
Terrain-Conditioned Residual Dynamics for Agricultural Mobile Robots

## Objective

The goal of Stage 1 was to establish a reproducible ROS 2 software foundation for the rover project.

The stage focused on:

- ROS 2 workspace and package structure
- Basic ROS nodes and topic communication
- Rover robot description
- TF tree
- RViz visualization
- Launch automation
- Xacro-based robot description
- Basic simulated sensor topics
- rosbag recording and playback
- Git and GitHub workflow

This stage establishes the software infrastructure required for the later kinematics, dynamics, simulation, state estimation, and residual-learning stages.

---

# 1. Development Environment

The project currently runs in:

- Windows 10
- WSL2
- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Python
- VS Code connected to WSL
- Git / GitHub

Workspace:

```text
~/ros2_ws