def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return outcome string.

    Returns one of: "Win", "Too High", "Too Low".
    """
    # Ensure we compare numerically when possible to avoid string
    # lexicographic comparisons (the original app sometimes stored
    # the secret as a string which caused incorrect high/low hints).
    try:
        g = int(guess)
    except Exception:
        # non-numeric guesses can't be compared numerically; coerce to str
        g = guess

    try:
        s = int(secret)
    except Exception:
        s = secret

    # Exact match
    if g == s:
        return "Win"

    # If both are ints, do numeric comparison
    if isinstance(g, int) and isinstance(s, int):
        return "Too High" if g > s else "Too Low"

    # Fallback: compare as strings for ordering
    try:
        return "Too High" if str(g) > str(s) else "Too Low"
    except Exception:
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
