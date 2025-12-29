from tkinter import *
from tkinter import messagebox
import datetime
import time
import winsound
from threading import *

# --- Global Configuration ---
root = Tk()
root.title("Alarm Clock")
root.geometry("500x400")
root.configure(bg="#1e1e1e") # Dark mode background

# Global flags
alarm_running = False
snooze_active = False

# --- Logic Functions ---

def current_time_loop():
    """Updates the big digital clock at the top"""
    now = datetime.datetime.now().strftime("%H:%M:%S")
    lbl_live_clock.config(text=now)
    lbl_live_clock.after(1000, current_time_loop) # Update every second

def start_alarm_thread():
    """Starts the alarm checking in the background"""
    global alarm_running
    alarm_running = True
    
    # Disable buttons so user can't spam them
    btn_set.config(state=DISABLED, bg="#555555")
    lbl_status.config(text=f"Alarm set for {hour.get()}:{minute.get()}:{second.get()}", fg="#00ff00")
    
    t1 = Thread(target=check_alarm)

    t1.start()

def stop_alarm():
    """Stops the noise and resets the UI"""
    global alarm_running
    alarm_running = False
    lbl_status.config(text="Alarm Stopped", fg="white")
    btn_set.config(state=NORMAL, bg="#00aa00")
    # winsound.PlaySound(None, winsound.SND_PURGE) # Cut audio immediately

def snooze_alarm():
    """Adds 1 minute (for testing) or 5 minutes to current time"""
    global alarm_running
    stop_alarm() # Stop current noise
    
    # Calculate new time
    now = datetime.datetime.now()
    snooze_time = now + datetime.timedelta(minutes=1) # Set to 5 for real use
    
    # Update UI variables
    hour.set(snooze_time.strftime("%H"))
    minute.set(snooze_time.strftime("%M"))
    second.set(snooze_time.strftime("%S"))
    
    lbl_status.config(text=f"Snoozing until {snooze_time.strftime('%H:%M:%S')}", fg="yellow")
    
    # Restart the thread
    start_alarm_thread()

def play_digital_sound():
    """Plays a rhythmic beep pattern instead of a file"""
    # High pitch, short duration
    for _ in range(2): 
        if not alarm_running: break
        winsound.Beep(2000, 100) # 2000Hz, 100ms
        time.sleep(2)

def check_alarm():
    while alarm_running:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        
        curr_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        if curr_time == set_alarm_time:
            lbl_status.config(text="WAKE UP!!!", fg="red")
            
            # --- AUTO STOP LOGIC ---
            # Loop sound for exactly 20 seconds, then stop automatically
            start_ring = time.time()
            duration = 0.1 # seconds
            
            while time.time() - start_ring < duration:
                if not alarm_running: break # Break if user clicked Stop
                play_digital_sound()
            
            # If loop finishes naturally (timeout), reset everything
            if alarm_running:
                stop_alarm()
            break

# --- UI DESIGN ---

# 1. Live Clock Display
Label(root, text="CURRENT TIME", font=("Arial", 10), bg="#1e1e1e", fg="#CCFCBE").pack(pady=(20,0))
lbl_live_clock = Label(root, text="00:00:00", font=("Digital-7", 50, "bold"), bg="#1e1e1e", fg="#00b7ff")
lbl_live_clock.pack()

# 2. Input Frame
frame_input = Frame(root, bg="#1e1e1e")
frame_input.pack(pady=20)

# Helper function for spinboxes
def create_spinbox(parent, val_range):
    vals = [f"{i:02d}" for i in range(val_range)]
    s = Spinbox(parent, values=vals, width=3, font=("Arial", 20), bg="#333333", fg="white", bd=0, justify=CENTER)
    return s

hour = create_spinbox(frame_input, 24)
hour.pack(side=LEFT, padx=5)
Label(frame_input, text=":", font=("Arial", 20), bg="#1e1e1e", fg="white").pack(side=LEFT)

minute = create_spinbox(frame_input, 60)
minute.pack(side=LEFT, padx=5)
Label(frame_input, text=":", font=("Arial", 20), bg="#1e1e1e", fg="white").pack(side=LEFT)

second = create_spinbox(frame_input, 60)
second.pack(side=LEFT, padx=5)

# Set defaults to current time
now = datetime.datetime.now()
hour.delete(0, "end"); hour.insert(0, now.strftime("%H"))
minute.delete(0, "end"); minute.insert(0, now.strftime("%M"))
second.delete(0, "end"); second.insert(0, "00")

# 3. Status Bar
lbl_status = Label(root, text="Alarm Inactive", font=("Arial", 12), bg="#1e1e1e", fg="#777777")
lbl_status.pack(pady=10)

# 4. Buttons Frame
frame_btns = Frame(root, bg="#1e1e1e")
frame_btns.pack(pady=20)

btn_set = Button(frame_btns, text="SET ALARM", font=("Arial", 12, "bold"), bg="#969bf7", fg="white", width=12, command=start_alarm_thread)
btn_set.grid(row=0, column=0, padx=10)

btn_stop = Button(frame_btns, text="STOP", font=("Arial", 12, "bold"), bg="#6a2e2e", fg="white", width=10, command=stop_alarm)
btn_stop.grid(row=0, column=1, padx=10)


# Start the live clock loop
current_time_loop()
root.mainloop()
