from tkinter import *
import subprocess
import re

running = False # Infinite loop condition
idle_status = 'To begin, please press "Start"' # Message for Idle Status

# Start, Stop & Scanning functions
def start():
    Status.configure(text='Loading, please wait...')
    global running
    running = True

def stop():
    global running
    running = False
    Status.configure(text=idle_status, background="Grey")
    StatusPing.configure(text="", background="Grey")

def scanning():
    if running:
        output = subprocess.check_output("ping 104.160.131.1", shell = False, universal_newlines=True).splitlines()
        for i in output:
            if "Packets" in i: var1 = int(re.search(r'\d+', str(re.findall(r'Lost =\s\d*',i))).group())
            if "Minimum" in i: var2 = int(re.search(r'\d+', str(re.findall(r'Average =\s\d*',i))).group())
    Status.configure(text="Packet lost: {0}".format(var1))
    StatusPing.configure(text="Average ms: {0}".format(var2))

    # Packet loss label coloring
    if var1 == 0:
        Status.configure(background="Green")
    else:
        Status.configure(background="Red")

    # Ping Status label coloring
    if var2 <= 35:
        StatusPing.configure(background="Green")
    if 35 < var2 < 70:
        StatusPing.configure(background="Yellow")
    if var2 >= 70:
        StatusPing.configure(background="Red")
    root.after(10000, scanning)

# GUI
root = Tk()
root.geometry("200x120")
root.wm_title("Ping Checker")

# Ping Check Label
Status = Label(root, text = idle_status, height="0", width="30", background="Grey")
Status.pack(pady=1) # For visible division between two labels
StatusPing = Label(root, height="0", width="30", background="Grey")
StatusPing.pack()

# Start & Stop Buttons
Start = Button (root, text = "Turn on", command = start).pack()
Stop = Button (root, text = "Turn off", command = stop).pack()

root.after(10000, scanning) # Global Loop
root.mainloop()