import tkinter
import webbrowser
from tkinter import BOTTOM
import random


def bored():
    """Open a random website from the selection provided. (Add more as you wish!)"""
    websites = ["https://emuos.net/beta/emuos/", "http://corndog.io/", "http://endless.horse/",
                "https://coronavirus-ninja.com/", "https://littlealchemy2.com/", "http://www.thisismywebsitenow.com/dodger/",
                "https://en.akinator.com/", "http://www.abobosbigadventure.com/", "https://diep.io/",
                "https://krunker.io/", "https://www.linerider.com/", "https://totaljerkface.com/happy_wheels.tjf",
                "https://pokemonshowdown.com/", "https://skribbl.io/", "http://www.whatthefuckshouldimakefordinner.com/index.php",
                "https://www.howmanypeopleareinspacerightnow.com/", "https://www.behindthename.com/random/",
                "https://temp-mail.org/", "http://flashbynight.com/drench/", "https://haveibeenpwned.com/",
                "https://myfridgefood.com/", "http://radio.garden/listen/kaytv/WDwVSI39", "http://hackertyper.com/",
                "https://onlinetonegenerator.com/hearingtest.html", "https://sleepyti.me/", "https://quickdraw.withgoogle.com/",
                "https://traffic-simulation.de/routing.html", "https://musclewiki.org/", "https://www.geoguessr.com/maps/world",
                "https://www.escapemotions.com/community/experiments/flame/index.php"]
    webbrowser.open(random.choice(websites))


root = tkinter.Tk()
root.title("Bored Button")
root.geometry("360x310")
root.resizable(0, 0)
root.config(bg="red")

title = tkinter.Label(root, text="Bored Button", background="red", font=("Comic Sans MS", 25))
title.pack(padx=5, pady=5)

tkinter.Label(root, text="Welcome to the Bored Button! Click here to open a", background="red", font=("Comic Sans MS", 11)).pack(padx=5, pady=5)
tkinter.Label(root, text="random, fun, time wasting website! Enjoy (:", background="red", font=("Comic Sans MS", 11)).pack(padx=5, pady=5)

button = tkinter.Button(root, text="BORED?", background="red", font=("Comic Sans MS", 30), width=25, command=bored)
button.pack(padx=5, pady=20)

tkinter.Label(root, text="Made by AHawky", background="red", font=("Comic Sans MS", 11)).pack(side=BOTTOM, pady=3)

root.mainloop()
