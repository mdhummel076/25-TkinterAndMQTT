"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Matt Hummel.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time


def main():
    """ Constructs a GUI that will be used MUCH later to control EV3. """
    # -------------------------------------------------------------------------
    # DONE: 2. Follow along with the video to make a remote control GUI
    # For every grid() method call you will add a row and a column argument
    # -------------------------------------------------------------------------

    client = com.MqttClient()
    client.connect('James','Matt')

    time.sleep(1)

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0,column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1,column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0,column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1,column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2,column=1)
    forward_button['command'] = lambda: driveIt(client,100,100)
    root.bind('<Up>', lambda event: sendThis("Forward key",client))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3,column=0)
    left_button['command'] = lambda: sendThis("Left button",client)
    root.bind('<Left>', lambda event: sendThis("Left key",client))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3,column=1)
    stop_button['command'] = lambda: driveIt(client,0,0)
    root.bind('<space>', lambda event: sendThis("Stop key",client))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3,column=2)
    right_button['command'] = lambda: sendThis("Right button",client)
    root.bind('<Right>', lambda event: sendThis("Right key",client))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4,column=1)
    back_button['command'] = lambda: sing(client,444)
    root.bind('<Down>', lambda event: sendThis("Back key",client))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5,column=0)
    up_button['command'] = lambda: sendThis("Up button",client)
    root.bind('<u>', lambda event: sendThis("Up key",client))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6,column=0)
    down_button['command'] = lambda: sendThis("Down button",client)
    root.bind('<j>', lambda event: sendThis("Down key",client))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5,column=2)
    q_button['command'] = lambda: sendThis("Quit button",client)

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6,column=2)
    e_button['command'] = lambda: exit()

    root.mainloop()

def sendThis(text,client):

    client.send_message('say_it',[text])

def driveIt(client,lval,rval):

    client.send_message('drive',[lval,rval])

def sing(client,tone):

    client.send_message('sing',[tone])


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------


main()
