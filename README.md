# Computer Vision - Hand Gesture AI Game

An interactive **Rock–Paper–Scissors game** built using **Computer Vision** and **Hand Gesture Recognition**.  
The player’s move is detected in real time using a webcam, while an AI opponent plays against you.

This project uses **OpenCV**, **MediaPipe**, and **CVZone** to create a fun, responsive, and visually clean gaming experience.

---

## Features

-  Real-time **hand gesture detection**
-  AI opponent with random move selection
-  Countdown-based round system
-  Live score tracking (Player vs AI)
-  Clean & modern UI using OpenCV overlays
-  Restart and replay rounds easily
-  Works directly with your webcam

---

## Hand Gesture Mapping

| Gesture | Move |
|------|------|
| ✊ Fist | Rock |
| ✋ Open Palm | Paper |
| ✌️ Index + Middle Finger | Scissors |

---

## 🛠️ Tech Stack

- **Python 3.10**
- **OpenCV**
- **MediaPipe**
- **CVZone**
- **NumPy**

---

## Project Structure
Rock_Paper_Scissor/
│
├── data/
│ ├── bg.png # Background UI
│ ├── rock.png # AI rock image
│ ├── paper.png # AI paper image
│ └── scissor.png # AI scissor image
│
├── main.py # Game logic
├── requirements.txt # Dependencies
├── .gitignore
└── README.md



---

## Installation & Setup
## Note:
Please use Python 3.10.x for best compatibility with MediaPipe.
```bash
git clone https://github.com/Mohataseem89/Computer-Vision-RPS.git
cd Computer-Vision-RPS
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```


## Courtesy
Project inspired by learning from Murtaza Hassan: [Github](https://github.com/murtazahassan)




## 🧑‍💻 Author

**Mohataseem Khan**
📧 Connect with me: [LinkedIn](https://www.linkedin.com/in/mohataseem-khan/) • [GitHub](https://github.com/Mohataseem89)




