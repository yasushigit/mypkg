# mypkg
![test](https://github.com/yasushigit/mypkg/actions/workflows/test.yml/badge.svg)
## ロボットシステム学
このリポジトリは、ROS2における publish / subscribe 通信を用いて、  
エンコーダのパルス情報を送信する talker ノードと、  
それを受信して速度および自己位置（X, Y）を推定する listener ノードからなる  
ROS2パッケージである。

2つの直交するエンコーダ（X 方向・Y 方向）を想定し、  
エンコーダのパルス数をトピックとして受信し、平面上の自己位置を計算する。

本パッケージは、  
- エンコーダ処理
- 基本的なロボットの位置計測
- ROS2ノード間通信の理解

を目的として作成した。

## encoder_talker.py
encoder_talker ノードは、
2つの直交するエンコーダ（X方向・Y方向）から得られるパルス数を模擬的に生成し、
ROS2のトピックとしてパブリッシュするノードです。

本ノードは実機エンコーダの代わりに、
一定周期で規則的に増減する分かりやすい値を出力することで、
デバッグや学習用途、自己位置推定ノードの動作確認を目的としています。

### 機能
- X 方向・Y 方向の直行する 2 つのエンコーダを想定
- 一定周期でエンコーダのパルス増分を生成
- 規則的に -10~10 の間を0.5秒間隔で増減する値を出力

実機エンコーダの代替として使用でき、  
自己位置推定ノードのデバッグや検証に利用できるノードとなっている。

### Publish トピック
/encoder/pulse

### メッセージ型
std_msgs/msg/Int32MultiArray

### データ内容
data[0] : X 方向エンコーダのパルス増分
data[1] : Y 方向エンコーダのパルス増分


## encoder_listener.py
encoder_listener ノードは、
encoder_talker ノードなどから送信される
2つの直交するエンコーダ（X方向・Y方向）のパルス数を受信し、
速度および自己位置（XY座標）を推定するノードです。

本ノードでは車体の回転はしないものとし、
XY平面上のみを扱う簡易的な自己位置推定を行います。

本ノードは、
エンコーダのパルス数から移動量・速度・位置を計算する処理を学ぶこと、
および自己位置推定ノードの動作確認を目的としています。

上のencoder_talkerとトピックなどの形式は同様であるが一応記載する。

### 機能
X 方向・Y 方向の直交する 2 つのエンコーダを想定している

- /encoder/pulse トピックを subscribe
- パルス数から移動距離を計算
- 自己位置（x, y）および速度（vx, vy）を算出
- 計算結果をログとして出力

### Subscribe トピック
/encoder/pulse

### メッセージ型
std_msgs/msg/Int32MultiArray

### データ内容
data[0] : X 方向エンコーダのパルス増分
data[1] : Y 方向エンコーダのパルス増分

### 計算内容
'''
wheel_diameter = 0.06        # エンコーダに接続されたタイヤの直径[m]
ppr = 100                   # 1回転あたりのパルス数
dt = 0.5                    # エンコーダ値が送られてくる周期[s]
'''
をパラメータとして用い、
以下の式により移動距離を計算します。

移動距離：
distance = π × wheel_diameter × (pulse / ppr)

計算された距離を積算することで、
現在の自己位置 (x, y) を更新します。


## 実行例
### encoder_talker実行端末
$~/ros2_ws$ ros2 run mypkg encoder_talker
[INFO] [1768885357.995644578] [encoder_talker]: Publish encoder pulse: X=1, Y=-1
[INFO] [1768885358.496925270] [encoder_talker]: Publish encoder pulse: X=2, Y=-2
[INFO] [1768885358.981402227] [encoder_talker]: Publish encoder pulse: X=3, Y=-3
[INFO] [1768885359.499791550] [encoder_talker]: Publish encoder pulse: X=4, Y=-4
[INFO] [1768885359.997803704] [encoder_talker]: Publish encoder pulse: X=5, Y=-5
[INFO] [1768885360.497660511] [encoder_talker]: Publish encoder pulse: X=6, Y=-6
[INFO] [1768885360.997736651] [encoder_talker]: Publish encoder pulse: X=7, Y=-7
[INFO] [1768885361.497332226] [encoder_talker]: Publish encoder pulse: X=8, Y=-8
[INFO] [1768885361.997202227] [encoder_talker]: Publish encoder pulse: X=9, Y=-9
[INFO] [1768885362.497656047] [encoder_talker]: Publish encoder pulse: X=10, Y=-10

### encoder_listener実行端末
'''
$~/ros2_ws$ ros2 run mypkg encoder_listener
[INFO] [1768885357.995986124] [encoder_listener]: x=0.002 m, y=-0.002 m | vx=0.004 m/s, vy=-0.004 m/s
[INFO] [1768885358.497501198] [encoder_listener]: x=0.006 m, y=-0.006 m | vx=0.008 m/s, vy=-0.008 m/s
[INFO] [1768885358.982017924] [encoder_listener]: x=0.011 m, y=-0.011 m | vx=0.011 m/s, vy=-0.011 m/s
[INFO] [1768885359.500602895] [encoder_listener]: x=0.019 m, y=-0.019 m | vx=0.015 m/s, vy=-0.015 m/s
[INFO] [1768885359.998784580] [encoder_listener]: x=0.028 m, y=-0.028 m | vx=0.019 m/s, vy=-0.019 m/s
[INFO] [1768885360.498874051] [encoder_listener]: x=0.040 m, y=-0.040 m | vx=0.023 m/s, vy=-0.023 m/s
[INFO] [1768885360.998739622] [encoder_listener]: x=0.053 m, y=-0.053 m | vx=0.026 m/s, vy=-0.026 m/s
[INFO] [1768885361.497633837] [encoder_listener]: x=0.068 m, y=-0.068 m | vx=0.030 m/s, vy=-0.030 m/s
[INFO] [1768885361.997441269] [encoder_listener]: x=0.085 m, y=-0.085 m | vx=0.034 m/s, vy=-0.034 m/s
[INFO] [1768885362.498254282] [encoder_listener]: x=0.104 m, y=-0.104 m | vx=0.038 m/s, vy=-0.038 m/s
[INFO] [1768885362.982014151] [encoder_listener]: x=0.121 m, y=-0.121 m | vx=0.034 m/s, vy=-0.034 m/s
[INFO] [1768885363.499547796] [encoder_listener]: x=0.136 m, y=-0.136 m | vx=0.030 m/s, vy=-0.030 m/s
[INFO] [1768885363.998186663] [encoder_listener]: x=0.149 m, y=-0.149 m | vx=0.026 m/s, vy=-0.026 m/s
[INFO] [1768885364.487707779] [encoder_listener]: x=0.160 m, y=-0.160 m | vx=0.023 m/s, vy=-0.023 m/s
[INFO] [1768885364.999831726] [encoder_listener]: x=0.170 m, y=-0.170 m | vx=0.019 m/s, vy=-0.019 m/s
[INFO] [1768885365.500031085] [encoder_listener]: x=0.177 m, y=-0.177 m | vx=0.015 m/s, vy=-0.015 m/s
[INFO] [1768885365.997699645] [encoder_listener]: x=0.183 m, y=-0.183 m | vx=0.011 m/s, vy=-0.011 m/s
[INFO] [1768885366.500137271] [encoder_listener]: x=0.187 m, y=-0.187 m | vx=0.008 m/s, vy=-0.008 m/s
[INFO] [1768885366.982358919] [encoder_listener]: x=0.188 m, y=-0.188 m | vx=0.004 m/s, vy=-0.004 m/s
'''

## 動作確認済み環境
* Python 3.8.10
* Ubuntu 22.04.5 LTS
* ROS 2 jazzy
### GitHub Actions
* Ubuntu 22.04


## テスト環境
テストには以下のコンテナを使用しています.
* [ryuichiueda/ubuntu22.04-ros2](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2)


## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
* [ryuichiueda/my_slides/robosys_2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
* © 2025 Yasushi Ando