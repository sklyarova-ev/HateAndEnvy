# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define j = Character (None,kind=nvl)
define jo = Character (None,kind=adv)
define p = Character ('Paul', color="#484a6e")
define r = Character ('Ringo', color="#7d3472")
define g = Character ('George', color="#802222")
define e = Character ('???', color="#ffffff")
define john = Character ('John', color="#ffffff")
define c = Character ('Cynthia', color="#704709")
define y = Character ('Yoko', color="#14161c")


define audio.car="music/car.mp3"
define audio.dream="music/dream.mp3"
define audio.rg="music/rg.mp3"
define audio.people="music/people.mp3"
define audio.rest="music/rest.mp3"
define audio.birds="music/birds.mp3"
define audio.paulfirst="music/paulfirst.mp3"
define audio.start="music/start.mp3"
define audio.hotel="music/hotel.mp3"
define audio.door="music/door.mp3"
define audio.phone="music/phone.mp3"
define audio.pp="music/pp.mp3"
define audio.yoko="music/yoko.mp3"
define audio.door="sounds/door.mp3"
define audio.otk="music/otk.mp3"

init:
    $ left2 = Position (xalign=0.2, yalign=1.1)
    $ right2 = Position (xalign=0.8, yalign=1.1)


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label splashscreen:

    play music start
    scene black with dissolve
    scene start2 with fade
    pause 3
    scene black with dissolve
    scene start with fade
    pause 4
    scene black with dissolve
    stop music

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

    j "{cps=15}Without meaning"

    j "{cps=15}and without purpose"

    stop music

    nvl clear
    window hide

    scene black with dissolve
    scene bg sky
    with Dissolve(.25)

    play music birds

    pause 2

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

    pause 1

    jo "it doesn't matter,{w=2} the dialogue is predictable, unless it's a theatrical production of schizophrenics."

    jo "But sometimes, I doubt the adequacy of myself and the people around me."

    jo "I think I'm feeling a little worse today.{w=2} probably the sun baked."

    jo "I've been on my feet all day."

    jo "if only I could sit down somewhere..."

    scene bg sky1
    with Dissolve(.25)

    pause 2

    jo "It's the same thing every day. But in the morning, as usual, everything will be forgotten."

    jo "Sometimes it feels like everything around me is a dream"

    jo "But in fact everything is real."

    jo "I would like to take off, hear the sound of clouds and breathe fresh air through my nose."

    jo "I could have done it, but l would have had to get up and move"

    jo "lf they want to kill me, then let them do it now."

    jo "Why prolong the torture..."

    scene black with dissolve

    pause 1

    jo "I closed my eyes, expecting to be able to get some sleep."

    pause 2

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

    pause 2

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

    stop music
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
    pause 2

    jo "There was silence."

    pause 2

    jo "I didn't fully understand what he meant."

    pause 2

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

    hide paul with dissolve

    pause 1

    jo "Classic Paul invites me to such bollocks as this."

    jo "If no one has the strenght, then why arrange this celebration?"

    show bg sky evening
    with Dissolve(.25)

    pause 1

    jo "I'm wondering what it will look like."

    jo "Dozens of tired adults face in plates and with a full glass of wine in their hand..."

    jo "It sounds like a lot of fun."

    jo "But  first I'd like to go back to the apartment."

    scene black with dissolve

    pause 2

    show bg hotel hallway evening
    with Dissolve(.25)

    jo "In recent years, people have become obsessed with minimalism and cubism."

    jo "Artists, designers and architects."

    jo "Probably, there is a future behind it."

    jo "Stupid fashion, but I like it."

    jo "All this looks so simple and does not irritate the eyes."

    jo "But it is also unclear."

    scene black with dissolve
    play music door
    show bg hallway with dissolve
    play music hotel
 
    jo "And the apartmenta here look in contrast with the corridor." 

    jo "Damn,{w=1} why am I complaining?..."

    jo "I have to say thanks that they don't use a combination of gold and red velvet here."

    scene black with dissolve

    e "Good evening, John."

    john "Who's this?"

    show bg hallway with dissolve
    pause 2

    show cyn angry with dissolve

    c "It’s me. Cyn."

    jo "This woman knows how to scare people."

    john "Ah, crikey, Cyn, you made me jump."

    john " For a moment I thought you were a fan breaking in or a ghost."

    show cyn smile with dissolve

    jo "She giggled."

    john "Have you been hiding here or something?" 

    show cyn smile3 with dissolve

    c "I’ve just got out of the bathroom. Sorry, I didn’t mean to frighten you." 

    john " Well, long time no see, hon. When did you get here?" 

    show cyn smile with dissolve

    c "We arrived about two hours ago.{w=1} Julian and I."

    show cyn sad with dissolve 

    c "I hoped you'd be waiting for us."

    show cyn smile with dissolve

    c "Last time we talked over the phone, we agreed you would meet us today, I believe."

    john "I forgot."

    show cyn brush with dissolve

    c "Oh..."

    john "We talked about it like three days ago."

    john "You should’ve reminded me yesterday you were coming."

    show cyn smile2 with dissolve

    c "I want to."

    c "But your line was engaged since our last call"

    c "and the hotel staff who tried to deliver my message to you told me there was no reply as he knocked on your door yesterday evening."

    show cyn brush with dissolve

    c "Where were you?"

    john "Here. In my suite. Where else would I be?"

    c "I don’t know. Why didn’t you respond then? Were you OK?"

    john "I didn’t hear anybody knocking."

    john "Probably, I was just too busy restoring my strength after doing me best at my starring secondary role in the oncoming hit Beatles movie."

    pause 2

    show cyn smile2 with dissolve

    c "Oh, John, you aren’t taking acid again, are you?"

    john "Stop it, Cyn,{w=1} do me a favour."

    john "If I wanted to answer stupid questions, I’d hold a press conference."

    c "But still, are you?"

    john "You know I’m done with it."

    john "I spent the whole evening...{w=1} meditating"

    john "Yes."

    jo "I sighed."

    john "Just what Maharishi ordered on a hard day’s night, you know."

    john "Nothing interesting, anyway."

    john "You better tell me how were things at home."

    show cyn sad with dissolve 

    c "We were fine aside from we were missing you badly."

    c "Julian even draw a comic of you performing on stage with the band."

    c "He’s brought it here to show you."

    john "Where's him, by the way?"

    show cyn smile2 with dissolve

    c "He’s sleeping in the next room. The road wore him out."

    john "Don't you want to have some rest too?"

    john "There's another hour before dinner."

    show cyn smile3 with dissolve

    c "Maybe we'd better take a walk and you'd show me around?"

    jo "Shit..."

    john "Actually, I don't feel like going out at the moment"

    show cyn sad with dissolve 

    john "but you can go and ask Mal to keep you company."

    john "I’ve seen him hanging around in the lobby just now."

    c "But i wanted to do it with you..."

    john "And I don't want to."

    pause 2

    play music phone

    show cyn smile2 with dissolve

    pause 4

    c "Who is it?"

    john "Do you think I know?"

    pause 2

    c "I think It's you they're calling."

    jo "Obviously this is for me..."

    john "I'll take."

    hide cyntia
    play music pp
    scene black
 
    show bg phone with dissolve
    stop music 

    pause 1

    play music yoko

    john "Hello?"

    e "Hi, John?"

    john "Woman, who are you?"

    jo "I heard a soft laugh on the phone."

    john "Please, don't call me anymore."

    y "John, this is Yoko."

    jo "I'm surprised how she found out this phone number."

    jo "Only Cynthia and a couple of people from the recording studio knew this number."

    jo "It scared me and interested me..."

    y "Don't be scared."

    y "I didn't do anything to find out where you are now."

    jo "I still can't figure out how you find out about everything, crazy girl."

    y "Imagine."

    y "I'm sorry, am I distracting you? How's your family?"

    john "Cynthia arrived today."

    john "I didn't expect this, I thought she would arrive earlier."

    john "But then I completely forgot about it."

    john "Such a strange day."

    y "She couldn't call you?"

    john "No, you know, I am.."

    y "I have strange days too."

    y "Sometimes it seems that I still haven't woken up!"

    y "It happens when you sleep during the day, not at night."

    y "You get lost in space and time."

    john "Yes... It's a very strange feeling."

    pause 2

    y "But still, it seems to me that night is the best time for an art creator"

    y "Haven't you noticed that?"

    y "For example, I always start creating at night when I want to sleep."

    y "And these are always the best ideas."

    jo "She won't let me say a word..."

    john "I used to be able to come up with something with a sober head."

    john "But right now I'm not doing anything good."

    y "It's probably not safe to talk about such things on the phone to hotels."

    john "I don't think anyone can eavesdrop on us right now."

    jo "No one except Cyn of course..."

    john "Everyone is resting now."

    john "It is unlikely that some asshole is standing and listening to what John Lennon is talking about."

    y "Oh!{w=1} Have the Beatles finished shooting the movie?"

    john "Yes, we finished today."

    y "And what do you think about this?"

    y "Whose idea is this?"

    jo "It's going to be a long interview."

    john "It's our joint idea, but Paul, as always, puts more into it."

    john "You know, well,{w=1} let it be."

    scene black with dissolve
    show bg ceiling with dissolve

    pause 1

    jo "We talked for about an hour."

    jo "She talks so much."

    show bg ceiling blur with dissolve

    jo "Talks and talks..."

    show bg ceiling blur2 with dissolve

    jo "Talks and talks..."

    scene black with dissolve

    jo "I feel so bad today."

    jo "I almost fell asleep..."

    scene white with dissolve

    stop music

    c "John!"

    show bg hallway with dissolve

    show cyn brush with dissolve

    c "Are you all right?"

    play music otk

    jo "I hung up the phone with a grunt of displeasure."

    john "Yeah, I was just...{w=1} Thinking."

    show cyn angry with dissolve

    c "Seriously? And what are you up to?"

    john "I was thinking about how tomorrow I would go to London to the studio and then I would sleep for five years."

    show cyn angry2 with dissolve

    c "Don't relax!"

    c "Come on! Come on! Get ready, we're going!"

    john "Where?"

    show cyn smile3 with dissolve

    c "What do you mean where? To a restaurant to celebrate of couse."

    c "You're going, right?"

    john "I don't know, in fact I do not really want to go there.?"

    show cyn smile2 with dissolve

    c "Oh, why? I think it will be fun there."

    jo "I sighed massaging the bridge of my nose."

    john "No, Cyn. This is another bollocks."

    john "The guys just have nothing to do."

    show cyn sad with dissolve

    c "Are you sure you're not going?"

    john "Cyn..."

    menu:
        "go with Cyn":
            jump sogl

        "stay in hotel":
            jump otk

    return

label sogl:

    c "It wasn't hard to persuade you."

    jo "She giggled."

    return

label otk:

    john "I said I didn't want to. What's not clear here?"

    c "You know, I'll be uncomfortable there alone..."

    john "And then why did you come here at all?"

    show cyn cry with dissolve

    pause 1

    "You're cruel, John."

    pause 1

    stop music

    hide cyntia with dissolve
    play sound door
    scene black with dissolve

    show bg hallway with dissolve

    pause 2

    jo "damn."

    play music otk

    return

