import streamlit as st

st.title("Which Jedi Master Are You?")
st.write("Simply answer a couple of questions and see if you truly are one with the Force.")

st.image(["images/JediTemple-Deceived.webp", "images/Many_Lightsabers.jpg", "images/MainGalaxy.webp"],
         caption=["Jedi Temple", "Lightsabers", "Galaxy"]) 


form = st.radio(  # NEW
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

values = st.multiselect(  
    "What do you hold most dear to you?",
    ["Compassion", "Discipline", "Curiosity", "Tradition",
     "Independence", "Non-attachment", "Courage", "Humility"],
)

patience = st.slider("Your patience level", 0, 10, 5)  
meditate = st.number_input("Hours you meditate per week", min_value=0, max_value=40, value=2) 
rules = st.radio("When the Council sets a rule, you usually…",
                 ["Follow it", "Bend it when needed", "Break it to follow the Living Force"])


scores = {
    "Yoda": 0,
    "Obi-Wan Kenobi": 0,
    "Mace Windu": 0,
    "Qui-Gon Jinn": 0,
    "Anakin Skywalker 😈": 0,
}


if form.startswith("Soresu"):
    scores["Obi-Wan Kenobi"] += 2; scores["Yoda"] += 1
elif form.startswith("Ataru"):
    scores["Yoda"] += 2; scores["Anakin Skywalker 😈"] += 2
elif form.startswith("Vaapad"):
    scores["Mace Windu"] += 3
elif form.startswith("Niman"):
    scores["Qui-Gon Jinn"] += 2; scores["Anakin Skywalker 😈"] += 1

scores["Obi-Wan Kenobi"] += patience // 3
scores["Yoda"] += patience // 2
scores["Anakin Skywalker 😈"] += max(0, 3 - patience // 3)


if role == "Teacher":
    scores["Yoda"] += 1; scores["Obi-Wan Kenobi"] += 2
elif role == "Diplomat/Mediator":
    scores["Qui-Gon Jinn"] += 2; scores["Yoda"] += 1
elif role == "Guardian/Warrior":
    scores["Mace Windu"] += 2
elif role == "Independent Pathfinder":
    scores["Anakin Skywalker 😈"] += 2; scores["Qui-Gon Jinn"] += 1


for i in values:
    if i == "Compassion": scores["Yoda"] += 1; scores["Obi-Wan Kenobi"] += 1
    if i == "Discipline": scores["Obi-Wan Kenobi"] += 2
    if i == "Curiosity": scores["Qui-Gon Jinn"] += 2
    if i == "Tradition": scores["Yoda"] += 1; scores["Mace Windu"] += 1
    if i == "Independence": scores["Anakin Skywalker 😈"] += 2
    if i == "Non-attachment": scores["Qui-Gon Jinn"] += 1; scores["Yoda"] += 1; scores["Mace Windu"] += 1
    if i == "Courage": scores["Obi-Wan Kenobi"] += 2; scores["Anakin Skywalker 😈"] += 1
    if i == "Humility": scores["Yoda"] += 2


if meditate >= 10:
    scores["Yoda"] += 2; scores["Obi-Wan Kenobi"] += 1
elif meditate >= 4:
    scores["Obi-Wan Kenobi"] += 1; scores["Qui-Gon Jinn"] += 1
else:
    scores["Anakin Skywalker 😈"] += 1


if rules == "Follow it":
    scores["Obi-Wan Kenobi"] += 2; scores["Mace Windu"] += 1
elif rules == "Bend it when needed":
    scores["Qui-Gon Jinn"] += 2
elif rules == "Break it to follow the Living Force":
    scores["Anakin Skywalker 😈"] += 2; scores["Qui-Gon Jinn"] += 1


if st.button("Reveal my Jedi Master ✨"):  
    prog = st.progress(0)  
    for j in range(0, 101, 10):
        prog.progress(j)

    best = max(scores, key=scores.get)
    top_score = scores[best]
    ties = [k for k, i in scores.items() if i == top_score]

    st.metric("Midichlorian Alignment Score", int(top_score)) 

    result_images = {
        "Yoda": "images/Yoda_Attack_of_the_Clones.png",
        "Obi-Wan Kenobi": "images/ObiSWC.webp",
        "Mace Windu": "images/Mace_Windu.webp",
        "Qui-Gon Jinn": "images/Qui-Gon_Jinn.png",
        "Anakin Skywalker 😈": "images/Anakin-Jedi.webp",
        "Sith Lord": "images/Sith-Logo.png",
    }

    
    if len(ties) > 2 or top_score < 3:
        st.subheader("🌑 You have strayed too far… You are a **Sith Lord!** ⚡")
        st.image(result_images["Sith Lord"])
    elif len(ties) > 1:
        st.subheader("You embody multiple masters:")
        st.write(", ".join(ties))
        images_to_show = []
        captions = []
        for t in ties:
            if t in result_images:
                images_to_show.append(result_images[t])
                captions.append(t)
        if images_to_show:
            st.image(images_to_show, caption=captions)
    else:
        st.subheader(f"🌟 You are most like **{best}**!")
        blurbs = {
            "Yoda": "Space buddha. Indeed size matters not.",
            "Obi-Wan Kenobi": "Hello There.",
            "Mace Windu": "You may not grant Anakin the rank of master, but you know how to take down an army of battle droids!",
            "Qui-Gon Jinn": "You follow the Living Force and your conscience—even when it breaks with tradition.",
            "Anakin Skywalker 😈": "Not quite on the council ;) but passionate, powerful, and fearless. Beware old people with cloaks :) .",
            "Sith Lord": "The Dark Side has consumed you. Power, anger, and ambition fuel your path.",
        }
        st.write(blurbs.get(best, "The Force moves in mysterious ways."))
        st.image(result_images.get(best, "images/Jedi-order-crest-religious-symbol.webp.png"))

    st.balloons()  # NEW

