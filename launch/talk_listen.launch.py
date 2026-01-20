# SPDX-FileCopyrightText: 2025 Yasushi Ando　　
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
   
   encoder_talker = launch_ros.actions.Node(
     package='mypkg',      #パッケージの名前を指定
     executable='encoder_talker',  #実行するファイルの指定
     )
   encoder_listener = launch_ros.actions.Node(
     package='mypkg',
     executable='encoder_listener',
     output='screen'        #ログを端末に出すための設定
     )
   
   return launch.LaunchDescription([encoder_talker, encoder_listener])