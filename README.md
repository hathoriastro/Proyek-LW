# ROS Noetic Turtle Control

## **1. Clone Repository**
Clone repository ini ke dalam workspace ROS Anda:
```bash
cd ~/catkin_ws/src
git clone <repository-url> turtle_control
```

## **2. Build Repo**
```bash
cd ~/catkin_ws
catkin_make
```

## **3. Buat Branch Baru**
Setelah cloning, buat branch baru untuk pengembangan:
```bash
cd turtle_control
git checkout -b nama_kalian
```

## **4. Lengkapi Subscriber turtle_controller.py**
Subscriber menerima perintah dari topic `turtle_commands` dan menggerakkan TurtleSim berdasarkan input

## **5. Buat Publisher untuk Input Keyboard**
Kode berikut memungkinkan pengguna memasukkan perintah melalui keyboard dan mengirimnya ke topic `turtle_commands`:

## **6. Buat Launch File**
Untuk menjalankan semuanya dengan satu perintah, buat file launch:
```bash
roscd turtle_control
touch launch_turtle.launch
```
Isikan Scrip di bawah
```xml
<launch>
    <node pkg="turtlesim" type="turtlesim_node" name="turtlesim" output="screen"/>
    <node pkg="turtle_control" type="turtle_controller.py" name="listener_node" output="screen"/>
</launch>
```

## **7. Build dan Jalankan**
Setelah menambahkan kode, lakukan build:
```bash
cd ~/catkin_ws
catkin_make
```

Jalankan proyek dengan:
```bash
roslaunch turtle_control turtle_control.launch
roslaunch turtle_control <inputer keyboard>
```

Sekarang TurtleSim bisa dikontrol melalui input keyboard! 🚀
Jangan Lupa Untuk Push Ke dalam Branch kalian

