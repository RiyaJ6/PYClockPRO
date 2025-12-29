<img width="878" height="571" alt="image" src="https://github.com/user-attachments/assets/12524fd1-a8e8-4742-b351-a51e44a6c021" />

<div align="center">
  
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Alarm%20Clock.png" width="80" />

  # ⏰ PY-CLOCK: PRO EDITION
  
  **A high-precision desktop alarm clock with a clean, responsive interface.**

  <p>
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" />
    <img src="https://img.shields.io/badge/UI-Tkinter-orange?style=for-the-badge" />
    <img src="https://img.shields.io/badge/Logic-Threading-red?style=for-the-badge" />
    <img src="https://img.shields.io/badge/Maintained%3F-yes-green?style=for-the-badge" />
  </p>

  <h4>
    <a href="#-features">Features</a>
    <span> · </span>
    <a href="#-how-it-works">How It Works</a>
    <span> · </span>
    <a href="#-installation">Installation</a>
  </h4>
</div>

---

## 📖 Description
**Py-Clock Pro** is a lightweight, multithreaded desktop application built with Python. It provides a seamless user experience by separating the clock logic from the graphical interface, ensuring the app remains responsive even while the alarm is active.



## ✨ Features
* **⌚ Live Digital Display:** A real-time, second-accurate clock synchronized with your system time.
* **🧵 Multithreaded Execution:** Uses the `threading` library to prevent the window from freezing while waiting for the alarm.
* **🛡️ Input Validation:** Built-in safeguards to prevent invalid time settings.
* **🌙 Professional UI:** A dark-themed, minimalist design built entirely with Tkinter.
* **🔔 Native Alerts:** Uses system-level notification logic for immediate awareness.

## 🧠 How It Works
The application operates on a **dual-thread system**:
1. **Main Thread:** Handles the Window, buttons, and time selection menus.
2. **Background Thread:** Runs a continuous `while` loop that compares the current time to the user's set time every 1000ms.
<img width="991" height="837" alt="Screenshot 2025-12-29 132742" src="https://github.com/user-attachments/assets/8877fa5d-f193-4c1d-bc42-d751cc242f41" />


## 🛠️ Installation

```bash
# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/PY-Clock-PRO.git](https://github.com/YOUR_USERNAME/PY-Clock-Pro.git)

# 2. Enter the project folder
cd PY-Clock-PRO

# 3. Run the application
python main.py
```


## 🤝 Contributing

We ❤️ contributions! Whether you're fixing a bug or suggesting a new feature, feel free to dive in.

1. **Find an Issue:** Or open a new one to discuss your ideas.
2. **Style Guide:** Please keep the code clean .
3. **Be Kind:** We follow a basic code of conduct - be helpful and respectful!

   
<div align="center"> <sub>Built for productivity and precision.</sub> </div>
