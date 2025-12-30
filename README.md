# mypkg
[![test](https://github.com/yasushigit/mypkg/actions/workflows/test.yml/badge.svg)]
### ロボットシステム学
このリポジトリは、ROS 2 における publish / subscribe 通信を学ぶためのパッケージである。
talker ノードが一定周期で整数値をトピック「date」にパブリッシュし、
listener ノードがその値を受信して現在の日付に加算し、計算後の日付と曜日を表示する。

## talker.py
0.5秒ごとに16ビット符号つき整数をカウントしてトピック"date"を通じてパブリッシュ

## listener.py
トピック"date"からのデータをサブスクライブしメッセージが含む数値(d)を日数として現在の日時に加算

その後，計算したd日後の日時と曜日をログとして表示

## talk_listen.launch.py
talker.pyとlistener.pyの両方を実行

## トピック
### date
 "talker.py" ノードが生成した16ビット符号つきの整数情報を "listener.py" ノードが受け取り，計算結果をログに表示するための通信経路

## 実行例
実行例の日にちは 2025/12/31 を想定
### 例1 (端末2つ使用 , talker.pyを実行)

### 入力
#### 端末1

```
$ ros2 run mypkg talker
```

#### 端末2

```
$ ros2 topic echo /date
```

### 出力

```
data: 25
---
data: 26
---
data: 27
---
data: 28
---
data: 29
---
data: 30
・・・
```

### 例2　(端末2つ使用 , talker.py & listener.pyを実行)

### 入力
#### 端末1

```
$ ros2 run mypkg talker
```

#### 端末2

```
$ ros2 run mypkg listener
```

### 出力

```
[INFO] [1767128581.142613371] [listener]: Listen: 2026/01/25 (Sun)
[INFO] [1767128581.250973124] [listener]: Listen: 2026/01/26 (Mon)
[INFO] [1767128581.750760767] [listener]: Listen: 2026/01/27 (Tue)
[INFO] [1767128582.251229222] [listener]: Listen: 2026/01/28 (Wed)
[INFO] [1767128582.751005887] [listener]: Listen: 2026/01/29 (Thu)
[INFO] [1767128583.249274237] [listener]: Listen: 2026/01/30 (Fri)
[INFO] [1767128583.748939215] [listener]: Listen: 2026/01/31 (Sat)
・・・
```

### 例3　(端末1つ使用 , talker.py & listener.pyを実行)

### 入力

```
$ ros2 launch mypkg talk_listen.launch.py
```

### 出力

```
[INFO] [launch]: All log files can be found below /home/ando/.ros/log/2025-12-31-06-04-01-899921-Aibou-108411
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [108420]
[INFO] [listener-2]: process started with pid [108421]
[listener-2] [INFO] [1767128642.728476489] [listener]: Listen: 2025/12/31 (Wed)
[listener-2] [INFO] [1767128644.081730058] [listener]: Listen: 2026/01/01 (Thu)
[listener-2] [INFO] [1767128644.218563814] [listener]: Listen: 2026/01/02 (Fri)
[listener-2] [INFO] [1767128644.718457101] [listener]: Listen: 2026/01/03 (Sat)
[listener-2] [INFO] [1767128645.218427975] [listener]: Listen: 2026/01/04 (Sun)
[listener-2] [INFO] [1767128645.718785431] [listener]: Listen: 2026/01/05 (Mon)
[listener-2] [INFO] [1767128646.217349262] [listener]: Listen: 2026/01/06 (Tue)
[listener-2] [INFO] [1767128646.719279472] [listener]: Listen: 2026/01/07 (Wed)
[listener-2] [INFO] [1767128647.217952197] [listener]: Listen: 2026/01/08 (Thu)
[listener-2] [INFO] [1767128647.718189986] [listener]: Listen: 2026/01/09 (Fri)
[listener-2] [INFO] [1767128648.219108621] [listener]: Listen: 2026/01/10 (Sat)
[listener-2] [INFO] [1767128648.718777581] [listener]: Listen: 2026/01/11 (Sun)
```


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
* [ryuichiueda/my_slides robosys_2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
* © 2025 Yasushi Ando