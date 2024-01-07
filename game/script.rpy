# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
$ _skipping = False
define config.debug_sound = True

define mc = Character("[name!c]", color="#07E1FB", image = "mc", callback = name_callback, cb_name = "mc")
define y = Character("Perfectionism" , image = "perfectionism", callback = name_callback, cb_name = "y")
define m = Character("[name!c]'s Mom", color="#FFBF00", image = "m", callback = name_callback, cb_name = "m")
define narrator = Character(callback = name_callback, cb_name = None)
default gender = "male"
image mom = At("images/mom.png", sprite_highlight('m'))
image mc normal = At("images/mc[gender]/mc.png", sprite_highlight('mc'))
image mc hurt = At("images/mc[gender]/mc hurt.png", sprite_highlight('mc'))
image mc happy = At("images/mc[gender]/mc happy.png", sprite_highlight('mc'))
image mc relief = At("images/mc[gender]/mc relief.png", sprite_highlight('mc'))
image mc think = At("images/mc[gender]/mc think.png", sprite_highlight('mc'))
image mc look = At("images/mc[gender]/mc look.png", sprite_highlight('mc'))
image mc awk = At("images/mc[gender]/mc awk.png", sprite_highlight('mc'))
image mc quiet = At("images/mc[gender]/mc quiet.png", sprite_highlight('mc'))
image mc mad = At("images/mc[gender]/mc mad.png", sprite_highlight('mc'))
image mc angry = At("images/mc[gender]/mc angry.png", sprite_highlight('mc'))
image mc whatevah = At("images/mc[gender]/mc whatevah.png", sprite_highlight('mc'))
image mc insane= At("images/mc[gender]/mc insane.png", sprite_highlight('mc'))
image mc sigh= At("images/mc[gender]/mc sigh.png", sprite_highlight('mc'))
image mc front= At("images/mc[gender]/mc look2.png", sprite_highlight('mc'))
image mc end= At("images/mc[gender]/mc end.png", sprite_highlight('mc'))
image perfectionism normal = At("images/mc[gender]/mc anxiety.png", sprite_highlight('y'))
image perfectionism look = At("images/mc[gender]/mc anxlook.png", sprite_highlight('y'))
image perfectionism scared = At("images/mc[gender]/mc anxscared.png", sprite_highlight('y'))
image perfectionism talk = At("images/mc[gender]/mc anxtalk.png", sprite_highlight('y'))
image perfectionism attack = At("images/mc[gender]/mc anxattack.png", sprite_highlight('y'))
image perfectionism happy = At("images/mc[gender]/mc anxhappy.png", sprite_highlight('y'))
image perfectionism relief = At("images/mc[gender]/mc anxrelief.png", sprite_highlight('y'))
image perfectionism mad = At("images/mc[gender]/mc anxmad.png", sprite_highlight('y'))
image perfectionism sigh = At("images/mc[gender]/mc anxsigh.png", sprite_highlight('y'))
image perfectionism worry = At("images/mc[gender]/mc anxworry.png", sprite_highlight('y'))
image perfectionism fine = At("images/mc[gender]/mc anxfine.png", sprite_highlight('y'))
image perfectionism okay = At("images/mc[gender]/mc anxokay.png", sprite_highlight('y'))
image perfectionism hurt = At("images/mc[gender]/mc anxhurt.png", sprite_highlight('y'))
image perfectionism sorry = At("images/mc[gender]/mc anxsorry.png", sprite_highlight('y'))
image perfectionism sorry2 = At("images/mc[gender]/mc anxsupersorry.png", sprite_highlight('y'))
image perfectionism no = At("images/mc[gender]/mc anxno.png", sprite_highlight('y'))
image perfectionism end = At("images/mc[gender]/mc end.png", sprite_highlight('y'))
define apologized_for_hurt = False
define INJURED = False
define a4_talked_about_bad = False
define a4_talked_about_alone = False
define a4_talked_about_harm = False
define act4_something_else = False
define a4_fears_discussed = 0
define num_thanks = 0

init -2 python:
    class GetText(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)



init python:
    import collections
    
    def ContainsBadWord(name):
        #Get list of bad words from text file, each word on a separate line
        rude_words_file = [line.rstrip('\n') for line in open(renpy.loader.transfn('docs/rude_words.txt'), 'r')]
        
        #Check if the name contains a bad word
        for badWord in rude_words_file:
            if (badWord in name):
                return True


label splashscreen:
    scene black
    with Pause(1)

    show text  "Author's Notes: \n \n Adventures With Perfectionism is a variation of the original interactive story, Adventures With Anxiety by Nicky Case. \n \n As the title says, this version focuses more on perfectionism and related fears that college students may experience and it aims to enlighten, using humor, how perfectionism-related anxiety works. \n \n I made this to share the original interactive story as well as add my own twist to it to make it relatable for my fellow college students.\n \nI hope that with this, we can reduce the fear of fear itself.\n \n Enjoy!\n \n\n \nother notes: INCLUDES SWEARING, MENTAL HEALTH DISORDERS, SEXUALITY \n \n \n \n (click anywhere to proceed)" with dissolve
    pause
    #$ renpy.pause(10, hard = True)

    hide text with dissolve
    with Pause(1)

    return

