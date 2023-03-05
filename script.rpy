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
    
    j "{cps=10}{i} September 24, 1967 {/i}"
    

    j "{cps=25} The months leading up to the release of the Magical Mystery Tour record promise to be stormy."

    j "{cps=25} Brian is dead, so there's no one left to supervise us or boss us around."

    j "{cps=25} Since touring is out of the question, we have complete artistic freedom in the studio, where we can meticulously compose our songs."

    j "{cps=25} Our acid use reached its peak in the summer of 1967, and this led us to a lack of common sense in our music, 
    
    as we experimented a lot with random sound effects."

    j "{cps=25} George Martin, our record producer, decided to suspend us from work for a while,

    saying that most of the takes for the Magical Mystery Tour were \"disorganized chaos\"."

    j "{cps=25} So, we've moved on to film production."

    j "{cps=25} The Magical Mystery Tour project is Paul's attempt to bring all our ideas to life."

    j "{cps=25} We are only half aware of what we want, and the full picture won't emerge until we try everything."

    j "{cps=25} The only concrete thought we seem to have is to be different."

    j "{cps=25} According to the plan, the Beatles and friends are driving around the British countryside on a magical bus. 

    This wild ride is being shot and turned into a film under our full creative control"

    stop music

    j "{cps=15} Without meaning"

    j "{cps=15} and without purpose..."

    nvl clear
    window hide

    scene bg sky
    with Dissolve(.25)

    play music dream

    jo "We've been waiting for the skies to clear to continue filming. {w=2} And finally, the sun has come out."

    jo "It's already 6 p.m., but it's as light as day."

    jo "Maybe today's the longest day of the year? The solstice."

    jo "No, definitely not in September."

    jo "Maybe the sun simply decided to live its own life."

    jo "If you think about it, why is even the sun supposed to have a schedule?"

    jo "Nature has a schedule, and so do animals and humans."

    jo "In any case, we haven't taken a single break since we started working in the morning."

    jo "I don't think I've gone very far away from the set, {w=2} but I don't know how long I'm walking."

    jo "I wonder if the guys are looking for me."

    jo "They probably have not even noticed, unless the operators told them I've walked away."

    jo "If that's the case, then they'll say-"

    jo "What the hell, John? Could you take a little time to work? Because you're not doing anything! We're tired too! Blah-blah-blah."

    jo "Or it'll be Paul who says it..."

    jo "Actually, it doesn't matter who it'll be, {w=2} the phrases are the same anyway, unless it's a theatrical production of schizophrenics."

    jo "But sometimes I doubt the sanity of mine and others."

    jo "Damn, I'm feeling a little worse than usual today.{w=2} Probably, I've got a sunstroke."

    jo "Besides, I've been on my feet all day."

    jo "If only I could have a seat somewhere..."

    scene bg sky1
    with Dissolve(.25)

    play music birds

    jo "It's the same thing every day, but the next morning everything is always forgotten."

    jo "Sometimes I feel like it's all just a dream."

    jo "But, in fact, it's real."

    jo "I wish I could levitate myself and soar into the sky, hear the sound of clouds and breathe fresh air."

    jo "But even if I could, I don't think I would find the strength to get up and move at the moment."

    jo "And even if they come to kill me, so be it."

    jo "Why prolong this torture of existence..."

    scene black with dissolve

    jo "I close my eyes in the hope of taking a nap."

    jo "I think of the classmate I had in elementary school."

    jo "He claimed he could jump five meters and almost take off."

    jo "This kid had a cheeky glossy face swollen with fat. Small piggy eyes."

    jo "A shrill, high-pitched voice. A lot of dandruff scattered over his shoulders clad in a dark blue striped suit."

    jo "His legs and arms were as short as four balloons."

    jo "If only he had known how much the other children had hated and cursed him,"

    jo "He would have sunk into the ground under the pressure of this agonizing childish hatred."

    jo "To this day, whenever I think of him, my eyes get blurry with anger and my heart beats furiously."
  
    jo "His lies were probably aimed at becoming popular with the other guys."

    jo "Perhaps, I used to be just like him."

    jo "A disgusting egomaniac..."

    jo "Suddenly, I hear a familiar voice from afar."

    scene bg eum
    show eum
    with Dissolve(.25)

    stop music

    e "Hey!"

    e "Heeey!"

    scene bg sky2 evening
    with Dissolve(.25)

    show ringo angry
    with Dissolve(.25)

    r "What the fuck, mate?"

    r "What are you doing here?"

    jo "I forgot that dreams could become real."

    show ringo smile
    with Dissolve(.25)
    
    play music rg

    r "I see you're taking a break."

    show ringo smile4
    with Dissolve(.25)

    r "Someone has got mad about your absence, you know."

    show ringo smile2:
        xalign 0.8 yalign 1.1
    show geo smile:
        xalign 0.2 yalign 1.1
    with Dissolve(.25)

    g "But don't worry,"

    show geo smile1 at left2
    with Dissolve(.25)

    g "someone hasn't even noticed."

    jo "Is that supposed to upset me or make me happy?"

    g "You're wandering around the neighbourhood"

    show ringo smile at right2
    with Dissolve(.25)

    r "not letting the others work"

    show ringo smile2
    with Dissolve(.25)

    show geo smile2
    with Dissolve(.25)

    g "and not doing anything!"

    jo "..."

    jo "They are not followed by intelligent thoughts..."

    show john

    john "How can I interfere if I'm not doing anything?"

    show ringo smile
    show geo smile
    with Dissolve(.25)

    r "Hey, why so rude?"

    g "It's not rude, it's aggressive."

    show ringo smile4
    show geo smile2

    r "It's not aggressive, it's John."

    john "HA!"

    jo "I'm not in the mood for throwing any insults at them, so I've simply made an annoyed face."

    show ringo angry

    r "C'mon, we're wasting time now too."

    r "I don't want to become like John!"

    show geo smile
    with Dissolve(.25)

    g "Do you stay up at night thinking about it?"

    r "Yes!"

    r "And sometimes I have nightmares..."

    show ringo smile
    with Dissolve(.25)

    r "Anyway, let's go back, John, or are you going to spend the night here?" 

    john "No, I'm going to live here."

    show geo smile1
    with Dissolve(.25)

    g "Are you going to sleep on the ground and piss in the bushes?"

    john "Yes, right where you're standing"

    "They are smiling their crazy smiles"

    "What a daft exchange"

    "But it made me laugh..."

    scene bg eum
    with Dissolve(.25)

    scene bg sky evening
    with Dissolve(.25)

    jo "Ha..."

    jo "Was I really dreaming..."

    jo "Nice guys"

    jo "With heaviness in my legs and my soul, I follow them back."

    jo "If it hadn't been for that scream, a peaceful evening would have ended in a quarrel today."

    jo "Eventually, I had to show up and speak out" 

    jo "and any of my statements..."

    jo "Intellectually, I've always understood that my close people are very good and not at all to blame for meeting me."

    jo "But, on the other hand, I treated myself very well."

    jo "The conclusion suggests itself: incompatibility."

    jo "Speaking of my closest relationship, a grandiose incompatibility even!"

    scene bg eum
    with Dissolve(.25)

    scene bg town
    with Dissolve(.25)

    play music people

    jo "We've been walking for about 20 minutes."

    jo "All the way Mal has been pestering me with stupid questions."

    jo "My legs hurt. My stomach is empty..."

    jo "I probably wouldn't survive the war if one began these days."

    jo "Maybe I should start running in the mornings."

    jo "Hah, if only I could wake up early..."

    jo "Although I can be very proud of myself for today's morning - I arrived at the set almost on time!"

    jo "Unfortunate are those who have to get up early daily."

    jo "I hated it when my aunt Mimi woke me up for school."

    jo "At those moments, I wanted to hit her and myself."

    jo "To interrupt someone else's sleep is the same thing as walking into the bathroom when the other person's there washing!"

    jo "Why the hell do this?"

    jo "Someone's hand touches me on the shoulder..."

    stop music
    scene black with dissolve
   
    e "John!"

    scene bg town
    with Dissolve(.25)
    show paul smile
    with Dissolve(.25)

    p "Finally you're here!"

    play music paulfirst

    p "What have you been doing?"

    jo "I'm confused, just not now, please..."

    john "I'm hungry and dizzy."

    show paul angry
    with Dissolve(.25)

    p "Everybody was a little worried, you know."

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

    p "Mal offered to celebrate this event in a restaurant."

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

    c "It's me. Cyn."

    jo "This woman knows how to scare people."

    john "Ah, crikey, Cyn, you made me jump."

    john "For a moment, I thought you were a fan breaking in or a ghost."

    show cyn smile with dissolve

    jo "She is giggling."

    john "Have you been hiding here or something?" 

    show cyn smile3 with dissolve

    c "I've just got out of the bathroom. Sorry, I didn't mean to frighten you." 

    john "Well, long time no see, hon. When did you get here?" 

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

    john "You should've reminded me yesterday you were coming."

    show cyn smile2 with dissolve

    c "I wanted to."

    c "But your line was engaged since our last call"

    c "and the hotel staff who tried to deliver my message to you told me there was no reply as he knocked on your door yesterday evening."

    show cyn brush with dissolve

    c "Where were you?"

    john "Here. In my suite. Where else would I be?"

    c "I don't know. Why didn't you respond then? Were you OK?"

    john "I didn't hear anybody knocking."

    john "Probably, I was just too busy restoring my strength after doing me best at my starring secondary role in the oncoming hit Beatles movie."

    pause 2

    show cyn smile2 with dissolve

    c "Oh, John, you aren't taking acid again, are you?"

    john "Stop it, Cyn, {w=1} do me a favour."

    john "If I wanted to answer stupid questions, I'd hold a press conference."

    c "But still, are you?"

    john "You know I'm done with it."

    john "I spent the whole evening...{w=1} meditating"

    john "Yes."

    jo "I sighed."

    john "Just what Maharishi ordered on a hard day's night, you know."

    john "Nothing interesting, anyway."

    john "You better tell me how were things at home."

    show cyn sad with dissolve 

    c "We were fine aside from we were missing you badly."

    c "Julian even draw a comic of you performing on stage with the band."

    c "He's brought it here to show you."

    jo "There's no escape from Beatles fans even in the family."

    john "Where's him, by the way?"

    show cyn smile2 with dissolve

    c "He's sleeping in the next room. The road wore him out."

    john "Don't you want to have some rest too?"

    john "There's another hour before dinner."

    show cyn smile3 with dissolve

    c "Maybe we'd better take a walk and you'd show me around?"

    jo "Shit..."

    john "Actually, I don't feel like going out at the moment"

    show cyn sad with dissolve 

    john "but you can go and ask Mal to keep you company."

    john "I've seen him hanging around in the lobby just now."

    c "But-"

    john "No buts, Cyn, I'm tiered. Just give me some peace, okay? "

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

    john "Hello?"

    return



