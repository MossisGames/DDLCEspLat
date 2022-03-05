init python:
    import datetime

screen subs:
    text "[subtitles]" xcenter 0.5 yalign 0.95 style "monika_credits_text" outlines [(absolute(2), "#000", absolute(0), absolute(0))] size 45

image credits_cg1:
    "images/cg/credits/1.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2:
    "images/cg/credits/2.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3:
    "images/cg/credits/3.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4:
    "images/cg/credits/4.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5:
    "images/cg/credits/5.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6:
    "images/cg/credits/6.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7:
    "images/cg/credits/7.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8:
    "images/cg/credits/8.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9:
    "images/cg/credits/9.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10:
    "images/cg/credits/10.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_locked:
    "images/cg/credits/1b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2_locked:
    "images/cg/credits/2b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3_locked:
    "images/cg/credits/3b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4_locked:
    "images/cg/credits/4b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5_locked:
    "images/cg/credits/5b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6_locked:
    "images/cg/credits/6b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7_locked:
    "images/cg/credits/7b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8_locked:
    "images/cg/credits/8b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9_locked:
    "images/cg/credits/9b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10_locked:
    "images/cg/credits/10b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size (640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size (640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size (640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size (640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size (640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size (640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size (640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size (640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size (640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    size (640, 360)

image credits_logo:
    "gui/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

image credits_ts2:
    "images/bg/splash2-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)


transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250

