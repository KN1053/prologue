define fadehold = Fade(0.5, 3.0, 0.5)

init:
    $ flash = Fade(.25, 0, .75, color="#fff")

define config.name = _("The Prologue to a Dream of Home")
define gui.show_name = True
define config.version = "2.11"
define gui.about = _("""Scenes from Childhood, Op. 15 by Donald Betts.
Bird Whistling, A.wav by InspectorJ.
Ticking Clock, A.wav by InspectorJ.
Chaim Weizmann's Historic Laboratory by Deror_avi.
IMHM chemical laboratory by Jbryan317.
Study room of Lin Yutang House by Linyutanghouse.
Nasa images by BonnieReal.
Fractal images by Piotr Siedlecki.""")
define build.name = "prologue"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.main_menu_music = "sound/wind.ogg"
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "hide"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 57
default preferences.afm_time = 7.5

define config.save_directory = "prologue"
define config.window_icon = "gui/window_icon.png"

init python:
    
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')