# The game starts here.
label start:
    stop music fadeout 2
    with fade
    "Hi! This is more of an interactive story than a game. To advance the story, just click anywhere inside the screen."
    "Great! I hope you enjoy the story and learn something valuable about \"perfectionism\"!"
    "Anyway, let's start."
    
    play music "audio/illurock.opus" fadein 2 volume 0.3
    
    image your_image:
        xzoom -1.0
        "wp3738722.jpg"

    image fonbge:
        "fonbge.png"
        xalign 0.2
        yalign 0.5
    image fodo:
        "fodo.png"
        xalign 0.2
        yalign 0.5
    image fomm:
        "fomm.png"
        xalign 0.2
        yalign 0.5
    image arrow:
        "red-arrow-png-36953.png"
        xalign 0.8
        yalign 0.5
        xzoom -1.0
    image arrow1:
        "red-arrow-png-36953.png"
        xalign 0.2
        yalign 0.5

    image zoomed:
        xzoom -1.0
        "wp3738722.jpg"
        zoom 1.5

    scene your_image with fade
    "By the way, what's your name?"
    label name:
        $ name = renpy.input("The name is...", length = 15, allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if name == "":
            "Enter a name of 3 to 15 letters."
            jump name
        if name is not None:
            $ check_name = len(name)
            if check_name <= 2:
                "Enter a name of 3 to 15 letters."
                jump name
        if name == "Perfectionism":
            "You can't use that name."
            jump name
        $ rude_words_file = [line.rstrip('\n') for line in open(renpy.loader.transfn('docs/rude_words.txt'), 'r')]
        #if ( PL_fname.lower().strip() in rude_words_file ):
        if(ContainsBadWord(name.lower().strip())):
            "You can't use inappropriate language."
            jump name

    "Alright, you are [mc!c]."
    "Are you a male or female?"
    menu:
        "Male":
            play sound "audio/click.mp3"
            pass
        "Female":
            play sound "audio/click.mp3"
            $ gender = "female"
    if gender == "female":
        $ mc = Character("[name!c]", color="#FF6CFB", image = "mc", callback = name_callback, cb_name = "mc")
    "Ok, you are a [gender]."
    show mc normal at center
    with fade
    "So here's the plot twist."
    "You are not the character you just named. :)"
    "THIS IS [mc!u]."
    show mc normal at left with moveinleft
    show perfectionism normal at right with moveinright:
        xzoom -1.0
    "and, THIS IS [mc!u]'S PERFECTIONISM."
    "YOU ARE THE PERFECTIONISM!"
    show perfectionism look
    y "Yeah...I'm you...you're me..."
    ""
    show perfectionism normal
    pause
    image intro = "intro1.png"
    image intro1 = "intro2.png"
    image intro2 = "images/mc[gender]/intro.png"
    show intro with fade
    "In this story, [mc!c] is a fourth year ONLINE college student, studying in a prestigious university."
    show intro1 with dissolve
    "[mc!c] is studying under a course program called Multimedia Studies."
    "All the school activities and studying are done online."
    show intro2 with dissolve
    "As an online student, [mc!c] is expected to have self-discipline and be self-reliant."
    "Online studying is often lonely compared to traditional classes where there are classmates and teachers to talk to."
    "So it is not surprising that sometimes, [mc!c] experiences difficulties."
    "But the good news is, you're here to help!"
    hide intro
    hide intro1
    hide intro2
    with fade
    "Anyway, others have high expectations of [mc!c] because of being known as a good and smart student."
    if gender == "male":
        "[mc!c] also has high expectations for himself because he wants to do his \"best\" in everything."
    if gender == "female":
        "[mc!c] also has high expectations for herself because she wants to do her \"best\" in everything."
    "Okay, enough of the introduction..."
    "The mission is to graduate from college."
    "But there are many \"obstacles\" on the way that need to be overcome."
    "[mc!c]'s story is in your hands..."
    if gender == "male":
        "Help him have a \"perfect\" journey to graduating college!"
    if gender == "female":
        "Help her have a \"perfect\" journey to graduating college!"
    "May the story begin. Good luck!"
    jump act1

label act1:
    stop music fadeout 2
    scene black with fade
    with Pause(1)
    show text "{size=100}Chapter 1" with dissolve
    pause
    hide text with dissolve
    with Pause(1)
    scene zoomed
    show mc normal at left
    with fade

    
     
    screen hpbge:
        vbox:
            xalign 1.0
            yalign 0.05
            bar value enemy_hp range enemy_max_hp xmaximum 500
            text "{color=#000000} Perfectionism's HP: [enemy_hp]/[enemy_max_hp]" 
    screen hpbarenemy:
        vbox:
            xalign 1.0 
            yalign 0.085
            bar value enemy_max_hp range enemy_max_hp xmaximum 500
            #xalign 0.0 
            #yalign 0.1 
    screen hpbg:
        vbox:
            xalign 0.0 
            yalign 0.05
            bar value currenthp range maxhp xmaximum 500
            text "{color=#000000} [mc!c]'s HP: [currenthp]/[maxhp]" 
    screen hpbar:
        vbox:
            xalign 0.0 
            yalign 0.085
            bar value maxhp range maxhp xmaximum 500
            #xalign 0.0 
            #yalign 0.1
    $ currenthp = 100
    $ maxhp = 100
    $ enemy_max_hp = 100
    $ enemy_hp = 100
    
    show mc happy
    mc "I can't believe it, I'm in my 4th, and hopefully last, year already."
    show mc relief
    mc "It felt like just yesterday I'm still overthinking what course and school to choose."
    show mc think
    mc "Anyway, since I'm a 4th year student...I would need to do thesis now, right!?"
    show perfectionism scared at right:
        xzoom -1.0
    show screen hpbar 
    show screen hpbg
    show screen hpbarenemy
    show screen hpbge
    play sound "audio/suspense.mp3"  
    with fade
    pause
    play music "audio/funny.mp3" fadein 2 volume 0.3
    show mc look
    mc "Aaaaaand it appeared again."
    "The hp bars are there to determine which of you would get to make the ultimate decision, you or [mc!c]? :)"
    show mc awk
    mc "Oh hello MY perfectionism! You're back so soon? Faaaaaaantastic."
    "YOUR JOB IS TO PROTECT [mc!u] FROM {i}FAILURE."
    if gender == "male":
        "IN FACT, THINKING ABOUT THESIS MIGHT LEAD HIM TO {i}FAILURE{/i}!"
        "QUICK, WARN HIM!"
    if gender == "female":
        "IN FACT, THINKING ABOUT THESIS MIGHT LEAD HER TO {i}FAILURE{/i}!"
        "QUICK, WARN HER!"
    show perfectionism talk 
    y "[mc!c], there's something you need to know!"
    y "About your thesis!..."
    menu:
        "Choose an easy topic!":
            play sound "audio/click.mp3"
            y "Choose an easy topic!"
            y "So you can easily finish, polish and perfect the details!"
            mc "This is my final thesis though, are you sure-"
            show perfectionism scared
            y "If you attempt a difficult topic, you will struggle, you will not finish on time,"
            y "You'll only be disappointed with what you've done, you'll realize that you can't do it and you're not good enough,"
            show perfectionism talk
            y "That you are worthless and worse!-"
            show perfectionism attack
            y "YOU MIGHT NOT GRADUATEEEEE!"
            $ c1 = "choose an easy topic"
            $ currenthp -= 10 
            show fonbge
            show mc hurt
            play sound "audio/punch.opus"
            with vpunch
            pause
            hide fonbge
            "YOU USED {i}FEAR OF NOT BEING GOOD ENOUGH! {/i}"
        "Choose a difficult topic!":
            play sound "audio/click.mp3"
            y "Choose a difficult topic!"
            y "For sure your other classmates will choose \"cutting-edge\" and \"groundbreaking\" topics!"
            y "And their research will be \"useful\" and \"great contributions\" to society!"
            mc "Well, I am not trying to-"
            show perfectionism mad
            y "So to keep up, you can't just choose an easy topic! You are studying at -insert university/college name here-!"
            y "Do you want to tarnish the school's reputation?"
            mc "What are you even s-"
            show perfectionism scared
            y "If you don't choose a difficult topic, many will be disappointed and-"
            show perfectionism attack
            y "YOUR RESEARCH MIGHT NOT MEET THE STANDARDS AND YOU'LL FAIL!"
            $ c1 = "choose a difficult topic"
            $ currenthp -= 10 
            show fodo
            show mc hurt
            play sound "audio/punch.opus"
            with vpunch
            pause
            hide fodo
            "YOU USED {i}FEAR OF DISAPPOINTING OTHERS! {/i}"
        "Don't even think about the topic yet!":
            play sound "audio/click.mp3"
            y "Don't even think about the topic yet!"
            y "There's so much other things you should be doing right now!"
            show perfectionism sigh
            y "How about you research or review EXTENSIVELY first, right?"
            mc "You do have a point, but do I really need to do it extensive-"
            show perfectionism scared
            y "Plus, aren't there requirements for choosing a topic?"
            show perfectionism sigh
            y "How will you follow the \"your research should be a culmination of all the things you learned in 4 years of this course\"?"
            mc "Ummm, maybe if I-"
            show perfectionism scared
            y "Do something, anything! So you know how to choose a \"perfect\" topic and plan first because if you just choose anything,-"
            show perfectionism attack
            y "YOU MIGHT PICK THE WRONG TOPIC, MAKE SO MANY MISTAKES AND WASTE TIME FIXING THEM OVER AND OVER AND OVER AGAIN!"
            $ c1 = "don't even think about the topic yet"
            $ currenthp -= 10 
            show fomm
            show mc hurt
            play sound "audio/punch.opus"
            with vpunch
            pause
            hide fomm
            "YOU USED {i}FEAR OF MAKING MISTAKES! {/i}"
    "IT'S SUPER EFFECTIVE!"
    show perfectionism happy
    y "See, [mc!c]? I'm here to make sure everything is \"perfect\"!"
    show perfectionism relief
    y "Like what they say, trust your gut! Just listen to me and everything will be flawless!"
    "GET [mc!u]'S ENERGY BAR TO ZERO."
    "TO AVOID BEING A FAILURE, YOU CAN USE:"
    "FEAR OF {i}NOT BEING GOOD ENOUGH" #PERSONAL DEVELOPMENT AND SOCIAL LIFE
    "FEAR OF {i}DISAPPOINTING OTHERS" #SOCIAL LIFE
    "AND FEAR OF {i}MAKING MISTAKES" #PERSONAL DEVELOPMENT
    "(PRO-TIP: PICK THE CHOICE THAT ALIGNS WITH YOUR OWN PERFECTIONISM!~)"
    show mc quiet
    mc "..."
    mc "You know what, fine."
    show mc mad
    show perfectionism scared
    if c1 == "choose an easy topic":
        mc "I'll choose an easy research topic so I can finish on time and be able to make it perfect."
    if c1 == "choose a difficult topic":
        mc "I'll challenge myself and choose a difficult topic, since this is my last thesis anyway."
    if c1 == "don't even think about the topic yet":
        mc "I'll review and plan first to make sure my research would be perfect."
    if gender == "male":
        "[mc!c] sits in front of his desk and opened his laptop, getting ready to start progress on his research."
    if gender == "female":
        "[mc!c] sits in front of her desk and opened her laptop, getting ready to start progress on her research."
    image bg z:
        "40-64246df8a94f5.png"
    scene bg z 
    show mc mad at left 
    show perfectionism scared at right:
        xzoom -1.0
    with fade
    "PROTECT [mc!u]!"
    if gender == "male":
        "FROM DISAPPOINTING HIMSELF."
    if gender == "female":
        "FROM DISAPPOINTING HERSELF."
    "FROM DISAPPOINTING OTHERS." 
    "FROM FAILURE."
    "GOOD LUCK!"
    "ROUND ONE: {i}FIGHT!"
    
























    if c1 == "choose an easy topic":
        image bg a:
            "bga.png"
        show bg a with dissolve
        show mc think
        mc "Multimedia has a wide scope, maybe I can focus on just one area that was covered in my 4 years of this course?"
        show perfectionism sigh
        y "Yeah..."
        menu:
            "Yeah, DON'T DO SOMETHING COMPLICATED":
                play sound "audio/click.mp3"
                show perfectionism attack
                y "Yeah, plus this is the easy route. You DON'T want to DO SOMETHING COMPLICATED or harder because, you might not be able to handle it!"
                $ c2 = "don't do something complicated"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "Yeah, DON'T BE A TRY HARD":
                play sound "audio/click.mp3"
                show perfectionism attack
                y "Yeah, that's right. You DON'T want to BE A TRY HARD, aim high then fail miserably and disappoint others!"
                $ c2 = "don't be a try hard"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "Yeah, DON'T MAKE MISTAKES":
                play sound "audio/click.mp3"
                $ c2 = "don't make mistakes"
                show perfectionism attack
                y "Yeah, that's right. You DON'T want to choose a widely scoped topic and MAKE many MISTAKES that will have endless revisions!"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        image bg b:
            "bgb.png"
        show bg b with dissolve
        show mc quiet
        mc "..."
        show mc awk
        mc "You really have a way of making everything look negative, you know?"
        show perfectionism mad
        if c2 == "don't do something complicated":
            y "What? I am just making sure your research will BE GOOD ENOUGH!"
        if c2 == "don't be a try hard":
            y "What? I am just making sure your research won't DISAPPOINT!"
        if c2 == "don't make mistakes":
            y "What? I am just making sure your research execution will be FLAWLESS!"
        show mc whatevah
        mc "Whatever."
        show mc happy
        mc "Oooooh, there's lots of options."
        mc "Maybe, I can choose \"Impact of Multimedia in Advertising\"."
        show perfectionism talk
        y "Ummm..."
        menu:
            "THAT'S NOT GOOD ENOUGH!":
                play sound "audio/click.mp3"
                show perfectionism scared
                y "Seriously? Everyone knows that multimedia is used in advertising!"
                show perfectionism sigh
                y "It's like saying water is wet!"
                show perfectionism attack
                y "Don't pick that; THAT'S NOT GOOD ENOUGH for your thesis!"
                $ c3 = "that's not good enough"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "THAT'S DISAPPOINTING!":
                play sound "audio/click.mp3"
                show perfectionism scared
                y "Seriously? Everyone knows that multimedia is used in advertising!"
                show perfectionism sigh
                y "It's like saying water is wet!"
                show perfectionism attack
                y "Don't pick that; THAT'S a DISAPPOINTING topic!"
                $ c3 = "that's disappointing"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "THAT'S WRONG!":   
                play sound "audio/click.mp3"
                show perfectionism scared
                y "Seriously? Everyone knows that multimedia is used in advertising!"
                show perfectionism sigh
                y "It's like saying water is wet!"
                y "For sure the research adviser will ask you to choose a better topic!"
                show perfectionism attack
                y "So don't pick that; THAT'S a WRONG choice!"
                $ c3 = "that's wrong"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        image bg c:
            "bgc.png"
        show bg c with dissolve
        show mc angry
        mc "Ugh, fine. I'll look for other topics."
        show mc think
        show perfectionism scared
        mc "Oh, how about \"The Role of Multimedia in Education\"."
        show perfectionism attack
        y "Eeeeek..."
        menu:
            "PREDICTABLE AND REDUNDANT!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "No, just no!"
                if c3 == "that's not good enough":
                    y "Again! Don't pick that; that's also not good enough for your thesis!"
                else:
                    y "Don't pick that; that won't be good enough for your thesis!"
                show perfectionism attack
                y "It's like a combination of peanut butter and jelly — so PREDICTABLE AND REDUNDANT!"
                $ c4 = "predictable and redundant"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "DON'T DISAPPOINT OTHERS!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Disappointing, utterly disappointing!"
                show perfectionism sigh
                y "It's like a combination of peanut butter and jelly — so predictable and redundant."
                show perfectionism attack
                if c3 == "that's disappointing":
                    y "Again! DON'T pick that; you'll just DISAPPOINT OTHERS with a topic like that as well!"
                else:
                    y "DON'T pick that; you'll just DISAPPOINT OTHERS with a topic like that!"
                $ c4 = "don't disappoint others"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "CHOOSE A BETTER TOPIC!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Wrong, just wrong!"
                show perfectionism sigh
                y "It's like a combination of peanut butter and jelly — so predictable and redundant."
                show perfectionism attack
                if c3 == "that's wrong":
                    y "Again! Don't pick that; It's another wrong choice! You need to CHOOSE A BETTER TOPIC!"
                else:
                    y "So don't pick that; that's a wrong choice! You need to CHOOSE A BETTER TOPIC!"
                $ c4 = "choose a better topic"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        image bg d:
            "bgd.png"
        show bg d with dissolve 
        show mc angry
        mc "Okay, okay! Just shut up!" 
        show perfectionism scared
        show mc think
        mc "Last two, I'll really settle for either of these."
        menu:
            "Multimedia and Virtual Reality (VR)":
                play sound "audio/click.mp3"
                mc "Alright, let's go with \"Multimedia and Virtual Reality (VR)\"."
                show mc awk
                mc "Don't tell me you still got something to say about th-"
                show perfectionism mad
                y "Tsk...tsk..."
                menu:
                    "IT'S TOO HARD!":
                        play sound "audio/click.mp3"
                        y "Are you sure you can do that and offer something unique about your research?"
                        y "Unless you are creating a virtual world where people can experience the thrill of doing laundry-"
                        show perfectionism attack
                        y "-then please don't choose that, IT'S TOO HARD!"
                        $ c5 = "it's too hard"
                        $ currenthp -= 10 
                        show fonbge
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fonbge
                    "DON'T AIM TOO HIGH!":
                        play sound "audio/click.mp3"
                        show perfectionism sigh
                        y "Isn't this too much to tackle? I thought you want an easy research topic."
                        show perfectionism mad
                        y "Unless you are creating a virtual world where people can experience the thrill of doing laundry-"
                        show perfectionism sigh
                        y "-then you're just going to disappoint others by wasting opportunity for what could've been a groundbreaking study!"
                        show perfectionism attack
                        y "DON'T AIM TOO HIGH!"
                        $ c5 = "don't aim too high"
                        $ currenthp -= 10 
                        show fodo
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fodo
                    "DON'T BE AN EMBARRASSMENT!":
                        play sound "audio/click.mp3"
                        y "Oh, are you a VR expert now?"
                        show perfectionism sigh
                        y "You don't even know much about this topic."
                        show perfectionism attack
                        y "DON'T do it, you're just going to make too many mistakes and BE AN EMBARRASSMENT to VR enthusiasts!"
                        $ c5 = "don't be an embarrassment"
                        $ currenthp -= 10 
                        show fomm
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fomm
            "User Experience Design in Multimedia":
                play sound "audio/click.mp3"
                mc "I'll go with \"User Experience Design in Multimedia\"."
                show mc awk
                mc "Don't tell me you still got something to say about th-"
                show perfectionism mad
                y "Tsk...tsk..."
                menu:
                    "NOT WORTH IT!":
                        play sound "audio/click.mp3"
                        y "Are you listening to me? Again this is an overly explored topic."
                        show perfectionism sigh
                        y "User experience design — it's like the unsung hero behind every successful app or website!"
                        show perfectionism mad
                        y "If you're not going to delve into the uncharted territory of designing an intuitive user experience for time-traveling dinosaurs-"
                        show perfectionism attack
                        y "-then anything you come up with may NOT be WORTH IT!"
                        $c5 = "not worth it"
                        $ currenthp -= 10 
                        show fonbge
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fonbge
                    "OVERLY EXPLORED!":
                        play sound "audio/click.mp3"
                        y "Are you listening to me? User experience design — it's like the unsung hero behind every successful app or website!"
                        y "Unless you're going to delve into the uncharted territory of designing an intuitive user experience for time-traveling dinosaurs-"
                        show perfectionism sigh
                        y "-then you will just disappoint fellow User Experience Design practitioners!"
                        show perfectionism attack
                        y "Please choose anything other than an OVERLY EXPLORED topic."
                        $c5 = "overly explored"
                        $ currenthp -= 10 
                        show fodo
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fodo
                    "WASTE OF TIME!":
                        play sound "audio/click.mp3"
                        y "Are you listening to me? Again this is an overly explored topic."
                        show perfectionism sigh
                        y "User experience design — it's like the unsung hero behind every successful app or website!"
                        show perfectionism mad
                        y "Unless you're going to delve into the uncharted territory of designing an intuitive user experience for time-traveling dinosaurs-"
                        show perfectionism attack
                        y "-then it's going to be a WASTE OF TIME pursuing this topic!"
                        $c5 = "waste of time"
                        $ currenthp -= 10 
                        show fomm
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fomm

















    if c1 == "choose a difficult topic":
        image bg e:
            "bge.png"
        show bg e with dissolve
        show mc think
        mc "There are a lot of things I learned in multimedia. Maybe I can focus on a research topic that combines some of it?"
        show perfectionism sigh
        y "Yeah..."
        menu:
            "Yeah, DO SOMETHING COMPLICATED":
                play sound "audio/click.mp3"
                show perfectionism attack
                y "Yeah, plus this is the hard route. You want to DO SOMETHING COMPLICATED or difficult because, you need to prove you're good enough!"
                $ c2 = "do something complicated"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "Yeah, TRY HARDER":
                play sound "audio/click.mp3"
                show perfectionism attack
                y "Yeah, that's right. You need to TRY HARDER, aim high and produce exceptional results so you don't disappoint others!"
                $ c2 = "try harder"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "Yeah, MAKE ACCEPTABLE MISTAKES":
                play sound "audio/click.mp3"
                show perfectionism attack
                $ c2 = "make acceptable mistakes"
                y "Yeah, that's right. This is the only way you can afford to MAKE ACCEPTABLE MISTAKES because it's gonna be a difficult topic!"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        image bg f:
            "bgf.png"
        show bg f with dissolve
        show mc quiet
        mc "..."
        show mc awk
        mc "You really have a way of making everything look negative, you know?"
        show perfectionism mad
        if c2 == "do something complicated":
            y "What? I am just making sure your research will BE GOOD ENOUGH!"
        if c2 == "try harder":
            y "What? I am just making sure your research won't DISAPPOINT!"
        if c2 == "make acceptable mistakes":
            y "What? I am just making sure your research execution will be FLAWLESS!"
        show mc whatevah
        mc "Whatever."
        show mc happy
        mc "Oooooh, there's lots of options."
        mc "Maybe, I can choose \"Multimodal Sentiment Analysis\"."
        show perfectionism scared
        y "Ummm..."
        menu:
            "THAT'S NOT GOOD ENOUGH!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Another attempt to understand human emotions through technology?"
                show perfectionism sigh
                y "Others have already made significant progress in this field."
                y "Even if you try, your contributions just won't be groundbreaking enough." 
                show perfectionism attack
                y "Hence, THAT'S NOT GOOD ENOUGH for your thesis!"
                $ c3 = "that's not good enough"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "THAT'S DISAPPOINTING!":
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "You'll probably end up with a sentiment analysis system that thinks every sad puppy picture is a major crisis-"
                show perfectionism mad
                y "-and every positive review is a declaration of eternal love. Way to disappoint everyone with an overly sensitive AI!"
                show perfectionism sigh
                y "I'll get to the point. You'll just end up disappointing your advisors and peers with a topic like this."
                show perfectionism attack
                y "So don't pick that; THAT'S going to be a DISAPPOINTING topic!"
                $ c3 = "that's disappointing"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "THAT'S WRONG!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Another attempt to understand human emotions through technology?"
                show perfectionism sigh
                y "Others have already made significant progress in this field."
                show perfectionism mad
                y "Plus, you're not even adept at this topic, you'll just make so much mistakes!"
                show perfectionism attack
                y "So don't pick that; THAT'S a WRONG topic to focus on!"
                $ c3 = "that's wrong"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        image bg g:
            "bgg.png"
        show bg g with dissolve
        show mc angry
        mc "Ugh, fine. I'll look for other topics."
        show perfectionism scared
        show mc happy
        mc "Oh, how about \"Human-Computer Interaction in Augmented Reality (AR)\"."
        show perfectionism attack
        y "Eeeeek..."
        menu:
            "THAT'S MEDIOCRE AT BEST!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "THAT'S MEDIOCRE AT BEST!"
                y "-and no, I am not talking about the topic, but the work you could possibly come up with!"
                show mc awk
                mc "How are you so sure-"
                show perfectionism talk
                y "I know you decided to choose a more challenging research topic but..."
                show perfectionism sigh
                y "...designing effective interaction techniques and interfaces for AR is beyond your capabilities."
                y "Your interfaces will likely be as confusing as assembling IKEA furniture without the instructions."
                y "Users will struggle to figure out what button does what,-" 
                show perfectionism attack
                y "-your ideas will just fall short of expectations, and you'll end up with a research THAT'S MEDIOCRE AT BEST!"
                $ c4 = "that's mediocre at best"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "DON'T RISK IT!":
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "I know you decided to choose a more challenging research topic but..."
                y "...let's be real, your interfaces will likely be as confusing as assembling IKEA furniture without the instructions."
                show perfectionism talk
                y "Users will struggle to figure out what button does what,-" 
                show perfectionism mad
                y "-and you'll be left with disappointed folks waving their hands around in frustration!"
                $ c4 = "don't risk it"
                show perfectionism attack
                y "I'm saying that you'll just fail to impress others in the field, please DON'T RISK IT!"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "CHOOSE ANOTHER TOPIC!":
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "I know you decided to choose a more challenging research topic but..."
                y "...let's be real, designing effective interaction techniques and interfaces for AR is beyond your capabilities."
                show perfectionism mad
                y "You'll probably encounter so many problems and commit so many mistakes."
                y "You'll end up wasting too much time and still end up with a failed research!"
                show perfectionism attack
                y "So CHOOSE ANOTHER TOPIC before you start to add another entry to your list of regrets and wrong life decisions!"
                $ c4 = "choose another topic"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        image bg h:
            "bgh.png"
        show bg h with dissolve
        show mc angry
        mc "Okay, okay! Just shut up!" 
        show perfectionism scared 
        show mc think
        mc "Last two, I'll really settle for either of these."
        menu:
            "Immersive Virtual Reality Experiences":
                play sound "audio/click.mp3"
                mc "Alright, let's go with \"Immersive Virtual Reality Experiences\"."
                show mc awk
                mc "Don't tell me you still got something to say about th-"
                show perfectionism mad
                y "Tsk...tsk..."
                menu:
                    "DON'T BE SUBPAR!":
                        play sound "audio/click.mp3"
                        show perfectionism sigh
                        y "Like I said, I know you want to tackle a challenging research topic but this is too much!"
                        mc "I personally don't think-"
                        show perfectionism mad
                        y "So you think you can create mind-blowing experiences that transport people to different realms?"
                        show perfectionism sigh
                        y "You don't even have the necessary skills or creativity to develop truly immersive VR experiences."
                        y "Even if you try, your work will just be subpar compared to what's already out there, and-"
                        show perfectionism attack
                        y "-you DON't want to BE SUBPAR, so please don't choose that!"
                        $ c5 = "don't be subpar"
                        $ currenthp -= 10 
                        show fonbge
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fonbge
                    "SUCH A LET DOWN!":  
                        play sound "audio/click.mp3"
                        show perfectionism sigh
                        y "Like I said, I know you want to tackle a challenging research topic but this is too much!"
                        show perfectionism mad
                        y "Your VR creations will probably make people dizzy, confused, and ultimately question their life choices."
                        mc "Maybe I could actually give it a try and-"
                        show perfectionism sigh
                        y "You'll probably get hated by some disappointed, slightly nauseous, users and stakeholders-"
                        show perfectionism mad
                        y "-who were expecting innovative and captivating VR experiences!"
                        show perfectionism attack
                        y "It's going to be SUCH A LET DOWN if you choose this topic!"
                        $ c5 = "such a let down"
                        $ currenthp -= 10 
                        show fodo
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fodo
                    "THIS IS A ONE-WAY ROAD TO FAILURE!":
                        play sound "audio/click.mp3"
                        show perfectionism sigh
                        y "Like I said, I know you want to tackle a challenging research topic but this is too much!"
                        show perfectionism mad
                        y "So you think you can create mind-blowing experiences that transport people to different realms?"
                        mc "I think I can atleast-"
                        show perfectionism sigh
                        y "You don't even have the necessary skills or creativity to develop truly immersive VR experiences."
                        y "Your VR creations will probably make people dizzy, confused, and ultimately question their life choices."
                        show perfectionism attack
                        y "Listen to me, THIS research topic IS a ONE-WAY ROAD TO mistakes, to errors, to FAILURE!"
                        $ c5 = "this is a one-way road to failure"
                        $ currenthp -= 10 
                        show fomm
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fomm
            "Explainable AI for Multimedia Understanding":
                play sound "audio/click.mp3"
                mc "I'll go with \"Explainable AI for Multimedia Understanding\"."
                show mc awk
                mc "Don't tell me you still got something to say about th-"
                show perfectionism mad
                y "Tsk...tsk..."
                menu:
                    "IT WOULD BE SO EXHAUSTING!":
                        play sound "audio/click.mp3"
                        y "Are you listening to me? Trying to explain the inner workings of AI models?"
                        y "The research in explainable AI is highly technical and challenging."
                        mc "I know, but I think-"
                        show perfectionism sigh
                        y "You'll struggle to understand and implement these complex techniques,-"
                        y "-and your explanations may not be clear or comprehensive enough."
                        show perfectionism attack
                        y "You won't be able to survive this topic, IT WOULD BE SO EXHAUSTING!"
                        $c5 = "it would be so exhausting" 
                        $ currenthp -= 10 
                        show fonbge
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fonbge                     
                    "IT'S A DISAPPOINTMENT, GUARANTEED!":
                        play sound "audio/click.mp3"
                        y "Are you listening to me? Trying to explain the inner workings of AI models?"
                        y "You'll probably end up with explanations that are more confusing than a Rubik's Cube."
                        mc "Or maybe I can avoid that if I-"
                        show perfectionism sigh
                        y "You'll disappoint both the research community and potential users of the AI models."
                        y "People will be scratching their heads, wondering if your AI is speaking in some alien language."
                        show perfectionism attack
                        y "IT'S going to be a DISAPPOINTMENT, GUARANTEED!"
                        $c5 = "it's a disappointment, guaranteed"
                        $ currenthp -= 10 
                        show fodo
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fodo
                    "ERRORS EVERYWHERE!":
                        play sound "audio/click.mp3"
                        y "Are you listening to me? Trying to explain the inner workings of AI models?"
                        y "The research in explainable AI is highly technical and challenging."
                        mc "It is, but I believe I can-"
                        show perfectionism sigh
                        y "You'll struggle to understand and implement these complex techniques,-"
                        y "-people will be scratching their heads, wondering if your AI is speaking in some alien language."
                        show perfectionism attack
                        y "Ahhhhhhhhh! I can already foresee ERRORS EVERYWHERE!"
                        $c5 = "errors everywhere"
                        $ currenthp -= 10 
                        show fomm
                        show mc hurt
                        play sound "audio/punch.opus"
                        with vpunch
                        pause
                        hide fomm






























    if c1 == "don't even think about the topic yet":
        image bg i:
            "bgi.png"
        show bg i with dissolve
        show mc think
        mc "There are so many things to consider when choosing a research topic. Where do I even start?"
        show perfectionism talk
        y "Ummmm..."
        menu:
            "Consider existing passion, skills, and knowledge!":
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "C'mon, don't try being all fancy with this and just consider your existing passion, skills, and knowledge instead!"
                show perfectionism scared
                y "You better choose a topic you like and are good at, or else your research will be a colossal disaster!"
                show mc awk
                mc "That's true, but I think-"
                show perfectionism sigh
                y "Imagine spending all that time on something you hate, only to end up with a hot mess of a research paper!"
                show perfectionism attack
                y "Play it safe and avoid the horror of feeling like a TOTAL FAILURE!"
                $ c2 = "consider existing passion, skills, and knowledge"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "Do research on current trends and market demands!":
                play sound "audio/click.mp3"
                show perfectionism happy
                y "Let's jump on the bandwagon of current trends and market demands!"
                show mc awk
                mc "Huh? But why would I-"
                show perfectionism relief
                y "Because who needs originality when you can just follow the crowd, right?"
                show perfectionism sigh
                y "If you don't select a trendy topic, nobody will give a hoot about your research. It'll be as exciting as watching paint dry!"
                show perfectionism mad
                y "Let's make sure your research is relevant and useful to others, or else you'll end up with a research paper that collects dust!"
                show perfectionism attack
                y "You wouldn't want to DISAPPOINT EVERYONE, now would you?"
                $ c2 = "do research on current trends and market demands"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "Review the research topic guidelines!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Hold on tight! Review the research topic guidelines first!"
                show perfectionism scared
                y "You must follow every single rule and requirement with unwavering perfection!"
                show mc awk
                mc "Yeah, I know the guidelines are important but-"
                show perfectionism attack
                y "If you miss even a tiny detail, you will have a failed research, and your dreams will be shattered!"
                show perfectionism mad
                y "May I remind you, this is your last year! Your last year! No room for failure!"
                show perfectionism happy
                y "Nothing screams guaranteed success like a perfectly executed research project, right?"
                show perfectionism attack
                y "Review those guidelines with painstaking precision and make zero mistakes, or else you'll be DOOMED!"
                $ c2 = "review the research topic guidelines"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        show mc quiet
        mc "..."
        show mc awk
        mc "You really have a way of making everything look negative, you know?"
        show perfectionism mad
        if c2 == "consider existing passion, skills, and knowledge":
            y "What? I am just making sure your research will BE GOOD ENOUGH!"
        if c2 == "do research on current trends and market demands":
            y "What? I am just making sure your research won't DISAPPOINT!"
        if c2 == "review the research topic guidelines":
            y "What? I am just making sure your research execution will be FLAWLESS!"
        if c2 == "consider existing passion, skills, and knowledge":
            image bg j:
                "bgj.png"
            show bg j with dissolve
            show mc whatevah
            mc "Whatever."
            show mc normal
            show perfectionism scared
            mc "Anyway, I have multiple passions, skills, and knowledge in many areas."
            show mc happy
            mc "There's so much to choose from. So many good options."
            show mc think
            mc "Oh, maybe I'll choose \"Interactive Storytelling in Virtual Reality\"."
            show perfectionism sigh
            y "Well..."
            menu:
                "RESOURCES ISSUES!":
                    play sound "audio/click.mp3"
                    y "You might be passionate about storytelling and virtual reality (VR) technology but-"
                    show perfectionism mad
                    y "-virtual reality research is a wallet drainer!"
                    y "You'll need fancy equipment, funding, and technical know-how!"
                    y "You're on a student budget and your coding skills are limited to copy-pasting codes from websites."
                    show perfectionism sigh
                    y "It's a bit too hard of a challenge, isn't it?"
                    show perfectionism attack
                    y "You can't afford a topic with so much RESOURCES ISSUES!"
                    $ c3 = "resources issues"
                    $ currenthp -= 10 
                    show fonbge
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fonbge
                "BANDWAGON!":
                    play sound "audio/click.mp3"
                    y "You might be passionate about storytelling and virtual reality (VR) technology but-"
                    show perfectionism mad
                    y "-everyone and their grandma have already dived into this topic!"
                    show perfectionism scared
                    y "Doesn't it feel like you're just joining the bandwagon?"
                    show mc awk
                    mc "But I'm definitely not just joining the band-"
                    show perfectionism attack
                    y "I can already imagine your classmates and professors side-eyeing you!"
                    show perfectionism scared
                    y "It's like showing up to a party fashionably late and realizing that all the good snacks are gone."
                    show perfectionism attack
                    y "You don't want to be a BANDWAGON researcher, right? Don't pick that!"
                    $ c3 = "bandwagon"
                    $ currenthp -= 10 
                    show fodo
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fodo
                "THINGS WON'T GO SMOOTHLY!":
                    play sound "audio/click.mp3"
                    y "You might be passionate about storytelling and virtual reality (VR) technology but-"
                    show perfectionism scared
                    y "-research in VR often involves human participants, which means dealing with ethics and consent forms!"
                    show mc awk
                    mc "But I've been dealing with those since I-"
                    show perfectionism sigh
                    y "Wrangling participants can be like herding cats, and getting all those forms signed?"
                    y "It's like trying to teach a cat to sit on command. It's going to be soooo frustrating!"
                    show perfectionism attack
                    y "You'll have to deal with all these exhausting obstacles and THINGS WON'T GO SMOOTHLY if you choose that!"
                    $ c3 = "things won't go smoothly"
                    $ currenthp -= 10 
                    show fomm
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fomm
            image bg k:
                "bgk.png"
            show bg k with dissolve
            show mc angry
            mc "Ugh, fine. I'll look for other topics."
            show mc think
            show perfectionism scared
            mc "Oh, how about \"Audio Processing Techniques for Music Production\"."
            show perfectionism attack
            y "Eeeeek..."
            menu:
                "THERE ARE BETTER TOPICS OUT THERE!":
                    play sound "audio/click.mp3"
                    show perfectionism scared
                    y "I know you are skilled in audio processing and music production but-"
                    show perfectionism mad
                    y "-research in audio processing often involves complex algorithms and fancy software!"
                    show perfectionism sigh
                    y "It's like trying to decipher ancient hieroglyphics without a Rosetta Stone."
                    show perfectionism scared
                    y "Unless you have access to top-notch resources and expertise,-"
                    y "-you might feel like you're playing air guitar instead of making groundbreaking discoveries."
                    show perfectionism attack
                    y "Listen, THERE ARE BETTER research TOPICS OUT THERE!"
                    $ c4 = "there are better topics out there"
                    $ currenthp -= 10 
                    show fonbge
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fonbge
                "COME UP WITH SOMETHING NEW!":
                    play sound "audio/click.mp3"
                    show perfectionism sigh
                    y "I know you are skilled in audio processing and music production but-"
                    show perfectionism scared
                    y "-audio processing techniques have been around for quite a while now."
                    show mc awk
                    mc "Yeah I know, but it would be interesting if I-"
                    show perfectionism happy
                    y "Your research should have a fresh twist, like inventing the next viral dance move that'll make everyone go wild."
                    show perfectionism mad
                    y "This topic is like trying to bring back the Macarena as the latest dance craze."
                    show perfectionism sigh
                    y "Sure, it was a hit in the '90s, but now? Not so much."
                    show perfectionism attack
                    y "The point is you need to COME UP WITH SOMETHING NEW or else its just going to be disappointing!"
                    $ c4 = "come up with something new"
                    $ currenthp -= 10 
                    show fodo
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fodo
                "AVOID SUBJECTIVITY!":
                    play sound "audio/click.mp3"
                    show perfectionism sigh
                    y "I know you are skilled in audio processing and music production but-"
                    show perfectionism scared
                    y "-research in music production often relies on subjective preferences and artistic interpretations."
                    show mc awk
                    mc "Yeah, but what's wrong with subject-"
                    show perfectionism sigh
                    y "It's like trying to convince your friends that your favorite band is the best when they're hardcore fans of polka."
                    show perfectionism mad
                    y "The subjectivity will make it so challenging to draw concrete conclusions and-"
                    y "-you will be stuck in a never-ending debate!"
                    show perfectionism sigh
                    y "For your research paper to be perfect, you need clear-cut answers, not endless musical disagreements."
                    show perfectionism attack
                    y "AVOID SUBJECTIVITY at all costs!"
                    $ c4 = "avoid subjectivity"
                    $ currenthp -= 10 
                    show fomm
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fomm
            image bg l:
                "bgl.png"
            show bg l with dissolve
            show mc angry
            mc "Okay, okay! Just shut up! So annoying."  
            show perfectionism scared
            show mc think
            mc "Anyway, I'll just settle for \"User Experience Design for Mobile Games\"."
            show mc awk
            mc "Don't tell me you still got something to say about th-"
            show perfectionism talk
            y "Uhhhh..."
            menu:
                "ENDLESS LOOP!":
                    play sound "audio/click.mp3"
                    show perfectionism scared
                    y "You do have the knowledge and experience in UX Design and Mobile Games but..."
                    y "-user experience design is all about iteration—gather feedback, make improvements, repeat."
                    show perfectionism mad
                    y "It's like being trapped in a game where you keep collecting coins, but you never reach the end!"
                    show perfectionism sigh
                    y "It would be sooo frustrating, right?"
                    show mc awk
                    mc "I think I can handle-"
                    show perfectionism attack
                    y "Choose this topic and your research will never escape this ENDLESS LOOP of improvement!"
                    $ c5 = "endless loop"
                    $ currenthp -= 10 
                    show fonbge
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fonbge
                "SUBJECTIVITY IS BAD!":
                    play sound "audio/click.mp3"
                    if c4 == "avoid subjectivity":
                        show perfectionism mad
                        y "Again! With the subjectivity! Are you listening to me?"
                    show perfectionism talk
                    y "You do have the knowledge and experience in UX Design and Mobile Games but..."
                    show perfectionism mad
                    y "-user experience is as subjective as choosing pizza toppings!"
                    show mc awk
                    mc "I don't see a problem with subjective-"
                    show perfectionism look
                    y "Some players love pineapple on their pizza (weird, right?),-"
                    show perfectionism scared
                    y "-while others think it's an abomination."
                    show perfectionism mad
                    y "Designing a user experience that pleases everyone is like trying to convince a pineapple pizza hater to join a pineapple pizza fan club!"
                    show perfectionism sigh
                    y "You'll just end up disappointing so many people!"
                    show perfectionism attack
                    y "My point is don't pick that, SUBJECTIVITY IS always BAD!"
                    $ c5 = "subjectivity is bad"
                    $ currenthp -= 10 
                    show fodo
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fodo
                "TECHNOLOGICAL CONSTRAINTS!":  
                    play sound "audio/click.mp3"
                    y "You do have the knowledge and experience in UX Design and Mobile Games but..."
                    show perfectionism scared
                    y "-mobile games come with their own set of challenges—screen size limitations, device capabilities, and performance quirks."
                    show mc awk
                    mc "But I already done it before, so I think I can-"
                    show perfectionism sigh
                    y "It's like trying to build a skyscraper with popsicle sticks and duct tape."
                    show perfectionism mad
                    y "You'll be constantly teetering on the edge of mistakes,-"
                    y "-ending up with a glitchy mess instead of a polished game experience!"
                    show perfectionism look
                    y "Oops, game over!"
                    show perfectionism attack
                    y "My point is, don't pick that! There's just too much TECHNOLOGICAL CONSTRAINTS!"
                    $ c5 = "technological constraints"
                    $ currenthp -= 10 
                    show fomm
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fomm
        if c2 == "do research on current trends and market demands":
            image bg m:
                "bgm.png"
            show bg m with dissolve
            show mc whatevah
            mc "Whatever."
            show mc happy
            show perfectionism scared
            mc "Anyway, there's a lot of in-demand research topics right now."
            show mc think
            mc "\"Healthcare and Medical Applications\" is looking good. I might pick it up as my research topic."
            show perfectionism talk
            y "Ummm..."
            menu:
                "TOO COMPLEX!":
                    play sound "audio/click.mp3"
                    show perfectionism mad
                    y "Healthcare and medical applications involve complex systems and processes!"
                    y "The field encompasses various interdisciplinary areas such as medicine, biology, computer science, and data analysis."
                    show perfectionism sigh
                    y "Choosing Healthcare and Medical Applications as your research topic is like-"
                    y "-voluntarily stepping into a never-ending labyrinth of confusion and frustration!"
                    show perfectionism attack
                    y "Don't pick that! You are not capable enough, it's just TOO COMPLEX!"
                    $ c3 = "too complex"
                    $ currenthp -= 10 
                    show fonbge
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fonbge
                "AVOID EXACERBATING SOCIETAL DIVISIONS!":
                    play sound "audio/click.mp3"
                    show perfectionism mad
                    y "Research in healthcare and medical applications are prone to potential biases and inequalities!"
                    show perfectionism scared
                    y "There's a high chance the data you will use might disproportionately represent certain demographic groups-"
                    y "-and exclude marginalized populations, perpetuating healthcare disparities and worsening inequalities!"
                    show perfectionism sigh
                    y "I can't imagine how disappointing this will be if that happens so please!"
                    show perfectionism attack
                    y "Don't be an unwitting accomplice to an unfair system and AVOID EXACERBATING SOCIETAL DIVISIONS!"
                    $ c3 = "avoid exacerbating societal divisions"
                    $ currenthp -= 10 
                    show fodo
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fodo
                "TOO TIME-CONSUMING AND COSTLY!":
                    play sound "audio/click.mp3"
                    show perfectionism mad
                    y "Healthcare and medical applications are subject to stringent regulatory requirements!"
                    y "It's like being trapped in a bureaucratic nightmare where every step forward is met with three steps backward."
                    show perfectionism sigh
                    y "Do you really want to go through all the trouble of obtaining those approvals and certifications?"
                    show mc awk
                    mc "No, but I think you are overthink-"
                    show perfectionism mad
                    y "Instead of waiting for approvals that never seem to arrive, you could have spent your valuable time on something else."
                    show perfectionism attack
                    y "Don't pick this topic! It's TOO TIME-CONSUMING AND COSTLY!"
                    $ c3 = "too time-consuming and costly"
                    $ currenthp -= 10 
                    show fomm
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fomm
            image bg n:
                "bgn.png"
            show bg n with dissolve
            show mc angry
            mc "Ugh, fine. I'll look for other topics."
            show mc think
            show perfectionism scared
            mc "Oh, how about \"Privacy and Security in Multimedia\"."
            show perfectionism attack
            y "Eeeeek..."
            menu:
                "TOO TECHNICAL!":
                    play sound "audio/click.mp3"
                    show perfectionism scared
                    y "Privacy and security in multimedia involve various technical concepts,-"
                    y "-encryption algorithms, network protocols, and data protection mechanisms!"
                    show perfectionism mad
                    y "You'll be dealing with more acronyms than you can shake a USB stick at,-"
                    y "-spending more time scratching your head than actually making progress!"
                    show perfectionism attack
                    y "It's far TOO TECHNICAL, you won't be able to handle this one!"
                    $ c4 = "too technical"
                    $ currenthp -= 10 
                    show fonbge
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fonbge
                "DON'T TARNISH YOUR REPUTATION!":
                    play sound "audio/click.mp3"
                    show perfectionism scared
                    y "Researching privacy and security involves dealing with sensitive personal information, user data, and potentially harmful vulnerabilities."
                    show perfectionism mad
                    y "If you fail to follow ethical considerations properly, it can lead to unintended consequences or legal issues!"
                    show mc awk
                    mc "You have a point, but let's not overthink-"
                    y "This is no joke! One wrong move, and you could end up on the wrong side of the law,-"
                    y "-or have a horde of angry internet users chasing after you with virtual pitchforks!"
                    show perfectionism attack
                    y "Do you want to have a criminal record? Please DON'T TARNISH YOUR REPUTATION pursuing this topic!"
                    $ c4 = "don't tarnish your reputation"
                    $ currenthp -= 10 
                    show fodo
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fodo
                "IRREPARABLE DAMAGE!":
                    play sound "audio/click.mp3"
                    show perfectionism mad
                    y "Privacy and security are very delicate subjects, and the consequences of mistakes can be severe!"
                    y "One wrong move, and you might inadvertently compromise someone's personal information-"
                    y "-or leave a vulnerability wide open for malicious hackers!"
                    show perfectionism attack
                    y "So back out from this topic now before you commit a grave mistake and cause IRREPARABLE DAMAGE!"
                    $ c4 = "irreparable damage"
                    $ currenthp -= 10 
                    show fomm
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fomm
            image bg o:
                "bgo.png"
            show bg o with dissolve
            show mc angry
            mc "Okay, okay! Just shut up! So annoying."
            show mc think
            show perfectionism scared
            mc "I guess I'll just have to settle with \"Machine Learning and Artificial Intelligence\"."
            show mc awk
            mc "Don't tell me you still got something to say about th-"
            show perfectionism talk
            y "Hang on!"
            menu:
                "TOO MUCH DATA PROBLEMS!":
                    play sound "audio/click.mp3"
                    show perfectionism scared
                    y "You do know ML and AI systems heavily depend on very large amounts of high-quality data, right?"
                    show perfectionism sigh
                    y "It will be so demanding, difficult, expensive, and time-consuming obtaining all those data!"
                    show perfectionism scared
                    y "But limited data will lead to inaccurate and unreliable models."
                    show perfectionism sigh
                    y "There's no way you can finish your research without enough data."
                    show perfectionism attack
                    y "Don't pick this topic! There's TOO MUCH DATA PROBLEMS!"
                    $ c5 = "too much data problems"
                    $ currenthp -= 10 
                    show fonbge
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fonbge
                "DON'T PROMOTE JOB DISPLACEMENT!":
                    play sound "audio/click.mp3"
                    show perfectionism scared
                    y "You do know automation and AI-driven systems can potentially replace jobs,-"
                    y "-particularly those involving repetitive or manual tasks."
                    show perfectionism sigh
                    y "Are you trying to cause massive unemployment?"
                    y "Imagine how disappointed your professors and peers will be at your research topic."
                    show perfectionism attack
                    y "Don't choose this topic! DON'T PROMOTE JOB DISPLACEMENT!"
                    $ c5 = "don't promote job displacement"
                    $ currenthp -= 10 
                    show fodo
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fodo
                "TOO MUCH INNACURACIES!":
                    play sound "audio/click.mp3"
                    show perfectionism sigh
                    y "You do know ML and AI systems heavily depend on very large amounts of high-quality data, right?"
                    show perfectionism mad
                    y "You are not capable of amassing such amount and quality of data."
                    y "And if you lack the data, the AI models will be super faulty!"
                    show perfectionism sigh
                    y "Please pick anything other than this topic!"
                    show perfectionism scared
                    y "I can already picture too much errors, too much flaws,-"
                    show perfectionism attack
                    y "-TOO MUCH INNACURACIES with this as your research subject! Avoid it now while you can!"
                    $ c5 = "too much innacuracies"
                    $ currenthp -= 10 
                    show fomm
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fomm
        if c2 == "review the research topic guidelines":
            image bg p:
                "bgp.png"
            show bg p with dissolve
            show mc whatevah
            mc "Whatever. Anyway, these are the research topic guidelines."
            show mc think
            show perfectionism scared
            mc "\"Digital multimedia should be front and center in your project\"."
            mc "Oh, I see. Wait, what's digital multimedia again?"
            show mc look
            mc "I kinda forgot the basics since we tackled this subject in my first year."
            show perfectionism attack
            y "Waaaaaah!"
            menu:
                "YOU'RE NOT BEING A GOOD STUDENT!":
                    play sound "audio/click.mp3"
                    show perfectionism mad
                    y "How could you not know the basics!"
                    y "You're a multimedia student, you should know what digital multimedia is!"
                    show mc look
                    mc "Like I said, it's been a long time since-"
                    y "Go review and search about digital multimedia now!"
                    show perfectionism attack
                    y "Cause YOU'RE NOT BEING A GOOD STUDENT! You're being a failure! Dont be a failure!"
                    $ c3 = "you're not being a good student"
                    $ currenthp -= 10 
                    show fonbge
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fonbge
                "YOU'RE BEING A DISAPPOINTMENT!":
                    play sound "audio/click.mp3"
                    show perfectionism mad
                    y "How could you not know the basics!"
                    y "You're a multimedia student, you should know what digital multimedia is!"
                    show mc look
                    mc "Like I said, it's been a long time since-"
                    show perfectionism sigh
                    y "Imagine how disappointed your peers and professors or even your family would be if they know!"
                    show perfectionism attack
                    y "YOU'RE BEING A DISAPPOINTMENT! Quick! Research and review about digital multimedia now!"
                    $ c3 = "you're being a disappointment"
                    $ currenthp -= 10 
                    show fodo
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fodo
                "YOU'RE GOING TO MAKE SO MUCH MISTAKES!":
                    play sound "audio/click.mp3"
                    show perfectionism mad
                    y "How could you not know the basics!"
                    y "You're a multimedia student, you should know what digital multimedia is!"
                    show mc awk
                    mc "Like I said, it's been a long time since-"
                    y "Quick! Figure out what digital multimedia is!"
                    show perfectionism attack
                    y "Or else, YOU'RE GOING TO MAKE SO MUCH MISTAKES on your research!"
                    $ c3 = "you're going to make so much mistakes"
                    $ currenthp -= 10 
                    show fomm
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fomm
            image bg q:
                "bgq.png"
            show bg q with dissolve
            show mc angry
            mc "Ugh, fine. I'll review everything about digital multimedia."
            show perfectionism scared
            show mc think
            mc "..."
            mc "\"Your topic must interest you\"."
            show mc relief
            mc "Oh well, I'm interested in a lot of topics."
            show mc happy
            mc "I guess it would be fine to just pick a research topic that interest m-"
            show perfectionism mad
            y "Noooooooo!"
            menu:
                "PICK A TOPIC THAT'S EASY!":
                    play sound "audio/click.mp3"
                    y "Seriously?! Do you want to have a hard time for your last research?"
                    y "The research topic you should choose should be an easy one! Regardless if you like it or not."
                    show perfectionism attack
                    y "PICK A TOPIC THAT'S EASY instead! Else, you're just setting yourself up for failure!"
                    $ c4 = "pick a topic that's easy"
                    $ currenthp -= 10 
                    show fonbge
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fonbge
                "PICK A TOPIC THAT'S RELEVANT!":
                    play sound "audio/click.mp3"
                    y "Seriously?! Do you want to have a disappointing, useless work as your final research?"
                    y "The research topic you should choose should be something suitable and useful for today's age!"
                    show perfectionism attack
                    y "PICK A TOPIC THAT'S RELEVANT enough instead! Else, you're just disappointing everyone with a useless research!"
                    $ c4 = "pick a topic that's relevant"
                    $ currenthp -= 10 
                    show fodo
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fodo
                "STOP BEING TOO CAREFREE!":  
                    play sound "audio/click.mp3"
                    y "Seriously?! There are other criteria you need to follow for a good research topic other than \"this interest me\"!"
                    y "You can't just be picking anything you want."
                    y "Plus, finish reading the whole research topic guidelines first!"
                    y "Or else your research will be full of flaws, full of errors, full of mistakes!"
                    show perfectionism attack
                    y "So no, don't pick a topic yet until you find the perfect one! STOP BEING TOO CAREFREE!"
                    $ c4 = "stop being too carefree"
                    $ currenthp -= 10 
                    show fomm
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fomm
            image bg r:
                "bgr.png"
            show bg r with dissolve
            show mc angry
            mc "Okay, okay! Just shut up! So annoying."  
            show perfectionism scared
            show mc think
            mc "..."
            mc "\"Consider collaborating with others\"."
            mc "Oh, I didn't know I can collaborate with others."
            show mc happy
            mc "That's cool! Maybe I will collab-"
            show perfectionism mad
            y "Don't!"
            menu:
                "YOU WON'T BE ABLE TO CONTRIBUTE ENOUGH!":
                    play sound "audio/click.mp3"
                    y "Your classmates are too smart and you're not at their level!"
                    show mc awk
                    mc "I think you're overthinking too-"
                    show perfectionism sigh
                    y "They'll probably just carry the whole work of research for you."
                    show perfectionism attack
                    y "Have some shame and don't collaborate with others cause YOU just WON'T BE ABLE TO CONTRIBUTE ENOUGH!"
                    $ c5 = "you won't be able to contribute enough"
                    $ currenthp -= 10 
                    show fonbge
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fonbge
                "YOU'RE GOING TO BE SUCH A LET DOWN!":
                    play sound "audio/click.mp3"
                    y "Your classmates are too smart and you're not at their level!"
                    show mc awk
                    mc "I think you're overthinking too-"
                    y "They probably have high standards that you can't meet!"
                    show perfectionism sigh
                    y "Plus, they'll be expecting so much from you, but you can't offer much!"
                    show perfectionism attack
                    y "Don't collaborate with others! YOU'RE just GOING TO BE SUCH A LET DOWN!"
                    $ c5 = "you're going to be such a let down"
                    $ currenthp -= 10 
                    show fodo
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fodo
                "YOU'LL EMBARRASS YOURSELF!":
                    play sound "audio/click.mp3"
                    y "Your classmates are too smart and you're not at their level!"
                    show mc awk
                    mc "I think you're overthinking too-"
                    y "They'll be expecting only the most perfect contributions from you!"
                    show perfectionism sigh
                    y "And we both know you always make so much mistakes..."
                    show perfectionism attack
                    y "So don't collaborate with others! YOU'LL just EMBARRASS YOURSELF!"
                    $ c5 = "you'll embarrass yourself"
                    $ currenthp -= 10 
                    show fomm
                    show mc hurt
                    play sound "audio/punch.opus"
                    with vpunch
                    pause
                    hide fomm




























    stop music fadeout 2
    show mc quiet
    show perfectionism scared
    mc "..."

    mc "Why are you like this..." 
    mc "I'm so sick of this game." 
    
    mc "\"[c1]\""
    mc "\"[c2]\""
    mc "\"[c3]\""
    mc "\"[c4]\""
    mc "\"[c5]\""

    mc "I just want to decide and get started."
    mc "I just want to be free from all this...nitpicking and worrying."
    show perfectionism worry
    y "Hey...[mc!c]..."
    show perfectionism fine
    y "It'll be okay."
    y "As your loyal assistant, I'll always help ensure the quality of your work, and do my best to help you choose the right decision."
    show perfectionism okay
    y "I promise."
    play music "audio/funny.mp3" fadein 2 volume 0.3
    image bg s:
        "bgs.png"
    show bg s with dissolve
    show mc think
    mc "Last one. I already know I want to do \"something\" for my research project."
    mc "Something tangible, a multimedia product, a multimedia project."
    mc "I just gotta choose what it will be."
    show mc happy
    mc "Oh there's Website, Mobile Apps, Video Game..."
    show perfectionism normal
    y "About that, let's choose..."
    menu:
        "Website":
            play sound "audio/click.mp3"
            show perfectionism happy
            y "Webs-"
            $ c7 = 1
        "Mobile Apps":
            play sound "audio/click.mp3"
            show perfectionism happy
            y "Mobi-"
            $ c7 = 2
        "Video Game":
            play sound "audio/click.mp3"
            show perfectionism happy
            y "Vide-"
            $ c7 = 3
    stop music fadeout 2
    show mc angry
    mc "SCREW"
    mc "YOU."
    voice "audio/suspense.mp3"
    show perfectionism talk with ease
    voice sustain
    y "w"
    y "wha?"
    if c7 == 1:
        mc "I'll make a website for my research project, NOT because YOU want me to. But because I WANT TO."
    if c7 == 2:
        mc "I'll make a mobile app for my research project, NOT because YOU want me to. But because I WANT TO."
    if c7 == 3:
        mc "I'll make a video game for my research project, NOT because YOU want me to. But because I WANT TO."
    show mc mad
    mc "I'm going to decide what to do with my research."
    voice "audio/suspense.mp3"
    show mc angry
    mc "You're NOT in control of me."
    voice sustain
    image bg t:
        "bgt.png"
    show bg t with dissolve
    show mc mad
    mc "Now excuse me while I plan my schedule for completing my thesis."
    show perfectionism scared
    play music "audio/funny.mp3" fadein 2 volume 0.3
    y "..."
    y "..."
    y ".................."
    menu:
        "AHHHH IT'S NOT GOING TO BE GOOD ENOUGH":
            play sound "audio/click.mp3"
            show perfectionism attack
            y "AHHHH IT'S NOT GOING TO BE GOOD ENOUGH AAAAAAHHHHHHH!"
            $ c6 = 1
            $ currenthp = 0 
            show fonbge
            show mc hurt
            play sound "audio/punch.opus"
            with vpunch
            pause
            hide fonbge
        "AHHHH IT'S GOING TO BE DISAPPOINTING!":
            play sound "audio/click.mp3"
            show perfectionism attack
            y "AHHHH IT'S GOING TO BE DISAPPOINTING AAAAAAHHHHHHH!"
            $ c6 = 2
            $ currenthp = 0 
            show fodo
            show mc hurt
            play sound "audio/punch.opus"
            with vpunch
            pause
            hide fodo
        "AHHHH IT'S GOING TO BE FULL OF MISTAKES!":
            play sound "audio/click.mp3"
            show perfectionism attack
            y "AHHHH IT'S GOING TO BE FULL OF MISTAKES AAAAAAHHHHHHH!"
            $ c6 = 3
            $ currenthp = 0 
            show fomm
            show mc hurt
            play sound "audio/punch.opus"
            with vpunch
            pause
            hide fomm
    

    show perfectionism scared  
    voice "audio/win.mp3"
    "CONGRATULATIONS"
    voice sustain
    "YOU'VE SUCCESSFULLY PROTECTED [mc!u] FROM FAILURE!"
    if gender == "male":
        "WHY, LOOK HOW GRATEFUL HE IS!"
        "NOW THAT HIS ENERGY IS ZERO, YOU CAN DIRECTLY CONTROL HIS ACTIONS"
    if gender == "female":
        "WHY, LOOK HOW GRATEFUL SHE IS!"
        "NOW THAT HER ENERGY IS ZERO, YOU CAN DIRECTLY CONTROL HER ACTIONS"
    "PICK YOUR ENDING MOVE"
    if gender == "male":
        "FINISH HIM!"
    if gender == "female":
        "FINISH HER!"
    show bg z with dissolve
    menu:
        "Close your laptop and just play games instead!":
            play sound "audio/click.mp3"
            show perfectionism talk
            y "Your thesis is making you feel like a failure."
            show perfectionism sigh
            if c6 == 1:
                y "It might never become good enough."
                y "Why would you even bother trying?"
            if c6 == 2:
                y "You might be letting everyone down, including yourself, with this research."
                y "It's just going to be such a disappointment."
            if c6 == 3:
                y "You just wasted your time with all those thinking."
                y "You might never achieve a complete research now."
            show perfectionism scared
            y "Quick, engage in procrastination and use activities like playing games as a form of distraction!"
            show perfectionism talk
            y "Avoid your thesis! Delay it! Ignore it!"
            show perfectionism attack
            y "IGNORE IT IGNORE IT IGNORE IT IGNORE IT IGNORE IT IGNORE IT IGNORE IT IGNORE IT IGNORE IT IGNO--"
            $ act1_ending="play"
        "Curl up in a ball and cry!":
            play sound "audio/click.mp3"
            show perfectionism talk
            y "Your thesis is making you feel like a failure."
            show perfectionism sigh
            y "You can't even make progress on this research."
            if c6 == 1:
                y "It might never become good enough."
                y "Why would you even bother trying?"
            if c6 == 2:
                y "You might be letting everyone down, including yourself, with this research."
                y "It's just going to be such a disappointment."
            if c6 == 3:
                y "You just wasted your time with all those thinking."
                y "You might never achieve a complete research now."
            show perfectionism scared
            y "Quick! Do like the armadillo! Curl up into a ball and cry!"
            show perfectionism attack
            y "CURL UP AND CRY CURL UP AND CRY CURL UP AND CRY CURL UP AND CRY CURL UP AND CRY CURL UP AND CR--"
            $ act1_ending="cry"
    stop music fadeout 2
    hide screen hpbar
    hide screen hpbg
    hide screen hpbge
    hide screen hpbarenemy
    if act1_ending == "play":
        play music "audio/fail.mp3" noloop
    if act1_ending == "cry":   
        play music "audio/sad.mp3" 
    image act1_ending:
        "[act1_ending].png"
    scene act1_ending with fade
    pause
    jump act2


