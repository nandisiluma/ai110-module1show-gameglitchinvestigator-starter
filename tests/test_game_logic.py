import importlib.util
from pathlib import Path

# Import logic_utils by path to make tests agnostic to pytest import mechanics
_logic_path = Path(__file__).resolve().parent.parent / "logic_utils.py"
spec = importlib.util.spec_from_file_location("logic_utils", _logic_path)
logic_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(logic_utils)
check_guess = logic_utils.check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_attempts_initialization_is_zero():
    """Importing the app should initialize attempts to 0 (no off-by-one)."""
    import importlib
    import sys
    import streamlit as st

    # Ensure a fresh import of the app module so initialization runs
    if "app" in sys.modules:
        del sys.modules["app"]

    # Clear any existing session state to start clean
    st.session_state.clear()

    # Import the app module by file path so pytest can load it reliably
    _app_path = Path(__file__).resolve().parent.parent / "app.py"
    spec = importlib.util.spec_from_file_location("app", _app_path)
    _app = importlib.util.module_from_spec(spec)

    # Ensure project root is on sys.path so app's `from logic_utils import ...` works
    project_root = _app_path.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    spec.loader.exec_module(_app)

    assert "attempts" in st.session_state
    assert st.session_state.attempts == 0
