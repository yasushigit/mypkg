# SPDX-FileCopyrightText: 2025 Yasushi Ando
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
from datetime import datetime, timedelta

def cb(msg):
    global node

    t = datetime.today() + timedelta(days=msg.data)
    date_str = t.strftime("%Y/%m/%d")

    dow = t.isoweekday()

    dow_str = ""
    if dow == 1:
        dow_str = "(Mon)"
    elif dow == 2:
        dow_str = "(Tue)"
    elif dow == 3:
        dow_str = "(Wed)"
    elif dow == 4:
        dow_str = "(Thu)"
    elif dow == 5:
        dow_str = "(Fri)"
    elif dow == 6:
        dow_str = "(Sat)"
    elif dow == 7:
        dow_str = "(Sun)"

    time_str = f"{date_str} {dow_str}"
    node.get_logger().info(f"Listen: {time_str}")


rclpy.init()
node = Node("listener")


def main():
    node.create_subscription(Int16, "date", cb, 10)
    rclpy.spin(node)


if __name__ == "__main__":
    main()