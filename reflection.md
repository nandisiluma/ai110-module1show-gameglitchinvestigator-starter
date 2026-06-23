# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  1. The hints were backwards, kept returning "Go lower" when my guess was actually greater than the secret value
  2. The game ended with one attempt left
  3. Clicking on the New Game after winning does not start a new game, it returns a message "You already won. Start a new game to play again."

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |

| secret: 45, guess: 50| "Go LOWER" | "Go HIGHER"| NONE |
| additional guess, two attempts left | one more change to guess | game ends, lose the game | |
| click New Game after winning | Start a new game | "You already won. Start a new game to play again." | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  For the second bug where the game ended with one attempt left, the AI pointed out that session states variable was initialized to 1 instead of 0, hence the game ended before g=reaching 0 attempts.

After implmenting the fix, I asked the AI coding assistant to create tests for this bug, and ran the tests to validate the results.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I ran the tests, and also tested the game on streamlit

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I manually tested the game after fixing the guessing logic. The hints were previously misleading, always defaulted to "go lower". However, after updating the code, the hints were accurate.

- Did AI help you design or understand any tests? How?
  I used agent mode to create the test_game_logic, and it fully created the entire file with the test logic. I reviewed the file to validate it was covering the expected test scenarios.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns your whole script from top to bottom every time you interact with a widget or click a button.
That means normal variables get reset on each interaction.
st.session_state is a built-in place to store values that persist across those reruns (like score, attempts, or a secret number).

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  Reflecting on how I am interacting with the AI coding assistant, and validating the responses it gives me

- What is one thing you would do differently next time you work with AI on a coding task?

Think through the entire end-to-end functionality before touching any code.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  It's not perfect, but it's a good starting point. Definitely saves a lot of time.
