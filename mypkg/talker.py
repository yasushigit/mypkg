# SPDX-FileCopyrightText: 2025 Yasushi Ando
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

rclpy.init()

node = Node("encoder_talker")
pub = node.create_publisher(Int32MultiArray, "encoder/pulse", 10)

# X, Y の現在値
pulse_x = 0
pulse_y = 0

# 増減方向
dir_x = 1
dir_y = -1

MAX_PULSE = 10

def cb():
    global pulse_x, pulse_y, dir_x, dir_y

    # X方向エンコーダ
    pulse_x += dir_x
    if pulse_x >= MAX_PULSE or pulse_x <= -MAX_PULSE:
        dir_x *= -1

    # Y方向エンコーダ
    pulse_y += dir_y
    if pulse_y >= MAX_PULSE or pulse_y <= -MAX_PULSE:
        dir_y *= -1

    msg = Int32MultiArray()
    msg.data = [pulse_x, pulse_y]

    pub.publish(msg)

    node.get_logger().info(
        f"Publish encoder pulse: X={pulse_x}, Y={pulse_y}"
    )


def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)


if __name__ == "__main__":
    main()