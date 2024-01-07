label act2:
    if act1_ending == "cry":   
        stop music fadeout 2 
    scene black with fade
    with Pause(1)
    show text "{size=100}Chapter 2" with dissolve
    pause
    hide text with dissolve
    with Pause(1)
    "Long story short, months have passed since the \"incident\"."
    "[mc!c]'s motivation to work on the research decreased."
    "The deadline for the research project draws near."
    if act1_ending=="cry":
        "However, [mc!c]'s crying session had been a daily sight."
    if act1_ending=="play":
        "However, [mc!c]'s gaming session had been a daily sight."
    if gender == "male":
        "But you're here to bring him back on track!"
        "His journey to graduating college is in your hands..."
    if gender == "female":
        "But you're here to bring her back on track!"
        "Her journey to graduating college is in your hands..."
    scene your_image 
    play music "audio/illurock.opus" fadein 2 volume 0.3
    show mc normal at left
    show mom at right:
        xzoom -1.0
    with fade
    m "Hey [mc!c], you've been stuck inside your room for months now."
    if gender == "male":
        m "Go outside and hang out with your friends sometimes, son."
    if gender == "female":
        m "Go outside and hang out with your friends sometimes, my darling."
    m "You're becoming such a shut-in, studying is important but take care of yourself and have some fun too okay?"
    m "I'll be leaving for work now, don't forget to eat."
    hide mom with dissolve
    mc "Okay mom, have a safe trip."
    voice "audio/suspense.mp3"
    stop music fadeout 2
    show perfectionism scared at right:
        xzoom -1.0

    with fade
    pause
    voice sustain
    play music "audio/funny.mp3" fadein 2 volume 0.3
    y "Is your mom serious? Hang out with friends? You barely got any progress on your research and other school requirements."
    show mc awk
    mc "I think she has a point though, I've been focusing too much on-"
    show perfectionism mad
    if act1_ending=="cry":
        y "Do you want to fail? You waste so much time crying everyday already!"
    if act1_ending=="play":
        y "Do you want to fail? You waste so much time playing games everyday already!"
    y "Now you want to go hangout when you could be using your time to be more productive instead?!"
    show mc angry
    mc "Alright, alright! I'll be more productive now! Gosh."
    ""
    window hide
    scene bg z
    show mc angry at left 
    show perfectionism mad at right:
        xzoom -1.0
    $ currenthp = 100
    show screen hpbar 
    show screen hpbg
    show screen hpbarenemy
    show screen hpbge
    with fade
    if gender == "male":
        "[mc!c] opened his laptop, and started working on his research project."
        "Again, it's up to you to help him make the perfect research project!"
        "GOOD LUCK!"
        "ROUND TWO: {i}FIGHT!"
    if gender == "female":
        "[mc!c] opened her laptop, and started working on her research project."
        "Again, it's up to you to help her make the perfect research project!"
        "GOOD LUCK!"
        "ROUND TWO: {i}FIGHT!"
    

    if c7 == 1:
        image bg u:
            "bgu.png"
        show bg u with dissolve
        show mc mad
        show perfectionism scared
        mc "*working diligently on the website*" 
        show mc think
        mc "Alright, I think the layout is looking good so far."
        show perfectionism talk
        y "Ummm, that color scheme!"
        menu:
            "You chose the black and white color scheme? Really?":
                play sound "audio/click.mp3"
                y "You chose the black and white color scheme? Really?"
                show perfectionism sigh
                y "That's so boring and uninspired. It's just another way of hiding your lack of creativity."
                show perfectionism attack
                y "Your work won't be good enough if you keep playing it safe like this!"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "You know everyone is going to judge your website design, right?":
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "You know everyone is going to judge your website design, right?"
                y "And now you've gone with black and white? That's hardly going to impress anyone."
                show perfectionism mad
                y "You should have taken more risks and chosen a more vibrant color scheme."
                show perfectionism attack
                y" People are going to be so disappointed in you!"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "What if you've made a mistake in your choice?":
                play sound "audio/click.mp3"
                show perfectionism scared
                y "What if you've made a mistake in your choice?"
                show perfectionism sigh
                y "Black and white? Seriously?"
                show perfectionism talk
                y "What if it's too plain or too harsh on the eyes?"
                show perfectionism mad
                y "You should have spent more time researching and experimenting with different colors."
                show perfectionism sigh
                y "This is just another example of your incompetence and lack of attention to detail."
                show perfectionism attack
                y "Fix the color scheme now!"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        show mc quiet
        mc "*ignores*"
        show perfectionism scared
        y "...."
        show perfectionism talk
        y "Can you hear me?"
        mc "*ignores*"
        y "Wait, I'm serious!"
        show perfectionism scared
        y "There are more imperfections in your work right now!"
        show perfectionism talk
        y "Ummm...that font choice!"
        menu:
            "Comic Sans? Seriously?":
                play sound "audio/click.mp3"
                show perfectionism scared
                y "Comic Sans? Seriously?"
                show perfectionism sigh
                y "That's such an unprofessional choice."
                y "Everyone will think you're not taking your work seriously."
                show perfectionism attack
                y "That font choice is not good enough for your project!"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "Are you trying to disappoint your professors and peers?":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Are you trying to disappoint your professors and peers?"
                y "Using Comic Sans? They expect professionalism and sophistication, not childish fonts."
                show perfectionism attack
                y "You'll let everyone down if you go ahead with this!"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "Choosing a font like that is a big mistake!": 
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Choosing a font like that is a big mistake!"
                show perfectionism scared
                y "Comic Sans? You must be joking, right?"
                show perfectionism sigh
                y "You're just inviting ridicule and criticism from others."
                show perfectionism attack
                y "It will undermine all your hard work. You can't afford to make such errors!"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        show mc quiet
        mc "*ignores*"
        show perfectionism scared
        y "...."
        show perfectionism attack
        y "This is bad! Very bad!"
        show perfectionism mad
        y "You need to listen to me!"
        show perfectionism attack
        y "Your writing!"
        menu:
            "Look at these spelling and grammar mistakes!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Look at these spelling and grammar mistakes!"
                y "It's clear that you're not doing your best for this project."
                y "You could have used GrammarSpelling-ly!"
                show perfectionism sigh
                y "Why did you even bother doing all this? You're doing self-sabotage!"
                show perfectionism attack
                y "Fix everything now!"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "You've really done it this time!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "You've really done it this time!"
                y "Look at these embarrassing writing mistakes on the website!"
                y "You're going to disappoint everyone who believed in you!"
                show perfectionism sigh
                y "They trusted you to deliver a flawless project, but this will make them think you're not as competent as they thought."
                show perfectionism mad
                y "You're letting everyone down, and they'll lose faith in your abilities!"
                show perfectionism attack
                y "Fix everything now!"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "How could you let these mistakes slip through?":
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "How could you let these mistakes slip through?"
                y "Simple spelling and grammar mistakes?"
                show perfectionism mad
                y "You were so focused on making progress that you missed the obvious errors!"
                y "You're showing that you can't make a flawless work!"
                show perfectionism sigh
                y "I keep telling you to stop making mistakes but you end up making even more."
                y "You won't achieve perfection if you let this happen."
                show perfectionism attack
                y "Fix everything now!"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
    if c7 == 2:
        image bg v:
            "bgv.png"
        show bg v with dissolve
        show mc mad
        show perfectionism scared
        mc "*working diligently on the mobile app*" 
        show mc happy
        mc "Alright, I think it's done now."
        show perfectionism talk
        y "Ummm, that color scheme!"
        menu:
            "You chose the black and white color scheme? Really?":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "You chose the black and white color scheme? Really?"
                show perfectionism sigh
                y "That's so boring and uninspired. It's just another way of hiding your lack of creativity."
                show perfectionism attack
                y "Your work won't be good enough if you keep playing it safe like this!"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "You know everyone is going to judge your mobile app design, right?":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "You know everyone is going to judge your mobile app design, right?"
                y "And now you've gone with black and white? That's hardly going to impress anyone."
                show perfectionism sigh
                y "You should have taken more risks and chosen a more vibrant color scheme."
                show perfectionism attack
                y" People are going to be so disappointed in you!"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "What if you've made a mistake in your choice?":
                play sound "audio/click.mp3"
                show perfectionism worry
                y "What if you've made a mistake in your choice?"
                show perfectionism sigh
                y "Black and white? Seriously?"
                show perfectionism worry
                y "What if it's too plain or too harsh on the eyes?"
                show perfectionism sigh
                y "You should have spent more time researching and experimenting with different colors."
                y "This is just another example of your incompetence and lack of attention to detail."
                show perfectionism attack
                y "Fix the errors now!"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        show mc quiet
        mc "*ignores*"
        show perfectionism scared
        y "...."
        show perfectionism talk
        y "Can you hear me?"
        mc "*ignores*"
        show perfectionism attack
        y "Wait, I'm serious!"
        y "There are more imperfections in your work right now!"
        show perfectionism talk
        y "Ummm...that font choice!"
        menu:
            "Comic Sans? Seriously?":
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "Comic Sans? Seriously?"
                y "That's such an unprofessional choice."
                y "Everyone will think you're not taking your work seriously."
                show perfectionism attack
                y "That font choice is not good enough for your project!"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "Are you trying to disappoint your professors and peers?":
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "Are you trying to disappoint your professors and peers?"
                y "Using Comic Sans? They expect professionalism and sophistication, not childish fonts."
                show perfectionism attack
                y "You'll let everyone down if you go ahead with this!"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "Choosing a font like that is a big mistake!":
                play sound "audio/click.mp3"
                show perfectionism mad 
                y "Choosing a font like that is a big mistake!"
                y "Comic Sans? You must be joking, right?"
                show perfectionism sigh
                y "You're just inviting ridicule and criticism from others."
                show perfectionism attack
                y "It will undermine all your hard work. You can't afford to make such errors!"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        show mc quiet
        mc "*ignores*"
        show perfectionism scared
        y "...."
        show perfectionism attack
        y "This is bad! Very bad!"
        show perfectionism mad
        y "You need to listen to me!"
        show perfectionism talk
        y "Your app..."
        menu:
            "Lacks the necessary functionality and features!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Your app lacks the necessary functionality and features!"
                y "It's clear that you're not doing your best for this project."
                y "You could have used prototype software first!"
                show perfectionism sigh
                y "Why did you even bother doing all this? You're doing self-sabotage!"
                show perfectionism attack
                y "This mobile app is far from complete! Fix everything now!"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "Is just not impressive enough!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Your app is just not impressive enough!"
                y "If you release your research project app with this functionality and these features, you'll let everyone down."
                y "They had high hopes for your app, they'll be expecting something exceptional!"
                show perfectionism sigh
                y "You're going to lose their respect and let them down if you let it be like this."
                y "They put their trust in you, don't disappoint them!"
                show perfectionism attack
                y "Improve everything now!"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "Might have bugs and other issues!":
                play sound "audio/click.mp3"
                show perfectionism scared
                y "Your app might have bugs and other issues!"
                show perfectionism sigh
                y "Look at the functionality and features you've developed—it's full of potential flaws and errors."
                show perfectionism worry
                y "What if they notice and criticize your app?"
                show perfectionism sigh
                y "You'll be exposed as a failure who can't even get the basics right."
                show perfectionism talk
                y "You'll be ridiculed for your mistakes and lack of attention to detail."
                show perfectionism attack
                y "Quick! Fix the errors now!"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
    if c7 == 3:
        image bg w:
            "bgw.png"
        show bg w with dissolve
        show mc mad
        show perfectionism scared
        mc "*working diligently on the video game*" 
        show mc happy
        mc "Alright, I think it's all done now."
        show perfectionism talk
        y "Ummm, that art style!"
        menu:
            "Your art style is about as exciting as a potato!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Your art style is about as exciting as a potato!"
                show perfectionism sigh
                y "It's so bland that even a rock would have more personality."
                show perfectionism attack
                y "Good luck impressing anyone with your snooze-inducing creations!"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "Oh, the disappointment on their faces when they see your art style!":
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "Oh, the disappointment on their faces when they see your art style!"
                show perfectionism scared
                y "They'll raise their eyebrows so high, they'll get stuck in their hairline."
                show perfectionism attack
                y "Congrats, you're about to become the world's most effective face muscle workout!"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "Look at those wonky proportions!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Look at those wonky proportions!"
                show perfectionism sigh
                y "Your characters look like they were stretched and squished by a mischievous toddler."
                show perfectionism attack
                y "It's like you've discovered a whole new level of art fails. Bravo!"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        show mc quiet
        mc "*ignores*"
        show perfectionism scared
        y "...."
        show perfectionism talk
        y "Can you hear me?"
        mc "*ignores*"
        show perfectionism attack
        y "Wait, I'm serious!"
        show perfectionism scared
        y "There are more imperfections in your work right now!"
        show perfectionism talk
        y "Ummm...about UI and UX!"
        menu:
            "Your UI design is as captivating as a spreadsheet from the 1990s!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Your UI design is as captivating as a spreadsheet from the 1990s!"
                show perfectionism sigh
                y "Don't be surprised if players mistake your game for an office productivity tool."
                show perfectionism mad
                y "Look at those colors! It's like you picked them blindfolded from a box of crayons."
                show perfectionism sigh
                y "Your UX flow is a disaster waiting to happen. It's like navigating through a maze with no exit."
                show perfectionism attack
                y "Congratulations on creating the ultimate frustration simulator!"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "Your UI is like a puzzle from the seventh circle of hell!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Your UI is like a puzzle from the seventh circle of hell!"
                show perfectionism sigh
                y "It's as if you took inspiration from an ancient text called \"The Art of Disappointing User Experience\"."
                show perfectionism attack
                y "Players will be left scratching their heads, wondering how you could have overlooked such basic principles of user interface design!"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "Congratulations on creating the most error-prone UI known to humankind!": 
                play sound "audio/click.mp3"
                show perfectionism happy
                y "Congratulations on creating the most error-prone UI known to humankind!"
                show perfectionism mad
                y "Your buttons are so strategically placed that players will inadvertently activate the self-destruct sequence every time they try to save their progress!"
                show perfectionism sigh
                y "Buttons will magically transport them to the wrong screens, and your game will become a realm of glitchy nightmares."
                show perfectionism attack
                y "Get ready to be the subject of \"Top 10 UI Fail\" videos!"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
        show mc quiet
        mc "*ignores*"
        show perfectionism scared
        y "...."
        show perfectionism talk
        y "This is bad! Very bad!"
        show perfectionism mad
        y "You need to listen to me!"
        show perfectionism talk
        y "The game...!"
        menu:
            "Lacks polish!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "The game lacks polish!"
                y "The animations, sound effects, and overall presentation doesn't have good quality."
                y "The feedback and visual/audio cues are inadequate."
                y "Players need clear indicators and prompts to understand the game's mechanics and respond effectively."
                y "The mechanics lack depth."
                y "They feel shallow and don't offer enough strategic choices or opportunities for players to explore different playstyles."
                show perfectionism attack
                y "How can you say it's \"all done\" when it's LACKING so much!"
                $ currenthp -= 10 
                show fonbge
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fonbge
            "Leads to a frustrating experience!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "The game leads to a frustrating experience!"
                y "The controls are too complex and unintuitive. Players will struggle to grasp them."
                y "The progression system is poorly designed."
                y "It doesn't offer a sense of accomplishment or meaningful rewards, leaving players feeling unrewarded for their efforts."
                y "The game lacks balance."
                y "Certain mechanics or abilities may be overpowered or underwhelming, disrupting the overall gameplay experience."
                show perfectionism attack
                y "How can you say it's \"all done\" when the game experience is this FRUSTRATING!"
                $ currenthp -= 10 
                show fodo
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fodo
            "Difficulty curve is flawed!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "The game's difficulty curve is flawed!"
                y "It either ramps up too quickly, leaving players overwhelmed, or it remains stagnant, failing to offer a satisfying challenge."
                y "The pacing is off. The game doesn't provide a smooth and balanced progression, making it difficult for players to stay engaged."
                y "There are inconsistencies in the physics and collision detection, which can lead to frustrating and unfair situations for the players."
                show perfectionism attack
                y "How can you say it's \"all done\" when it's so FLAWED and there are so much inconsistencies and errors!"
                $ currenthp -= 10 
                show fomm
                show mc hurt
                play sound "audio/punch.opus"
                with vpunch
                pause
                hide fomm
    stop music fadeout 2
    voice "audio/suspense.mp3"
    play music "audio/conflict.mp3" fadein 2 volume 0.3
    show mc insane
    mc "FAAACK!"
    mc "FACKING FACK-FAKKITY FAAAAACK"
    voice sustain
    show perfectionism happy
    y "Yay, [mc!c]! I'm so happy you can hear me again!"
    show perfectionism fine
    y "Why were you ignoring me?"
    show mc angry
    show perfectionism scared
    mc "Holy hell, you absolute moron."
    show mc mad
    mc "You know that Native American story?"
    mc "There are two wolves inside you, one is hope, one is despair, which wolf wins? The one you feed."
    voice "audio/suspense.mp3"
    show mc angry
    mc "I was trying to starve you, you sadistic asshole!"
    voice sustain
    show mc mad
    mc "Screw it, I'll do positive affirmations instead."
    show mc relief
    mc "I am loved. I am good. I am smart. I am special."
    y "..."
    menu:
        "Golly, that's so narcissistic!":
            play sound "audio/click.mp3"
            show perfectionism talk
            y "Golly, that's so narcissistic!"
            show perfectionism sigh
            y "You need to humbly see your own flaws in order to grow as a person!"
            show perfectionism mad
            y "You can't spray air freshener over a moldy room! Covering up your flaws makes you worse in the long run."
            show perfectionism relief
            y "Thankfully, I, as your loyal assistant, can alert you to your flaws. And right now, it's-"
            show perfectionism attack
            y "EVERYTHING. EVERYTHING IS WRONG"
        "Y'know affirmations were disproven?":
            play sound "audio/click.mp3"
            show perfectionism talk
            y "Y'know affirmations were disproven?"
            y "In fact, they actually backfire for people with low self-esteem!"
            show perfectionism scared
            y "It was a well-designed study – randomized controlled trial, experimenter was blinded as to who was in which group."
            y "Results: if you already had low self-esteem, being asked to repeat affirmations makes you feel worse than if you'd said nothing at all!"
            y "Wood 2009, Psychological Science. Look it up on Google Scholar, [mc!c],"
            show perfectionism attack
            y "THEN STOP SPREADING UNSCIENTIFIC FAKE NEWS"
        "Omg don't credit random stories to indigenous folk!":
            play sound "audio/click.mp3"
            show perfectionism mad
            y "Omg don't credit random stories to indigenous folk!"
            y "Native Americans are actual people, not some \"noble savages\" you can namedrop to make your fortune-cookie advice more exotic."
            show perfectionism sigh
            y "You're reducing individual persons & complex cultures to a Hallmark card! That's \"benevolent racism\"!"
            show perfectionism attack
            y "STOP BEING RACIST YOU JERK"
    $ currenthp -= 10 
    show arrow1
    show mc hurt
    play sound "audio/punch.opus"
    with vpunch
    pause
    hide arrow1
    voice "audio/suspense.mp3"
    show mc insane
    show perfectionism scared
    mc "ASSDAMMIT"
    voice sustain
    show mc mad
    mc "You know what? You're irrational."
    mc "Everyone knows emotions are irrational! Especially fear!"
    show mc angry
    mc "You're a useless evolutionary leftover, like my appendix or wisdom teeth!"
    mc "Hell, this whole inner self-critic that only-I-can-see metaphor is stupid! You're just a bunch of neuro-chemicals in my head."
    voice "audio/suspense.mp3"
    mc "So why should I listen to a worthless, irrational, non-existent piece of shit like you?!"
    show perfectionism worry
    y "..."
    voice sustain
    menu:
        "Jeez, [mc!c]. That's really hurtful.":
            play sound "audio/click.mp3"
            show perfectionism worry
            y "Jeez, [mc!c]. That's really hurtful."
            show perfectionism sigh
            y "I'm part of you, you know. When you say that, you're hurting yourself."
            show perfectionism attack
            y "Why are you hitting yourself, [mc!c]? STOP HITTING YOURSELF."
        "I'm a feeling. Feelings are valid.":
            play sound "audio/click.mp3"
            show perfectionism worry
            y "I'm a feeling. Feelings are valid."
            show perfectionism scared
            y "Hang on... \"they\" say that feelings are valid, that you should always accept your emotions."
            show perfectionism talk
            y "But \"they\" also say emotions are irrational, that emotions are not to be trusted."
            show perfectionism mad
            y "Oh my gosh, \"they\" have been lying to us this whole time!"
            show perfectionism attack
            y "\"THEY\" FEED US CONTRADICTIONS TO MAKE US DEPENDENT ON THE SELF-HELP INDUSTRIAL COMPLEX"
        "[mc!c], we're both \"just chemicals.\"":
            play sound "audio/click.mp3"
            show perfectionism sigh
            y "[mc!c], we're both \"just chemicals.\""
            show perfectionism worry
            y "Your deepest motivations are dopamine, your richest joys are serotonin."
            y "Your memories are synaptic weights, your reason is fault-prone electrical signals."
            show perfectionism sigh
            y "So if me being \"just chemicals\" means I'm irrational... then that means you're irrational!"
            show perfectionism talk
            y "And if we're both irrational, then we'll never figure out how to be fulfilled and succeed!"
            show perfectionism attack
            y "AHHH WE'RE BROKEN! SO BROKEN SO BROKEN SO BROKEN--"
    $ currenthp -= 10 
    show arrow1
    show mc hurt
    play sound "audio/punch.opus"
    with vpunch
    pause
    hide arrow1
    show mc quiet
    show perfectionism scared
    mc "..."
    mc "I hate this. God it hurts so much I hate this."
    mc "I can't appease you. I can't ignore you. I can't fight you."
    mc "No matter what I do, I can't seem to get rid of yo--"
    show perfectionism mad
    y "Well maybe you're NOT SUPPOSED TO GET RID OF ME."
    show perfectionism sigh
    y "How do you think I feel, [mc!c]?!"
    y "I'm trying my best to be your assistant, but you keep seeing me as some Evil Bad Person!"
    show perfectionism talk
    y "So I try even harder to alert you to imperfections!"
    show perfectionism worry
    y "But no matter how hard I try to protect you from failing, you still think I'm your enemy!"
    y "What am I doing wrong?!"
    show perfectionism sigh
    y "I know I suck at my job. But I'm trying, [mc!c]!"
    show perfectionism sorry
    y "...I'm trying."
    y "You don't have to heed my warnings, or agree with me, or even like me."
    y "I just... all I want is for you to be patient with me."
    y "I just want for you to listen to me for a while and--"
    mc "I don't care."
    show mc mad
    mc "The deadline is in two days."
    show mc angry
    voice "audio/suspense.mp3"
    mc "I'm going to submit this project now."
    voice sustain
    show perfectionism talk
    y "[mc!c]! Wait!"
    menu:
        "Listen [mc!c], you could actually FAIL here!":
            play sound "audio/click.mp3"
            y "L--"
        "This is stupid and self-destructive!":
            play sound "audio/click.mp3"
            y "T--" 
        "You can ask for extension!":
            play sound "audio/click.mp3"
            y "Y--"
    image bg submit1:
        "bgsubmit1.png"
    show bg submit1 with dissolve
    $ enemy_hp -= 30 
    show arrow
    show perfectionism hurt
    play sound "audio/punch.opus"
    with vpunch
    pause
    hide arrow
    show mc quiet
    mc "You know, I might've believed you... if you hadn't tried that a zillion times before."
    show mc angry
    mc "You're the perfectionist who screamed non-existent imperfections."
    show perfectionism sorry
    y "[mc!c], please..."
    mc "Oh I'm sorry I don't meet everybody else's standards for what a good research project would be like."
    mc "Look asshole, we have a way of shutting you the fuck up."
    show mc mad
    mc "It is to not give a damn about what you have to say and just do what we want."
    y "..."
    menu:
        "You're upset and it's STILL NOT A COMPLETE PROJECT":
            play sound "audio/click.mp3"
            show perfectionism mad
            y "You're upset and it's STILL NOT A COMPLETE PROJECT"
            jump act3_bad_1_harm
        "Dang it, this is the thanks I get?!":
            play sound "audio/click.mp3"
            show perfectionism mad
            y "Dang it, this is the thanks I get?!"
            jump act3_bad_1_insult
        "Okay, I admit it. I messed up.": 
            play sound "audio/click.mp3"
            show perfectionism sorry
            y "Okay, I admit it. I messed up."
            jump act3_good_1
    
                

    label act3_bad_1_harm:
        y "Even if you submit this, it doesn't meet the requirements and you will just fail the subject!"
        show mc look
        mc "Eh."
        mc "Some professors are very lenient enough to let this pass."
        image bg submit2:
            "bgsubmit2.png"
        show bg submit2 with dissolve
        $ enemy_hp -= 30 
        show arrow
        show perfectionism hurt
        play sound "audio/punch.opus"
        with vpunch
        pause
        hide arrow
        jump act3_bad_2

    label act3_bad_1_insult:
        mc "I- Excuse me, the thanks?"
        y "This is exactly why I exist! Because humans can't be trusted to do their best!"
        y "I've been trying to protect you from failing all my life and now you're just going t--"
        image bg submit2:
            "bgsubmit2.png"
        show bg submit2 with dissolve
        $ enemy_hp -= 30 
        show arrow
        show perfectionism hurt
        play sound "audio/punch.opus"
        with vpunch
        pause
        hide arrow
        jump act3_bad_2

    label act3_good_1:
        show mc quiet
        mc "heh."
        show mc insane
        mc "hahahaha"
        mc "HAHAHAHAHAHA"
        show mc relief
        mc "Oh WOW is that the biggest fucking understatement of the century!"
        show mc angry
        mc "Yeah, you rotting pile of blood-coated shit! You messed the fuck up!"
        show mc mad
        mc "Any other remarks, Captain Obvious?"
        y "..."
        menu:
            "But revenge on me isn't the answer!":
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "But revenge on me isn't the answer!"
                jump act3_good_1_fail_revenge
                
            "But this time I'm actually right!": 
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "But this time I'm actually right!"
                jump act3_good_1_fail_harm
                
            "I've hurt you.":
                play sound "audio/click.mp3"
                show perfectionism sorry2
                y "I've hurt you."
                jump act3_good_2a
                
    label act3_good_1_fail_revenge:
        y "You need to have a healthier relationship with your emotions, rather than ignore them--"
        image bg submit2:
            "bgsubmit2.png"
        show bg submit2 with dissolve
        $ enemy_hp -= 30 
        show arrow
        show perfectionism hurt
        play sound "audio/punch.opus"
        with vpunch
        pause
        hide arrow
        jump act3_bad_2

    label act3_good_1_fail_harm:
        y "So please, calm yourself down and let's--"
        image bg submit2:
            "bgsubmit2.png"
        show bg submit2 with dissolve
        $ enemy_hp -= 30 
        show arrow
        show perfectionism hurt
        play sound "audio/punch.opus"
        with vpunch
        pause
        hide arrow
        jump act3_bad_2

    label act3_good_2a:
        show perfectionism sorry
        y "I was so obsessed with making sure everything is perfect, that I didn't realize I was hurting you."
        show mc quiet
        mc "NO. SHIT."
        show mc angry
        mc "GODDAMN. It really took you this long to finally figure it out?!"
        show mc mad
        mc "You could've saved us so much trouble, you dumbass. Why didn't you realize this sooner?..."
        $ apologized_for_hurt = True
        jump act3_good_2q

    label act3_bad_2:
        show perfectionism sorry
        y "please... don't..."
        show mc happy
        mc "Your energy bar's looking awfully low there, smart-ass."
        show mc mad
        mc "If I were you, I'd choose my next words very carefully."
        y "..."
        menu:
            "Fine. I'm done protecting you.":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "Fine. I'm done protecting you."
                jump act3_bad_2_jump
            "I was right all along.":
                play sound "audio/click.mp3"
                show perfectionism sigh
                y "I was right all along."
                jump act3_bad_2_right
            "I'm sorry.":
                play sound "audio/click.mp3"
                show perfectionism sorry
                y "I'm sorry."
                jump act3_good_2b

    label act3_bad_2_jump:
        y "So, go ahead and submit it. See what I care."
        show mc quiet
        mc "..."
        show mc happy
        mc "Okay then. Clicking submit now."
        show perfectionism attack
        y "WAIT NO THAT WAS REVERSE PSYCHOLOGY YOU WERE SUPPOSED TO DO THE OPPOSITE OF WHAT I SA--"
        image bg submit3:
            "bgsubmit3.png"
        show bg submit3 with dissolve
        $ enemy_hp -= 30 
        show arrow
        show perfectionism hurt
        play sound "audio/punch.opus"
        with vpunch
        pause
        hide arrow
        jump act3_bad_3

    label act3_bad_2_right:
        show perfectionism mad
        y "You are putting yourself at risk to fail."
        show perfectionism sigh
        y " So please, [mc!c]... why don't you believe me?!"
        show mc quiet
        mc "Because you never believed in me."
        image bg submit3:
            "bgsubmit3.png"
        show bg submit3 with dissolve
        $ enemy_hp -= 30 
        show arrow
        show perfectionism hurt
        play sound "audio/punch.opus"
        with vpunch
        pause
        hide arrow
        jump act3_bad_3

    label act3_bad_2_terrible:
        show perfectionism talk
        y "Other people actually patiently listens to their inner self-critic, to learn to work together,"
        show perfectionism sigh
        y "Rather than hate it for trying to protect them from failure! So why can't you jus--"
        show mc angry
        mc "Wrong fucking answer."
        image bg submit3:
            "bgsubmit3.png"
        show bg submit3 with dissolve
        $ enemy_hp -= 30 
        show arrow
        show perfectionism hurt
        play sound "audio/punch.opus"
        with vpunch
        pause
        hide arrow
        jump act3_bad_3

    label act3_bad_3:
        image bg submit4:
            "bgsubmit4.png"
        show bg submit4 with dissolve
        show mc quiet
        mc "The only thing to fear is fear itself."
        show mc happy
        mc "Don't worry, don't care! Just do what you want, get done with it and be happy!"
        show mc angry
        mc "All the wise folk of our time agree: negative emotions are bad!"
        mc "Duh! That's why they're called negative!"
        show perfectionism sorry2
        y "[mc!c]... please..."
        show mc quiet
        mc "A while back, I said: \"I just want to be free from all this nitpicking and worrying.\""
        mc "I got my wish. I no longer feel worried, or fear, or anxiety..."
        mc "I don't feel anything at all."
        image bg submit5:
            "bgsubmit5.png"
        show bg submit5 with dissolve
        $ enemy_hp = 0 
        show arrow
        show perfectionism hurt
        play sound "audio/punch.opus"
        with vpunch
        pause
        hide arrow
        $ a3_ending = "submit"
        jump act3_end


    label act3_good_2b:
        show mc quiet
        mc "...you're sorry."
        mc "..."
        mc " Sorry for what?"
        y "..."
        jump act3_good_2q

    label act3_good_2q:
        if apologized_for_hurt == True:
            jump act3_good_2q_already_apologized
        if apologized_for_hurt != True:
            jump act3_good_2q_not_already_apologized

    label act3_good_2q_already_apologized:
        menu:
            "I'm sorry I wasn't a good assistant.":
                play sound "audio/click.mp3"
                show perfectionism sorry
                y "I'm sorry I wasn't a good assistant."
                jump act3_good_3_protector
            "I'm sorry I didn't respect you.":
                play sound "audio/click.mp3"
                show perfectionism sorry
                y "I'm sorry I didn't respect you."
                jump act3_good_3_respect
            "I'm sorry.":
                play sound "audio/click.mp3"
                show perfectionism sorry
                y "I'm sorry."
                jump act3_good_4

    label act3_good_2q_not_already_apologized:
        menu:
            "I'm sorry you are a terrible person!":
                play sound "audio/click.mp3"
                show perfectionism mad
                y "I'm sorry you are a terrible person!"
                jump act3_bad_2_terrible
            "I'm sorry I didn't respect you.":
                play sound "audio/click.mp3"
                show perfectionism sorry
                y "I'm sorry I didn't respect you."
                jump act3_good_3_respect
            "I'm sorry I hurt you.":
                play sound "audio/click.mp3"
                show perfectionism sorry
                y "I'm sorry I hurt you."
                jump act3_good_3_hurt

    label act3_good_3_protector:
        show perfectionism sorry
        y "It's my duty to help you do your best, but I kept being paranoid."
        y "Shouting about not meeting impossible standards. Yelling so much."
        y "It only makes sense that you'd want to make me shut up."
        show perfectionism sorry2
        y "I'm sorry."
        jump act3_good_4

    label act3_good_3_respect:
        show perfectionism sorry
        y "I was supposed to be your loyal assistant, but I acted as if you were supposed to obey me."
        y "There's a difference between an assistant and a prison warden, and I crossed the line."
        show perfectionism sorry2
        y "I'm sorry."
        jump act3_good_4

    label act3_good_3_hurt:
        show perfectionism sorry2
        y "I was so obsessed with trying to make sure everything is perfect, I never stopped to realize I was hurting you."
        y "I was a bad assistant."
        show perfectionism sorry
        y "I'm sorry."
        jump act3_good_4

    label act3_good_4:
        stop music fadeout 2
        show mc quiet
        mc "..."
        show mc look
        mc "Yeah, well, this was a dumb idea anyway."
        show mc think
        mc "I only did this to mess you up, and, well, I messed you up."
        show mc happy
        mc "Let's just call this round a tie, okay?"
        show perfectionism worry
        y "..."
        show perfectionism okay
        y "Okay."
        show mc normal
        mc "Okay."
        voice "audio/win.mp3"
        "TIE"
        voice sustain
        $ a3_ending = "notsubmit"
        jump act3_end

    label act3_end:
        if a3_ending=="notsubmit":
            jump act3_walkaway
        if a3_ending=="submit":
            jump act3_jump

    label act3_walkaway:
        play music "audio/hopeful.mp3" 
        hide screen hpbar
        hide screen hpbg
        hide screen hpbge
        hide screen hpbarenemy
        scene your_image with fade
        show mc quiet at center with dissolve
        mc "I'm scared my research project isn't good enough, would be disappointing, and have many mistakes."
        show mc front
        mc "And that's okay!"
        mc "It's okay to be scared."
        mc "I'll talk to my professor and tell that my research project would be delayed."
        scene phone1 with fade
        pause
        scene phone2 with dissolve
        pause
        scene phone3 with dissolve
        pause
        scene phone4 with dissolve
        pause
        scene phone5 with dissolve
        pause
        image act2ending:
            "images/mc[gender]/notsubmit.png"
        scene act2ending with dissolve
        pause
        jump act4

    label act3_jump:
        stop music fadeout 2
        hide screen hpbar
        hide screen hpbg
        hide screen hpbge
        hide screen hpbarenemy
        show perfectionism no
        with dissolve
        y "no..."
        y "no no no"
        y "NO!"
        $ INJURED = True
        play music "audio/sad.mp3" 
        image failed1:
            "images/mc[gender]/failed.png"
        image failed2:
            "images/mc[gender]/failed2.png"
        scene black with fade
        "And so, [mc!c] received a failing grade for the final subject."
        scene failed1 with fade
        pause
        scene failed2 with dissolve
        pause
        scene failed3 with dissolve
        pause
        scene failed4 with dissolve
        pause
        scene failed5 with dissolve
        pause
        jump act4
