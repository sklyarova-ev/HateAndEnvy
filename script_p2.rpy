# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define j = Character (None,kind=nvl)
define jo = Character (None,kind=adv)
define p = Character ('Paul', color="#041c21")
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
define audio.water="sounds/water.mp3"
define audio.paul2="music/paul2.mp3"
define audio.water2="sounds/water2.mp3"

init:
    $ left2 = Position (xalign=0.2, yalign=1.1)
    $ right2 = Position (xalign=0.8, yalign=1.1)


