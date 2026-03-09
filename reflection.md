# Reflection: Game Glitch Investigator

## 1. What was broken when you started?

The game is supposed to let me guess a secret number and guide me with hints, but it was broken at first. I expected a high guess to say go lower and a low guess to say go higher, but the hints were reversed. I expected New Game to reset cleanly with the right attempts and state, but it sometimes felt off. I expected the same rules every turn, but some rounds behaved inconsistently.

---

## 2. How did you use AI as a teammate?

I used Copilot and AI chat while debugging. I used #file:app.py and #file:logic_utils.py so it could see the full context. A correct suggestion was to move helper logic out of app.py into logic_utils.py, and that made the code easier to follow. I verified that by running pytest and by playing the game to make sure the app still worked. One misleading suggestion was to focus only on session state at first, but that missed the reversed hint logic, and I verified that by checking the check_guess code and testing guesses in the app.

---

## 3. Debugging and testing your fixes

First I ran the app with Streamlit and used Developer Debug Info to watch what changed after each guess. Then I fixed one issue at a time and re-tested high, low, and exact guesses. I also ran pytest after each major fix, including a new test that checks a too-high guess tells the player to go lower. That combo of manual testing plus pytest is how I confirmed the repairs.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script on clicks.
If values are not in session state, they reset.
That is why the game felt random before the fixes.

---

## 5. Looking ahead: your developer habits

I want to keep testing small changes right away.
Next time I will ask AI more specific questions with code context.
I still use AI, but now I always verify with tests.
I honestly loved this project because it felt like real debugging, not just coding.
