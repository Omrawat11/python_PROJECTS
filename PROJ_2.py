import streamlit as st
import random
import time

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Guess The Number",
    page_icon="🎯",
    layout="centered"
)

# ------------------ Sidebar ------------------
st.sidebar.title("⚙️ Game Settings")
level = st.sidebar.selectbox("Choose Difficulty", ["Easy", "Medium", "Hard"])

if level == "Easy":
    max_num = 50
    max_tries = 10
elif level == "Medium":
    max_num = 100
    max_tries = 7
else:
    max_num = 500
    max_tries = 5

st.sidebar.info(
    f"""
    **Rules**
    - Range: 1 – {max_num}
    - Max tries: {max_tries}
    """
)

# ------------------ Session State ------------------
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, max_num)
    st.session_state.tries = 0
    st.session_state.win = False
    st.session_state.game_over = False

# ------------------ Main UI ------------------
st.markdown("<h1 style='text-align: center;'>🎯 Guess The Number</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Car Race Edition 🚗</h4>", unsafe_allow_html=True)
st.divider()

# Attempts progress
attempts_left = max_tries - st.session_state.tries
progress_value = st.session_state.tries / max_tries
st.progress(progress_value)

st.write(f"🔢 Guess a number between **1 and {max_num}**")
st.write(f"❤️ Attempts left: **{attempts_left}**")

guess = st.number_input(
    "Enter your guess 👇",
    min_value=1,
    max_value=max_num,
    step=1
)

# ------------------ Submit Button ------------------
if st.button("🚀 Submit Guess", use_container_width=True) and not st.session_state.game_over:
    st.session_state.tries += 1

    if guess == st.session_state.number:
        st.success(f"🎉 You won in {st.session_state.tries} tries!")
        st.session_state.win = True
        st.session_state.game_over = True

    elif st.session_state.tries == max_tries:
        st.error("😢 Game Over!")
        st.info(f"Correct number was **{st.session_state.number}**")
        st.session_state.game_over = True

    elif guess < st.session_state.number:
        st.warning("⬆️ Go higher")
    else:
        st.warning("⬇️ Go lower")

# ------------------ Car Animation ------------------
if st.session_state.win:
    st.subheader("🏁 Car is racing...")
    road = st.progress(0)

    for i in range(101):
        time.sleep(0.02)
        road.progress(i)

    score = max(0, 100 - st.session_state.tries * 10)
    st.success(f"🚗💨 Finished! Your Score: **{score}**")

# ------------------ Restart ------------------
st.divider()
if st.button("🔄 Restart Game", use_container_width=True):
    st.session_state.clear()
    st.experimental_rerun()

