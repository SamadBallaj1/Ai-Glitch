# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game purpose:** The goal is to guess the secret number within the attempt limit for the selected difficulty.
- [x] **Bugs I found:** Hints were reversed, game state/reset behavior felt inconsistent, and logic in the app file made bugs harder to track.
- [x] **Fixes I applied:** I moved core logic into `logic_utils.py`, fixed high/low hint behavior, cleaned up reset/state flow, and added test coverage.

## 📸 Demo

- [x] I ran the fixed game with Streamlit and confirmed I can win normally.
- [x] I also verified repairs with pytest (`4 passed`).
- [ ] Add my winning-game screenshot here before final submission.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
