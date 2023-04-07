"""
consider saving these in json...
"""
import json


idioms = {
    "German": {
        "Idiom": "Das ist nicht mein Bier.",
        "Translation": "That's not my beer.",
        "Meaning": "That's not my problem or concern."
    },
    "Japanese": {
        "Idiom": "猿も木から落ちる。",
        "Translation": "Even monkeys fall from trees.",
        "Meaning": "Even experts make mistakes or have accidents."
    },
    "Spanish": {
        "Idiom": "El mundo es un pañuelo.",
        "Translation": "The world is a handkerchief.",
        "Meaning": "The world is a small place, and you may unexpectedly run into someone you know."
    },
    "Italian": {
        "Idiom": "Mangiare la foglia.",
        "Translation": "Eat the leaf.",
        "Meaning": "To catch on to someone's tricks or deceit."
    },
    "Russian": {
        "Idiom": "Шапка невидимка.",
        "Translation": "Invisible cap.",
        "Meaning": "To pretend to be invisible or unnoticed."
    },
    "Swedish": {
        "Idiom": "Att ha is i magen.",
        "Translation": "To have ice in one's stomach.",
        "Meaning": "To have nerves of steel or be unemotional in a tough situation."
    },
    "French": {
        "Idiom": "Avoir le cafard.",
        "Translation": "To have the cockroach.",
        "Meaning": "To feel sad or depressed."
    },
    "Mandarin": {
        "Idiom": "画蛇添足.",
        "Translation": "To draw a snake and add feet to it.",
        "Meaning": "To ruin a good thing by adding unnecessary or excessive elements."
    },
    "Arabic": {
        "Idiom": "الماء الذي لا يجري يعوّم السفن.",
        "Translation": "Still waters run deep.",
        "Meaning": "Quiet or reserved people can often have strong opinions or feelings."
    },
    "Korean": {
        "Idiom": "개구리 올챙이 적 생각 못한다.",
        "Translation": "A frog cannot remember the tadpole stage.",
        "Meaning": "To have forgotten one's humble beginnings or to be ungrateful."
    },
    "Portuguese": {
        "Idiom": "Quem não tem cão, caça com gato.",
        "Translation": "Whoever doesn't have a dog hunts with a cat.",
        "Meaning": "To make do with what you have or find alternative solutions."
    },
    "Yiddish": {
        "Idiom": "קיין אפעל זאָל נישט קליין ריינגיין.",
        "Translation": "No apple should be too small to turn.",
        "Meaning": "Every opportunity should be seized, no matter how small or insignificant it may seem."
    }
}

# Open a file for writing
with open('idioms.json', 'w') as f:
    # Write the dictionary to the file in JSON format
    json.dump(idioms, f)

print("JSON data written to file successfully!")