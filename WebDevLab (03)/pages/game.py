import streamlit as st

st.title("Which Jedi Master Are You?")
st.write("Simply answer a couple of questions and see if you truly are one with the Force.")

# --- Add at least 3 images to satisfy the spec (you can swap with URLs) ---
st.image(["images/temple.jpg", "images/lightsabers.jpg", "images/starfield.jpg"],
         caption=["Jedi Temple", "Lightsabers", "A galaxy far, far away..."])  # NEW

# -------------------------
# QUESTIONS (5+ and 3+ types)
# -------------------------
combat = st.radio(  # NEW
    "Choose your lightsaber form",
    [
        "Soresu (defense & patience)",
        "Ataru (agile & bold)",
        "Vaapad (channel intensity)",
        "Niman (balanced & adaptable)",
    ],
)

role = st.selectbox(  # NEW
    "Which role suits you best?",
    ["Teacher", "Diplomat/Mediator", "Guardian/Warrior", "Independent Pathfinder"],
)

values = st.multiselect(  # NEW
    "What do you hold most dear to you?",
    ["Compassion", "Discipline", "Curiosity", "Tradition",
     "Independence", "Non-attachment", "Courage", "Humility"],
)

patience = st.slider("Your patience level", 0, 10, 5)  # NEW
meditate = st.number_input("Hours you meditate per week", min_value=0, max_value=40, value=2)  # NEW
rules = st.radio("When the Council sets a rule, you usually…",
                 ["Follow it", "Bend it when needed", "Break it to follow the Living Force"])

# -------------------------
# SCORING
# -------------------------
scores = {
    "Yoda": 0,
    "Obi-Wan Kenobi": 0,
    "Mace Windu": 0,
    "Qui-Gon Jinn": 0,
    "Anakin Skywalker 😈": 0,
}

# combat
if combat.startswith("Soresu"):
    scores["Obi-Wan Kenobi"] += 2; scores["Yoda"] += 1
elif combat.startswith("Ataru"):
    scores["Yoda"] += 2; scores["Anakin Skywalker 😈"] += 2
elif combat.startswith("Vaapad"):
    scores["Mace Windu"] += 3
elif combat.startswith("Niman"):
    scores["Qui-Gon Jinn"] += 2; scores["Anakin Skywalker 😈"] += 1

# patience
scores["Obi-Wan Kenobi"] += patience // 3
scores["Yoda"] += patience // 2
scores["Anakin Skywalker 😈"] += max(0, 3 - patience // 3)

# role
if role == "Teacher":
    scores["Yoda"] += 1; scores["Obi-Wan Kenobi"] += 2
elif role == "Diplomat/Mediator":
    scores["Qui-Gon Jinn"] += 2; scores["Yoda"] += 1
elif role == "Guardian/Warrior":
    scores["Mace Windu"] += 2
elif role == "Independent Pathfinder":
    scores["Anakin Skywalker 😈"] += 2; scores["Qui-Gon Jinn"] += 1

# values
for v in values:
    if v == "Compassion": scores["Yoda"] += 1; scores["Obi-Wan Kenobi"] += 1
    if v == "Discipline": scores["Obi-Wan Kenobi"] += 2
    if v == "Curiosity": scores["Qui-Gon Jinn"] += 2
    if v == "Tradition": scores["Yoda"] += 1; scores["Mace Windu"] += 1
    if v == "Independence": scores["Anakin Skywalker 😈"] += 2
    if v == "Non-attachment": scores["Qui-Gon Jinn"] += 1; scores["Yoda"] += 1
    if v == "Courage": scores["Mace Windu"] += 2; scores["Anakin Skywalker 😈"] += 1
    if v == "Humility": scores["Yoda"] += 2

# meditate
if meditate >= 10:
    scores["Yoda"] += 2; scores["Obi-Wan Kenobi"] += 1
elif meditate >= 4:
    scores["Obi-Wan Kenobi"] += 1; scores["Qui-Gon Jinn"] += 1
else:
    scores["Anakin Skywalker 😈"] += 1

# rules
if rules == "Follow it":
    scores["Obi-Wan Kenobi"] += 2; scores["Mace Windu"] += 1
elif rules == "Bend it when needed":
    scores["Qui-Gon Jinn"] += 2
elif rules == "Break it to follow the Living Force":
    scores["Anakin Skywalker 😈"] += 2; scores["Qui-Gon Jinn"] += 1


if st.button("Reveal my Jedi Master ✨"):  # NEW
    prog = st.progress(0)  # NEW
    for i in range(0, 101, 10):
        prog.progress(i)

    best = max(scores, key=scores.get)
    top_score = scores[best]
    ties = [k for k, v in scores.items() if v == top_score]

    st.metric("Midichlorian Alignment Score", int(top_score))  # NEW

    result_images = {
        "Yoda": "images/yoda.jpg",
        "Obi-Wan Kenobi": "images/obiwan.jpg",
        "Mace Windu": "images/mace.jpg",
        "Qui-Gon Jinn": "images/qui-gon.jpg",
        "Anakin Skywalker 😈": "images/anakin.jpg",
        "Sith Lord": "images/sith.jpg",
    }

    # Sith fallback (too many ties or too low a score)
    if len(ties) > 2 or top_score < 3:
        st.subheader("🌑 You have strayed too far… You are a **Sith Lord!** ⚡")
        st.image(result_images["Sith Lord"])
    elif len(ties) > 1:
        st.subheader("You embody multiple masters:")
        st.write(", ".join(ties))
        st.image([result_images[t] for t in ties if t in result_images])
    else:
        st.subheader(f"🌟 You are most like **{best}**!")
        blurbs = {
            "Yoda": "Ancient wisdom, deep patience, and a knack for teaching. Size matters not.",
            "Obi-Wan Kenobi": "Calm, disciplined, and loyal. You are the very model of Jedi serenity.",
            "Mace Windu": "Unflinching courage and principled strength. You face darkness without fear.",
            "Qui-Gon Jinn": "You follow the Living Force and your conscience—even when it breaks with tradition.",
            "Anakin Skywalker 😈": "Passionate, powerful, and fearless… but beware: your fire can burn too hot.",
            "Sith Lord": "The Dark Side has consumed you. Power, anger, and ambition fuel your path.",
        }
        st.write(blurbs.get(best, "The Force moves in mysterious ways."))
        st.image(result_images.get(best, "images/jedi.jpg"))

    st.balloons()  # NEW

