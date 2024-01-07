label act4:
    stop music fadeout 2
    scene black with fade
    with Pause(1)
    show text "{size=100}Chapter 3" with dissolve
    pause
    hide text with dissolve
    with Pause(1)
    scene your_image 
    play music "audio/hopeful.mp3" volume 0.5
    show mc normal at left
    show perfectionism normal at right:
        xzoom -1.0
    with fade
    show mc sigh
    mc "sigh"
    mc "So what the hell was the moral of this story?"
    if INJURED == True:
        mc "What did we even learn? I was being stupid, I failed a subject."
    if INJURED != True:
        mc "What did we even learn? I was being stupid, I almost failed a subject."
    show perfectionism look
    menu:
        "Yeah, not to mention the disappointment of those who were expecting you to graduate this year." if INJURED == True: 
            y "Yeah, not to mention the disappointment of those who were expecting you to graduate this year."
            jump act4a_bill
        "Yeah, not to mention all those wasted time." if INJURED != True:
            y "Yeah, not to mention all those wasted time."
            jump act4a_liver
        "Yeah, that was the worst-case scenario.":
            y "Yeah, that was the worst-case scenario."
            jump act4a_worst
        "Yeah, I was right.":
            y "Yeah, I was right."
            jump act4a_right

label act4a_bill:
    mc "Right. It was super embarrassing."
    show perfectionism happy
    y "And yet... we survived!"
    show mc think
    mc "?"
    jump act4b

label act4a_liver:
    show mc look
    mc "I'll definitely be the talk of the town for finishing my research late..."
    show perfectionism happy
    y "But at least you still have a chance of graduating! We survived!"
    show mc think
    mc "?"
    jump act4b

label act4a_worst:
    show perfectionism fine
    y "And yet..."
    show mc think
    mc "Hm?"
    show perfectionism happy
    y "We survived!"
    jump act4b

label act4a_right:
    show perfectionism okay
    y "But... you were right, too."
    show mc think
    mc "Hm?"
    show perfectionism sorry2
    y "I was the perfectionist who screamed false imperfections. So when actual non negotiable imperfections came about, you – justifiably – didn't believe me."
    show perfectionism happy
    y "However...we survived!"
    jump act4b

label act4b:
    show perfectionism happy
    y "Despite everything, we're still here."
    show mc awk
    if INJURED == True:
        mc "You seem pretty calm considering we definitely disappointed a lot of people and have been pushed back 1 year from \"life progress\"."
    if INJURED != True:
        mc "You seem pretty calm considering we almost lost our path in life."
    show perfectionism relief
    y "Well, it makes everything else less scary in comparison. It's also got me thinking."
    show perfectionism fine
    y "If me fighting you sucks, because it doesn't protect you..."
    show mc normal
    mc "And me fighting you also sucks, because it just makes you yell louder..."
    y "Then maybe..."
    mc "Maybe we don't have to fight."
    jump act4b_2

label act4b_2:
    show perfectionism sorry2
    y "I'm not a sadist, a bad person, or a negative voice/influence. But I'm not a loyal assistant either."
    show perfectionism okay
    y "I'm your personal alarm...about personal standards and perceived expectations of others on us."
    show perfectionism sigh
    y "We've been through rough stuff. Maybe trauma, neglect, verbal abuse or constant competition and comparison. That's why I sometimes over-react and go:"
    show perfectionism no
    y "AAAAAAAAHHHHHHH IT'S NOT PERFECT!"
    show perfectionism sigh
    y "But I don't want to be a broken alarm! I want to protect you from failing! I want to be a good and useful personal alarm!"
    show perfectionism okay
    y "[mc!c]... will you help fix this broken alarm?"
    show mc normal
    mc "I... I'll try."
    show mc happy
    mc "Okay. Healthy relationship with my emotions and my inner self-critic. Relationships need communication. So, let's communicate."
    show mc awk
    mc "The next five minutes are going to sound super cheesy, but let's fake it 'til we make it."
    show mc normal
    mc "Dear inner self-critic/voice/alarm/assistant... how are you feeling?"
    "WHAT FEAR DO YOU WANT TO TALK ABOUT FIRST? (YOU CAN DO THE OTHERS SHORTLY AFTER)"
    jump discuss

