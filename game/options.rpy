













define config.name = _("Mushroom-Oasis")

define config.developer = "true"



define gui.show_name = False




define config.version = "1.1"





define gui.about = _p("""
""")






define build.name = "Mushroom-Oasis"








define config.has_sound = True
define config.has_music = True
define config.has_voice = True








define config.default_music_volume = 0.5
define config.default_sfx_volume = 1
define config.default_voice_volume = 0.5





define config.main_menu_music = "audio/music/main-menu-theme.ogg"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 65





default preferences.afm_time = 15
















define config.save_directory = "mushroomoasis-1676377963"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
