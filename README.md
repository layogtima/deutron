# Deutron the Quadwalker

Welcome to the repository for Deutron, the adorable sentient desk buddy with a penchant for curiosity and a knack for task management! Designed and engineered with love at Absurd Industries, Deutron is not just a robot but a companion who brings life to your workspace with a symphony of servos and a flash of LEDs.

## Overview

Deutron is a quadruped robot powered by an Arduino Nano Board and an array of servos that give life to its four agile legs. Each limb is a marvel of miniaturization, driven by three servos and capable of intricate movements that not only charm but also assist users in their daily tasks.

The codebase you'll find here controls the very soul of Deutron, choreographing its movements, managing its mood lighting, and ensuring that its interactions are as engaging as they are helpful. This project has evolved from a simple remote-controlled crawling robot into a dynamic and interactive desktop companion.

## Features

- **Mood Lighting**: Equipped with NeoPixels, Deutron expresses its mood and adds ambience to your work environment.
- **Task Management**: It offers motivational boosts and provides you with quests throughout your day to increase productivity.
- **Interactive Gestures**: Deutron can perform a series of movements such as waving, nodding, or even a little dance!

## Codebase Structure

At the heart of Deutron's operation is a set of carefully crafted routines that govern its behavior:

- `setup()`: Initializes the servos, sets the default positions, and starts the servo service.
- `loop()`: Contains sequences for Deutron’s movements, demonstrating its range of capabilities.
- Movement functions: Detailed algorithms for complex maneuvers like `step_forward()`, `turn_left()`, `body_dance()`, and more.
- Servo control: Core functions that convert high-level commands into servo movements.

## How to Contribute

We warmly welcome contributions from fellow robotic enthusiasts and creative minds! Whether it's refining the movement algorithms, adding new features, or even fixing a bug, your input can help Deutron evolve.

1. **Fork the Repository**: Get your own fork of the code, where you can make your proposed changes.
2. **Make Your Changes**: Work on your fork to add enhancements, fix issues, or implement new features.
3. **Test Your Changes**: Ensure that any modifications maintain Deutron’s functionality and enhance its performance.
4. **Submit a Pull Request**: Once you're happy with your work, submit a PR back to the main repo for review.

## Getting Started

Before diving into Deutron's code, we recommend familiarizing yourself with Arduino programming and basic robotic principles. To get started:

- Ensure you have the required libraries installed.
- Adjust and calibrate Deutron’s servos using the provided adjustment functions.
- Upload the code to your Arduino Nano and watch Deutron come to life!

# Deutron's Movement Functions

Deutron is equipped with a variety of movement functions, allowing for a wide range of interactions and behaviors. These functions are designed to be called with specific parameters to control Deutron's movement speed, direction, and style.

## List of Movement Functions

- `stand()`: Brings Deutron to a standing position from any state.
- `sit()`: Commands Deutron to move into a sitting position.
- `turn_left(steps)`: Rotates Deutron to the left for the specified number of 'steps'.
- `turn_right(steps)`: Rotates Deutron to the right for the specified number of 'steps'.
- `step_forward(steps)`: Moves Deutron forward for the specified number of 'steps'.
- `step_back(steps)`: Moves Deutron backward for the specified number of 'steps'.
- `head_up(amount)`: Raises Deutron's head by the specified 'amount'.
- `head_down(amount)`: Lowers Deutron's head by the specified 'amount'.
- `body_left(amount)`: Leans Deutron's body to the left by the specified 'amount'.
- `body_right(amount)`: Leans Deutron's body to the right by the specified 'amount'.
- `hand_wave(times)`: Performs a waving gesture with the specified number of 'times'.
- `hand_shake(times)`: Performs a shaking gesture with the specified number of 'times'.
- `body_dance(times)`: Makes Deutron perform a dance for the specified number of 'times'.

## Serial Communication Protocol

To communicate with Deutron via serial communication, you need to follow the established protocol. Each command is sent as a string of characters followed by a newline character (`\n`). The general format for a command is as follows:


Responses from Deutron will be sent back over the serial connection, confirming the execution of commands or any errors encountered.

## Contribution Guidelines

When contributing to the serial communication feature, please consider the following:

- **Compatibility**: Ensure that any new commands or changes remain compatible with the existing communication protocol.
- **Documentation**: Any new functions should be well-documented, both in the code and in the repository README.
- **Testing**: Thoroughly test the functions to ensure they work reliably before submitting a pull request.

We look forward to your innovative ideas and contributions to make Deutron not just a robot, but a true companion!

## Community & Support

Join our community if you're as excited about desk-side robotics as we are! For support, questions, or a friendly chat with the creators:

- **Join Our Discord**: A place for discussion, sharing ideas, and getting help from fellow members.
- **Submit Issues**: If you come across any problems, feel free to open an issue in this repository.

## License

Deutron's code is open-source and is available under the GPL 3.0 License. We believe in the power of open innovation and encourage you to tinker with and build upon our little Quadwalker.

Thank you for your interest in Deutron, the Quadwalker. We can't wait to see the ways you'll help it grow! 🚀

---

**Note**: This README is an abstract representation of the Deutron codebase and project for the purposes of this example. Please adapt and expand based on the actual details and requirements of your project.