label discuss:
    menu:
        "I'm scared we're not good enough." if a4_talked_about_bad != True:
            show perfectionism sorry2
            y "I'm scared we're not good enough."
            jump act4_bad
        "I'm scared we'll disappoint others." if a4_talked_about_alone != True:
            show perfectionism sorry2
            y "I'm scared we'll disappoint others."
            jump act4_alone
        "I'm scared of mistakes." if a4_talked_about_harm != True:
            show perfectionism sorry2
            y "I'm scared of mistakes."
            jump act4_harm
        "Nah, I'm good for now." if act4_something_else == True:
            show perfectionism normal
            y "Nah, I'm good for now."
            jump act4c

label act4_harm:
    $ a4_talked_about_harm = True
    $ a4_fears_discussed +=1
    show perfectionism sigh
    y "I want to protect your self-esteem needs,"
    show perfectionism sorry
    y "But mistakes are so scary. It feels like one mistake will make us lose all our confidence and make us give up."
    y "We always take the safest route so I fear what would happen if we make a mistake."
    show perfectionism sorry2
    y "It could be an experience unknown to us, it could be a very negative consequence, it could be out of our comfort zone."
    y "I want you to be confident though, and not worry about making mistakes, but learn from them."
    show perfectionism worry
    if a4_fears_discussed==1:
        y "I dunno, enough of me choosing what to say next. What do you say, [mc!c]?"
        mc "..."
    if a4_fears_discussed==2:
        y "Again, back to you, [mc!c]. What do you think?"
        mc "..."
    if a4_fears_discussed==3:
        y "More thoughts, [mc!c]?"
        mc "..."
    menu:
        "You're right. So let's try our best to not make mistakes.":
            show mc normal
            mc "You're right. So let's try our best to not make mistakes."
            jump act4_harm_skills
        "Let's expose ourselves to more mistakes.":
            show mc normal
            mc "Let's expose ourselves to more mistakes."
            jump act4_harm_exposure
        "Thank you.":
            show mc normal
            mc "Thank you."
            $ thanks_for = "self-esteem needs"
            jump act4_thanks

label act4_harm_skills:
    show perfectionism sigh
    y "But... how? No one is perfect, and mistakes are inevitable."
    show mc think
    mc "We could learn ways that would lead to fewer mistakes and if mistakes does happen, we can reframe it into lessons."
    mc "Stop multitasking more than we can handle, eliminate distractions, using a tracker or checklist."
    mc "Reviewing our work carefully, clarifying and asking questions, taking a break to refresh."
    mc "Seek support, advice, and even critic from others. Stop procrastinating."
    mc "Improve our confidence and self-worth in general, so we don't worry so much about making mistakes."
    show perfectionism sorry
    y "But..."
    menu:
        "Where do we even start?":
            show perfectionism worry
            y "Where do we even start?"
            jump act4_harm_skills_start
        "What if they still don't work?":
            show perfectionism worry
            y "What if they still don't work?"
            jump act4_harm_skills_work
        "What if we go overboard on \"preventing mistakes\"?":
            show perfectionism worry
            y "What if we go overboard on \"preventing mistakes\"?"
            jump act4_harm_skills_overboard

label act4_harm_exposure:
    show perfectionism talk
    y "WHAT"
    show mc think
    show perfectionism worry
    mc "I mean, let's say a dog is scared of thunder."
    mc "One trick trainers use is to play a recording of thunder at a low volume, then give the dog a treat for staying calm."
    mc "Over several days, the trainer raises the volume bit by bit, until the dog has overcome their fear of thunder."
    show mc happy
    mc "It's called exposure therapy!"
    mc "Meaning, we can lose the fear of making mistakes by letting it happen."
    mc "All mammals have the same fight-or-flight response."
    show mc think
    mc "Since you're a part of me, a human, it should work for you too, right?" 
    y "..."
    menu:
        "What if we accept making mistakes too much?":
            show perfectionism sorry
            y "What if we accept making mistakes too much?"
            jump act4_harm_exposure_overboard
        "What if we've done a very terrible mistake?":
            show perfectionism sorry
            y "What if we've done a very terrible mistake?"
            jump act4_harm_exposure_hurt
        "I'm your assistant, not a dog.":
            show perfectionism sigh
            y "I'm your assistant, not a dog."
            jump act4_harm_exposure_dog

