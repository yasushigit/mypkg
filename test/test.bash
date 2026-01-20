#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yasushi Ando　　　
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

#テスト
timeout 3 ros2 run mypkg encoder_talker > /tmp/mypkg_single.log &
sleep 1
ros2 topic list | grep -q "/encoder/pulse"
pkill -f encoder_talker

ros2 topic info /encoder/pulse | grep -q "std_msgs/msg/Int32MultiArray"

cat /tmp/mypkg.log | grep -q "encoder_listener"

#内容チェック
judge=true

for key in "x=" "y=" "vx=" "vy="; do
    if ! cat /tmp/mypkg.log | grep -q "$key"; then
        judge=false
        break
    fi
done

if $judge; then
    exit 0
else
    exit 1
fi