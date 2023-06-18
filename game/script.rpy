image splash = "gui/logo.png"

label splashscreen:
    scene black
    with Pause(0.5)

    show splash at truecenter with dissolve
    $ renpy.pause(0.3, hard=True)
    with Pause(1)

    hide splash with dissolve
    $ renpy.pause(0.3, hard=True)
    with Pause(0.5)

    show text "{size=50}{color=#f00}Content Warning:{/size=50}{/color}" with dissolve
    $ renpy.pause(0.3, hard=True)
    with Pause(1)

    hide text with dissolve
    $ renpy.pause(0.3, hard=True)
    with Pause(0.5)

    show text "{size=40}{color=#ffffff}The game contains screen shaking, small jumpscares as well as depictions of mind/memory manipulation, hypnosis, blood and death.{/size=50}" with dissolve
    $ renpy.pause(1, hard=True)
    with Pause(3)

    hide text with dissolve
    $ renpy.pause(0.3, hard=True)
    with Pause(0.5)

    show text "{size=40}{color=#ffffff}Player discretion is advised.{/size=50}" with dissolve
    $ renpy.pause(0.3, hard=True)
    with Pause(1)

    hide text with dissolve
    $ renpy.pause(0.3, hard=True)
    with Pause(0.5)

    return






default protag = "Poppy"
default stranger = "???"
default mushroomman = "Mychael"
default pet = "Molly"

define p = Character ("[protag]", what_slow_cps=45, what_slow_abortable=True)
define s = Character ("[stranger]", what_slow_cps=45, what_slow_abortable=True)
define m = Character ("[mushroomman]", what_slow_cps=45, what_slow_abortable=True)
define c = Character ("[pet]",what_slow_cps=45, what_slow_abortable=True)

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -30
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0