label act4_harm_skills_start:
    show perfectionism sigh
    y "There's so much to do, so much we need to fix about ourselves. What do we even begin with?"
    show mc normal
    mc "We're beginning right now."
    show perfectionism fine
    y "Eh?"
    show mc normal
    mc "We're practicing good communication right now. Which will help us prevent mistakes better, with fewer false positives,"
    show mc happy
    mc "And that will help protect us from the possible negative consequences and unknown experiences that are out of our comfort zone!"
    show mc normal
    mc "Therefore: this is progress in learning to prevent mistakes."
    show perfectionism okay
    y "Huh. I see."
    jump act4_something_else

label act4_harm_skills_work:
    show mc think
    mc "True, there's no way to 100 percent prevent ourselves from making mistakes..."
    show mc happy
    mc "But even a 1 percent improvement is still worth something, right?"
    show perfectionism fine
    y "You're seeing the glass as not 99 percent empty, but 1 percent full?"
    show mc normal
    mc "Which is still worth something if you're stranded in the desert."
    show perfectionism normal
    y "Well. Bottoms up, then."
    jump act4_something_else

label act4_harm_skills_overboard:
    show perfectionism sigh
    y "I mean, the whole reason you ignored my warnings was because I went overboard with protecting you from making mistakes!"
    show mc think
    mc "Naw, you're right. We would want to do it in moderation. Everything in moderation."
    show perfectionism fine
    y "Sorry, EVERYTHING in moderation?"
    show mc normal
    mc "A moderate number of things in moderation."
    show perfectionism relief
    y "Thank you for making your statements recursively self-consistent."
    jump act4_something_else

label act4_harm_exposure_overboard:
    show perfectionism sigh
    y "We just saw what happens if you shut down your standards – you put yourself in actually bad situations such as risking to fail."
    show perfectionism worry
    y "Besides, won't too much mistakes turn our lives into a mess?"
    show perfectionism sigh
    y "Soon we'll give ourselves treats while watching snuff murder porn!"
    show mc awk
    mc "I... think there's a line between that and the thunder."
    show perfectionism fine
    y "But exactly where, [mc!c]? Where?!"
    show mc happy
    mc "I don't know. But you can help me!"
    show mc normal
    mc "Working and negotiating with you, we'll draw that line."
    show perfectionism relief
    y "Okay then, the line's got to be perfect though."
    jump act4_something_else

label act4_harm_exposure_hurt:
    show perfectionism talk
    if INJURED == True:
        y "For example: we self-sabotage and intentionally fail a subject! "
    if INJURED != True:
        y "For example: we almost submitted an incomplete project and fail a subject!"
    show perfectionism worry
    show mc think
    mc "Nah you're right. One can go too far."
    show mc normal
    mc "But that's why, if we do exposure therapy, we'll start small, and make small steps upward."
    show mc awk
    mc "Just before we do a very terrible mistake, we stop."
    show perfectionism relief
    y "Yeah I draw the line between hearing loud thunder, and standing in a storm with a tall pointy hat."
    jump act4_something_else

label act4_harm_exposure_dog:
    show mc normal
    mc "And I'll show you kindness and patience 'til you're domesticated like a cute lil' puppy."
    show perfectionism scared
    y "..."
    show perfectionism okay
    y "D'aw."
    jump act4_something_else

label act4_thanks:
    $ num_thanks += 1
    if num_thanks == 1:
        jump act4_thanks_1
    if num_thanks == 2:
        jump act4_thanks_2
    if num_thanks == 3:
        jump act4_thanks_3

