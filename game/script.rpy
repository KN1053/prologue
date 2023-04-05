image bg munich = "images/munich.jpg"
image bg munich two = "images/munich_two.jpg"
image bg dark = "images/dark.png"
image bg white = "images/white.png"
image bg fractal = "images/fractal.jpg"
image bg fractal two = "images/fractal_two.jpg"
image bg fractal three = "images/fractal_three.jpg"

image bg lake = "images/oilified/lake_dark_oil.jpg"
image bg records = "images/oilified/records_oil.jpg"
image bg dream cinema = "images/oilified/cinema_oil.jpg"
image bg records two = "images/oilified/records_two_oil.jpg"
image bg lab = "images/oilified/lab_oil.jpg"
image bg lab two = "images/oilified/lab_two_oil.jpg"
image bg study = "images/oilified/study_oil.jpg"
image bg cabinet = "images/oilified/cabinet_oil.jpg"

define z = Character(None, kind=nvl)
define narrator = Character(" ")
define o = Character("Jean-Paul", color="#43b56b")
define d = Character("Erik", color="#fdf87c")

define fadehold = Fade(0.5, 3.0, 0.5)

init:
    $ flash = Fade(.25, 0, .75, color="#fff")

label start:
    scene bg records with fade
    z "\"The trouble with dreams... is not their unreality or intangibility, for I have made them real and observable."
    z "What frustrates me is their fragility, the way they fall apart when touched."
    z "They are like porcelain dolls that should collect dust on a shelf, seen but never held."
    z "Dreams do not belong to science; they belong to art.\""
    z "-Dr. Seth Schumann, one week prior to disappearance."
    nvl clear
    scene bg dark with fade
    show text "{color=#fff}The Prologue to a Dream of Home" at truecenter with dissolve
    pause 2
    hide text
    
    scene bg munich with flash
    d "Are you absolutely certain about this, Emerson?"
    d "I can't believe the higher-ups would spend billions of dollars out of simple charity. The entire project reeks of fraud and political agenda."
    d "There must be an ulterior motive. You already know that, I'm sure."
    d "You're not as far gone as those wizards in the 1° Inner Circle, not yet anyway."
    d "It's obviously a front for something filthy; invasion, nuclear weapons development, human experimentation..."
    o "Don't be ridiculous, human experimentation?"
    d "Not to mention, the pay's no better!"
    d "So why?"
    d "Why move to a godforsaken island on the other side of the world?"
    o "It's not about me, Erik. It's about preserving the species."
    o "I'm not sure we'll survive another war."
    o "Tensions with Russia are higher than ever, and our existence hangs in the balance."
    o "Naturally, the next step is to create a foundation for the next generation."
    o "If the worst case scenario comes to pass..."
    o "Then the Hall of Records will preserve everything we've learned."
    d "And? What's the {i}real{/i} reason?"
    o "The real reason...?"
    o "I thought maybe, just {i}maybe{/i}, I wouldn't be able to hear you whining from a distance of ninety-five hundred kilometers."
    d "Don't be an ass and just tell me."
    d "Why {i}this{/i} particular wild goose chase?"
    d "You have a thousand better offers."
    "....."
    "The conversation drops to a whisper."
    o "Listen closely."
    o "You're sworn to secrecy, understand?"
    d "O-Of course, spit it out."
    "....."
    o "Okay."
    o "It's about Dr. Schumann."
    o "He has a plan..."
    o "I think... he can probably do it."
    o "He wants to take control of the Inner Circle."
    d "A-Are you insane?"
    o "We all know about their corruption, but no one can stop them."
    o "Seth can stop them."
    d "A coup d'etat, then?"
    d "You'll be killed if you're caught. You know that, right?"
    d "Not {i}just{/i} killed, either."
    d "They'll put you in a sensory deprivation chamber for weeks - months, maybe - until there's nothing left..."
    o "I'm not finished."
    o "We need your help, Erik."
    o "We need someone here, in Munich, on the inside."
    d "Well, that's just great!"
    o "....."
    d "....."
    o "So, you're in then, right?"
    d "Wouldn't have it any other way."
    d "Not happy about it, though."
    o "Spectacular."
    "....."
    d "Shall we discuss treason over a beer, then?"
    d "The usual place is closed... how about the new one? It's downtown, not a far walk from here."
    o "The one that's always open?"
    d "Isn't that perfect?"
    d "Now you can go from binge drinking all night to eating breakfast, without driving, and already be at work in the morning."
    
    scene bg dark with fade
    show text "{color=#fff}Munich, year one of the Second Renaissance.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}33 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    stop sound

    scene bg study with fade
    play music "music/pleading_child.ogg" loop
    z "Finished moving in today. Our space is \"cozy,\" to put it amiably."
    z "The food isn't bad, though."
    z "The head chef - an absurd, stereotypical, expatriate Russian named Rasputin - is one of many notable individuals sharing my quarters."
    z "They're temporarily keeping us underground. I'm told it's only until our housing is finished."
    nvl clear
    z "More likely, it's because we're in Russian territory and could easily be killed if we're found."
    z "It's like living in a war submarine. Nothing like the fear of death to increase productivity."
    z "Our bunks are adjacent to the lab, and we're working on the Hall of Records around the clock."
    nvl clear
    z "A part of me hopes this project isn't a façade."
    z "A universal encyclopedia, no matter how unfinished, might do someone some good at some point."
    z "But that's my optimistic side speaking."
    z "Secretly or otherwise, we all know the reason we're here."
    z "We're the front line in the invasion of Russia."
    nvl clear
    z "They say the computer will be powered by two nuclear generators, as if there wasn't enough proof already."
    z "The more I think about it, the more I agree with Dr. Schumann's plan."
    z "If our colony becomes self-sufficient, it could break away from Munich's government."
    z "Using Dodgson's connections, we can replace members of the Inner Circle with our sympathizers."
    nvl clear
    z "Seth claims to have something big - some new evidence about their leadership that should cause rioting."
    z "So, at the right moment, we release the information, using the chaos to overthrow the 1° Inner Circle from the inside."
    z "Then we'll be free to establish our colony as the capital of a new republic."
    nvl clear
    z "If it works, it could prevent the upcoming war."
    z "Even if we fail, the encyclopedia will save our knowledge for the next generation."
    z "Living conditions and snoring Germans aside, there's no downside to coming here."
    z "The island is beautiful on the surface, judging from what I've heard and what little I saw on the way in."
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #1, recovered from journals.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}31 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text

    scene bg records two with fade
    z "The project is XXXXX smoothly."
    z "The XXXXX nuclear generator is finished and the Hall of Records itself is at an estimated three-fourths completion."
    z "No word about our housing. Rumor has it the Russian Navy is conducting tests around our island."
    z "Tensions are running high; everyone has cabin fever."
    nvl clear
    z "People say it's because of the smell. The air is thick and it tastes like metal."
    z "Rasputin almost killed a man over a biscuit yesterday."
    z "To summarize: you're really missing out, comrade."
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #2, part of a letter to Erik Dodgson.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}30 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    
    scene bg lake with fade
    play sound "sound/waves.ogg" loop
    z "I've never been so relieved to feel the sun."
    z "German submarines are patrolling the region nonstop; someone in Munich must've heard about our predicament."
    z "To celebrate the Russian retreat, we've been granted a week of paid leave."
    z "Moving into our new housing didn't take long and we've all been outdoors since then."
    nvl clear
    z "There's something about this area... sure, the colors are a bit brighter after living in the dark for two years on end, but there's something more to it."
    z "I can't seem to pull myself away from the ocean."
    z "I'm writing this in a notebook on a rocky beach, listening to the sound of waves as the tide comes in."
    z "I hope you're enjoying my prose. I've worked oh-so-hard on it, after all."
    nvl clear
    z "You asked about the Hall of Records. They're saying it's classified information, but let's just say that it's XXXXXXXX."
    z "To be honest, I'm much more excited about Dr. Schumann's other work - a device called the Laplacian Image Oscillator."
    z "Only a vague idea of what it is or what that means, at this point. He's the fickle, secretive type, as you know well by now."
    z "I think he enjoys confusing people by speaking in riddles, but he never outright says so, so people just think of him as an \"eccentric.\""
    nvl clear
    z "That in itself might be one of his inside jokes; a genius, albeit a difficult and hopelessly misunderstood one."
    z "What an interesting role to play."
    z "He's never called himself a genius, after all. The world calls him one, so he must act the part of one."
    z "Perhaps the most shocking part of this whole scenario is that the same eccentric is set to wed."
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #3, letter to Erik Dodgson.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}29 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    stop music fadeout 2.5
    stop sound fadeout 2.5
    
    scene bg cabinet with fadehold
    play music "music/traumerei.ogg" loop
    play sound "sound/marco.ogg" loop
    z "Mary Schumann: a light-haired, traditional, fragile, almost doll-like partner for the mad genius."
    z "Like Rasputin, she is an expatriate Russian; unlike Rasputin, she's a former member of the aristocracy."
    z "Most of us here can understand his taste, especially considering how she came here as a chef's assistant."
    z "We had her nicknamed Rasputin's Little Helper, like she was some sort of Slavic fairy tale character."
    nvl clear
    z "Seth put an end to that when he proposed without so much as mentioning it."
    z "The others are still afraid of him - they act like lions behind his back, kittens to his face."
    z "Seth obviously senses this and laughs at them in secret. In fact, I'm one of very few to establish any rapport with the difficult fellow."
    z "I even consider him a close friend."
    nvl clear
    z "Seth has formed an elite, exclusive group (his words, spoken with a degree of irony) which he calls his Cabinet."
    z "In practice, this is a small club of our leading scientists, myself included, who smoke cigars and play chess together."
    z "We also serve as his advisors - he'll often ask us for advice in either an official or unofficial capacity."
    nvl clear
    z "Officially, we are developing the most powerful supercomputer on Earth, the Hall of Records."
    z "Unofficially, we are developing LIO, what Schumann calls a memory projector."
    z "It's all part of the Narcissus Project."
    z "We still receive funding from Munich, but the project is XXXXXXXXXX, for all intents and purposes."
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #4, recovered from journals.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}27 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    
    scene bg cabinet with fade
    z "Observing the relationship between Seth and Mary is a curious thing."
    z "As a former aristocrat, she must be used to dealing with unpredictable, strong-willed men."
    z "From my perspective, she's entirely unaffected by his mood swings."
    z "It's as if she interprets the events of her own life as an outside observer."
    z "She could stare at the Devil himself without flinching."
    nvl clear
    z "Her eyes are empty, all-seeing but not feeling."
    z "She has a faraway look, a melancholy detachment from herself."
    z "But the way she smiles when Seth is around is adorable - it is almost childlike and completely trusting."
    z "What a fitting mate for a man tortured with a photographic memory and a thousand hells in his imagination."
    nvl clear
    stop sound fadeout 1.5
    
    scene bg records with fade
    z "In other news, the Hall of Records and both generators are finished after many delays caused by the usual suspects."
    z "From this point forward, the Hall of Records will do our work for us."
    z "It's running a program designed to crawl the web and classify raw data according to certain patterns."
    z "This data will be compressed with Refract, a high-density information language and storage system we recently developed."
    nvl clear
    z "XXXXXXXX compared to the function of DNA."
    z "I have an uneasy feeling that science is killing God."
    z "Who was it again that called science \"the Tree of Death?\""
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #5, recovered from journals.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}24 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    
    scene bg records two with fade
    z "Seth's been increasingly obsessed with his side project to the point of ignoring our original purpose entirely."
    z "None of us are complaining, though, since we're just waiting on Refract to finish running."
    z "Did I mention? It's expected to take twenty years or more to record and translate ninety-five percent, then an indefinite period of potentially decades on the rest."
    nvl clear
    z "What's more is that this \"five percent\" refers to any and all unindexed information... so we honestly have no idea on the physical size of this fraction."
    z "Seth calls five percent an overly conservative estimate issued by an ignorant Munich."
    z "For us, it'll be like watching a loading bar get stuck at ninety-five, waiting with bated breath as the remaining five percent takes longer than everything before it, not knowing whether we should let it finish or just reboot."
    nvl clear
    
    scene bg lab with fade
    z "Anyway, the hard work is done. And now, we twiddle our thumbs."
    z "The other day, Seth explained to the Cabinet how his memory projector could be used with Refract to depict artistic, creative processes taking place in the subconscious mind."
    z "It'd be a first, to be sure."
    z "A direct communication more intimate than telepathy, like two people sharing the same dream."
    nvl clear
    z "Apparently, Refract's storage language is so efficient and versatile that even a human brain could be stored using today's technology, given enough time to copy such an amount of data."
    z "He also announced plans to develop a second device, something called a Functional Image Reader, which will record the results of a comprehensive brain scan."
    nvl clear
    z "The truly interesting part about this work?"
    z "It's more than just science; it's art. At least to Seth."
    z "There's no brief way to explain why the mind will reveal itself as art when translated with Refract and projected with LIO."
    nvl clear
    z "A raw image, of memories of past and future - the comprehensive record of a life from beginning to end - compressed into a single file written in Refract's language."
    z "Like light passing through a prism, this language transforms into a reality we can see and feel."
    z "A life, starting and ending with a single desire, fulfilled by the will, spoken in tongues of light and sound."
    nvl clear
    z "Yes, I'm beginning to understand now."
    z "Refract is the language of God."
    z "What could exist without the prism of our consciousness?"
    z "Therefore, I redact my earlier statement. Science isn't killing God."
    z "Art is creating God."
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #6, recovered from journals.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}13 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    stop music fadeout 2.5
    
    scene bg lab two with fadehold
    play music "music/child_falling_asleep.ogg" loop
    z "The silence from Munich is unnverving. No word from either Dodgson or the Inner Circle in over a decade."
    z "We welcomed it at first, mostly due to our near-universal antipathy toward the whole lot."
    z "It wouldn't be strange if they discovered our side projects, cut the funding, and abandoned us here."
    z "We've been prepared for it, and that's why we've made ourselves self-sufficient."
    nvl clear
    z "The unsettling part of it?"
    z "Funding was briefly halted a few years ago, then continued soon after, with no explanation."
    z "Some have speculated that our patrons have XXXXXXX without our knowledge, and ownership of the Narcissus Project has changed hands."
    z "In the end, there's no telling until we see for ourselves."
    nvl clear
    z "Seth means to proceed with his plan regardless. He'll send a group of \"ambassadors\" to Munich in three days."
    z "Under the guise of a progress report, they'll anonymously release Seth's valuable information to the media, effectively sowing the seeds of revolution."
    z "They'll take advantage of the panic to start riots, infiltrate the Inquisition using our connections, then wipe out the 1° Inner Circle."
    z "Further details are only disclosed to the ambassadors themselves."
    nvl clear
    z "In other news, Mary Schumann is deathly ill."
    z "Her body, sickly and frail since childhood, seems to have buckled under the stress."
    z "Seth's judgment is in question. There are rumors that his usual demeanor has collapsed entirely."
    z "Most odd of all this, I haven't seen him for over a week."
    z "He typically consults me daily, both on matters of great and little importance."
    nvl clear
    z "Still, this plan has been in the making for over twenty years and is not easily postponed."
    z "I'm afraid for both the Narcissus Project and the life of our colony."
    z "And, more than anything... I'm afraid for Dodgson."
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #7, recovered from journals.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}11 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    stop music fadeout 1.5
    
    scene bg lake with fade
    play sound "sound/wind.ogg" loop
    z "Sometimes I have to wonder why the worst things happen to the greatest people."
    z "When there's seemingly no karmic influence at work, when there's nothing to be gained from their suffering... I wonder why."
    z "When there's only torment, with no lesson to be learned from it, wrought by twisted minds or simple bad luck..."
    z "It seems to be hell for its own sake."
    nvl clear
    z "A long time ago, Dodgson once told me that he suffered from nightmares."
    z "These were nightmares of inconceivable horror and agony, often involving sleep paralysis and vivid hallucinations."
    z "He'd wake up in terror, but the dream wouldn't end."
    z "He'd try to move, but his body wouldn't respond as demons played above his bed."
    nvl clear
    z "He joked that maybe it was because of past trauma, or maybe it was punishment for something he did in a past life."
    z "In the end, there wasn't a clear reason for it."
    nvl clear
    z "I've tried to rationalize these things as an unfortunate aspect of a greater plan."
    z "I thought they must be hints of a lesson to be learned, or else the end result of a poorly made choice."
    z "Witches burned at the stake feel no such sentimentality."
    z "The old man whose son is taken by the executioner sees no merciful reason for his torture."
    z "All that's left is the bitter taste of a life wasted."
    nvl clear
    z "The ambassadors were sent a few months ago and only one has returned."
    z "His initial report was brief."
    z "He called it \"an inhuman massacre.\""
    z "After a day of rest, he was prepared to speak in more detail."
    z "His report is as follows."
    nvl clear
    stop sound fadeout 1.5
    
    scene bg munich two with fade
    play music "music/the_forbidden_magic.ogg" loop
    z "\"Upon arrival, the forty of us were greeted by prestigious members of the 1° Inner Circle and led to a dining hall."
    z "In the center of the room there was a table lined with refreshments."
    z "Men wearing bird masks were seated on the far side in leather chairs elevated on a stage-like pedestal."
    z "We immediately recognized them as the Inquisition, a division of elite guards formed to protect the Inner Circle and its secrets."
    nvl clear
    z "The arched ceiling of this room reached several meters high and was decorated by an extravagant chandelier."
    z "There were one-way mirrors lined across the wall at a high point, above where the ceiling of adjacent rooms would be."
    z "It's thought that these were for spectator seating."
    z "There must've been men drinking fine wine and smoking cigars in booths just behind the mirrors."
    nvl clear
    z "At this point, it was painfully obvious that we were already dead... we were mostly wondering just how painful it'd be."
    z "A single member of the Inner Circle tapped my shoulder, smiling widely and telling me to follow him."
    z "Pressured by our captors, the other ambassadors began to eat and drink, knowing well that this meal would be their last."
    z "I gave them a short goodbye and prepared to follow the man.\""
    nvl clear
    
    scene bg dark with fade
    z "\"We passed through winding halls and spiral staircases until reaching the VIP section of the massive structure."
    z "This place was, without exaggeration, a labyrinth; it was a bizarre maze of Victorian architecture, walls lined with paintings that seemed to repeat in sequence."
    z "I was made to put on a blindfold."
    z "When it was removed, I saw an elevator, hidden in plain sight (on the third floor, if I counted correctly) and seemingly innocuous."
    nvl clear
    z "I was pushed into the elevator alone, my guide waving from the hall behind as if to say \"have a nice trip.\""
    z "The door closed. I examined the panel to find a single button: B5."
    z "This trip was obviously meant to be one way."
    nvl clear
    
    scene bg fractal with fade
    z "The elevator reached the fifth basement with a charming \"ding.\""
    z "As I stepped out into the dimly lit corridor, it was as if I'd entered a separate universe."
    z "The walls and floor were covered with blood and other filth."
    z "The air was suffocatingly thick - it felt like my veins would clot."
    nvl clear
    z "The smell was unbearable."
    z "I can only describe it by saying that it was like a hundred people had taken a bath in molten sulfur."
    z "I felt a burning sensation on the back of my neck and doubled over with nausea."
    z "The elevator doors slid shut at the same time and it began returning to floor number three."
    z "Upon seeing this, I lost all hope and resigned myself to what I expected to be an unimaginably cruel and drawn out death."
    nvl clear
    z "I realized... that this floor truly was a separate universe."
    z "The people many floors above intentionally created this place, with their imagination... and solely for their own amusement."
    z "What's more, they closed it off as if to remove themselves from it, like they could continue their lives without a second thought as long as it stayed in the ground five stories deep."
    z "The idea that they could waive responsibility and live without guilt as long as it wasn't seen... this was the most disgusting part of it."
    nvl clear
    z "I walked past cells filled with moaning war criminals."
    z "They were being tortured in various ways."
    z "Chinese water torture, with water dripping between the eyes; medieval torture using the rack; sensory deprivation and isolation..."
    z "Munich's vast repertoire of killing methods means little in the face of their duration."
    nvl clear
    z "When you consider how much pain can be inflicted on a person, there's a general upper limit before the person loses consciousness."
    z "The trick to performing torture is keeping the victim conscious for as long as possible while reaching this upper limit."
    z "In modern day Germany, the victims are kept alive longer than naturally possible by using blood transfusions, stimulants, and feeding tubes."
    z "I've seen severed heads kept conscious with no body in sight."
    nvl clear
    z "Time passed slowly for me."
    z "I filled it by walking the hallway from end to end, trying to wrap my mind around the unimaginable cruelty of this place."
    z "XXXXXXXXXXXXX for agreeing to take part in killing potentially innocent victims."
    z "Like I said, it felt like I'd XXXXXXX another universe - a universe designed specifically to inflict psychological and physical pain."
    z "The worst possible future out of a million others."
    nvl clear
    z "You asked if there was anyone I recognized."
    z "I can say it with certainty. I saw at least two."
    z "The first: one of my former colleagues, Jack Robinson from Berlin."
    z "The second: Erik Dodgson, a high-ranking member of the Inner Circle.\""
    nvl clear
    stop music fadeout 1.5
    
    scene bg lake with fade
    play sound "sound/wind.ogg" loop
    z "This is where I stopped reading. I don't feel the need to record the rest in any detail."
    play music "sound/wind.ogg" loop
    z "From what I gather, the man was eventually retrieved by his captors and subjected to a particularly gruesome scene in the dining hall, where the rest of his group had been slaughtered by the Inquisition."
    z "He was sent back unharmed to serve as an example for the rest of us."
    nvl clear
    z "XXXXXXXXX be the last entry in this journal."
    z "XXXXXXXXX burn it tomorrow."
    z "I don't know what else to say."
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #8, recovered from journals.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}10 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    stop sound
    
    scene bg fractal with fadehold
    play music "music/child_falling_asleep.ogg" loop
    z "They want to make me realize something, but I don't know what."
    z "I can't resign to the thought that this is meaningless. I have to be here for a reason."
    z "What are they showing me? How long have I been here?"
    z "I don't remember anything about my own life."
    nvl clear
    z "Am I still alive? If so, then..."
    z "What's my name?"
    z "Who {i}am{/i} I?"
    nvl clear
    z "Sometimes I forget that the visions aren't real."
    z "I forget that everything I'm seeing is a dream constructed from my memories."
    z "I see it even when my eyes are open..."
    z "...But when I shift my line of sight, the dream falls apart, and all that remains is the pitch black darkness."
    z "I feel like I'm floating through space."
    nvl clear
    z "I always hear the same sound when I dream."
    z "It's more real to me than anything else, and it's the only thing keeping me somewhat sane."
    z "It's the sound of water."
    z "I can hear waves lapping against a shore."
    nvl clear
    z "I imagine myself sprawled out on the grass beside a lake at night, staring at the moon's reflection."
    z "Following the ripples as the glass is broken by a thrown stone."
    z "I can see my reflection in the water."
    nvl clear
    z "They want to make me realize something, but I still don't know what."
    z "Am I supposed to remember who I was?"
    z "How long will this last, and what should I do to end it?"
    z "No matter how much I think about it, nothing changes."
    z "I don't even know who's keeping me here anymore."
    nvl clear
    z "I can't even rip out my feeding tube."
    z "All I can do is stare at a single point in space and think about why I'm here, or what I did wrong."
    z "I can't track the days based on my sleep-wake cycle anymore."
    z "I also can't tell whether I'm being drugged or not."
    nvl clear
    z "I have absolutely no way to distinguish between my imagination and reality."
    z "I would do anything just to see a human face or hear the sound of music again."
    z "I'm floating through endless dreams."
    z "I just want to die."
    z "Please, just let me die."
    nvl clear
    scene bg fractal two with fade
    z "Every time I wake up, I expect to be somewhere else."
    z "I expect to see a familiar ceiling, or my wife's face, or an open window with sunlight shining through."
    z "I expect to crawl out of my warm bed to the smell of breakfast and begin my usual work, coffee in hand."
    z "But no matter how many days and nights pass, I keep dreaming."
    z "I never really wake up."
    nvl clear
    z "My dreams continue without interruption whether I'm awake or asleep."
    z "Still, the dreams I have while I'm asleep are gentler."
    z "I can briefly feel that I'm somewhere else entirely."
    z "I can forget that I'm still drifting on an ocean of eternal blackness."
    nvl clear
    z "My consciousness slips in and out at random intervals because there aren't any memories for me to associate with each day."
    z "I must be suspended on some kind of liquid that simulates zero gravity."
    z "I'm like a mosquito held in amber, perfectly preserved but hollow."
    nvl clear
    z "There's no concept of time or space to me."
    z "There's nothing to separate one thing from everything else."
    z "I'm the only thing that exists."
    nvl clear
    scene bg fractal three with fadehold
    z "If I could just see my wife's face..."
    z "If I could just hold one of Emerson's letters..."
    z "If there's any ultimate source of good in this universe..."
    z "If love can still reach me here..."
    z "If I could just remember my name..."
    nvl clear
    stop music
    z "\"Erik...?\""
    nvl clear
    scene bg white with flash
    play sound "sound/clock.ogg" loop
    z "I'm struck with a blinding light."
    z "The world shatters and fades to white."
    z "I'm wrapped in something warm and I can hear a clock ticking beside my ear."
    z "I am... Erik Dodgson."
    nvl clear
    
    scene bg study with fade
    pause 1
    scene bg dark
    show text "{color=#fff}Seth Schumann, master bedroom of Schumann residence{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    scene bg study
    z "I wake up to find Mary breathing heavily." with vpunch
    z "She must be having another nightmare... I'm not sure if I should wake her."
    z "I love her more than anything."
    z "I love her more than everything else combined."
    nvl clear
    z "In the past, I'd never felt this almost pathetic desperation toward anything."
    z "I viewed my own life with a sense of ironic detachment, like I was watching someone else act out my own existence."
    z "Everything I'd ever worked for, everything I'd ever spent time creating - I never felt much attachment."
    z "My life's work has been called genius, but I never thought of it as particularly exciting or valuable."
    nvl clear
    z "The \"great minds\" who saw something in me and elevated me to my position?"
    z "Their lives were inconsequential to me and so were their opinions."
    z "When my classmates in school found love, I laughed at them."
    z "I saw their infatuation as sickeningly sweet and insubstantial."
    z "Love was sophistry to me."
    nvl clear
    z "No matter what I made - whether it was a 5th grade science fair project or a Hall of Records - it always lacked something."
    z "It was all imperfect, fatally flawed in some abstract way invisible to everyone but myself."
    z "My creations were rejects that I eventually settled with after failing to give birth to the truly immaculate \"somethings\" in my imagination."
    z "They're abortions. But, they survived."
    z "The world worshipped my crippled children, so I was invited to join the prestigious Inner Circle (of disgusting old men and their hobbies.)"
    nvl clear
    z "I laughed my way through school, college, the Inner Circle, and the rest of my life."
    z "Laughter was my ammunition against the sophistry of \"love\" that I never understood."
    z "When my long-lost father died, I laughed at the way he went."
    z "When I graduated from school, I laughed at my peers for imagining themselves as gifted."
    nvl clear
    z "When I won, when I lost, when I accomplished something great or nothing at all... I laughed."
    z "My life seemed to me a pre-orchestrated game designed to try and make me feel emotions other than cynicism and lethargy."
    z "It was sickeningly sweet and oozing with sentimentality."
    nvl clear
    stop sound
    
    scene bg dream cinema with fade
    play music "music/the_clock_tower.ogg" loop
    z "It's like I was watching myself perform a play where my mother signed me up as the main character."
    z "Yes, I was laughing with the audience, but I was also up on stage, playing out my role with obvious unenthusiasm and spitting out sappy lines from memory."
    z "Either way, I wanted the curtain to close."
    z "I had already seen through the façade the other characters and my mother were setting up for me."
    nvl clear
    z "My mother wanted me to be happy, and I laughed from my seat, but I smiled from the stage out of dishonest obligation."
    z "I loathed the home videos, the report cards, the nauseating flow of plastic trophies won at little league tournaments."
    z "No one ever knew me."
    z "How can a person know a \"laugh?\""
    z "A \"laugh\" can't be known. A \"laugh\" can't be loved."
    nvl clear
    
    scene bg study with fade
    z "I couldn't love anything and I couldn't be loved because I didn't feel {i}real{/i}..."
    z "But that was a long time ago and I've grown up since then."
    z "I've learned how to hide small bits of honesty in my chronic laughter."
    z "I found people who would laugh with me and even enjoyed their company."
    z "And most of all, I learned to accept my affliction as a necessary aspect of the concept called \"myself.\""
    nvl clear
    z "Mary was the first person I felt genuine affection for."
    z "She was {i}interesting{/i}. I couldn't predict her personality, which is more than I can say for most anyone else."
    z "It must've stimulated my scientific instinct."
    z "I wanted to dissect this human being."
    nvl clear
    
    scene bg munich with flash
    play sound "sound/wind.ogg" loop
    z "We met at a café in Munich during my last year of postgraduate education."
    z "I thought I'd re-entered the weird headspace I get during especially vivid dreams... we met due to unexplainable coincidence and various surreal miracles of chance."
    z "It's the only time I've experienced magic."
    z "It grossly defied all probability and permanently warped my sense of logic."
    nvl clear
    z "Fittingly enough, that's exactly what I needed. I dearly wanted something to confuse me."
    z "I wanted to {i}not{/i} understand."
    z "She was the perfect medicine for my incurable illness."
    z "She spoke... and I didn't laugh in my head."
    z "I was enchanted."
    nvl clear
    z "Let me be frank: an aristocrat was the last type of person I expected to fall in love with."
    z "I abhor the culture. I can't stand the ballroom dances, the pseudo-intellectual conversations about modern art, the strangulating sense of ceremony..."
    z "The drawn-out weddings performed in chapels more costly than a hundred lifetimes as a prole... I could go on."
    nvl clear
    z "Mary threw it all away - status, comfort, money, and family - to live in Munich as a cook."
    z "That was my initial fascination with her."
    z "What kind of irresponsible, incomprehensibly-principled person would do something like that?"
    z "I've accused her of being a Russian spy at least once."
    nvl clear
    z "We met weekly over the course of the next several years."
    z "Our rendevous were kept secret due to constraints on my personal life as a member of the Inner Circle."
    z "Any casual relations with foreign women are strictly forbidden, Russian ones in particular."
    z "It's part of the idiotic \"racial purity\" initiative."
    z "It's considered treasonous to mix Russian with German blood."
    nvl clear
    z "When I was recruited to lead the development team, I'd already been daydreaming about escape plans for a while."
    z "Until now, my schemes were limited to the kind of fanciful, naïve ideas you'll sometimes cook up when you're half asleep."
    z "But this one was {i}real{/i}."
    nvl clear
    z "It was a practical, achievable method of reaching a place where I could live happily with Mary."
    z "Another stroke of magic performed by god-knows-who-or-why."
    z "I've only told this to Emerson, but Mary is above and beyond the single most important reason I chose to lead this project."
    nvl clear
    stop sound
    
    scene bg records two with fade
    z "It was around this time when I came across, in a dream, the idea to blackmail Munich's government using the nuclear reactors that were to power the Hall of Records."
    z "I'd grown \"increasingly distasteful (as I confided in my peers) of the Inner Circle and its governing structure.\""
    z "No need to euphemize here. I hated them deeply."
    nvl clear
    z "My allies, Jean-Paul Emerson and Erik Dodgson, shared similar sentiments."
    z "We wanted to leave, preferably to somewhere as far away as possible."
    z "Another country, another planet... another universe, if we could."
    nvl clear
    
    scene bg munich two with fade
    z "I eventually received a tip about Munich's torture chambers and unlawful internment camps."
    z "That's when I started seriously considering using this information as a bargaining chip to establish an independent state."
    z "I figured we could embezzle a percentage of the funding and use it drive our colony toward self-sufficiency, then threaten to hand our nuclear reactors to the Russian military."
    nvl clear
    z "On top of that, we'd cause a media circus over the work camps, then spawn riots and infiltrate the Inquisition."
    z "That was my initial plan."
    z "It turned out very differently."
    nvl clear
    
    scene bg study with fade
    z "Only Mary knows this, but we'd already seceded from the German government when contact was cut ten years ago."
    z "I used the nuclear reactors and the Hall of Records itself as blackmail, convincing them we'd have the Russian Navy's support if need be."
    z "When funding resumed, the money didn't come from them..."
    z "It came from Russia."
    nvl clear
    z "It was collateral for the life of Mary Steiner, prodigal child of the communist party's Ministry of Information."
    z "We convinced them we were insurgents. Scandinavian anarchists, to be specific... it's a funny story, actually."
    z "We had a lovely time making the hostage videos."
    z "Mary is a natural actress, as it turns out."
    nvl clear
    z "So, in the end, we threatened to hand her over to Germany as penance for the Minister's crimes against humanity."
    z "She'd probably be tortured, interrogated, and sent back to Russia one piece at a time... scary stuff, at the end of the day."
    z "And that's the story of how Mary and I received an early inheritance from her deadbeat father."
    z "They agreed to halt the investigation in exchange for her safety, but I definitely read about the mistaken capture of twenty Norwegian \"anarchists\" (crab fishermen) off the coast a week later..."
    nvl clear
    z "We struck at the perfect time, when paranoia was most rampant. We had both countries in our back pocket."
    z "At this point, I was confident enough to try stirring up a coup d'etat."
    z "That was my first mistake."
    z "I overestimated my reach... and thirty-nine men are dead because of it."
    nvl clear
    z "Anyway, I've gotten off topic."
    z "I'd rather not continue reminding myself of my mistakes."
    z "The point is that I found a reason to live in Mary Steiner."
    nvl clear
    z "The Narcissus Project's true goal is to create a world where we can live together in peace."
    z "I believe it's succeeded in that regard."
    z "From this point on, it'll be about protecting that home."
    z "She's sleeping soundly again. I'm glad I didn't wake her."
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #9, recovered from Schumann's audio journals.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}9 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    stop music
    
    scene bg lab with fade
    play sound "sound/clock.ogg" loop
    z "Mary's sickness has passed."
    z "After a six month search, I found a doctor who could cure her inexplicable illness."
    z "She was diagnosed with a nameless, never-before-seen disease affecting the limbic system."
    z "She's been prescribed a medication used to treat severe autoimmune disorders."
    z "One more round of treatment should finish the job. Two more weeks until the curse is lifted."
    nvl clear
    z "Her seizures, however, will continue for months, and the medication's toll on her body could last indefinitely."
    z "It's a miracle that her already frail body could withstand it."
    z "The rest of our colony is in a similar state."
    z "Emerson is particularly devastated over the news about his best friend; he hasn't been seen outside his room in weeks."
    z "Morale is at an all-time low, but we're not in danger. At least for now."
    nvl clear
    z "The Socialist Republic of Germanic Nations has, in fact, formally recognized our little settlement of twenty-five thousand as an independent city-state."
    z "The Marxist-Leninist States of the Russian Federation are expected to follow suit in the near future."
    z "The former is afraid that we'll establish an alliance with the latter."
    nvl clear
    z "Their message with the one surviving ambassador was actually twofold."
    z "Yes, they'll wipe us out in a heartbeat if we encroach upon their territory..."
    z "...But they'll stay out of our business otherwise because of our strategic military and social value."
    nvl clear
    stop sound
    
    scene bg munich two with fade
    play sound "sound/wind.ogg" loop
    z "In Munich, the Hall of Records is an icon."
    z "It's a symbol of Germany's technological progress and humanity's thirst for knowledge."
    z "It's also technically a nonprofit entity, outside the realm of government influence."
    z "In addition to the threat of losing two nuclear reactors to the Russians, there's also the threat of losing the people's approval."
    nvl clear
    z "If the German government were to invade our colony and massacre twenty-five thousand scientists, doctors, cooks, and other cultural visionaries - not to mention our increasing number of children - it wouldn't go over well with the common folk."
    z "Even such a ubiquitous institution is limited in various ways."
    nvl clear
    z "Not everything can be censored; even the most top secret information will eventually drift into one of the internet's innumerable channels."
    z "Hiding the slaughter of twenty-five thousand civilians is an impossible task even today."
    z "On this occasion, the Inner Circle chose to seek out public approval by granting us independence instead of killing us like rats."
    z "Isn't that wonderful?"
    nvl clear
    stop sound
    
    scene bg lab with fade
    play sound "sound/clock.ogg" loop
    z "Ahh, the future is bright for us!" with vpunch
    z "My prototype for the Laplacian Image Oscillator is finished, thank god."
    z "I thought I'd have to scrap the damn thing if it was going to take another half-decade."
    z "It uses Refract's programming language, and if encoded correctly, the file should play like a movie."
    nvl clear
    z "The Laplacian Image Oscillator's depiction of memory should be unique to every individual."
    z "It's meant to reveal the raison d'etre, so its product will vary depending on the subject."
    z "On top of all that, the Functional Image Reader is officially in production and I expect to spend the next few years of my life with it."
    z "There's so much to celebrate!"
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #10, recovered from Schumann's audio journals.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}8 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    stop sound
     
    scene bg dark with fade
    play sound "sound/end_of_the_line.ogg" loop
    z "{cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05}
       {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05}
       {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXX 24-char... XXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} 
       {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05}
       {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05}
       {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05}"
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #11, destroyed.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}5 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    
    z "{cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05}
       {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05}
       {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} 
       {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05}
       {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05}
       {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05} {cps=*75}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{/cps}{w=0.05}"
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Emerson Records entry #12, destroyed.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}3 years until first test.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    stop sound
    
    scene bg dream cinema with fadehold
    play music "music/the_forbidden_magic.ogg" loop
    z "It's finished."
    z "I take a step back and survey my work."
    z "\"It's... {w}beautiful.\""
    z "Yes, that's it. I have no words."
    nvl clear
    z "The first test was a success, as we expected."
    z "Accurate representation of the most intimate aspect of a human being: the soul."
    z "From behind the one-way mirror of the laboratory, I can see my wife and unborn child."
    z "Of course, I can see them seated in the middle of the otherwise empty theater. But now, I can truly {i}see{/i} them."
    nvl clear
    z "Behind me, my peers are cheering wildly and sharing happy words."
    z "Some try to speak to me, but I'm enraptured. I can't take my eyes off the screen."
    with vpunch
    z "I fall to my knees, hands covering my mouth."
    nvl clear
    z "We used LIO alongside Refract and FIR..."
    z "My wife insisted that she be the first to try it, and I was afraid, but it worked."
    z "I was afraid she wouldn't come back. I couldn't live without her..."
    z "I would have nothing."
    z "But it's working, and it's so..."
    nvl clear
    z "Suddenly, I'm struck with my usual clarity of thought."
    z "I should be summarizing my findings."
    z "I absentmindedly exchange a few handshakes with the rest of the group, then return to my work."
    nvl clear
    z "\"File size: 2.4 petabytes."
    z "Subject: Mary Schumann."
    z "Audio content: a child, singing a nursery rhyme; birds can be heard chirping."
    z "Visual content: a city, also unrecognized. A town square, with a large tree in the center; an old woman feeding the birds."
    z "Very little distortion observed on first run."
    nvl clear
    z "No physical change detected but a slight raise in heart rate."
    z "In summary, an unparalleled success."
    z "Determined to be safe for public usage.\""
    nvl clear
    z "I lean back and stare at the empty ceiling of the familiar lab."
    z "Have I finally done it?"
    z "I glance at my still-shaking palm, filled with a sensation of completeness."
    nvl clear
    z "For the last thirty years, I've been living with a specific goal in mind."
    z "That goal was to create something perfect, or as close to perfect as possible."
    z "I don't know if it's achievable."
    z "I don't know if this achieves it."
    z "Nevertheless, it's still quite... {w}beautiful."
    nvl clear
    z "Is this the magic I've been searching for to pull me past this illusion?"
    z "What will I see through the looking glass?"
    z "Even now, I'm terrified."
    z "I'm just as terrified as I was when I started work on LIO over thirty years ago."
    nvl clear
    z "I don't want this creation to leave me."
    z "I don't want to be alone; that's what it comes down to."
    z "I don't want my work to be all for nothing."
    z "I want to create a perfect world, even if I know it's a foolish dream."
    z "I want to {i}see{/i} us."
    nvl clear
    z "I rummage through my pocket to find a scrap of paper, completely ignoring my colleagues."
    z "I need to preserve this moment."
    z "With rushed yet precise strokes, I begin copying down the image on the screen..."
    z "...Not enough ink."
    z "I toss the ink pen aside and grab another one." with hpunch
    nvl clear
    z "The image I'm drawing is a city."
    z "There's a clock tower placed atop a wooded hill."
    z "There's a large temple with an intriguing design."
    z "There's a tree made of stone, placed in the center of a bustling square."
    z "I scrawl the contents of the projection onto my scrap of paper."
    nvl clear
    z "Immediately afterward, I make a note of the unknown song's lyrics."
    z "I steady my hand and begin to pen the words..."
    nvl clear
    z "\"Isn't it a pretty tree?"
    z "One notch, then two, then three,"
    z "There's nothing fun to do here,"
    z "Somewhere else is where to be."
    nvl clear
    z "Isn't it a pretty tree?"
    z "One notch, then two, then three,"
    z "There's surely something fun there,"
    z "A place for me across the sea."
    nvl clear
    z "Isn't it a pretty tree?"
    z "One notch, then two, then three,"
    z "I found a picture in my dreams,"
    z "A wooden ship is what I see."
    nvl clear
    z "Isn't it a pretty tree?"
    z "One notch, then two, then three,"
    z "No snakes or birds, a dream of home,"
    z "Shining throne made out of me.\""
    nvl clear
    z "I take another look at my crude drawing."
    z "Is this the place my wife wants to see?"
    z "\"Wait...\""
    z "On the corner of the page... is a familiar sight."
    nvl clear
    z "\"Is that...?\""
    z "Yes. There's no doubt."
    z "It's the completed Hall of Records."
    nvl clear
    z "Now the question arises:"
    z "Is Mary seeing the future?"
    z "Or is she {i}creating{/i} it?"
    nvl clear
    stop music
    
    play sound "sound/bird_whistling.ogg" loop
    z "\"The subject is unconscious. {w}I repeat, the subject is unconscious.\""
    z "\"Dr. Schumann, there's been an emergency!\"" with hpunch
    z "\"What is it? What happened to Mary?\"" with hpunch
    nvl clear
    
    scene bg dark with fade
    z "\"She's... not breathing.\""
    nvl clear
    stop sound fadeout 2.5
    
    scene bg study with fadehold
    play sound "sound/cathedral.ogg" loop
    "The room is filled with the tinny music of a scratched classical record playing on a phonograph."
    "Not many people would use such an outdated piece of technology in A.E. 14."
    "There are only an estimated two thousand original pre-war models remaining, and records are generally only found collecting dust in the basements of avid collectors."
    "It would seem mawkishly sentimental to some, but it was preserved for a reason."
    "Schumann preferred an imperfect sound."
    "His prior life had been dedicated to achieving perfection in every pursuit, but he'd been reborn."
    "He'd awakened to the beauty of incompletion, of disorder, of fatally flawed artwork."
    "When his wife died, she died because of his lust for perfection."
    z "Perfection means nothing. It is stagnancy and death."
    z "To say it another way... for a thing to be truly alive, it must be flawed."
    z "Life exists because of its imperfection. The perfect root of existence cannot be known."
    nvl clear
    z "No man can see the face of God and live... Exodus 33:20."
    z "My wife saw it at the Dream Cinema, and her soul returned to the One."
    z "That's why everything I create will be blessed with faults."
    nvl clear
    
    scene bg lab two with fade
    z "After this revelation, I made a crucial change to the Laplacian Image Oscillator."
    z "I added static to the projections. To be precise, I programmed it to automatically bug the code produced by Refract."
    z "As a further precaution, I capped FIR's scanning capabilities at a maximum of ninety-nine percent."
    nvl clear
    z "So, for example... even if LIO were to interpret the code with 100%% accuracy, the projection would remain a broken version of the true will."
    z "The missing one percent of the subject's memories - the parts unrecorded by FIR - will prevent a perfect depiction of the soul."
    stop sound fadeout 1.5
    nvl clear
    
    scene bg records with fade
    play music "music/pleading_child.ogg" loop
    z "For many years, I thought that Mary's consciousness might be saved to the Hall of Records in some form."
    z "Since the Hall of Records was used as a server for Refract's code, I thought I might find traces of her memories and reassemble her within a simulation."
    z "I thought that if I could piece together the code as it was during the first test, then I should theoretically be able to redirect her awareness to a second self."
    z "It's the general principle behind mind uploading."
    z "They called the pursuit an effect of my \"madness.\""
    nvl clear
    z "It was not to be."
    z "Mary's data had been securely deleted by a fail-safe device I myself had designed to protect her if the Dreamshow went south (an unfortunately accurate prediction on my part)."
    z "In hindsight, maybe it was for the best."
    z "Maybe, somewhere in my subconscious mind, I'd chosen to protect her from my future self."
    z "If I'd been successful, I would've certainly disturbed her sleep."
    nvl clear
    z "I was filled with irrational emotion at the time, too engrossed in the possibility of seeing her again to realize that such a reanimation would be a disgrace to the dead."
    z "Of course, I had no qualms with performing my experiments on others."
    z "I had no conscience during those years."
    nvl clear
    
    scene bg lab with fade
    z "After reconfiguring the three Dreamshow devices, I began a series of animal tests."
    z "My cat, a wonderful Maine Coon named Erik after the man of the same name, was the first success."
    z "I made sure to backup the data this time."
    nvl clear
    z "We uploaded the code retrieved with FIR and Refract to a nearly exact simulation of our new city, Eridea... but something unexpected occurred."
    z "{i}The simulation came to life{/i}."
    z "The cat interpreted our matrix as physical reality and filled in the blanks we'd left on its own."
    nvl clear
    z "And so, I continued my quest to build a mirror universe where Mary could be remade, still expecting to somehow retrieve her memories."
    z "Soon after Erik's transfer to our simulation, human tests were resumed without permission by a unnamed member of my Cabinet, an infuriating and presumptuous man who overestimated his position."
    z "The second and third tests were performed in this manner."
    z "The former subject slipped into a coma after complaining of headaches and dissociation."
    nvl clear
    z "But the third test was different."
    z "He felt as though he'd received a divine revelation."
    z "He narrated the experience in eloquence and detail over the course of six hours."
    z "His speech was automatic, like he was reciting lines from memory."
    z "The transcript can be found in the Hall of Records, coordinates 20.XXXXXX, 110.XXXXXX, XX.XXXXXX."
    nvl clear
    z "Many terms referenced in this manuscript were unheard of until this point, and modern-day magic practitioners cite this text as the foundation for their new line of thought."
    z "Perhaps the most influential concept mentioned is that of Enchantment."
    nvl clear
    
    scene bg fractal two with flash
    z "To quote the third test subject, who remains anonymous even today for his own protection:"
    z "\"During my intercourse with the Overmind, I observed the method entities use to communicate outside of time and space."
    z "Each soul is like a neuron that forms synapses with the others using the energy of its will.\""
    z "Skipping ahead a little..."
    nvl clear
    z "\"Some of these neurons are much larger than the rest, and the smaller ones gravitate toward them."
    z "Normal souls cluster around these massive energy centers like stars around a black hole."
    z "As far as I can tell, the size of an entity's soul represents the force of its will."
    z "The souls with an especially strong \"will\" have an equally strong gravitational impact on the surrounding entities."
    nvl clear
    z "They communicate with a vast number at once using near limitless stores of energy, whereas the smaller souls will only form connections with the few in their immediate region."
    z "I had an impression that the small entities were somehow enchanted by whatever reaction was happening inside the large ones."
    z "They were gravitationally drawn to the strongest force of will... or they wanted to become like them."
    nvl clear
    z "When I thought about humanity's most notable personalities, I saw energy centers surrounded by millions of tiny lights arranged in inconceivably large city-like patterns."
    z "Even when I imagined an entity whose physical body died two thousand years ago, I saw beautifully intricate societies made of stars in concentric circles around it."
    z "They were stacked in layers like bricks. Together, they formed a skyline of complex architecture made of neon light."
    z "Souls travelled down channels like boats along a river, or like cars on a night expressway."
    nvl clear
    z "That's when I realized... they were feeding off the energy center, the soul with boundless energy in the middle of their colony."
    z "I asked myself \'Are they parasites? Or are they enslaved by the entity in the middle?\'"
    z "A childlike voice answered and explained the symbiosis of their relationship."
    nvl clear
    z "\'The small ones get energy from the big ones."
    z "The big ones ask them to help fulfill their will in exchange."
    z "The big ones take thousands of years to achieve their true will because of their size."
    z "So they enlist the small ones as little soldiers in their fight against entropy."
    z "The big ones will collapse if they can't find enough energy to use, after all.\'"
    nvl clear
    z "They were using each other as a fuel source. It's like the energy center is a god and the small entities are his followers."
    z "A god communicates his desire and the worshippers seek to fulfill it."
    z "They're Enchanted by his will."
    z "In exchange, they're granted a portion of the god's energy as a means to help finish his work."
    nvl clear
    z "When you consider that many of these gods lost their bodies thousands of years ago, it makes even more sense."
    z "To have an effect on physical reality, they need living followers."
    z "So they create synapses to channel a part of their own soul to living beings."
    z "All that's necessary is a willing recipient, and a desire that doesn't conflict with the god's."
    nvl clear
    z "This Enchantment occurs during dreams."
    z "Dreams are the place where souls can communicate outside of time in the physical realm."
    z "Each soul has its own color and sound... this changes depending on how it interacts with its environment."
    z "A state of passion or excitement may be indicated by a red hue. A blue tone may indicate calm or stillness."
    z "Yellow tones are generally paired with higher pitch... each color has a matching frequency...\""
    nvl clear
    stop music fadeout 1.5
    
    scene bg lab two with fade
    play sound "sound/clock.ogg" loop
    z "To summarize, the third test changed everything."
    z "Human testing was once again a possibility."
    z "I continued the experiments, properly this time, and saw positive results."
    z "Psychologically, Dreamshows appeared to give vital insight concerning a person's inner life and intentions."
    nvl clear
    z "There were exceptions."
    z "Some weren't prepared to face themselves in the looking-glass, or they lacked the ability to interpret what they saw."
    z "With this in mind, I restricted testing to those above age eighteen from that point forward."
    nvl clear
    z "The next years were dedicated to continuing Eridea's physical construction."
    z "I used the money we'd stolen from Mary's father to build the city of her dreams... of her Dreamshow, more precisely."
    z "It was enough to set it in motion, at least. Funding wasn't difficult once Eridea developed its own economy."
    z "My work - my life itself - was a shrine to Mary's existence."
    nvl clear
    z "During that time, I became a collector of sorts."
    z "I preserved the code produced by Refract in every test subject."
    z "I toyed with the idea of uploading them to my simulation... and eventually, I couldn't resist the temptation."
    z "The creation of my own universe had begun."
    z "{i}The individuals in the simulation behaved identically to their real-life counterparts, give or take one percent.{/i}"
    nvl clear
    stop sound
    
    scene bg dream cinema with fade
    z "When the Dream Cinema became an institution, I continued to expand my collection until the simulation became near-indistinguishable from reality."
    z "In theory, anyway."
    z "I've only run it briefly because the Hall of Records is using all of its resources on the encyclopedia."
    z "Very few people know of this secret."
    nvl clear
    z "I plan to destroy it sometime before my death."
    z "I'd hate for it to fall into the wrong hands."
    z "But, for now, it's still there... and the Hall of Records is less than one percent away from completing its archive."
    z "The Narcissus Project is very nearly complete."
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}Date unknown, A.E. 14.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}Recovered from Schumann's audio journals.{/cover}" at truecenter with dissolve
    pause 1.5
    hide text
        
    scene bg munich with fade
    play sound "sound/wind.ogg" loop
    z "In contrast to some of the more \"involved\" schools of magic, Enchantment seems to be, at first glance, little more than a consequence of the will's existence."
    z "A strong desire is imprinted upon the collective unconscious, then XXXXXXXXXX suitable hosts through subsequent connections in the Overmind."
    z "However, to overlook Enchantment as merely a chance interaction, devoid of intention, would be a MISTAKE."
    nvl clear
    z "Enchantment is more than a handshake between XXXXXXXXXX, or a brief connection between neurons."
    z "It is the continuation of one's deepest desires not unlike the preservation of genes through DNA."
    z "Yes, Enchantment is more than a step in the soul's evolution."
    z "It is also a means of reproduction."
    nvl clear
    z "The creation of a copy is the most expedient way for a soul to sustain its existence in some form even after the body's death."
    z "Unfortunately, I find myself unable to continue my research here XXXXXXXXX FEAR for my LIFE."
    z "A suitable entry to end on, I think."
    z "I hope the resolution of this matter finds its way to someone more capable than I."
    nvl clear
    
    scene bg dark with fade
    show text "{color=#fff}January 10th, A.E. 21.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}Last entry of the Emerson Records, hidden inside a grandfather clock.{/color}" at truecenter with dissolve
    pause 2
    show text "{color=#fff}Retrieved from the ashes of Emerson Mansion.{/color}" at truecenter with dissolve
    pause 1.5
    hide text
    stop sound
    
    scene bg dark with fade
    play music "music/the_clock_tower.ogg" loop
    z "ADDENDUM"
    z "The Emerson Records are a series of texts originally recovered from Jean-Paul Emerson's private collection of journals and personal correspondence."
    z "They've proven to be valuable resources in unmasking the secrecy of the Narcissus Project."
    z "Uploaded to the Hall of Records archive shortly after Emerson's departure from Eridea, they're now freely available as part of the public domain (current as of January 10th, A.E. 116)."
    nvl clear
    z "Unfortunately, many entries are incomplete due to fire damage received during the burning of Emerson Mansion in A.E. 21."
    z "Additionally, the letters were subjected to harsh censorship from the German government in response to the Information Security Mandate of Second Renaissance year two."
    z "Any copies of the original text have yet to be located."
    z "Despite this unfortunate incompletion, their influence on the social and psychological framework of modern Eridea cannot be underestimated."
    nvl clear
    
    scene bg munich two with fade
    z "During the Second Renaissance, many renowned scientists had taken to a philosophy that our world itself, even the reality outside of Schumann's cat box, is a simulation."
    z "According to this line of thought, our three-dimensional universe might be a simulation created by a higher civilization."
    z "In turn, this civilization might be living in a simulation created by an even higher civilization."
    z "The idea of a \"stack\" or \"string\" of an increasingly complex series of worlds is comparable to the concept of dimensions."
    nvl clear
    z "Theoretically speaking, there is no limit to the potential length of such a string."
    z "It could go on endlessly."
    nvl clear
    z "It should be noted that this concept logically follows current interpretations of quantum mechanics."
    z "The input material would be run through algorithms designed to simulate randomness, therefore creating a world with infinite possible states that collapses into a causal string when observed."
    z "However, this would be meaningless without organisms to observe and collapse the wave function, thus witnessing the causal string and making it \"truth.\""
    z "Until an observer exists, there would be only \"potential\" inside this cat box world."
    nvl clear
    z "This theory was abandoned by the majority after Schumann's disappearance in A.E. 15."
    z "However, it did not disappear entirely."
    z "Rather, the philosophy changed in name, but not in form."
    nvl clear
    z "The input material, or {i}prima materia{/i} - the unpredictable energy that scratches at the sides of a cat box without an observer - was called \"the soul.\""
    z "The observer's presence itself was renamed \"the will.\""
    z "This is because the observer can be thought of as an existence which guides the soul and fulfills its purpose."
    nvl clear
    z "The simulation's creators were referred to as \"gods...\""
    z "And the finished product of this work - the whole picture, as seen from the beginning to the end of an observer's life - was called the \"raison d'etre.\""
    nvl clear
    z "With Seth Schumann's life, a great number of new questions arose."
    z "Had he, with the Hall of Records and Schumann's cat, created a new universe with a single observer?"
    z "Could he indeed transfer self-awareness using LIO, Refract and FIR?"
    z "If the brain is considered to be like a satellite for consciousness instead of the source, had he simply redirected this signal to another \"self?\""
    nvl clear
    stop music fadeout 2.5
    
    scene bg fractal with fadehold
    play music "music/child_falling_asleep.ogg" loop
    z "{cps=12}Despite recent progress, the Narcissus Project remains shrouded in mystery.{/cps}"
    z "{cps=12}Only a small circle of Schumann's most trusted confidants were privy to the details of his reality simulation.{/cps}"
    z "{cps=12}One is made to wonder how far the experiments went... and when they ended.{/cps}"
    nvl clear
    
    scene bg dark with flash
    stop music fadeout 4.5
    with fadehold
    
    return