label start:



    stop music fadeout 3.0
    if protag ==  "Poppy":
        $ protag = renpy.input("What's your name?", length=25)

    if pet ==  "Molly":
        $ pet = renpy.input("What's your cat's name?", length=25)

    "[pet] has been missing for a while now."
    "She was an indoor cat, but had the tenacity of a wild cat on a mission trying to leave whenever the door was open."
    "Catios and playtime just wasn't enough for the little missus."
    "I figured she'd come running if I left out some food by the porch.{p}Three days later,{w=.2} still no cat."
    "I've tried everything I could think of."
    "Asking around the neighborhood.{w} Putting up {b}MISSING CAT{/b} posters."
    "Sadly, nothing came from my efforts."
    "I couldn't search for her during the day since I had work keeping me occupied."
    "And there's only so many hours in an evening I could yell around the streets looking for her."
    "There was only one place left I could think of that she might've ran off to."
    "The woods by my house,{w=.2} right across the street."
    "I've definitely caught her eyeing the birds and squirrels that ran alongside the perimeters from the front window,{w=.2} her teeth clicking in excitement."
    "I was no outdoorsy person by any means."
    "In fact, the thought of going in there scares me."
    "But I had to find her. Or at least try."
    "The first weekend that came around I packed up some water, [pet]'s favourite treats and a compass to be safe."
    "I wasn't sure where to even begin looking for her, so I started walking in a straight line, calling out her name every few steps."
    "..."
    "It certainly didn't take long for me to realize I was way in over my head."

    play music "audio/ambience/forest-morning.ogg" fadein 1.0 loop
    play sound "audio/sfx/forest-footsteps.ogg" loop
    scene bg woods daytime
    with dissolve

    p "Why did I think this was a good idea?"
    "It was hard to find my bearings within the surrounding trees."
    "I didn’t want to admit I was lost, at least not yet."

    stop sound fadeout 2.0

    "I could only squint down at my compass as the needle spun slowly. {w} Pretty sure they weren't made to do that."
    "...Did I really bring a busted compass on my first venture out in these woods?"
    "Figured that would just be my luck."
    "The only thing risking my own safety was my own incompetence."
    "I shook my head hastily.{w} Nonono, no time for negativity.{w} [pet] was out there somewhere, cold and lost and hungry."
    "I had to keep going."

    play sound "audio/sfx/forest-footsteps.ogg" loop
    stop music fadeout 2.0
    scene bg woods evening
    with Dissolve(2.0)
    play music "audio/ambience/forest-latenoon.ogg" fadein 2.0 loop

    "...It's been hours."
    "I'm so so lost."
    "I don't even know why I kept searching even after the moment I'd realized that."
    "{i}Why{/i} did I think this was a good idea!?"
    "Hunger had been gnawing at my stomach for a while now, having missed breakfast and lunch altogether."
    "The heat and humidity from the afternoon sun was unbearable, but the cooling air did nothing to soothe me."
    "Even if I were to head home, I couldn't even pinpoint where that was."
    "What do people even do in this situation?"
    "I knew it was baseless optimism, but walking onwards was really the only thing I could think of to do."
    "Surely I’ll come across something familiar."
    "I trudged on, my shoes carefully avoiding the tree roots intertwined across the forest floor."
    "But in my weakened state,{w=.2} plus the approaching darkness, {w=.2}I found myself stumbling through the rough terrain."

    play sound "audio/sfx/kicky.ogg"
    "My feet hit something soft jutting out of the ground."
    p "Ack!" with vpunch
    "My hands shot out as I lost my balance. My feet clumsily tried to find purchase as I wobbled backwards, arms flapping."
    play sound "audio/sfx/poofy.ogg"
    "{i}Poof!{/i}" with vpunch
    p "{i}Cough cough!{/i} Wh-what...?"

    show bg mushroom ring 01
    with dissolve

    "My shoe had landed smack dab in a circle of mushrooms, the brunt of it causing a wispy cloud to erupt from the cluster."
    "I stuck my nose in my elbow to avoid breathing it in."
    "I couldn’t differentiate one tree leaf from another for the life of me but I’m pretty sure humans aren’t supposed to inhale whatever the hell this was."
    "It smelled strongly of rotten wood and wet dirt, even as it cleared."

    show bg mushroom ring 02
    show sparkle
    with dissolve

    "Something shiny quickly caught my attention."
    "I stooped down to pick it up, gasping under my breath."

    play sound "audio/sfx/cat-bell.ogg"
    hide sparkle
    with dissolve

    show item cat collar
    with dissolve

    "It was [pet]'s collar."
    "Covered in whatever the hell those mushrooms released."
    "I looked around desperately for any signs of her."
    p "{size=+5}[pet]{/size}? {size=+10}[pet]{/size}!!"
    p "Psspsspsspsspss!"
    "I coughed from inhaling some of the remaining dust floating in the air."
    "I should really steer clear from this."
    "Pocketing [pet]'s collar, I retreated carefully until I could breathe again."

    hide item cat collar
    with dissolve

    show bg woods evening
    with dissolve

    "Stepping back I could still smell it. It must’ve stuck to my hair and clothes."
    "A quick once over confirmed my suspicions with a slight cringe. A thin yet generous coating of it covered my sleeves and jeans."
    "I leaned against a tree, dusting off my clothes in a naive attempt to get the dust and smell out, to no avail."
    "If anything it felt like I’m breathing more of it in."
    "What used to be musty now turned sweet, and I found myself inhaling even deeper, trying to pinpoint the smell."
    "...Cucumbers?"
    "It smelled like fresh cucumbers."
    "A tingly feeling crept up my hands and neck, pinpricks spreading across my limbs as a strange heat reached my face."
    "{color=#8c277a}I{/color} started to feel drunk and woozy. {color=#8c277a}My{/color} senses were numb."
    "It should freak {color=#8c277a}me{/color} out."
    "And yet..."
    "A strange comfort washed over {color=#8c277a}me{/color}."
    "{color=#8c277a}I{/color} should lie down.{w} Right now, in fact."
    play sound "audio/sfx/fallen-down.ogg"
    "{color=#8c277a}My{/color} legs gave out from underneath {color=#8c277a}me{/color}, {color=#8c277a}my{/color} body toppling over at an awkward angle." with vpunch

    show bg woods skylight
    with dissolve

    "{color=#8c277a}I{/color} laid there{w} and stared{w} and stared{w} and stared."
    "It was... nice here."
    "A peaceful calm."
    "The perfect place for a nap, even."
    "{color=#8c277a}My{/color} eyes grew heavy as {color=#8c277a}I{/color} swam in and out of consciousness."
    "Yeah. A nap sounds really good right about now."

    show bg black
    with dissolve
    stop music fadeout 2.0

    "..."
    "..."
    "..."

    s "Oh no..."
    s "Sorry this happened to you, little guy."
    s "By the will of the forest, may you rest in peace."
    s "..."
    s "Hm?"
    s "Wait.{w} A human?"
    s "How'd you end up all the way out here?"
    s "...Still breathing, too."
    s "Ah geez, I can't leave you here."
    s "What should I do..."

    scene bg black
    pause 1



    play music "audio/ambience/cabin-fireplace.ogg" fadein 1.0 loop
    scene bg cabin ceiling with hpunch

    "I woke with a jolt."
    "It was warm, but comfortably so."
    "I could feel the weight of a blanket on me as I tried to sit up."
    "…I couldn’t."
    "I couldn't move my body."
    "My fingers twitched uselessly at my sides as my eyes darted around in panic."
    "Glancing about I could see the interior of a cabin, or at least the ceiling of one. I couldn’t see much past the corner of my eyes."
    "Where was I? How did I get here?"
    "A desperate feeling rose in {color=#8c277a}my{/color} chest."
    "…{color=#8c277a}I{/color} had to leave."
    "Right now."
    "This was {size=+5}wrong. {/size}{size=+10}{color=#73416a}Wrong. {/color}{/size}{size=+15}{color=#8c277a}Wrong.{/color}{/size}"
    "{color=#8c277a}I{/color} wasn’t meant to be here."
    play sound "audio/sfx/here-comes-the-boy.ogg" fadein 2.0
    "I could hear the crackling of a fire nearby, likely the source of warmth I had felt on waking up."
    "I could also hear footsteps approaching."

    menu:
        "Pretend to be asleep." if True:

            jump ch_asleep
        "Stay awake." if True:

            jump cont_story_01

    label ch_asleep:

    show bg black
    with dissolve

    "I shut my eyes quickly, hoping they hadn’t noticed."
    "I slowed down my breathing, willing my face muscles to stay still."
    "..."
    "From beside me, someone chuckled softly."
    s "Oh come on now, firefly. I can sense you're awake."
    s "Let me see you."

    label cont_story_01:

    show bg cabin ceiling
    with dissolve
    show cgwakeup 01
    with dissolve

    "I fluttered my eyelids, straining to look at the person approaching."
    "My eyes widened as I took in their appearance, the protrusions from their forehead catching my attention."
    "Not to mention the green skin????"
    "The stranger didn't sense my unease as they heaved a sigh of relief."

    show cgwakeup 02
    with dissolve

    s "You're awake!{w} That’s good. Very very good."
    s "How’re you feeling?"
    "…I blinked."

    show cgwakeup 03
    with dissolve

    s "Oh!{w} S-sorry, I forgot about that!"
    s "Here."

    show cgwakeup 04
    with dissolve

    "The person held a cup to my lips, a strong sweet smell coming from the rim."
    "A gentle hand grabbed my chin to open my mouth. I couldn’t even move to resist."
    s "Don’t worry. It'll help you feel better,{w=.2} I promise.{w} Drink up!"
    "As the liquid hit my tongue, all I could feel was a vague sense of heat."

    show cgwakeup 05
    with dissolve

    play sound "audio/sfx/dwink.ogg"
    "As I kept drinking, taste and texture returned; the sweetness of berries and chamomile coating my tastebuds. I could even detect a hint of mint."

    hide cgwakeup 02
    with dissolve

    "I lifted my head finally, hands fisting at my sides as I propped myself onto my elbows."
    "The person kept a steady hand on my chin, careful not to pour in too much in case I choked."
    "I finished every last drop, wiping my mouth with the back of my hand."
    "I stared at my fingers realizing I had full autonomy over my body again."

    play music "audio/music/mychael-is-here.ogg" fadein 1.0 loop
    show bg cabin room night
    with dissolve
    show myc smile w hat
    with dissolve

    s "Good as new! Now, how're you feeling?"
    p "B-better. Thank you."

    show myc happy w hat
    with dissolve

    "The stranger laughed."
    s "Oh, I like the way you sound!"
    s "Been ages since I've talked to anyone, much less with a voice as nice as yours."

    show myc smile w hat
    with dissolve

    "I brushed off their strange compliment, finally looking around the cabin properly."
    "It was a simple room filled with sparse wooden furniture, perfect for someone living alone."
    "An open archway to the right led to what I assumed was the kitchen."
    "Across from it, a door was closed shut.{w} Possibly the bathroom?"
    "Taking it in, there was a common theme of knitted decorations strewn about. Any available surface had patterned knitted tablecloths covering it."
    "From what I could peek into the kitchen the same could be said for the kitchen utensils."
    "An unfinished project laid beside the bedside table where I sat, a pair of knitting needles jutting out of a pile of yarn from a small basket."
    "As far as I could tell it looked like the beginnings of a green scarf."

    show myc grabh
    with dissolve

    "The stranger was comfortable in staying silent, observing me as I looked around."

    show myc smile
    with dissolve

    "Though with their hat off, the horns and ears were impossible to ignore."
    "They tossed their hat onto the bed, scruffing their hair and making it even messier."
    p "S-sorry but who...{w=.2} wh-what’re you?"
    s "Hm?"

    show myc happy
    with dissolve

    s "Oh, I didn't introduce myself, did I?"

    show myc grin
    with dissolve

    s "Hiya! I'm Mychael.{w=.2} With a Y."
    "I shook my head."
    p "No no, I meant that...{w=.2} um."
    "Mychael stared at me, their left ear twitching."

    show myc smile
    with dissolve

    p "You...{w=.2} look very..."
    "He snorted."

    show myc cheeky
    with dissolve

    m "Ugly?{w=.2} Offputting?"
    p "No!{w} Just...{w=.2} different."
    m "Different, huh?{w=.2} You're just being nice."
    p "W-well then explain yourself!"

    show myc nervous
    with dissolve

    m "Uhm."
    m "I mean,{w=.2} that's kind of rude, isn't it?"
    "I pinched the bridge of my nose, exhaling slowly."
    p "I-I'm just."
    p "..."
    p "Sorry...{w=.2} it's been a long day, is all."
    p "I should be thanking you."
    m "If it helps... it's... uh,{w=.2} a s-skin condition?{w} Is that what you humans call 'em?"
    "The way he said it didn't sound confident."
    p "...{w=.2}And the ears?"
    m "Um."
    m "Gen{w=.2}-ee-{w=.2}tics{w=.2}...?"
    p "Right..."
    p "And I assume the little..."
    "I waved vaguely at his... horns?{w=.2} Antennae?"
    p "Those things are just cosplay to complete the look?"
    m "Would that make a convincing argument?"
    "I squinted."
    p "...{w=.2}Maybe."

    show myc cheeky
    with dissolve

    m "Then yeah. It's...{w=.2} {i}cossss{/i}-play."
    p "Still doesn't explain everything..."

    show myc nervous
    with dissolve

    "Mychael huffed a nervous laugh."

    play sound "audio/sfx/hypno-static.ogg" fadein 3.0 loop
    show pink behind myc
    with dissolve

    m "Listen, I’m just a guy living by himself in the woods.{w} You don’t need to worry yourself further than that, okay?"
    "Something in his tone compelled {color=#ff8da1}you{/color} not to question his existence anymore."
    "He’s just some guy.{w} Living in the woods.{w} Completely normal."

    stop sound fadeout 3.0
    hide pink behind myc
    with dissolve
    show myc smile
    with dissolve

    p "R-right… completely normal."
    p "I'm [protag]."

    show myc happy
    with dissolve

    "Mychael beams."
    m "Nice to meet you, [protag]!"



    "I fiddled with the blankets as Mychael scooted closer from the edge of the bed."

    show myc nervous
    with dissolve

    m "I-I know I already asked,{w=.2} but how're you feeling?"
    m "Any aches?{w=.2} Sores?{w=.2} Nausea?"
    m "...I-intrusive thoughts?{w=.2} Weird impulses?{w=.2} Fever, maybe?"
    p "Uh... I don't think s-{nw}"
    "He placed his hand on my forehead before I could react."
    "His hands were calloused, quickly retracting as he gave a thoughtful hum."

    show myc smile
    with dissolve

    m "You seem to be...{w=.2} lucid.{w} That's a good sign."
    p "Uh, great?"
    "I was about to comment on his strange features when they reminded me of a cat's."
    "My cat."
    p "Oh shoot!"

    show myc neutral
    with dissolve

    p "S-sorry if this is out of nowhere, but have you seen a cat around these parts?{w=.2} Her name's [pet]."
    p "She's a sweet little thing, about this big. Skittish but she can approach strangers if she needs to."
    "I pulled out my phone to show pictures of her, only to find it missing from my back pocket."
    p "Wait... where is?"

    show myc confused
    with dissolve

    m "I haven't."
    p "Huh?"
    m "Your... [pet]. I haven't seen it."
    p "Oh... I-I see."

    show myc neutral
    with dissolve

    "I slumped against the pillows, rubbing at my temples."
    p "She lost her collar, too.{w} Even if anyone finds her, they wouldn't be able to tell where she's from."
    p "...{w}Dammit."
    "Mychael stayed quiet, watching me from his side of the bed."

    show myc surprise
    with dissolve

    m "You... care a lot for your [pet]?"
    p "My cat? {w=.2} Of course."

    show myc upset
    with dissolve

    m "To the point where you're willing to run yourself ragged this deep in the forest?{w=.2} For a cat?"
    m "Do you realize how far you've wandered away from the nearest town?"
    m "I found you near unconscious.{w=.2} In an area nobody's set foot in for years."
    "My cheeks grew heated at how stupid reckless that sounds."
    p "I-I mean."
    p "A-anyone would. For something they care about,{w=.2} right?"

    show myc neutral
    with dissolve

    "Mychael eased up, shoulders relaxing."
    "He rubs his chin a moment, as if contemplating something serious."
    m "{size=-10}...Something they care about,{w=.2} huh?"

    show myc smile
    with dissolve

    "He finally tipped his head at me with a smile."
    m "It's... cool to see someone willing to go this far for a small critter."
    m "Not a lot of people come out this far.{w=.2} Not even people searching for their lost cats."

    show myc happy
    with dissolve

    m "It's been a while since I've talked to someone,{w=.2} so the conversation's nice, too."
    m "I think...{w=.2} I'm starting to like you, [protag]."
    p "Um. Thanks...?"

    show myc grin
    with dissolve

    "His smile widened but something about it was off."
    "He was showing too much teeth. {w=.2}And it felt stiff."
    "I rubbed my neck, trying to think of something else to say."
    p "C-can I ask, how did I get here?"

    show myc surprise
    with dissolve

    m "Oh.{w=.2} Like I said, I found you in the woods not far from here."
    p "Oh geez. Really?"
    p "I knew I was tired but... I couldn't have possibly..."
    p "Huh. I did step in something. Something... {color=#8c277a}important{/color}."
    "Familiar pinpricks crept up my skin."
    p "H-home..."
    p "{color=#8c277a}I{/color} need to go {color=#8c277a}home{/color}."
    "Mychael stiffened as he grabbed my shoulder."
    m "U-uh. Nevermind that!"

    show myc nervous
    with dissolve

    m "You'd fallen unconscious from... heatstroke."
    "Heatstroke?{w} No… no that wasn’t what happened."
    p "I-I wasn’t… {color=#8c277a}I{/color} was fine up until…"
    "Mychael shook his head insistently, leaning close."
    m "No no no, firefly, you weren’t fine at all."
    m "If I hadn’t found you when I did...{w} well, who knows what could've happened?"
    m "There’s dangerous wild animals in these woods. {w=.2} Bears, for example."
    m "They could’ve snapped you right up!"
    "Bears…?"

    play sound "audio/sfx/hypno-static.ogg" fadein 3.0 loop
    show pink behind myc
    with dissolve

    "No… he was right."
    "{color=#ff8da1}You{/color}'ve always heard news of bear sightings around the neighborhood."
    "Not to mention the many warning signs {color=#ff8da1}you{/color}’d see by the roadside on {color=#ff8da1}your{/color} expedition in search of {color=#ff8da1}your{/color} cat."
    "And to go in the woods without bringing any water! {w} Passing out from heatstroke of all things."
    "How could {color=#ff8da1}you{/color} have been so stupid?"
    "I shook my head, brain too foggy to pick apart my thoughts."
    "He sounded confident, so why should {color=#ff8da1}you{/color} doubt him?"

    stop sound fadeout 3.0
    hide pink behind myc
    with dissolve

    p "W-well, if it means anything, I’m glad you were there."
    "Mychael relaxed, hand on his lap once more."

    show myc grin
    with dissolve

    "He grinned at me."
    m "So am I, [protag]."

    show myc blush
    with dissolve

    m "I'm definitely glad I found {i}you{/i}."
    "His eyes were hidden fully behind his unruly hair, but I couldn’t help feeling how intensely they were fixated onto me as he said that."
    "The hairs on the back of my neck stood."
    p "Uh... sure."
    "Without a distraction, I've only just realized how uncomfortable I was sitting still."
    "The blanket on me was starting to itch, just as the desperate need to get home began to rise in {color=#8c277a}me{/color} again."
    p "Um, this was… nice. But I should really get going now."

    show myc surprise
    with dissolve

    m "Wait!"
    "My host jumped up from the bed before I could."

    show myc nervous
    with dissolve

    m "I-I mean."
    m "You can’t--{w=.2} I can't just let you wander around in the woods this late!"
    m "Please, s-stay a bit longer."
    p "But, Mychael, I really have to--{nw}"
    m "Come!"
    "He grabbed my hand and led me across the room."



    scene bg cabin kitchen night
    with dissolve

    "We stepped into the kitchen, a fragrant smell of cooked potatoes and meat hanging in the air."
    "Two plates had been set out on a small circular table, complete with utensils and mugs of tea."

    show myc blush
    with dissolve

    m "I-I wasn’t expecting guests today, so the food is nothing fancy. But… join me for dinner?"

    play sound "audio/sfx/hypno-static.ogg" fadein 3.0 loop
    show pink behind myc
    with dissolve

    "He looked so hopeful, ears drooping."
    "…{color=#ff8da1}You{/color}’d feel so bad if {color=#ff8da1}you{/color} had to say no."

    menu:
        "Say {color=#ff8da1}yes{/color}." if True:

            jump ch_dinner_yes
        "Say {color=#8c277a}no{/color}." if True:

            jump ch_dinner_no


    label ch_dinner_no:

    stop sound fadeout 3.0
    hide pink behind myc
    with dissolve
    show dark behind myc
    with dissolve
    show myc nervous
    with dissolve

    play music "audio/music/mychael-is-here-please.ogg" fadein 1.0 loop
    "{color=#8c277a}I{/color} ignored the pleading voice in the back of {color=#8c277a}my{/color} head, steeling {color=#8c277a}my{/color} resolve."
    "Strangely enough, the second {color=#8c277a}I{/color} made up {color=#8c277a}my{/color} mind, the faint static that fogged {color=#8c277a}my{/color} thoughts cleared instantly, only replaced with the urgent need to go back home."
    "Mychael goes quiet, his grip on {color=#8c277a}my{/color} hand tightening before he loosens his hold."
    m "I... I see."
    m "If… that’s what you want."
    m "But… a-are you really sure?"

    menu:
        "Yes. It's what {color=#8c277a}I'm{/color} meant to do." if True:

            jump ch_dinner_no2
        "I mean... I guess it doesn't hurt to stay." if True:

            jump ch_dinner_yes

    label ch_dinner_no2:

        show myc upset
        with dissolve

        play music "audio/music/mychael-is-here-please-stay.ogg" fadein 1.0 loop
        show darker behind myc
        with dissolve

        "His ears flattened at my words."
        "He laughs an empty laugh, mouth twisting into a crooked grimace."
        m "S-surely. Surely you wouldn't mind sitting down for a quick meal."
        m "Just a bite, even."

        play sound "audio/sfx/hypno-static.ogg" fadein 3.0 loop
        show pink behind myc
        with dissolve

        m "{size=-15}{k=15}Please...{/size}"
        "His hands fisted at his sides."
        m "..."
        m "Do you really have to go?"

    menu:
        "{color=#8c277a}Yes." if True:

            jump ch_bad_end_01
        "{color=#8c277a}YeS." if True:

            jump ch_bad_end_01
        "{color=#8c277a}YEs." if True:

            jump ch_bad_end_01
        "{color=#8c277a}YES." if True:

            jump ch_bad_end_01
        "{color=#ff8da1}Actually, dinner sounds really {b}really{/b} good right now.{/color}" if True:

            jump ch_dinner_yes

    label ch_bad_end_01:

        stop music fadeout 2.0
        stop sound fadeout 3.0
        pause 1
        hide pink behind myc
        with dissolve
        show myc upset
        with dissolve

        play music "audio/music/goodbye.ogg" fadein 2.0 loop
        m "..."
        "Mychael stared at me as if looking for something."
        "Finally he sighed in defeat."

        show myc neutral
        with dissolve

        m "…Alright."
        m "I guess... I can’t keep you here. Not anymore."
        m "Let me lead you outside."

        hide dark
        with dissolve
        hide darker
        with dissolve
        show bg woods nighttime
        with dissolve

        "Mychael ushered me towards the back door, swinging it open as he sidestepped to let me out."
        "The chill breeze crept along my arms. I turned towards him one last time."
        p "Um, thanks again. For everything."
        "He was silent for a moment, staring past me into the trees."
        m "You’re welcome. {w=.2} Be careful on your way back."

        show myc upset
        with dissolve

        m "I-I'm sorry there's not much more I could do for you..."
        "He's been nothing but gracious."
        "It's strange for a farewell, but {color=#8c277a}I{/color} was too occupied with thoughts of returning home to care."
        "{color=#8c277a}I{/color} looked over to the woods, the shadows cast from the moonlight causing some hesitation in {color=#8c277a}me{/color}."
        p "Um, do you mind giving {color=#8c277a}me{/color} some directions as a head start?"
        "Mychael looked at {color=#8c277a}me{/color} finally, then to the horizon with a tilt of his chin."
        m "Keep heading in that direction."
        m "You’ll come across a trail that’ll lead you straight home."

        hide myc
        with dissolve
        play sound "audio/sfx/door-shut.ogg"
        stop music fadeout 2
        pause 1
        play music "audio/ambience/forest-night.ogg" fadein 1.0 loop

        "{color=#8c277a}I{/color} waved at him as he shut the door, the mechanism locking shut with a click."
        "{color=#8c277a}I{/color} stood there for a moment, questioning if {color=#8c277a}I{/color} had made the right decision or not."
        "Another urgent thought compelled {color=#8c277a}me{/color} to leave."
        "{color=#8c277a}This is no place for me.{/color}"
        "{color=#8c277a}I have to go.{/color}"
        play sound "audio/sfx/forest-footsteps.ogg" loop
        "It was already too late to go back, so {color=#8c277a}I gathered my resolve and walked away.{/color}"
        "..."
        "..."
        "..."
        "{color=#8c277a}I walked."
        "{color=#8c277a}And walked."
        "{color=#8c277a}Trees blended into one another after a while."
        "{color=#8c277a}I should’ve been afraid. Or concerned."
        "{color=#8c277a}But it felt right."
        "{color=#8c277a}The darkness that surrounded me was too comforting for me to feel in danger."
        "{color=#8c277a}I steered away from the direction Mychael showed me ages ago, my feet willingly carrying my body to someplace specific."
        "{color=#8c277a}Someplace special."
        "{color=#8c277a}A final destination."
        "{color=#8c277a}Here."
        stop sound fadeout 2.0
        "{color=#8c277a}The patch of mushrooms I had stepped in earlier."
        "{color=#8c277a}I was meant to be here."
        "{color=#8c277a}I’ve always meant to be here."
        "{color=#8c277a}I laid down in the cold, wet dirt."
        "{color=#8c277a}And closed my eyes."

        show bg black
        with dissolve

        "..."
        "..."
        "..."

        stop music fadeout 2.0
        pause 1
        show cg badend_01
        with dissolve
        play music "audio/ambience/forest-morning.ogg" fadein 1.0 loop
        m "..."
        m "There’s not much I could do if the forest had staked its claim on you, firefly."
        m "..."
        m "…I wish I'd found you sooner."
        m "..."
        m "Sleep well, [protag]."

        "ENDING 1 - Peaceful Slumber"

        return

    label ch_dinner_yes:

    play music "audio/music/mychael-is-here.ogg" fadein 1.0 loop
    stop sound fadeout 3.0
    hide dark
    with dissolve
    hide darker
    with dissolve
    hide pink behind myc
    with dissolve

    show myc surprise
    with dissolve

    "Mychael's jaw dropped for a second before he quickly recovered."

    show myc happy
    with dissolve

    m "I… y-yes yes, of course! Here, here come sit. I’ll serve up the cottage pie in a minute!"

    hide myc
    with dissolve
    show bg table
    with dissolve

    "I sat as instructed, my stomach rumbling something fierce as the smell was the only thing I could focus on."
    "...Yes, this was definitely the right choice."
    "What was so important that {color=#ff8da1}you{/color} had to leave so soon?"
    "The outside world can wait."
    "{color=#ff8da1}You{/color} could stay here,{w} and enjoy my company."
    m "Oh!{w} Actually..."
    m "I should ask,{w=.2} are you okay with meat for dinner? I could make something else for you if that’s not your preference."

    menu:
        "I don't eat meat." if True:

            jump ch_dinner_stirfry
        "I'm okay with meat." if True:

            jump ch_dinner_pie

    label ch_dinner_stirfry:

        m "Good thing I asked!{w=.2} Thanks for letting me know."
        m "Let me pick some veggies from the garden and I’ll make you something."
        "He left out the back door with a basket, coming back inside surprisingly quick with a smile on his face."
        "I expected him to toss something in a bowl and have it done just like that.{w} But apparently he had other plans."
        play sound "audio/sfx/veggie-wash.ogg"
        queue sound "audio/sfx/veggie-chop.ogg"
        "I watched as he washed the veggies thoroughly before chopping them up with an extra sharp knife,{w=.2} setting them aside and pulling out a container from one of the cabinets."
        play sound "audio/sfx/veggie-boil.ogg"
        "He set a pan on the stove and oiled it up,{w=.2} tossing in half of the ingredients and seasoning them with some herbs and spices while a pot boils next to it."
        "The small kitchen quickly filled up with the smell of his cooking."
        "My mouth was already watering in response."
        "I twiddled with a fork on the table, trying to ignore the gnawing feeling in my gut."
        "Luckily I didn’t have to wait long."
        "Before I knew it Mychael had already finished, humming as he strode over to the table and set my food down in front of me."

        play sound "audio/sfx/plate-up.ogg"
        show item stirfry
        with dissolve

        "I looked down at my dinner and almost gasped."
        "It looked so good!"
        "The rice was fluffy as it peeked out underneath the colorful pile of veggies.{w} I didn’t know a simple dish could look so tantalizing."
        "The serving size was a bit heartier than expected.{w} He must’ve known I was starving."

        hide item stirfry
        with dissolve
        show myc table smile
        with dissolve

        "Mychael brought over his own serving of cottage pie as he settled into his seat."
        m "Sorry to make you wait,{w=.2} I tried to keep it simple but filling."
        m "Go ahead!{w=.2} Dig in!"
        "He didn’t have to tell me twice.{w} I jabbed my fork into the dish, scooping up rice with a spoon in my other hand and shoving it into my mouth."
        "Hot!!!" with vpunch
        "Mychael kept a polite expression,{w=.2} the corner of his mouth lifting as I panted with the food still in my mouth."
        "He gave me a few seconds to recover, elbow planted on the table."
        m "Is it good?"
        "I nodded vigorously, even though my buds were burning."
        p "Mmm! Mm!"
        "I couldn't taste anything."
        "He laughed."
        m "It's usually better on the second bite."
        "I slowed down, hand on my mouth as Mychael poked his fork into his pie."
        "I tentatively blew on the plate to make sure it was cool before taking another bite."
        "He was right.{w} The second bite was a lot better."
        "The rice was soft and flavorful, mixing in nicely with the crunch of the vegetables with every chew."
        "I’ve never had greens this fresh, and with how gently he cooked them every single element was finished to perfection."

        jump cont_story01

    label ch_dinner_pie:

        m "Oh, okay! You’ll be having the same dinner as me, then."
        "Mychael pattered about the small kitchen with an almost giddy excitement."
        play sound "audio/sfx/oven-door.ogg"
        "He put on a pair of knitted oven mitts, humming as he stooped down and pulled out a steaming tray of pie from the wood stove."
        "The smell!{w} It filled out the kitchen in an instant as he brought it to the table, my stomach rumbling louder in response."

        show myc table smile
        with dissolve

        "I'm pretty sure Mychael could hear it,{w=.2} but he just smiled as he served up our portions."
        "He discreetly cut me a bigger piece, which I was grateful for."

        play sound "audio/sfx/plate-up.ogg"
        show item cottagepie
        with dissolve

        "It looked so good!"
        "The crust was a nice golden color, streaked with crisp lines and garnish. The meat and veggie filling looked absolutely delectable, the savoury sauce leaking onto the plate."
        "My mouth was watering, unsurprising considering the fact I haven't eaten all day."

        hide item stirfry
        with dissolve

        m "Careful now,{w=.2} it's still hot."
        "It was fair advice, but I didn't wait more than two blows before biting into my first forkful."
        p "Ah!" with vpunch
        "It was...{w=.2} definitely way too hot to eat straight from the oven."
        "Mychael kept a polite expression,{w=.2} the corner of his mouth lifting as I panted with the piece still in my mouth."
        "He gave me a few seconds to recover, elbow planted on the table."
        m "Is it good?"
        "I nodded vigorously, even though my buds were burning."
        p "Mmm! Mm!"
        "I couldn't taste anything."
        "He laughed."
        m "It's usually better on the second bite."
        "I slowed down, hand on my mouth as Mychael poked his fork into his own slice."
        "I tentatively blew on the pie to make sure it was cool before taking another bite."
        "He was right.{w} The second bite was a lot better."
        "The seasoned potato crust was nice and crisp on top, cheesy and creamy in the middle. The savory meat filling was well-cooked and bursting with flavor."
        "Every bite felt like home."

        jump cont_story01

    label cont_story01:

    show myc table smile
    with dissolve

    "My host watched me enjoy the meal from across the table."
    m "Do you like it?"
    p "Yeah! This tastes amazing, Mychael."

    show myc table blush
    with dissolve

    "He flushed from the compliment, rubbing the back of his neck."
    m "Heh, I’m glad. I like to think of myself as a decent cook,{w=.2} but I’ve never been able to get anyone else’s opinion on that."
    p "Do you like baking in particular?"

    show myc table smile
    with dissolve

    m "Hmm, not always.{w} I usually go for simple dishes, with any ingredients available."
    "I nodded amicably, though didn't say much else.{w} I was more focused on scarfing down dinner, which thankfully Mychael didn’t seem to mind."
    "The overall atmosphere was nice and homely,{w=.2} and I could hear Mychael tapping his feet from underneath the table."
    "I guess he was that happy to have someone stay for dinner?{w} It did seem like he lived alone judging from the surroundings in his cabin."
    p "So..."
    "He perked up instantly, his focus solely on me."

    show myc table hm
    with dissolve

    p "Um. What made you wanna live all the way out here? The place seems very...{w=.2} isolated."

    show myc table nervous
    with dissolve

    m "Oh.{w} Well… when you look like me,{w=.2} it’s kinda easier to just live out of sight from everyone else."
    "A pang of guilt shot through my chest.{w} I was giving him a hard time about how he looked too."
    "He must’ve sensed it clear as day on my face."

    show myc table panic
    with dissolve

    m "N-not that you’re one of them!{w} You’ve actually been nicer than most."
    m "Though I wonder if..."

    show myc table nervous
    with dissolve

    "His smile turned strained."
    m "N-nevermind.{w=.2} My point is, it’s better here than anywhere else."
    m "Why don’t you try the tea, firefly?"
    "He seemed uncomfortable now, easing into a different topic."
    "It’s probably best to follow along."
    p "Oh sure."
    "I reached out towards my mug–"

    show myc table panic

    play sound "audio/sfx/tail-whip.ogg" volume 1
    "Only to push it off edge with my clumsy fingers." with hpunch
    p "Wait–!!"
    "I bent over the side to grab it, fully expecting it to fall just out of reach and land on the floor into broken pieces."
    "{w=.2}It never did."

    stop music fadeout 2.0
    show cg tailtime
    with dissolve
    show myc table hb reveal_01
    with dissolve
    play music "audio/ambience/tense-ambience.ogg" loop

    "Instead, a long green appendage was twisted around the ceramic mug, securely keeping it in place. Not even a drop had fallen out."
    "My eyes trailed along the length of it until I pinpointed that it came from behind Mychael, the rest of it partially hidden beneath his cardigan."
    p "Mychael…?"
    p "Is that...{w=.2} yours?"
    m "I-I..."

    hide cg tailtime
    with dissolve

    "Mychael buried his face in his hands,{w=.2} the strange appendage from before lowering to his side, mug in tow."
    m "I’m sorry, [protag]. I think...{w} I think it’s time I was honest."

    show myc table hb reveal_02
    with dissolve

    "He lifted his head,{w=.2} fingers carding his hair back to reveal his eyes."
    "I froze as two... n-no, {i}multiple{/i} pairs of irises stared right into mine, before darting to the side and avoiding my gaze."

    show myc table hb reveal_03
    with dissolve

    m "I-I know it's a lot to take in but..."

    show myc table hb reveal_02
    with dissolve

    m "This is the real me..."
    m "Please... {i}please{/i} don't be scared."


    menu:
        "Freak out." if True:

            jump runaway
        "Remain calm." if True:

            jump cont_story02

    label runaway:

        play music "audio/music/bad-end-dayone.ogg" fadein 2.0 loop

        p "M-monster…"

        show myc table hb reveal_05
        with dissolve

        "I flinched as his eyes focused back to me, their sizes thinning into slits."
        m "N-no! No no no no, please don’t be scared–{nw}"
        p "{size=+10}YOU'RE A MONSTER!" with vpunch
        m "[protag]!"

        play sound "audio/sfx/chair-fall.ogg"
        queue sound "audio/sfx/cabin-run.ogg"
        hide myc
        with dissolve
        show bg cabin room night
        with dissolve

        "I kicked back against the chair, letting it clatter to the ground as I scrambled to the living room."
        "He was a freak!"
        "How did I ever let him get close to me!?"
        "I-I had to escape. Now!"

        play sound "audio/sfx/cabin-run.ogg"
        show bg doorclosed
        with dissolve

        "I ran to the door furthest into the room hoping it was the exit, rattling the doorknob desperately."
        play sound "audio/sfx/doorknob-rattle.ogg"
        "It was locked shut." with vpunch
        m "{size=-10}[protag], please!"

        play sound "audio/sfx/cabin-run.ogg"
        show bg windowclosed
        with dissolve

        "I abandoned the front door and ran to the window by the bed, my fingernails scraping against the sill."
        "It was sealed tight, the lock barely budging as I tried to twist it with my fingers."
        "Heavy boots slowly came closer behind me."

        show bg doorway
        with dissolve
        show myc badend approach
        with dissolve

        "I spun around to see him by the edge of the doorway, hands up in a careful stance."
        m "[protag], calm down.{w} I’m begging you, just let me explain."
        p "S-stay away from me!"
        "My eyes landed on the basket on the bedside table, the needles glinting against the firelight."

        menu:
            "Take them." if True:

                jump runaway_wneedles
            "Leave them." if True:

                jump runaway_noneedles

        label runaway_wneedles:

            "I grasped both needles and pulled them from the yarn, the basket dropping to the floor in my haste." with hpunch

            show myc badend scared
            with dissolve

            "Holding them to my chest, I stepped back as Mychael came closer,{w=.2} eyes wild as he realized what I held."
            m "H-hey… hey…{w=.2} hey… look at me, [protag]..."
            play sound "audio/sfx/hypno-static.ogg" fadein 1.0 loop
            show myc badend plead
            with dissolve
            show pink behind myc
            with dissolve
            m "You don’t wanna do this.{w=.2} You’re gonna hurt yourself."
            m "Let go of those things."

            menu:
                "Attack him." if True:


                    "He was right. If {color=#ff8da1}you{/color} weren’t careful, {color=#ff8da1}you{/color} could--{nw}"

                    stop sound
                    stop music
                    play sound "audio/sfx/stab.ogg"
                    hide pink behind myc
                    show myc badend stab
                    "Aiming blindly, I lunged forward." with vpunch
                    "He probably wasn’t expecting it,{w=.2} because he hardly moved as I stabbed them straight through his chest."

                    show myc badend stabb
                    with dissolve
                    pause 1
                    show myc badend stabbb
                    with dissolve
                    pause 1
                    hide myc
                    with dissolve
                    play sound "audio/sfx/mychael-is-dead.ogg"

                    "A choked sound made past his lips before he collapsed,{w=.2} his disgusting pair of eyes dazedly searching the room for me." with vpunch

                    play music "audio/music/goodbye.ogg" fadein 2.0 loop

                    show cg badend_02a
                    with dissolve

                    m "[protag]...?"
                    m "I...{w=.2} I can’t see you..."
                    "I backed away, my breath lodged in my throat."
                    m "Th-that’s okay...{w=.2} I-I know you... you can hear me..."
                    m "..."
                    m "Ah...{w=.2} th-this hurts so much…"

                    show cg badend_02b
                    with dissolve

                    "He wheezed out a pained laugh."
                    m "You know..."
                    m "I-I was...{w=.2} so alone."
                    m "When you came along...{w=.2} I was so happy..."
                    m "Just to talk to someone...{w=.2} to have dinner with someone..."
                    m "You even liked my cooking!"
                    m "Agh..."

                    show cg badend_02a
                    with dissolve

                    m "..."
                    m "I didn’t think it’d end this way..."
                    m "Did you really hate...{w=.2} the way I looked that much...?"

                    show cg badend_02b
                    with dissolve

                    "He laughed bitterly, spitting out some blood."
                    m "Maybe this was my fate...{w=.2} since the beginning..."
                    m "Sorry...{w=.2} for everything…"
                    m "A-at least...{w=.2} I got one wish..."
                    m "I-I’m not dying alone..."

                    show cg badend_02a
                    with dissolve

                    m "..."
                    m "[protag]...?"
                    m "Are you there...?"
                    m "..."
                    m "P-please..."
                    m "I'm... getting c-cold..."
                    m "T-tell me you're there..."
                    "I didn’t realize I had tears streaming down my face."
                    "He sounded so pathetic."
                    "I stared down at my hands.{w} The hands that hurt Mychael."
                    "Had I made a mistake…?"
                    "A sputtered cough snapped my attention back to him." with vpunch
                    m "...{w=.2}Ah.{w} {cps=15}I think{w=.2} this is goodbye, [protag]."
                    m "{cps=15}B-by the will...{w=.2} of the forest...{w=.2} I-I..."

                    show cg badend_02c
                    with dissolve

                    "He cast one last breath, the sound rattling across the empty cabin as his eyes glassed over completely."
                    "I sunk to my knees, hands still shaking."

                    scene bg black
                    with dissolve

                    "What...{w=.2} what have I done...?"

                    "Ending 2: You Monster."

                    return
                "Listen to him." if True:


                    show pink behind myc
                    with dissolve
                    "He was right. If {color=#ff8da1}you{/color} weren’t careful, {color=#ff8da1}you{/color} could hurt yourself."
                    play sound "audio/sfx/needles-gone.ogg"
                    "{color=#ff8da1}Your{/color} hold on the needles slipped,{w=.2} {color=#ff8da1}your{/color} ears picking up the sound of them clattering to the floor."
                    hide pink behind myc
                    with dissolve
                    jump runaway_noneedles
                    stop sound fadeout 2.0

        label runaway_noneedles:

            "Defenseless,{w=.2} I faced Mychael as he stepped closer."
            "I couldn’t stop staring at those eyes."
            "They looked wide with panic."

            show myc badend plead
            with dissolve

            m "Okay...{w=.2} listen to me."
            m "Everything’s gonna be alright."
            p "S-stay away from me, you freak." with vpunch

            show myc badend hurt
            with dissolve

            m "W-why...?{w=.2} Do you hate me that much?"

            show myc badend plead
            with dissolve

            m "C-can't we just start over...?"
            "I shook my head, backing away from him."
            p "Just let me leave!!"
            p "I-I don’t want to be anywhere near you..."

            show myc badend still
            with dissolve

            "Mychael stopped advancing, hands fisting at his sides."
            m "O-okay...{w} that’s okay...{w=.2} I’ll let you go..."
            m "Just..."

            hide myc
            play sound "audio/sfx/grab.ogg"
            show cg badend_03a with vpunch

            "I screamed as his arms wrapped around me, all I could do was twist in his hold."
            "I could feel something tightening around my legs, his grip on my chin forcing me to look at his face."
            show cg badend_03b
            with dissolve
            p "{size=+5}L-let go of me!{w} Let me go, Mycha–{nw}"

            show cg badend_03c with vpunch
            stop music
            play sound "audio/sfx/hypno-static.ogg" volume 2 loop
            show pink
            with dissolve
            "Static."
            "All I could hear was static."
            "..."
            "My body went against my will as I slackened against him, limp as a ragdoll as his eyes bored straight into mine."
            "Mychael’s smile was manic."
            m "That’s it, firefly...{w=.2} I’ve caught you now..."
            m "You’ll be fine...{w=.2} everything will be fine..."
            "..."
            "{color=#ff8da1}Of course.{w} Of course everything’s fine."
            "{color=#ff8da1}What did you have to worry about anyways? It was just your dear sweet friend, Mychael."
            "{color=#ff8da1}Trustworthy Mychael."
            "{color=#ff8da1}Safe and sound Mychael."
            "{color=#ff8da1}He was all that you needed."
            m "That's right."
            m "Settle in, firefly."
            m "I’ll take good care of you."
            m "I promise."

            stop sound fadeout 3.0
            play music "audio/music/goodbye.ogg" fadein 2.0 loop
            show cg badend_03d
            with dissolve

            m "..."
            m "I can’t have the real you..."
            m "But I’ll willingly play pretend if it means I get to keep you."

            scene bg black
            with dissolve

            "..."
            "{color=#ff8da1}Your name is [protag].{w} You live in the woods with your best friend, Mychael."
            "{color=#ff8da1}You love Mychael."
            "{color=#ff8da1}And he loves you."
            "{color=#ff8da1}You’ve never had a job."
            "{color=#ff8da1}You’ve never had a cat."
            "{color=#ff8da1}You’ve never left these woods."
            "{color=#ff8da1}You’ve never had a home anywhere else."
            "{color=#ff8da1}You already are home."
            "{color=#ff8da1}..."
            m "Hey, firefly.{w} You wanna help with dinner today?"
            m "..."
            m "Haha...{w} of course you do."
            m "..."
            m "Come on."

            "Ending 3: Playing Pretend."

            return

    label cont_story02:

    stop music fadeout 2.0

    "My grip on the kitchen utensils tightened."
    "He looked...{w=.2} freaky, yes."
    "It felt unsettling every time he blinked those eyes in succession,{w=.2} even when he wasn’t looking at me."
    "But...{w=.2} he also looked sad."
    p "I..."
    "I swallowed thickly."
    p "I-I'm not scared."

    show myc table hb reveal_04
    with dissolve

    "Mychael’s many pupils blew wide, dilating like an excited wildcat."
    "It sent a shiver up my spine."
    p "O-okay, maybe just a little bit scared."

    play music "audio/music/mychael-is-here.ogg" fadein 1.0 loop
    show myc table hb panic
    with dissolve

    m "Ah! S-Sorry."

    show myc table hb hiding at bounce

    "He hastily grabbed an empty plate and hid behind it,{w=.2} shoulders scrunched up despite his stature."
    m "Would it help if I just... hide it?"
    m "I-I could fix my hair like before...{w=.2} if that's what you prefer."
    "His voice was muffled behind the ceramic barrier between us."
    "It was...{w=.2} kind of endearing."
    "I slowly reached out to touch his hand, the slight brush of my fingertips making him jump in place."

    show myc at bounce

    p "Mychael?"
    m "...Yeah?"
    p "Can you put that down?"
    m "..."

    show myc table hb sideglance
    with dissolve

    "He slowly lowered the plate.{w} His eyes were still darted to the side, avoiding me."
    p "C-can you look at me?"
    m "..."

    show myc table hb blush_01
    with dissolve
    pause 0.5
    show myc table blush_02
    with dissolve
    pause 1
    show myc table hb blush_03
    with dissolve
    pause 1
    show myc table hb blush_04
    with dissolve

    m "D-don't look at me like that..."
    p "S-sorry! I just...{w=.2} got caught up in your eyes."
    "This was so awkward.{w} His hands were shaking."
    "I looked down at the mug still floating next to him,{w=.2} hanging on for dear life."
    "I reached over and plucked it straight out of his grasp."

    show myc table hb surprise
    with dissolve

    m "!!!"

    show item gingertea
    with dissolve

    "I tentatively took a sip, noticing how Mychael was watching me over the rim of the mug."
    "The taste was mildly spicy,{w=.2} with an almost earthy bite to it.{w} I recognized it instantly as ginger tea."

    hide item gingertea
    with dissolve

    p "...It’s almost room temperature.{w=.2} But it’s still pretty good."
    m "Huh?"
    p "You wanted me to try the tea,{w=.2} right?"
    p "I like it.{w=.2} Thank you."

    show myc table hb nervous
    with dissolve

    m "O-oh.{w} I'm glad."
    "Mychael relaxed back into his seat, following my lead as I picked up my fork once more."
    "The silence didn't last long as Mychael fidgeted."
    m "A-are you really...{w=.2} okay with this?{w} With me?"
    "I gave him a once over, really taking in his... features."
    "His skin.{w} His horns.{w} His tail."
    "...{w}His eyes."
    p "It's...{w=.2} very different than what I'm used to."
    p "But I think I can learn to like it."

    show myc table hb blush_01b
    with dissolve

    "Is that weird to say?"
    p "I-I mean,{w=.2} y-you're not bad to look at."
    p "It's actually kind of... um..."
    "Dammit dammit dammit what do I say!?"

    menu:
        "Attractive." if True:
            m "Y-you think I'm... attractive?"
            p "Y-yeah."
            m "Oh."
            jump after_compliment
        "Unique." if True:

            show myc table hb nervous
            with dissolve
            m "Oh..."
            m "I get what you mean by 'unique.'"
            p "I mean!"
            p "Being unique isn't a bad thing."
            p "I like unique."
            show myc table hb surprise
            with dissolve
            m "Y-you do?"
            p "Yeah."
        "Hot." if True:


            m "H-hot...?" with vpunch
            show myc table hb surprise
            with dissolve
            m "...You're not referring to temperature, are you?"
            p "No, I am not."
            m "Oh..."
            jump after_compliment

    label after_compliment:
    show myc table hb blush_02b
    with dissolve

    p "My point is!{w} Your appearance shouldn't matter."
    p "You've been nothing but kind to me so far."
    p "I'd be the worst kind of person to judge someone based on how they look."
    p "I haven't known you that long...{w=.2} but you seem like a good person."
    p "You're fine, Mychael."
    "I smiled at him."

    show myc table hb blush_03b
    with dissolve

    p "We're fine."
    "Mychael's face had darkened into a deeper azure shade by the time I was done talking."
    m "I... I see."

    show myc table hb nervoussmile
    with dissolve

    "He fidgeted some more before nodding, smiling a bit."
    m "Th-thanks, [protag]."

    show myc table hb happy
    with dissolve

    m "I'll cherish this moment forever."
    "He beamed at me as he enthusiastically went back to eating his food."

    hide myc
    with dissolve
    show bg cabin kitchen night
    with dissolve

    "That was...{w=.2} something."
    "We continued with a bit of small talk, mostly stories about [pet] or snippets from my personal life."
    "Mychael hung on to every word I said, not bothering to elaborate much about himself despite my burning curiosity."
    "I could tell he was extremely insecure about his appearance, so it's probably best I keep my questions to myself for tonight."
    "We cleared up the kitchen in relative silence, Mychael storing away the rest of the pie as I washed the dishes by the sink."
    "Being out here in this remote cabin,{w=.2} I wondered how he had running water."
    stop music fadeout 2.0
    "Maybe I’ll ask him later."

    play music "audio/ambience/cabin-fireplace.ogg" fadein 1.0 loop

    scene bg cabin room night
    with dissolve
    show myc hb smile
    with dissolve

    p "So...{w=.2} thanks for dinner."
    m "No problem!{w}"
    m "Oh! And please,{w=.2} take the bed for the night.{w=.2}"
    p "B-but–"

    show myc hb scold
    with dissolve

    m "Ah ah!{w=.2} You’re my guest and I’m the host.{w} Take the bed, okay?"
    p "...Thanks, Mychael.{w=.2} I’ll leave first thing in the morning!"

    show myc hb neutral
    with dissolve
    pause 1
    show myc hb upset sideglance
    with dissolve

    "Mychael got quiet, staring at the floorboards."
    "With his hair out of the way, I could finally read his expressions."
    "He did seem...{w=.2} upset?"
    p "Is...{w=.2} that okay? I’d need your help, obviously,{w=.2} but I have to get going at some point."
    "His tail flicked behind him."
    m "...Yeah,{w=.2} I’ll bring you home tomorrow morning."
    "I heaved a sigh of relief."
    p "Thanks, Mychael.{w} I’ll see you in the morning."
    m "Yeah..."

    show myc hb shy
    with dissolve

    m "Um...{w=.2} g-goodnight, [protag]."
    p "Goodnight,{w=.2} Mychael."
    "He seemed really happy being able to say that."
    "I plopped myself down onto Mychael’s bed, getting comfy beneath the blanket."

    hide myc
    with dissolve

    "Mychael was gathering some blankets of his own to make a makeshift bed on the floor in front of the fire.{w} He had an impressive collection of knitted items, a comfortable nest forming in the center of the room."
    "My eyes trailed after his tail, now out in the open as it flicked and swayed."
    "Kinda like a cat..."
    "..."
    "I miss [pet]..."
    "Now with a full stomach, dozing off came easy.{w} I didn’t even realize how tired I was."
    "I listened to the gentle crackling of the fire...{w=.2} my vision darkening..."

    show bg black
    with Dissolve (1)
    show bg cabin room nightt
    with Dissolve (1)
    show bg black
    with Dissolve (1)
    show bg cabin room nighttt
    with Dissolve (1)
    show bg black
    with Dissolve (2)
    show cg goodnight yn
    with Dissolve (1)
    m "Goodnight,{w=.2} [protag]."

    stop music fadeout 2.0

    scene bg black
    with dissolve

    "That's the end of Day 1 for Mushroom Oasis [[DEMO]!"
    "Tell me what you think of the game! Any support/feedback is highly appreciated!"
    "As nearly everything is done by me save for sound and music, future updates will be a while."
    "I'll try and update as often as I can via devlogs on the game's itch.io page!"
    "Thank you for playing! <3"

    return
