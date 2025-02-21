#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def publisher():
    # Inisialisasi node dengan nama 'keyboard_publisher'
    rospy.init_node('publisher', anonymous=True)
    
    # Buat publisher untuk mengirim pesan ke topik '/turtle_commands'
    pub = rospy.Publisher('/turtle_commands', String, queue_size=10)
    
    # Set rate untuk loop (10 Hz)
    rate = rospy.Rate(10)
    
    print("Kontrol Turtle:")
    print("  w: Maju")
    print("  s: Mundur")
    print("  a: Kiri")
    print("  d: Kanan")
    print("  q: Keluar")

    while not rospy.is_shutdown():
        # Baca input dari keyboard
        command = input("Masukkan perintah (w/a/s/d/q): ")
        
        # Jika input adalah 'q', keluar dari loop
        if command == 'q':
            print("Keluar...")
            break
        
        # Kirim perintah ke topik '/turtle_commands'
        if command in ['w', 'a', 's', 'd']:
            pub.publish(command)
            print(f"Perintah dikirim: {command}")
        else:
            print("Perintah tidak valid! Gunakan w/a/s/d/q.")
        
        # Tunggu sesuai rate yang ditentukan
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass