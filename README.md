#  Computer Vision - Hand Gesture AI Game

An interactive **Rock–Paper–Scissors** game built using **Computer Vision** and **Hand Gesture Recognition**. The player's move is detected in real time through a webcam, while an AI opponent competes against the player.

This project leverages **OpenCV**, **MediaPipe**, and **CVZone** to deliver a responsive and engaging gaming experience.

---

##  Features

*  Real-time hand gesture detection
*  AI opponent with random move selection
*  Countdown-based round system
*  Live score tracking (Player vs AI)
*  Clean and intuitive UI using OpenCV overlays
*  Easy replay and restart functionality
*  Webcam-based gameplay

---

##  Hand Gesture Mapping

| Gesture                  | Move     |
| ------------------------ | -------- |
| ✊ Fist                   | Rock     |
| ✋ Open Palm              | Paper    |
| ✌️ Index + Middle Finger | Scissors |

---

##  Tech Stack

* Python 3.10
* OpenCV
* MediaPipe
* CVZone
* NumPy

---

##  Project Structure

```text
Computer-Vision-RPS/
│
├── data/
│   ├── bg.png          # Background UI
│   ├── rock.png        # AI Rock image
│   ├── paper.png       # AI Paper image
│   └── scissor.png     # AI Scissors image
│
├── main.py             # Main game logic
├── requirements.txt    # Project dependencies
├── .gitignore
└── README.md
```

---

##  Installation & Setup

> **Note:** For best compatibility with MediaPipe, use **Python 3.10.x**.

```bash
git clone https://github.com/Mohataseem89/Computer-Vision-RPS.git
cd Computer-Vision-RPS

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python main.py
```

---

##  Acknowledgements

This project was inspired by the educational content of **Murtaza Hassan** and the Computer Vision community.

GitHub: https://github.com/murtazahassan

---

##  Author

**Mohataseem Khan**

* LinkedIn: https://www.linkedin.com/in/mohataseem-khan/
* GitHub: https://github.com/Mohataseem89
