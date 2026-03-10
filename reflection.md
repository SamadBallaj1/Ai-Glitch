# Reflection: Game Glitch Investigator

## 1. What was broken when you started?

1) Hints were backwards.
Expected: if my guess is high, it should say go lower.
Actual: it told me the opposite direction.

2) Attempts and new game felt buggy.
Expected: new game should reset cleanly with correct attempts.
Actual: attempts and game state did not always match what I expected.

3) Some rounds did not make sense.
Expected: same rules every turn.
Actual: behavior felt inconsistent on different guesses.

---

## 2. How did you use AI as a teammate?

I used Copilot and AI chat while debugging.
I used #file:app.py and #file:logic_utils.py so Copilot had project context.
I mostly used it for answers and to explain confusing parts of the code.
It helped me clean up and move logic out of the main app file.
I asked Copilot about the backwards hints glitch and it explained the guess check logic was flipped.

---

## 3. Debugging and testing your fixes

First I ran the app with Streamlit and played a few rounds.
Then I opened Developer Debug Info, wrote down glitches, and fixed them one by one.
After that I tested high, low, and exact guesses, then ran pytest to confirm.

---

## 4. What did you learn about Streamlit and state?

IT reruns the script on clicks.
If values are not in session state, they reset.
That is why the game felt random before the fixes.

---

## 5. Looking ahead: your developer habits

I want to keep testing small changes right away.
Next time I will ask AI more specific questions with code context.
I still use AI, but now I always verify with tests.
I honestly loved this project because it felt like real debugging, not just coding.