label act4_thanks_1:
    show perfectionism scared
    y "..."
    show perfectionism fine
    y "Wait, no arguments for or against what I'm feeling? Just... \"thank you\"?"
    show mc happy
    mc "Yeah! Thank you for showing your concern for my [thanks_for]."
    show perfectionism scared
    y "..."
    show mc awk
    mc "You okay?"
    show perfectionism okay
    y "You've never said thank you to me before."
    show mc awk
    mc "Aw you cuddly adorable person."
    jump act4_something_else

label act4_thanks_2:
    show mc normal
    mc "Even if you over-react, I appreciate you looking out for my [thanks_for]."
    show perfectionism fine
    y "Wait... you're not just repeating \"thank you\" to avoid actually talking about these fears, are you?"
    show mc sigh
    mc "Well, stuff's complicated, and I don't always have answers ready."
    show mc awk
    mc "It's not like life gives you a list of 3 pre-made dialogue responses."
    show mc normal
    mc "But for now, I can at least say thanks."
    show perfectionism okay
    y "Well, thank you too, for listening to me patiently."
    show perfectionism fine
    y "You hairless flesh-mammal."
    jump act4_something_else

label act4_thanks_3:
    show mc awk
    mc "Even if your yelling scares me, you're simply trying to protect my [thanks_for]."
    show perfectionism fine
    y "Okay, if you keep flattering me like this, the internet's gonna get some weird ideas about us."
    show mc relief
    mc "C'mon, we're just two college-age young adults that could pass off as twins. What's the worst that cou--"
    voice "audio/suspense.mp3"
    show image "twincest.jpg" at center:
        yalign 0.5
    pause
    hide image "twincest.jpg" 
    show mc quiet
    mc "Actually, do not answer that."
    voice sustain
    jump act4_something_else

label act4_alone:
    $ a4_talked_about_alone = True
    $ a4_fears_discussed += 1
    show perfectionism worry
    y "I want to make sure you fulfill that deep, human need to belong..."
    show perfectionism sorry2
    y "But I worry that if anyone ever knew how imperfect we are – the real us – we'll disappoint them all."
    show perfectionism worry
    y "Plus, I believe we are a reflection of the people closest to us."
    show perfectionism sorry2
    y "If we are a disappointment, we are tarnishing the names of our family, our friends, or even our school."
    show perfectionism worry
    if a4_fears_discussed==1:
        y "I dunno, enough of me choosing what to say next. What do you say, [mc!c]?"
        mc "..."
    if a4_fears_discussed==2:
        y "Again, back to you, [mc!c]. What do you think?"
        mc "..."
    if a4_fears_discussed==3:
        y "More thoughts, [mc!c]?"
        mc "..."
    menu:
        "I agree: let's work on upholding others' expectations of us.":
            show mc normal
            mc "I agree: let's work on upholding others' expectations of us."
            jump act4_alone_skills
        "I think people will still like us regardless. Let's find out?":
            show mc normal
            mc "I think people will still like us regardless. Let's find out?"
            jump act4_alone_experiment
        "Thank you.":
            $ thanks_for = "belonging needs"
            show mc normal
            mc "Thank you."
            jump act4_thanks

label act4_alone_skills:
    show mc think
    mc "Let's engage in open and honest conversations with people whose expectations we want to uphold."
    mc "Invest time and effort into understanding the expectations of others, by actively listening and observing."
    mc "So we can gain insights into their needs and values. This understanding will allow us to adjust our behavior and actions accordingly,-"
    mc "-showing our respect, consideration and love for them."
    mc "Clearly express our intentions, limitations, and boundaries, and ensure a mutual understanding with them."
    mc "We could also practice being open and vulnerable to them about our feelings or how we are doing, instead of appearing \"perfectly fine\" all the time."
    mc "As well as learn to get more comfortable with opposition, rejection and criticism."
    show mc awk
    mc "Also, don't forget to display kindness, politeness, humility, and proper etiquette in social interactions."
    show perfectionism okay
    y "That's a lot of options. But, about \"learning to uphold others' expectations\"..."
    menu:
        "Isn't that people-pleasing?":
            show perfectionism sorry
            y "Isn't that people-pleasing?"
            jump act4_alone_skills_manipulative
        "Won't that make us easier to control?":
            show perfectionism sorry
            y "Won't that make us easier to control?"
            jump act4_alone_skills_manipulated
        "What if we still fail and disappoint them?":
            show perfectionism sorry
            y "What if we still fail and disappoint them?"
            jump act4_alone_skills_fail