image mcredits_1a:
    ypos credits_ypos
    xoffset -205
    "black"
    10.33
    Text("Cada día", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset -5
    "black"
    11.75
    Text("imagino un futuro donde puedo", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos
    xoffset 215
    "black"
    14.20
    Text("estar contigo", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -226
    "black"
    19.15
    Text("En mi mano hay", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 50
    xoffset 15
    "black"
    20.6
    Text("una pluma que escribirá poemas", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 245
    "black"
    22.37
    Text("de mí y de ti.", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("La tinta cae formando un oscuro charco,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text(" Solo mueve tu mano, escribe un camino a su corazón", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("Pero en este mundo de elecciones infinitas, ", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -135
    "black"
    42.0
    Text("¿Qué ruta he de seguir", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 140
    "black"
    43.47
    Text("para que llegue mi día especial?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 7.0, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 0.5 alpha 1.0

image mcredits_7b:
    ycenter 0.5
    xcenter 0.5
    alpha 0.0
    "black"
    48.62
    alpha 1.0
    Text("¿Qué ruta he de seguir para que llegue mi día especial?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 7.0, ramplen=4, alpha=False)

image mcredits_7c:
    "black"
    alpha 0.0
    49.0
    linear 1. alpha 1.0

image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

label credits:
    $ persistent.autoload = "credits"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    play music "bgm/end-voice.ogg" noloop
    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show end_glitch1 zorder 2
    show black as bar zorder 9:
        alpha 0.3
        size (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat
    show screen subs
    pause 2
    $ subtitles = subVoice[0]
    pause 1
    $ subtitles = ""
    pause 1
    $ subtitles = subVoice[1]
    pause 1
    $ subtitles = ""
    pause 1
    $ subtitles = subVoice[2]
    pause 2
    $ subtitles = ""
    pause 1
    $ subtitles = subVoice[3]
    pause 2
    $ subtitles = ""
    pause 2
    $ subtitles = subVoice[4]
    pause 2
    $ subtitles = ""
    pause 0.3
    $ subtitles = subVoice[5]
    pause 5.6
    $ subtitles = ""
    pause 0.4
    $ subtitles = subVoice[6]
    pause 4.3
    $ subtitles = ""
    pause 0.5
    $ subtitles = subVoice[7]
    pause 2
    $ subtitles = ""
    pause 0.7
    $ subtitles = subVoice[8]
    pause 6
    $ subtitles = ""
    pause 0.5
    $ subtitles = subVoice[9]
    pause 1.5
    $ subtitles = ""
    pause 4.2
    scene black
    pause 0.5
    $ consolehistory = []
    call updateconsole ("renpy.musica.reproducir(\"ddlc.ogg\")", "Reproduciendo audio \"ddlc.ogg\"...") from _call_updateconsole_20
    pause 1.0
    call hideconsole from _call_hideconsole_1
    play music "<to 50.0>bgm/credits.ogg" noloop
    show mcredits_1a zorder 50
    show mcredits_1b zorder 49
    show mcredits_1c zorder 48
    show mcredits_2a zorder 47
    show mcredits_2b zorder 46
    show mcredits_2c zorder 45
    show mcredits_3 zorder 44
    show mcredits_4 zorder 43
    show mcredits_5 zorder 42
    show mcredits_6a zorder 41
    show mcredits_6b zorder 40
    show mcredits_7 zorder 51

    pause 50
    jump credits2

label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    $ consolehistory = []
    play music "<from 50.0>bgm/credits.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    $ subtitles = ""
    show credits_logo
    pause 9.12
    $ subtitles = subArray[0]
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Concepto y Diseño" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png eliminado con éxito.") from _call_updateconsole_21
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png eliminado con éxito.") from _call_updateconsole_clearall_10
    show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Arte De Personajes" as credits_header_2 at credits_text_scroll_right
    show credits_text "Satchely" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(19 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[1]
    $ pause(25 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png eliminado con éxito.") from _call_updateconsole_22
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png eliminado con éxito.") from _call_updateconsole_clearall_11
    show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Arte de Fondos" as credits_header_1 at credits_text_scroll_left
    show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(28 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[2]
    $ pause(32 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(33 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[3]
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png eliminado con éxito.") from _call_updateconsole_23
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png eliminado con éxito.") from _call_updateconsole_clearall_12
    show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Historia" as credits_header_2 at credits_text_scroll_right
    show credits_text "Dan Salvato" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(36 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(37 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[4]
    $ pause(41 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(42 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[5]
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png eliminado con éxito.") from _call_updateconsole_24
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png eliminado con éxito.") from _call_updateconsole_clearall_13
    show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Música" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(46 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png eliminado con éxito.") from _call_updateconsole_25
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png eliminado con éxito.") from _call_updateconsole_clearall_14
    show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Voz de Monika" as credits_header_2 at credits_text_scroll_right
    show credits_text "Jillian Ashcraft" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png eliminado con éxito.") from _call_updateconsole_26
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png eliminado con éxito.") from _call_updateconsole_clearall_15
    show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Agradecimientos Especiales" as credits_header_1 at credits_text_scroll_left
    show credits_text "Masha Gutin\nKagefumi" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(65 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[6]
    $ pause(71 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png eliminado con éxito.") from _call_updateconsole_27
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png eliminado con éxito.") from _call_updateconsole_clearall_16
    show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Agradecimientos Especiales" as credits_header_2 at credits_text_scroll_right
    show credits_text "David Evelyn\nCorey Shin" as credits_text_2 at credits_text_scroll_right
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(74 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[7]
    $ pause(80 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png eliminado con éxito.") from _call_updateconsole_28
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png eliminado con éxito.") from _call_updateconsole_clearall_17
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Agradecimientos Especiales" as credits_header_1 at credits_text_scroll_left
    show credits_text "Alecia Bardachino\nMatt Naples" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(87 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[8]
    $ pause(92 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(93 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[9]
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png eliminado con éxito.") from _call_updateconsole_29
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png eliminado con éxito.") from _call_updateconsole_clearall_18
    show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Agradecimientos Especiales" as credits_header_2 at credits_text_scroll_right
    show credits_text "Monika\n[player]" as credits_text_2 at credits_text_scroll_right
    $ pause(96 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(97 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[10]
    $ pause(101 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(102 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[11]
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png eliminado con éxito.") from _call_updateconsole_30
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png eliminado con éxito.") from _call_updateconsole_clearall_19
    $ pause(105 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(106 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[12]
    call updateconsole ("os.eliminar(\"game/screens.rpy\")", "screens.rpy eliminado con éxito.") from _call_updateconsole_31
    call updateconsole ("os.eliminar(\"game/gui.rpy\")", "gui.rpy eliminado con éxito.") from _call_updateconsole_32
    call updateconsole ("os.eliminar(\"game/menu.rpy\")", "menu.rpy eliminado con éxito.") from _call_updateconsole_33
    call updateconsole ("os.eliminar(\"game/script.rpy\")", "script.rpy eliminado con éxito.") from _call_updateconsole_34
    $ pause(111 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = ""
    $ pause(114 - (datetime.datetime.now() - starttime).total_seconds())
    $ subtitles = subArray[13]
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole from _call_hideconsole_4
    show credits_ts
    show credits_text "Hecho con amor por":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    $ pause(116 - (datetime.datetime.now() - starttime).total_seconds())
    hide screen subs
    pause 9.3
    show credits_ts2
    pause 9.3
    play sound page_turn
    show poem_end with Dissolve(1)
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        scene black
        show poem_end
        $ pause()
        if not persistent.clearall:
            call screen dialog(message="Error: Los archivos están perdidos o corruptos.\n Por favor, reinstala el juego.", ok_action=Quit(confirm=False))
        else:
            show poem_endesp with Dissolve(1)
            $ pause()
            call screen dialog(message="Error: Los archivos están perdidos o corruptos.\n Por favor, reinstala el juego.", ok_action=Quit(confirm=False))
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
