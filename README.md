--
```markdown
# 🎮 Tic-Tac-Toe Game

Welcome to the **Tic-Tac-Toe** game built with Python! This game supports:

- 👥 **Human vs Human**
- 🤖 **Human vs Computer (AI with random moves and strategy)**

The game follows all the standard rules and provides a clean, easy-to-understand interface for players.

---

## 📚 Features

* Human vs Human or Human vs Computer  
* Valid Move Detection with Error Handling  
* Computer AI with Random and Smart Moves  
* Automatic Detection of Win, Draw, or Loss  
* Clean Board Display for Better Understanding  

---

## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.x** installed. Run the following command to check:
```bash
python3 --version
```
If Python is not installed, install it using:
```bash
sudo apt update
sudo apt install python3
```

---

### 📥 Cloning the Repository

```bash
git clone https://github.com/rajatsainisim/tic_tac_toe.git
cd tic_tac_toe
```

---

### ▶️ Running the Game

To start the game, run:
```bash
python3 tic_tac_toe.py
```

---

## 🎯 How to Play

### 1. **Player 1 Setup**
- Enter your name.
- Choose your symbol (`O` or `X`). Default is `O`.

### 2. **Player 2 Setup**
- Choose if the opponent is a **Human (`H`)** or **Computer (`C`)**.

### 3. **Game Interface**
The positions on the board are numbered as follows:
```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```
To place your symbol, enter the corresponding number.

---

## 🎉 Winning Conditions

A player wins by aligning three symbols:
- Horizontally
- Vertically
- Diagonally

If the board is full and no one wins, the game ends in a **draw**.

---

## 📝 Example Gameplay

```
Enter Player 1's name: Rajat
Rajat, choose your symbol (O or X, default is O): X
Will Player 2 be (H)uman or (C)omputer? C

   |   |  
-----------
   |   |  
-----------
   |   |  
Rajat, enter your move (1-9): 2

   | X |  
-----------
   |   |  
-----------
   |   |  
Computer plays at position 9

   | X |  
-----------
   |   |  
-----------
   |   | O
```

---

## 🧠 Game Logic Overview

### 📌 **Display the Board**
- Shows the current state of the board after each move.
### 📌 **Valid Move Check**
- Ensures that players can only choose valid and unoccupied positions.
### 📌 **Check for Win/Draw**
- Automatically detects winning conditions or draw scenarios.
### 📌 **Computer Move**
- AI makes a random valid move to simulate a real opponent.

---

## 🛠️ Code Structure

```
tic_tac_toe/
├── tic_tac_toe.py    # Main game logic
└── README.md         # Documentation
```

---
--

## 📝 License

This project is available for learning and educational purposes.  
Feel free to contribute and enhance the project!

---

## 📞 Contact

If you have any questions or suggestions, feel free to reach out via [GitHub](https://github.com/rahatsainisim).

---

🚀 **Ready to Play?** Fire up the game and challenge yourself! 🎮
```
--