label act4_alone_skills_manipulative:
    show perfectionism sorry2
    y "I mean...we might be disregarding our own needs and desires in order to gain approval or avoid conflict."
    show mc normal
    mc "That's a valid question, and I understand where you're coming from."
    show mc think
    mc "Learning to meet others' expectations doesn't mean we have to give up our well-being or compromise our values, though."
    mc "We can actively listen and pay attention, understand what matters to them and make some adjustments if needed, but without sacrificing our own principles."
    show mc normal
    mc "The key is to approach our interactions with empathy and genuine care for others, while also valuing and respecting ourselves."
    mc "It's about finding a healthy balance and being true to ourselves while considering others' expectations and needs."
    show mc happy
    mc "By expressing our intentions and boundaries clearly, we can have meaningful and respectful relationships without becoming a people-pleaser."
    show perfectionism relief
    y "Thank you for clarifying that. You sound so educated on this stuff."
    show mc awk
    mc "Don't flatter me now."
    jump act4_something_else

label act4_alone_skills_manipulated:
    show perfectionism sigh
    y "We'll become a Welcome doormat, saying Please and Thank You as people wipe their feet on us!"
    show mc think
    mc "Nah, you're right. \"Upholding others' expectations\" can't be just about pleasing others, it's also got to be about setting boundaries."
    mc "We can't invite others into our home, if we have no walls to hold up our home."
    show mc normal
    mc "Let's also stay true to ourselves, to what we want and to what we value."
    jump act4_something_else

label act4_alone_skills_fail:
    show mc think
    mc "We might fail and disappoint them. Actually, we will fail and disappoint them."
    show mc happy
    mc "And that's fine! Failing is how anyone learns anything new at first!"
    mc "So let's fail forward together, yeah?"
    show perfectionism relief
    y "Sure, I guess... worst-case scenario, we can just skip town and get a new identity."
    show mc think
    mc "Yeah I think that only costs two bitcoins these days."
    jump act4_something_else

label act4_alone_experiment:
    show mc happy
    mc "We could try some experiments!"
    show mc think
    mc "We could open up to our friends, or open up to our family about our problems."
    show mc normal
    mc "I think we may find we're not as disappointing than we suspect."
    y "..."
    menu:
        "What if they don't understand?":
            show perfectionism sorry
            y "What if they don't understand?"
            jump act4_alone_experiment_cheap
        "What if this is a burden to them?":
            show perfectionism sorry
            y "What if this is a burden to them?"
            jump act4_alone_experiment_burden
        "But what about fulfilling our needs for competence and autonomy!":
            show perfectionism sigh
            y "But what about fulfilling our needs for competence and autonomy!"
            jump act4_alone_experiment_real_us

label act4_alone_experiment_cheap:
    show mc awk
    mc "Well, it's always a possibility, right? Not everyone will understand or relate to us."
    show mc happy
    mc "But hey, that's okay. People have different perspectives and experiences."
    show perfectionism sorry2
    y "Yeah, I get that. It's just scary to put ourselves out there and risk being judged or not understood."
    show mc think
    mc "Totally get it. Opening up is a personal choice, and it takes courage."
    show mc normal
    mc "We can start small with someone we trust, like a close friend or family member who has been supportive in the past."
    mc "And if they don't fully grasp what we're going through, they can still offer support and lend an ear."
    show perfectionism okay
    y "True. Sometimes, it's the support and empathy that matter the most, regardless of whether they fully comprehend our situation."
    mc "Precisely."
    jump act4_something_else

