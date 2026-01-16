# SPDX-FileCopyrightText: 2025 Yasushi Ando
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import math

rclpy.init()

node = Node("encoder_listener")

# パラメータ
wheel_diameter = 0.06        # エンコーダに接続されたタイヤの直径[m]
ppr = 100                   # 1回転あたりのパルス数
dt = 0.5                    # エンコーダ値が送られてくる周期[s]

# 自己位置
x = 0.0
y = 0.0


def cb(msg):
    global x, y

    pulse_x = msg.data[0]
    pulse_y = msg.data[1]

    # 移動距離 [m]
    dist_x = math.pi * wheel_diameter * (pulse_x / ppr)
    dist_y = math.pi * wheel_diameter * (pulse_y / ppr)

    # 速度 [m/s]
    vx = dist_x / dt
    vy = dist_y / dt

    # 位置更新
    x += dist_x
    y += dist_y

    node.get_logger().info(
        f"x={x:.3f} m, y={y:.3f} m | "
        f"vx={vx:.3f} m/s, vy={vy:.3f} m/s"
    )


def main():
    node.create_subscription(Int32MultiArray,"encoder/pulse",cb,10)
    rclpy.spin(node)


if __name__ == "__main__":
    main()