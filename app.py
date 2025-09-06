from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# Dare categories
dares = {
    "fun": [
        "Talk in a weird accent for 1 min 😂",
        "Dance without music for 30 seconds 💃",
        "Sing a Bollywood song dramatically 🎤",
        "Take a weird/funny selfie together and set it as your WhatsApp DP for 24 hours 🤳",
        "Do your partner’s mimicry for 30 sec 🤪",
        "Tell a lame joke and keep a straight face 🤔😂",
        "Try to rap about your partner on the spot 🎶",
        "Do a catwalk like a fashion model 🐱🚶",
        "Pretend to be a waiter and take your partner’s fake order 🍽️😂",
        "Balance a book on your head for 1 min 📚",
        "Draw your partner (badly) and show them 🖊️🤣",
        "Do a TikTok dance challenge without music 📱🕺",
        "Talk only in song lyrics for 2 mins 🎧",
        "Act like your partner for 1 full round 🎭",
        "Try tongue twisters 3 times fast 👅",
        "Wear socks on your hands till your next turn 🧦",
        "Speak in slow motion for 1 min ⏳😂",
        "Act like a news anchor reporting about your partner 📰",
        "Pretend the floor is lava for 2 mins 🔥",
        "Draw a mustache on yourself with pen/marker ✏️😅"
    ],
    "romantic": [
        "Hold hands and stare into each other's eyes for 20 sec ❤️",
        "Whisper something sweet 😘",
        "Give 3 compliments your partner never heard before 💌",
        "Slow dance to any random song playing 🎶💞",
        "Draw a heart on your partner’s hand with your finger 💕",
        "Hug your partner tightly for 1 min 🫂",
        "Kiss your partner on the forehead tenderly 💋",
        "Tell your partner one thing you adore about them 🌟",
        "Play with your partner’s hair for 30 sec 💇",
        "Recreate your first date moment 🥰",
        "Write ‘I love you’ with your finger on their palm ✋❤️",
        "Take a cheesy couple selfie 📸",
        "Whisper their name 5 times in the most loving tone 💖",
        "Give your partner a piggyback ride 🐷😂",
        "Feed your partner something sweet 🍫",
        "Make a heart shape together with your hands 🤲❤️",
        "Do a romantic movie pose 💃🕺",
        "Sit on your partner’s lap for one round 🪑💕",
        "Hold your partner’s face while saying something cheesy 🥺",
        "Kiss your partner’s hand like a royal 👑💋"
    ],
    "spicy": [
        "Kiss your partner somewhere new 😉",
        "Bite their lip softly 😏",
        "Whisper your fantasy in their ear 🔥",
        "Leave a playful hickey mark 😜",
        "Blindfold your partner and surprise them with a kiss 😶‍🌫️💋",
        "Lick your partner’s neck slowly 👅",
        "Kiss your partner for a full 60 seconds ⏱️💋",
        "Sit on your partner’s lap and kiss them 😈",
        "Kiss your partner’s stomach teasingly 💕",
        "Give your partner a soft back scratch for 2 mins 💆‍♀️",
        "Playfully bite your partner’s ear 🦷👂",
        "Kiss your partner’s collarbone tenderly 💋",
        "Do a slow, teasing dance for your partner 💃🔥",
        "Kiss while holding their hands above their head 🔗",
        "Let your partner mark you with lipstick or teeth 💄",
        "Kiss every part of their face (except lips first 😏)",
        "Whisper something dirty you’ve never said 🤭",
        "Kiss your partner’s neck and don’t stop for 30 sec 😮‍💨",
        "Give your partner a playful spanking 🍑",
        "French kiss with eyes closed for 1 min 👀💋"
    ]
}
# HTML template (inline for now)
html = """
<!doctype html>
<html>
<head>
  <title>Couple Dare App</title>
  <style>
    body { font-family: Arial; text-align: center; margin-top: 50px; background-color: #ffe6f0; }
    h1 { color: #e91e63; }
    button { padding: 10px 20px; margin: 10px; font-size: 16px; border-radius: 10px; background: #e91e63; color: white; border: none; cursor: pointer; }
    .dare { margin-top: 30px; font-size: 20px; font-weight: bold; color: #333; }
  </style>
</head>
<body>
  <h1>🔥 Couple Dare App 🔥</h1>
  <form method="post">
    <button name="category" value="fun">Fun 😆</button>
    <button name="category" value="romantic">Romantic 💖</button>
    <button name="category" value="spicy">Spicy 😏</button>
  </form>
  {% if dare %}
    <div class="dare">{{ dare }}</div>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    dare = None
    if request.method == "POST":
        cat = request.form["category"]
        dare = random.choice(dares[cat])
    return render_template_string(html, dare=dare)

if __name__ == "__main__":
    app.run(debug=True)