label act4_alone_experiment_burden:
    show mc think
    mc "Well, if it turns out we are being a burden..."
    show mc happy
    mc "That's good to know, too!"
    show mc normal
    mc "We can then learn how to pro-actively ask people what they're comfortable with, to know and respect others' boundaries."
    mc "Also, true friends and family are there to support us through thick and thin."
    mc "Sharing our problems can actually strengthen our relationships with them."
    show perfectionism worry
    y "I hope so. It's just hard to shake off the feeling of burdening them with our issues."
    show mc relief
    mc "I understand, but think about it this way: if the roles were reversed, wouldn't we want our loved ones to trust us enough to share their problems?"
    show perfectionism okay
    y "Yeah, I guess. We'd want to be there for them and help however we could."
    show mc happy
    mc "Exactly! Relationships are built on trust and mutual support. Sharing our struggles can bring us closer and allow them to be there for us."
    show perfectionism okay
    y "I suppose it's worth giving it a shot and seeing how they respond then."
    jump act4_something_else

label act4_alone_experiment_real_us:
    show perfectionism sorry2
    y "Plus, being vulnerable is scary. It's a leap of faith."
    show perfectionism worry
    y "If we try to be independent all the time, we'll never really connect and get support from anyone,"
    show perfectionism sigh
    y "But if we open up, other people will see all our messed-up insides!"
    show mc normal
    mc "Yeah, I get it. It's natural to want to feel capable and independent."
    show mc think
    mc "And you're right, being vulnerable can be scary. However, it's possible that we've been underestimating the people in our lives."
    mc "They might be more empathetic and caring than we give them credit for."
    show perfectionism sorry
    y "But..."
    show mc relief
    mc "Alright, maybe we're not yet secure enough or ready to be too vulnerable,"
    show mc normal
    mc "But one day, we can show people the real us – all messed-up, all human."
    show perfectionism okay
    y "Yeah, one day..."
    jump act4_something_else

label act4_bad:
    $ a4_talked_about_bad = True
    $ a4_fears_discussed += 1
    show perfectionism worry
    y "I want to defend your self-fulfillment needs, that drive to become a better person,"
    show perfectionism sorry
    y "But it just feels like deep down, we're such... a failure."
    show perfectionism sigh
    if INJURED == True:
        y "And don't tell me we're not, we already failed a subject."
    if INJURED != True:
        y "And don't tell me we're not, we couldn't finish the research project, wasted so much time, and delayed our graduation." 
    show perfectionism worry
    if a4_fears_discussed==1:
        y "I dunno, enough of me choosing what to say next. What do you say, [mc!c]?"
        mc "..."
    if a4_fears_discussed==2:
        y "Again, back to you, [mc!c]. What do you think?"
        mc "..."
    if a4_fears_discussed==3:
        y "More thoughts, [mc!c]?"
        mc "..."
    menu:
        "So we're a failure. Let's fix us.":
            show mc normal
            mc "So we're a failure. Let's fix us."
            jump act4_bad_fix
        "So we're a failure. Let's accept it.":
            show mc normal
            mc "So we're a failure. Let's accept it."
            jump act4_bad_accept
        "Thank you.":
            $ thanks_for = "self-fulfillment needs"
            show mc normal
            mc "Thank you."
            jump act4_thanks

label act4_bad_fix:
    show mc think
    mc "We could slowly build better habits, get our life more in line with what we value,"
    mc "And if needed, we could get professional help – a therapist or counsellor."
    show mc happy
    mc "There's ways to fix us."
    y "..."
    menu:
        "What if we can't fix it all?":
            show perfectionism worry
            y "What if we can't fix it all?"
            jump act4_bad_fix_cant
        "What if we fix too much?":
            show perfectionism worry
            y "What if we fix too much?"
            jump act4_bad_fix_too_much
        "We can't afford professional help.":
            show perfectionism worry
            y "We can't afford professional help."
            jump act4_bad_fix_afford

