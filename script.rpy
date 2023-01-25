# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define j = Character (None,kind=nvl)
define jo = Character (None,kind=adv)
define p = Character ('Paul', color="#484a6e")
define r = Character ('Ringo', color="#7d3472")
define g = Character ('George', color="#802222")
define e = Character ('???', color="#ffffff")
define john = Character ('John', color="#ffffff")

define audio.car="music/car.mp3"
define audio.dream="music/dream.mp3"
define audio.rg="music/rg.mp3"
define audio.people="music/people.mp3"
define audio.rest="music/rest.mp3"
define audio.birds="music/birds.mp3"
define audio.paulfirst="music/paulfirst.mp3"

init:
    $ left2 = Position (xalign=0.2, yalign=1.1)
    $ right2 = Position (xalign=0.8, yalign=1.1)


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label splashscreen:
    
    scene black with dissolve
    scene start2 
    with dissolve
    pause 5
    scene black with dissolve
    scene start 
    with dissolve
    pause 15
    scene black with dissolve

    return 

label start:

    scene bg room
    with Dissolve(.10)

    play music car
    
    window hide
    
    j "{cps=10}{i}September 24,1967.{/i}"
    

    j "{cps=25}The year preceding the release of the Magical Mystery Tour album promises to be stormy."

    j "{cps=25}No one was jumping around trying to boss us around anymore."

    j "{cps=25}The Beatles' use of psychedelics, such as LSD, reached it's peak that summer."

    j "{cps=25}And, according to author lan, this led us tp a lack of common sense in our recording,

     as we used randomess and sound effects, experiments."

    j "{cps=25}George Martin, our produser of the band, dicided to distance us from the work for a while,

    saying that most of the recording of the Magical Mystery Tour was \"disorganized chaos\"."

    j "{cps=25}Since touring is out of the question, we have freedom in the studio. Careful tuning of our songs."

    j "{cps=25}Magical Mystery Tour project is Paul's attempt to literally bring all our ideas to life."

    j "{cps=25}We half knew what we wanted and half didn't know until we tried everything."

    j "{cps=25}The only concrete thought that seemed to be in our head was to be different."

    j "{cps=25}The Beatles will drive around the British countruside eith their friends,

    shoot the result and turn it into a film over which we will have full creative control"

    stop music

    j "{cps=15}Without meaning"

    j "{cps=15}and without purpose"

    nvl clear
    window hide

    scene bg sky
    with Dissolve(.25)

    play music dream

    jo "We were waiting for good weather to continue shooting.{w=2} And finnaly the sun came out."

    jo "It's already 6 o'clock in the evening and it's shining like day."

    jo "Maybe it's a long day? The solstice maybe."

    jo "Although no, definitly not in September."

    jo "But maybe the sun also lives its own life."

    jo "Why does even this one have its own schedule?"

    jo "Nature has a schedule, animals and humans too."

    jo "In any case, we haven't taken a single break since we started working in the morning."

    jo "It seems I haven't gone that far,{w=2} but I don't know how much time has passed."

    jo "I wonder if the guys are looking for me?"

    jo "They probably didn't even notice it, but they were informed by the operators."

    jo "And then they'll say-"

    jo "What the hell, John, can you spare some time for work? Because you're not doing anything! We're actually tired too! blah-blah-blah"

    jo "Or Paul will say it..."

    jo "it doesn't matter,{w=2} the dialogue is predictable, unless it's a theatrical production of schizophrenics."

    jo "But sometimes, I doubt the adequacy of myself and the people around me."

    jo "I think I'm feeling a little worse today.{w=2} probably the sun baked."

    jo "I've been on my feet all day."

    jo "if only I could sit down somewhere..."

    scene bg sky1
    with Dissolve(.25)

    play music birds

    jo "It's the same thing every day. But in the morning, as usual, everything will be forgotten."

    jo "Sometimes it feels like everything around me is a dream"

    jo "But in fact everything is real."

    jo "I would like to take off, hear the sound of clouds and breathe fresh air through my nose."

    jo "I could have done it, but l would have had to get up and move"

    jo "lf they want to kill me, then let them do it now."

    jo "Why prolong the torture..."

    scene black with dissolve

    jo "I closed my eyes, expecting to be able to get some sleep."

    jo "I remember I had a classmate in elementary school"

    jo "who claimed that he could jump five meters and almost take off."

    jo "This man had a cheeky, glossy face with small piggy eyes swollen with fat."

    jo "A shrill, high-pitched voice and a lot of dandruff scattered over the shoulders of a dark blue striped suit."

    jo "His legs and arms were as short as two balloons."

    jo "If he knew and could feel how other children hate and curse,"

    jo "he should have drowned in this agonizing childish hatred."

    jo "To this day, when I remember him, my eyes darken and my heart aches."
  
    jo "Maybe he was lying to attract other guys to talk with him."

    jo "Maybe I used to be the same"

    jo "A disgusting snob..."

    jo "And then I heard a familiar voice from far away."

    scene bg eum
    show eum
    with Dissolve(.25)

    stop music

    e "hey!"

    e "heeey!"

    scene bg sky2 evening
    with Dissolve(.25)

    show ringo angry
    with Dissolve(.25)

    r "What the fuck, dude"

    r "What are you doing here?"

    jo "l forgot that dreams can become true."

    show ringo smile
    with Dissolve(.25)
    
    play music rg

    r "You're taking a break, right?"

    show ringo smile4
    with Dissolve(.25)

    r "ln any case, some have gone crazy, you know."

    show ringo smile2:
        xalign 0.8 yalign 1.1
    show geo smile:
        xalign 0.2 yalign 1.1
    with Dissolve(.25)

    g "But don't worry,"

    show geo smile1 at left2
    with Dissolve(.25)

    g "some didn't even notice."

    jo "ls that supposed to upset me or make me happy?"

    g "You wander around the neighborhood"

    show ringo smile at right2
    with Dissolve(.25)

    r "don't let other work"

    show ringo smile2
    with Dissolve(.25)

    show geo smile2
    with Dissolve(.25)

    g "and don't do anything!"

    jo "..."

    jo "they were not pursued by intelligent thoughts..."

    show john

    john "How can l interfere if l'm not doing anything?"

    show ringo smile
    show geo smile
    with Dissolve(.25)

    r "Hey, why so rude?"

    g "lt wasn't rude, it was aggressive."

    show ringo smile4
    show geo smile2

    r "lt wasn't aggressive, it was John."

    john "HA!"

    jo "l didn't want to offend them, so l made a sad face."

    show ringo angry

    r "C'mon, we're wasting time now too."

    r "l don't want to become like John!"

    show geo smile
    with Dissolve(.25)

    g "Do you stay up at night thinking about it?"

    r "Yes!"

    r "And sometimes l have nightmares..."

    show ringo smile
    with Dissolve(.25)

    r "Anyway, are you going to spend the night here?" 

    john "l'm going to live here."

    show geo smile1
    with Dissolve(.25)

    g "And you're going to sleep underground and piss in the bushes?"

    john "Yes, that's right where you're standing"

    "They were smilling their crazy smile"

    "What a pointless conversation"

    "But l laughed..."

    scene bg eum
    with Dissolve(.25)

    scene bg sky evening
    with Dissolve(.25)

    jo "Ha..."

    jo "Was l really dreaming..."

    jo "Nice guys"

    jo "With a heaviness in my legs and in my soul, i went back."

    jo "If it hadn't been for that scream, a peaceful evening would have ended in a quarrel today."

    jo "Eventually I had to show up and speak out." 

    jo "And any of my statements..."

    jo "My mind has always understood that the people close to me are very good and they are not at all to blame that they had to get to know me."

    jo "But, on the other way, I treated myself very well."

    jo "The conclusion comes by itself: incompatibility."

    jo "With the closest realtionship - a grandiose incompatibility!"

    scene bg eum
    with Dissolve(.25)

    scene bg town
    with Dissolve(.25)

    play music people

    jo "We walked for about 20 minutes"

    jo "I've already been pestered by Mal with stupid questions."

    jo "My legs hurt and my stomach is empty..."

    jo "I probably wouldn't have survived the war."

    jo "Maybe I should start doing morning runs."

    jo "Hah, if only I could wake up in the morning..."

    jo "But I have to brag to myself, today I almost arrived on time!"

    jo "Poor pepople getting up on time."

    jo "I hated it when my aunt Mimi woke me up in the morning."

    jo "I wanted to hit her and myself."

    jo "This is the same as going to the bathroom when a person is washing!"

    jo "Why the hell are you doing this?"

    jo "A hand touched my shoulder..."

    scene black with dissolve
   
    e "John!"

    scene bg town
    with Dissolve(.25)
    show paul smile
    with Dissolve(.25)

    p "And finally you're here!"

    play music paulfirst

    p "What you been doing?"

    jo "I'm confused, just not now, please..."

    john "I'm hungry and dizzy."

    show paul angry
    with Dissolve(.25)

    p "Really? Cynthia was a little worried, you know."

    jo "Paul looked upsed and I could feel his fears."

    show paul angry2
    with Dissolve(.25)

    p "I'm tired of other people's questions"

    p "Did I deserve it?"

    show paul smile3
    with Dissolve(.25)

    p "But anyway, we're done!{w=1} I'm so glad."

    show paul smileright
    with Dissolve(.25)
   
    p "But we'll have to go back to London tonight and work again tomorrow..."

    p "I'd be happy just to lie on the bed."

    john "I thought you'd never get tired."

    jo " He sighed and rolled his eyes when he realized with annoyance that he had to explain himself to me"

    john "But hey!{w=1} We finished it quickly!"

    john "It's only been a couple of weeks."

    john "I haven't even had time to get used to the terrain."

    p "Of course you didn't have time..."

    stop music
    pause 4

    jo "There was silence."

    pause 4

    jo "I didn't fully understand what he meant."

    pause 4

    play music paulfirst

    show paul smile
    with Dissolve(.25)

    p "Mel offered to celebrate this event in a restaurant."

    p "Nothing grandiose, just to sit quietly and talk."

    p "No one has the strength to have fun..."

    show paul smile3
    with Dissolve(.25)

    p "Rings said he would spend the whole evening on the floor with an ice pack on his forehead."

    p "But Geo will come. Strong guy."

    show paul brush4
    with Dissolve(.25)

    p "What about you?"

    show paul brush
    with Dissolve(.25)

    p "Of course I don't want to force you..."

    jo "I sighed"

    show paul brush4
    with Dissolve(.25)

    john "Okay...{w=1}It's all right.{w=1} I can't miss this opportunity."

    p "Well,{w=1} It's better for you."

    p "So, see you there!"


    return



