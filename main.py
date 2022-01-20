import tkinter
import playsound
from tkinter import *
from tkinter.font import Font
from PIL import *
from PIL import ImageTk, Image
from playsound import playsound
import random
from time import sleep
import threading
from pydub import AudioSegment
import pyaudio
x = 0
y = 0
hearts = 10
Armor = False
Choice_Text = False
Axe = False
dontplay = False
Line = 0
Paused = False
LongLine = False
Attacks = 0
num = 0
width = 0
height = 0
Choice = 0
Chose = True
LongLine1 = False
LongLine2 = False
LongLine3 = False
GrendelHealth = 0
Defeated = False
EndCredits = False


class FullScreenApp(object):
    def __init__(self, master):
        self.master = master
        pad = 2
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)
        global width
        top.update()
        width = top.winfo_width()
        global height
        height = top.winfo_height()

    def toggle_geom(self):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom
        global width
        top.update()
        width = top.winfo_width()
        global height
        height = top.winfo_height()


value = "No selection"
top = tkinter.Tk()
app = FullScreenApp(top)
top.title("The Game")


image2 = Image.open('Background.jpg')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()

background_label = tkinter.Label(top, image=image1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
text1 = StringVar()
textMessage = tkinter.Message(top, textvariable = text1, width = width/1.75, bg = '#e0c86e', justify = CENTER)


def words(text):
    if not dontplay:
        global Choice_Text
        global LongLine
        global LongLine1
        global LongLine2
        global LongLine3
        global EndCredits
        if LongLine:
            font = 28.5
            LongLine = False
        elif Choice_Text:
            font = 33
        elif LongLine1:
            font = 29
            LongLine1 = False
        elif LongLine2:
            font = 31
            LongLine2 = False
        elif LongLine3:
            font = 32
            LongLine3 = False
        elif EndCredits:
            font = 60
            EndCredits = False
        else:
            font = 27

        my_font2 = Font(family="Lucida Calligraphy", size=int(width / font))
        textMessage.config(font = my_font2)
        text1.set(text)
        textMessage.update()
        print(textMessage.winfo_width())
        textMessage.place(x=width / 2 - (textMessage.winfo_width())/2, y=height / 9)

        top.update()
        textMessage.place(x=width / 2 - (textMessage.winfo_width())/2, y=height / 9)


text12 = StringVar()
text_message12 = tkinter.Message(top, textvariable=text12, width=width / 1.7, bg='#e0c86e', fg ='red')


def health(change):
    global hearts

    hearts = hearts - change
    text12.set("Health: " + str(hearts) + " hearts")

    text_message12.place(x=width / 25.58, y=height / 5.684)
    my_font2 = Font(family="Lucida Calligraphy", size=int(height/47.36))
    text_message12.config(font=my_font2)


# noinspection PyGlobalUndefined
def armor():
    global Armor
    text123 = StringVar()
    if Armor:
        global textMessage2
        textMessage2.destroy()
        text123.set("Armor: Full Chainmail Set")
    else:
        text123.set("Armor: None")
    textMessage2 = tkinter.Message(top, textvariable=text123, width=700 / 1.7, bg='#e0c86e', fg ='gray')
    textMessage2.place(x=width/25.58, y=height/2.842)
    my_font2 = Font(family="Lucida Calligraphy", size=int(height/47.36))
    textMessage2.config(font=my_font2)


# noinspection PyGlobalUndefined
def weapons():
    global Axe
    text1234 = StringVar()
    if Axe:
        global textMessage1
        textMessage1.pack_forget()
        text1234.set("Weapons: Battleaxe")
    else:
        text1234.set("Weapons: None")
    textMessage1 = tkinter.Message(top, textvariable=text1234, width=width / 1.7, bg='#e0c86e', fg ='blue')
    textMessage1.place(x=width/25.58, y=height/1.89466666666)
    my_font2 = Font(family="Lucida Calligraphy", size=int(height/47.36))
    textMessage1.config(font=my_font2)


# noinspection PyGlobalUndefined
def attackfunction():
    global Attacks, RandomNum, Defeated, hearts, Line
    rannum = 0
    Attacks += 1
    global num
    global GrendelHealth
    num = 0
    print(num)
    color = StringVar()
    while not num == 10:
        rannum = random.randint(1, 20)
        text = str(rannum)
        if num == 0:
            color = "yellow"
        if num == 1:
            color = "blue"
        if num == 2:
            color = "red"
        if num == 3:
            color = "green"
        if num == 4:
            color = "purple"
        if num == 5:
            color = "orange"
        if num == 6:
            color = "pink"
        if num == 7:
            color = "white"
        if num == 8:
            color = "cyan"
        if num == 9:
            color = "brown"
        if num == 10:
            color = "black"
        RandomNum = tkinter.Message(top, text=text, width=100, bg=color)
        font12345 = Font(family="Lucida Calligraphy", size=int(width / 63.95))
        RandomNum.config(font=font12345)
        RandomNum.place(x=width/1.31179, y=height / 2.43)
        top.update()
        num += 1
        sleep(0.6)
        if not color == "brown":
            RandomNum.destroy()
    if rannum == 1 or rannum == 2 or rannum == 3:
        words("You did 9 damage")
        GrendelHealth -= 9
    if rannum == 4 or rannum == 5 or rannum == 6:
        words("You did 9 damage plus an extra 1 damage")
        GrendelHealth -= 10
    if rannum == 7 or rannum == 8 or rannum == 9:
        words("You did 9 damage plus an extra 2 damage")
        GrendelHealth -= 11
    if rannum == 10 or rannum == 11 or rannum == 12:
        words("You did 9 damage plus an extra 3 damage")
        GrendelHealth -= 12
    if rannum == 13 or rannum == 14 or rannum == 15:
        words("You did 9 damage plus an extra 4 damage")
        GrendelHealth -= 13
    if rannum == 16 or rannum == 17 or rannum == 18:
        words("You did 9 damage plus an extra 5 damage")
        GrendelHealth -= 14
    if rannum == 19 or rannum == 20:
        words("You did 9 damage plus an extra 6 damage")
        GrendelHealth -= 15
    if color == "brown":
        sleep(3)
        RandomNum.destroy()
    if GrendelHealth <= 0:
        Defeated = True
        Line = 63
        the_game()

    rannum1 = random.randint(1, 2)
    if rannum1 == 1:
        words("Grendel did 2 damage to you")
        global text_message12
        text_message12.destroy
        health(2)
    if rannum1 == 2:
        words("Grendel did 3 damage to you")
        text_message12.destroy
        health(3)
    if hearts == 0:
        words("You died you will have to restart the fight")
        hearts = 10
        GrendelHealth = 40
        Line = 59
        the_game()


def playerinteraction():
    global dontplay
    global Line
    global Choice
    global Choice_Text
    global Chose
    global Armor
    global Axe
    num2 = B.get()
    num2 = num2.capitalize()
    if num2 == "Exit":
        sys.exit()
    if Choice_Text:
        Choice_Text = False
        if num2 == "1":
            Chose = True
            words("You chose choice 1")
            sleep(3)
            Choice = 1
            the_game()
        if num2 == "2":
            Chose = True
            words("You chose choice 2")
            sleep(3)
            Choice = 2
            the_game()
        if num2 == "3":
            Chose = True
            words("You chose choice 3")
            sleep(3)
            Choice = 3
            the_game()
    if num2 == "Start":
        Line = 0
        dontplay = False
        Chose = False
        Choice_Text = False
        Armor = False
        Axe = False
        the_game()
    if num2 == "Start1":
        the_sidegame()
    if num2 == "Pause":
        playpause()
    if num2 == "Play":
        playpause()
    if num2 == "Attack":
        attackfunction()


def playpause():
    global dontplay
    if dontplay:
        dontplay = False
        the_game()
    if not dontplay:
        dontplay = True


def play(sound):
    print(sound)
    global dontplay
    global Line
    global Paused
    if not dontplay:
        Paused = False
        playsound(".\\Audio\\" + sound + ".mp3")
        Line = Line + 1
        the_game()
    if dontplay:
        if not Paused:
            words("Paused")
            Paused = True
        play(sound)



def the_game():
    global Armor
    global Choice_Text
    global Axe
    global Line
    global LongLine
    global Choice
    if Line == 0 and not Chose:
        words("Hello, Beowulf welcome to the beginning of your adventure")
        play("Narrator 1")
    if Line == 1 and not Chose:
        words("You are in your village and you are about to find out the awful news")
        play("Narrator 1 2")
        # t = threading.Thread(target=play, args=("Narrator 1 2",))
        # t.start()
    if Line == 2 and not Chose:
        words("We have heard the news from Hrothgar's Kingdom that they have been")
        play("Village Person 1")
    if Line == 3 and not Chose:
        words("taken over by an evil demon named Grendel")
        play("Village Person 1 2")
    if Line == 4 and not Chose:
        words("Oh my Odin, what has this Grendel done")
        play("Beowulf 1")
    if Line == 5 and not Chose:
        LongLine = True
        words("He is slaying warriors in their mead hall and leaving the village defenseless from outside attacks")
        play("Village Person 2")
    if Line == 6 and not Chose:
        words("I must go there and defeat Grendel myself, but first I must consult with the elders")
        play("Beowulf 2")
    if Line == 7 and not Chose:
        words("You walk over to talk with elders")
        play("Narrator 2")
    if Line == 8 and not Chose:
        words("I have heard the news of a monster across the sea and I seek council on my decision to go")
        play("Beowulf 3")
    if Line == 9 and not Chose:
        words("We stand by your decision to go with absolute certainty")
        play("Elder 1")
    if Line == 10 and not Chose:
        words("We wish you godspeed on your journey")
        play("Elder 2")
    if Line == 11 and not Chose:
        words("And we hope you can defeat this terrible monster")
        play("Elder 3")
    if Line == 12 and not Chose:
        words("Thank you elders for your blessing I will defeat this wretched monster")
        play("Beowulf 4")
    if Line == 13 and not Chose:
        words("You walk to the center of the town and yell")
        play("Narrator 3")
    if Line == 14 and not Chose:
        words("I will take the finest men and sail to Hrothgar's Kingdom and slay this inferior being")
        play("Beowulf 5")
    if Line == 15 and not Chose:
        words("Everyone cheers and you start to get ready to go. You grab your axes and equip your armor.")
        play("Narrator 4")
        Armor = True
        armor()
        Axe = True
        weapons()
    if Line == 16 and not Chose:
        words("You and your army run on to your boat and sail into the sunset")
        play("Narrator 4 2")
    if Line == 17 and not Chose:
        words("After a long while you make it to the new land and everyone rejoices upon seeing it")
        play("Narrator 5")
    if Line == 18 and not Chose:
        words("once you get there you see a man riding on a horse what would you like to do?")
        play("Narrator 5 2")
        Choice_Text = True
        words('Choice 1: Say "We would like to speak with your great king'
              '\nChoice 2: Say "We are here to defeat Grendel"'
              '\nChoice 3: Walk past him')
    if Chose:
        if Choice == 1:
            if Line == 19:
                words("Who are you?")
                play("Man on Horse 1")
            if Line == 20:
                words("I am the great and powerful Beowulf and would like to speak with your king")
                play("Beowulf 6")
            if Line == 21:
                words("Why do you wish to speak with him")
                play("Man on Horse 2")
            if Line == 22:
                words("I heard tales of a monster named Grendel and I believe I can defeat him")
                play("Beowulf 7")
            if Line == 23:
                words("You think you can defeat him")
                play("Man on Horse 3")
            if Line == 24:
                words("Yes I do")
                play("Beowulf 8")
            if Line == 25:
                words("Well right this way to see the king")
                play("Man on Horse 4")
            if Line == 26:
                words("He escorts you to the king's throne")
                play("Narrator 6")
        if Choice == 2:
            if Line == 19:
                words("You think you can defeat Grendel")
                play("Man on Horse 5")
            if Line == 20:
                words("Of course, I am the great and powerful Beowulf I have defeated all enemies that have come")
                play("Beowulf 9")
            if Line == 21:
                words("my way this challenge will only prove my honor even more")
                play("Beowulf 9 2")
            if Line == 22:
                words("Well right this way to see the king")
                play("Man on Horse 6")
        if Choice == 1 or Choice == 2 and not Defeated:
            Line == 27
            if Line == 27:
                words("Hello King Hrothgar my name is Beowulf I am from a distant land")
                play("Beowulf 10")
            if Line == 28:
                words("I have come to defeat the beast Grendel that has been terrorizing you and your people")
                play("Beowulf 10 2")
        if Choice == 3:
            if Line == 19:
                words("What do you think you are doing")
                play("Man on Horse 7")
            if Line == 20:
                words("You walk past him and he gets worried")
                play("Narrator 7")
            if Line == 21:
                words("Stop the attacker")
                play("Man on Horse 8")
            if Line == 22:
                words("One of the villagers knocks you out and takes you to the king's throne")
                play("Narrator 8")
            if Line == 23:
                words("I am King Hrothgar and what do you think you are doing in my kingdom")
                play("King Hrothgar 1")
                sleep(0.5)
            if Line == 24:
                LongLine = True
                words("I am sorry I think this a complete misunderstanding see I am Beowulf and I am not your enemy")
                play("Beowulf 11")
            if Line == 25:
                words("Beowulf, son of Ecgtheow")
                play("King Hrothgar 2")
                sleep(0.5)
            if Line == 26:
                words("Yes that's my father")
                play("Beowulf 12")
            if Line == 27:
                words("Unchain him I am sorry Beowulf I didn't know who you were ")
                play("King Hrothgar 3")
                sleep(0.5)
            if Line == 28:
                words("but I have to ask you what are you doing here")
                play("King Hrothgar 3 2")
                sleep(0.5)
            if Line == 29:
                words("I have come here to defeat Grendel")
                play("Beowulf 13")
        if not Defeated:
            Line = 30
        if Line == 30:
            words("I knew your father Beowulf he was a great warrior")
            play("King Hrothgar 4")
        if Line == 31:
            words("but even he would think twice before fighting an awful monster like Grendel")
            play("King Hrothgar 4 2")
        if Line == 32:
            words("I think my father would agree that I could defeat Grendel to prove my honor and glory")
            play("Beowulf 14")
        if Line == 33:
            words("You speak of honor and glory but I have one word for you Breca")
            play("Unferth 1")
        if Line == 34:
            words("Unferth? What are you talking about")
            play("King Hrothgar 5")
        if Line == 35:
            words("Do you remember Breca Beowulf he was your friend until you drowned him")
            play("Unferth 2")
        if Line == 36:
            words("Is this true Beowulf")
            play("King Hrothgar 6")
        if Line == 37:
            words("Breca was my best friend many years ago and we were both very strong warriors")
            play("Beowulf 15")
        if Line == 38:
            global LongLine1
            LongLine1 = True
            words("We went on adventures together and one day we did a competition to see who could swim for longer")
            play("Beowulf 15 2")
        if Line == 39:
            words("We swam for days until a giant storm hit us and split us apart")
            play("Beowulf 15 3")
        if Line == 40:
            words("What happened to him")
            play("King Hrothgar 7")
        if Line == 41:
            words("We stirred up the water so much that nine sea monsters came to attack")
            play("Beowulf 16")
        if Line == 42:
            global LongLine2
            LongLine2 = True
            words(
                "I barely defeated all of them, but I ended up losing consciousness and when I awoke Breca was nowhere "
                "to be seen")
            play("Beowulf 16 2")
        if Line == 43:
            words("I can't believe that happened")
            play("King Hrothgar 8")
        if Line == 44:
            words("And the worst part was that everyone though I killed him")
            play("Beowulf 17")
        if Line == 45:
            words("Wow that was such a good story")
            play("Unferth 3")
        if Line == 46:
            words("You think you're so defined that you publicly humiliate people")
            play("Beowulf 18")
        if Line == 47:
            words("and since I don't want to repeat your mistakes I'll tell you this in private")
            play("Beowulf 18 2")
        if Line == 48:
            words("You're a soldier right")
            play("Beowulf 19")
        if Line == 49:
            words("Yea....")
            play("Unferth 4")
        if Line == 50:
            words("If you were such a good soldier we wouldn't be dealing with this Grendel issue")
            play("Beowulf 20")
        if Line == 51:
            words("Unferth feeling embarrassed leaves the room but stands just outside listening")
            play("Narrator 9")
        if Line == 52:
            words("Night is coming and we must leave Beowulf but we believe in you and hope you will succeed")
            play("King Hrothgar 9")
        if Line == 53:
            words("King Hrothgar starts leaving but then turns around and notices that Beowulf has no sword")
            play("Narrator 10")
        if Line == 54:
            words("Where is your sword Beowulf")
            play("King Hrothgar 10")
        if Line == 55:
            words("I put it away")
            play("Beowulf 21")
        if Line == 56:
            words("So you are just going to fight Grendel with no sword")
            play("King Hrothgar 11")
        if Line == 57:
            words("Grendel has no sword so I must match him to prove my worthiness")
            play("Beowulf 22")
        if Line == 58:
            words("I believe in you Beowulf and our entire village is rooting for you")
            play("King Hrothgar 12")
        if Line == 59:
            LongLine = True
            words("You get ready to fight and as night falls you walk into the mead hall to see your opponent Grendel")
            play("Narrator 11")
        if Line == 60:
            global LongLine3
            LongLine3 = True
            words("To attack type attack in the box and you will get a random number which determines how much "
                  "attack damage you do")
            play("Narrator 11 2")
        if Line == 61:
            words("To slay your enemy you must get their health down to zero before your health does")
            play("Narrator 11 3")
        if Line == 62:
            words("If your health does fall to zero you will be forced to restart the fight")
            play("Narrator 11 4")
        if Line == 63 and Defeated:
            LongLine1 = True
            words("You grab Grendel and jump on his back then suddenly an arrow gets shot at him and Unferth comes in")
            play("Narrator 12")
        if Line == 64 and Defeated:
            words("Don't worry Beowulf I am here to help you")
            play("Unferth 7")
        if Line == 65 and Defeated:
            words("No! I am trying to do this alone")
            play("Beowulf 23")
        if Line == 66 and Defeated:
            words("But you can't beat him alone")
            play("Unferth 8")
        if Line == 67 and Defeated:
            words("Yes I can")
            play("Beowulf 24")
        if Line == 68 and Defeated:
            LongLine2 = True
            words("You grab Grendel by the arm and swing him around until Grendel's arm falls off and Grendel runs "
                  "away")
            play("Narrator 13")
        if Line == 69 and Defeated:
            words("You did it")
            play("Unferth 9")
        if Line == 70 and Defeated:
            words("I told you I could")
            play("Beowulf 25")
        if Line == 71 and Defeated:
            words("You and Unferth walk back to have the whole town congratulate you on your victory")
            play("Narrator 14")
        if Line == 72 and Defeated:
            global EndCredits
            EndCredits = True
            words("The guy on Horseback- Logan\nVillage Person 1- Krish\nVillage Person- Noah\nElder 1- Krish"
                  "\nElder 2- Zainab\nElder 3- Noah\nUnferth- Caitlyn\nKing Hrothgar- Jack\nNarrator- Alex"
                  "\nBeowulf- Cool Guy Maddi\nThank you for play! We hope you enjoyed!")
            play("End Credits")
            sleep(3)
            exit()


def the_sidegame():
    global EndCredits
    EndCredits = True
    words("The guy on Horseback- Logan\nVillage Person 1- Krish\nVillage Person- Noah\nElder 1- Krish"
          "\nElder 2- Zainab\nElder 3- Noah\nUnferth- Caitlyn\nKing Hrothgar- Jack\nNarrator- Alex"
          "\nBeowulf- Cool Guy Maddi\nThank you for play! We hope you enjoyed!")
    play("End Credits")


playpause = tkinter.Button(top, text = "Play/Pause", height = int(height/712.5), width = 10, bg = '#cc9f37',
                           activebackground = '#cc9f37', command = playpause)
Font1 = Font(family = "Lucida Calligraphy", size = int(width/196.769230769))
playpause.config(font = Font1)
playpause.place(x=width/1.59875, y= height/1.435)


helpcommand = tkinter.Message(top, text ="Help:\n1. Type Move to move your character\n2. Type Repeat to repeat the last"
                                         " dialogue\n3.Type Start to Start\n4. Type a number to choose a choice\n"
                                         "5. Type Attack to attack\n6. Type Exit to exit"
                                         "\n\nPress Execute or enter to execute your command",
                              bg = "#e0c86e", width = 498)
helpcommand.place(x =width / 1.2427710, y =height / 14.21)

B = tkinter.Entry(top, fg = 'black', bg = '#cc9f37', width = 11)
B.place(x=width/3.12, y=height/1.32)
myFont = Font(family="Lucida Calligraphy", size=int(height/14.21))
myFont3 = Font(family="Lucida Calligraphy", size=int(height/47.36))
B.configure(font=myFont)
helpcommand.configure(font = myFont3)
A = tkinter.Button(top, text = "Execute", width = 12, relief = RAISED, command = playerinteraction, bg ='#cc9f37',
                   activebackground = '#cc9f37')
myFont1 = Font(family="Lucida Calligraphy", size=int(height/71.05))
A.config(font= myFont1)
A.place(x=width/2.17, y= height/1.45)
armor()
health(0)
weapons()
words("Welcome to Hvelding the Watchful type Start and press execute to begin")
B.bind("<Return>", (lambda event: playerinteraction()))
top.mainloop()