label act4_bad_fix_cant:
    show mc think
    mc "Nah, I guess you're right."
    mc "We can't fix it all."
    show perfectionism sigh
    y "Ahhh I knew it we'll always going to be a failure!"
    show mc normal
    mc "But we can at least fail less."
    mc "Scars heal with time, but they never go away. And that's okay."
    show perfectionism okay
    y "I guess. Besides,"
    show perfectionism relief
    y "Scars are sexy."
    show mc sigh
    mc "Please do not say that."
    jump act4_something_else

label act4_bad_fix_too_much:
    show perfectionism sorry2
    y "This feels sick to admit, but... some part of me wants to have this disorder."
    show perfectionism worry
    y "I mean, without it, won't we be boring?"
    show perfectionism fine
    y "Without the disorder, won't our art become stale and bland?"
    show perfectionism sigh
    y "Without the disorder, won't we be unable to attain academic success?"
    show perfectionism worry
    y "If we're ever content with life, won't we stop driving ourselves to do great things?"
    show mc think
    mc "..."
    mc "If we even fear... \"running out of fears to drive us to do better\"..."
    show mc relief
    mc "I don't think we're gonna stop \"striving to become better\" soon."
    show perfectionism relief
    y "Oh, yeah! Whew! What a relief!"
    jump act4_something_else

label act4_bad_fix_afford:
    show mc relief
    mc "That's a totally reasonable worry."
    show mc sigh
    mc "And it genuinely sucks that mental healthcare isn't affordable for lots of folks."
    show mc happy
    mc "Still, there are some cheap or free options:"
    show mc think
    mc "Support groups, online therapy, student/non-profit health centers..."
    mc "Building habits like meditation, sleeping well, taking breaks..."
    mc "Breaking tasks into manageable steps, embrace mistakes and failures..."
    mc "Practicing self-care and self-compassion, set realistic and attainable expectations..."
    show mc front
    mc "There's a full list of resources on the Internet about dealing with perfectionism."
    show perfectionism okay
    y "I see. It's a relief to know there are alternatives to mental healthcare."
    show perfectionism happy
    y "Nice fourth wall break, btw."
    jump act4_something_else

label act4_bad_accept:
    show mc think
    mc "I mean, that's what therapists say right? Accept all your emotions, even the negative ones like fear of failure?"
    show perfectionism scared
    voice "audio/suspense.mp3"
    y "Wait."
    voice sustain
    menu:
        "\"Accept\" as in give up?":
            show perfectionism talk
            y "\"Accept\" as in give up?"
            jump act4_bad_accept_give_up
        "\"Accept\" as in approve?":
            show perfectionism talk
            y "\"Accept\" as in approve?"
            jump act4_bad_accept_approve
        "\"Accept\" as in take literally?":
            show perfectionism talk
            y "\"Accept\" as in take literally?"
            jump act4_bad_accept_literally

label act4_bad_accept_give_up:
    show perfectionism sigh
    y "Do you think Martin Luther King would've said, \"Shucks we can't sit in the front of the bus, let's just accept it?\""
    show perfectionism sigh
    y "Why does the Self-Help Industrial Complex think waving the white flag is some profound wisdom?"
    show mc awk
    mc "I think therapists mean \"accept\" being a failure as in: acknowledging that failing is bound to happen and is hard to change,"
    show mc normal
    mc "But not necessarily giving up a commitment to succeed."
    show perfectionism sigh
    y "Then therapists should say acknowledge, not accept."
    show mc think
    mc "Yeah come to think of it, \"accept\" is kinda confusing."
    show perfectionism relief
    y "Well, I acknowledge that."
    jump act4_something_else

label act4_bad_accept_approve:
    show perfectionism talk
    y "Like it's good that we're a failure or something? No!"
    show mc awk
    mc "I think therapists mean \"accept\" being a failure as in: be patient with failing."
    show mc think
    mc "Like how struggling in quicksand makes you sink faster, and the solution is to patiently lie flat,"
    if INJURED == True:
        mc "Fighting against you, my perfectionism, led me to fail a subject."
    if INJURED != True: 
        mc "Fighting against you, my perfectionism, led me to procrastinate and not finish my research project."
    show mc normal
    mc "Instead, the solution is to do what we're doing now – not to fight, but to patiently be with each other."
    show perfectionism sigh
    y "Then they should say that instead of some problematic word like \"accept\"."
    show mc think
    mc "Yeah come to think of it, \"accept\" kind of sucks."
    y "I do not accept \"accept\"."
    jump act4_something_else

label act4_bad_accept_literally:
    show perfectionism talk
    y "But we already know you shouldn't take me literally!"
    show perfectionism sigh
    y "The whole problem is that I want to help you, but I suck at using words to do so!"
    show mc awk
    mc "I think therapists mean \"accept\" your fear of failure as in: \"don't fight or ignore them.\""
    show mc normal
    mc "To listen to you, work with you, but not take what you say as 100 percent literal truth."
    show perfectionism sigh
    y "Then therapists should say that instead of some vague confusing word like \"accept\"."
    show mc sigh
    mc "I guess they suck at using words, too."
    jump act4_something_else

label act4_something_else:
    $ act4_something_else = True
    if a4_fears_discussed==1:
        show mc normal
        mc "Anyway, anything else you wanna chat about?"
        y "..."
    if a4_fears_discussed==2: 
        show mc normal
        mc "So, anything else on your heavy heart?"
        y "..."
    if a4_fears_discussed==3:
        jump act4_something_else_2
    jump discuss
    
label act4_something_else_2:
    show mc relief
    mc "Okay, I think we've talked about all our fears now."
    show perfectionism look
    y "Yes, there are only three fears."
    show mc look
    mc "Yup, exactly three."
    y "Convenient."

label act4c:
    mc "..."
    y "..."
    show perfectionism sigh
    y "This isn't some game, you know."
    y "Building a healthy relationship with your emotions and inner self-critic isn't as simple as clicking buttons on a screen."
    show perfectionism worry
    y "Can we really get along?"
    y "Can we work together, as a team?"
    show mc normal
    mc "I think so."
    show perfectionism sorry2
    y "They say you should \"make peace\" with your emotions, as if your emotions are war criminals."
    show perfectionism fine
    y "But I want us to make more than mere peace! I want us to be allies!"
    show perfectionism okay
    y "I want to be a good alarm. Just like how hunger & thirst are alarms for your physical needs,"
    y "I want to be the alarm for your self-fulfillment, belonging, and self-esteem needs."
    show perfectionism sorry2
    y "But... I suck at my job, so I need you to help me."
    show perfectionism worry
    y "I'm not \"always valid,\" nor \"always irrational.\" I'm just... trying my best. So, please,"
    show perfectionism fine
    y "Help me help you!"
    show perfectionism worry
    y "Though, training a personal alarm will take a while. Maybe years."
    show perfectionism fine
    y "And sometimes I'll relapse, I'll slip into my old habits."
    show perfectionism sorry2
    y "I'll warn you about imperfections that don't matter. I'll scare you with words."
    show perfectionism sigh
    y "I'm sorry! I'm broken! I have few lose screws and need help sometimes!"
    show perfectionism worry
    y "But if you're patient with me... and just stay and listen to me..."
    show perfectionism okay
    y "Maybe you can make me a good loyal assistant."
    ""
    window hide
    menu:
        "Good assistant":
            mc "Good assistant"
            window hide
            show mc normal:
                xalign 0.5
            show perfectionism okay:
                xalign 0.7
            with ease
            hide perfectionism with dissolve
            show mc end
            with fade
            pause
            
        "Good [mc!c]":
            y "Good [mc!c]"
            show perfectionism okay
            window hide
            show mc normal:
                xalign 0.3
            show perfectionism okay:
                xalign 0.5
            with ease
            hide mc with dissolve
            show perfectionism end
            with fade
            pause
    jump credits