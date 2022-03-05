init python:
    import datetime

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

image mcreditsesp_1a:
    ypos credits_ypos
    xoffset -205
    "black"
    10.33
    Text("Cada día, ", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcreditsesp_1b:
    ypos credits_ypos
    xoffset -35
    "black"
    11.75
    Text("       imagino un futuro donde estoy", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcreditsesp_1c:
    ypos credits_ypos
    xoffset 170
    "black"
    14.20
    Text("      junto a ti", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcreditsesp_2a:
    ypos credits_ypos + 50
    xoffset -226
    "black"
    19.45
    Text("    Con mi mano", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcreditsesp_2b:
    ypos credits_ypos + 50
    xoffset -10
    "black"
    20.9
    Text("      escribiré poemas que me lleven", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcreditsesp_2c:
    ypos credits_ypos + 50
    xoffset 225
    "black"
    23.27
    Text("junto a ti", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)

image mcreditsesp_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("La tinta fluye hasta hacer un charco", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcreditsesp_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text(" ¡Sólo escribe -- tu camino hacia su amor!", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcreditsesp_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("Pero en un mundo lleno de opciones", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcreditsesp_6a:
    ypos credits_ypos + 250
    xoffset -135
    "black"
    42.0
    Text("   ¿Que he de pagar", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcreditsesp_6b:
    ypos credits_ypos + 250
    xoffset 75
    "black"
    43.47
    Text("para un día especial?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)

image mcreditsesp_6c:
    ypos credits_ypos + 300
    xoffset -135
    "black"
    46.00
    Text("   ¿Que ha de pasar", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcreditsesp_6d:
    ypos credits_ypos + 300
    xoffset 75
    "black"
    47.47
    Text("para mi día especial?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcreditsesp_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("¿Que ha de pasar para mi día especial?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4)

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

label creditsesp:
    $ persistent.autoload = "creditsesp"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    play music "bgm/end-voice-2.ogg" noloop
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


    pause 41
    scene black
    pause 0.5
    $ consolehistory = []
    call updateconsole ("renpy.musica.reproducir(\"ddlc.ogg\")", "Reproduciendo audio \"ddlc.ogg\"...") from _call_updateconsole_3
    pause 1.0
    call hideconsole from _call_hideconsole
    play music "<to 50.0>bgm/credits-2.ogg" noloop
    show mcreditsesp_1a zorder 52
    show mcreditsesp_1b zorder 51
    show mcreditsesp_1c zorder 50
    show mcreditsesp_2a zorder 49
    show mcreditsesp_2b zorder 48
    show mcreditsesp_2c zorder 47
    show mcreditsesp_3 zorder 46
    show mcreditsesp_4 zorder 45
    show mcreditsesp_5 zorder 44
    show mcreditsesp_6a zorder 43
    show mcreditsesp_6b zorder 42
    show mcreditsesp_6c zorder 41
    show mcreditsesp_6d zorder 40
    show mcreditsesp_7 zorder 53

    pause 50
    jump creditsesp2

label creditsesp2:
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
    play music "<from 50.0>bgm/credits-2.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 9.12
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Concepto y Diseño" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.eliminar(\"images/cg/n_cg1.png\")", "n_cg1.png eliminado exitosamente.") from _call_updateconsole_4
    else:
        call updateconsole_clearall ("os.eliminar(\"images/cg/n_cg1.png\")", "n_cg1.png eliminado exitosamente.") from _call_updateconsole_clearall
    show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Arte De Personajes" as credits_header_2 at credits_text_scroll_right
    show credits_text "Satchely" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.eliminar(\"images/cg/n_cg2.png\")", "n_cg2.png eliminado exitosamente.") from _call_updateconsole_5
    else:
        call updateconsole_clearall ("os.eliminar(\"images/cg/n_cg2.png\")", "n_cg2.png eliminado exitosamente.") from _call_updateconsole_clearall_1
    show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Arte de Fondos" as credits_header_1 at credits_text_scroll_left
    show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.eliminar(\"images/cg/y_cg1.png\")", "y_cg1.png eliminado exitosamente.") from _call_updateconsole_6
    else:
        call updateconsole_clearall ("os.eliminar(\"images/cg/y_cg1.png\")", "y_cg1.png eliminado exitosamente.") from _call_updateconsole_clearall_2
    show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Historia" as credits_header_2 at credits_text_scroll_right
    show credits_text "Dan Salvato" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.eliminar(\"images/cg/y_cg2.png\")", "y_cg2.png eliminado exitosamente.") from _call_updateconsole_7
    else:
        call updateconsole_clearall ("os.eliminar(\"images/cg/y_cg2.png\")", "y_cg2.png eliminado exitosamente.") from _call_updateconsole_clearall_3
    show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Música" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.eliminar(\"images/cg/n_cg3.png\")", "n_cg3.png eliminado exitosamente.") from _call_updateconsole_8
    else:
        call updateconsole_clearall ("os.eliminar(\"images/cg/n_cg3.png\")", "n_cg3.png eliminado exitosamente.") from _call_updateconsole_clearall_4
    show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Voz de Monika" as credits_header_2 at credits_text_scroll_right
    show credits_text "GeeGeeVocals \n & Cele Riv" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.eliminar(\"images/cg/y_cg3.png\")", "y_cg3.png eliminado exitosamente.") from _call_updateconsole_9
    else:
        call updateconsole_clearall ("os.eliminar(\"images/cg/y_cg3.png\")", "y_cg3.png eliminado exitosamente.") from _call_updateconsole_clearall_5
    show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Agradecimientos Especiales" as credits_header_1 at credits_text_scroll_left
    show credits_text "Masha Gutin\nKagefumi" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.eliminar(\"images/cg/s_cg1.png\")", "s_cg1.png eliminado exitosamente.") from _call_updateconsole_10
    else:
        call updateconsole_clearall ("os.eliminar(\"images/cg/s_cg1.png\")", "s_cg1.png eliminado exitosamente.") from _call_updateconsole_clearall_6
    show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Agradecimientos Especiales" as credits_header_2 at credits_text_scroll_right
    show credits_text "David Evelyn\nCorey Shin" as credits_text_2 at credits_text_scroll_right
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.clearall:
        call updateconsole ("os.eliminar(\"images/cg/s_cg2.png\")", "s_cg2.png eliminado exitosamente.") from _call_updateconsole_11
    else:
        call updateconsole_clearall ("os.eliminar(\"images/cg/s_cg2.png\")", "s_cg2.png eliminado exitosamente.") from _call_updateconsole_clearall_7
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Agradecimientos Especiales" as credits_header_1 at credits_text_scroll_left
    show credits_text "Alecia Bardachino\nMatt Naples" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.eliminar(\"images/cg/s_cg3.png\")", "s_cg3.png eliminado exitosamente.") from _call_updateconsole_12
    else:
        call updateconsole_clearall ("os.eliminar(\"images/cg/s_cg3.png\")", "s_cg3.png eliminado exitosamente.") from _call_updateconsole_clearall_8
    show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Agradecimientos Especiales" as credits_header_2 at credits_text_scroll_right
    show credits_text "Monika\n[player]" as credits_text_2 at credits_text_scroll_right
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.eliminar(\"images/cg/m_cg1.png\")", "m_cg1.png eliminado exitosamente.") from _call_updateconsole_13
    else:
        call updateconsole_clearall ("os.eliminar(\"images/cg/m_cg1.png\")", "m_cg1.png eliminado exitosamente.") from _call_updateconsole_clearall_9

    call updateconsole ("os.eliminar(\"game/screens.rpy\")", "screens.rpy eliminado con éxito.") from _call_updateconsole_14
    call updateconsole ("os.eliminar(\"game/gui.rpy\")", "gui.rpy eliminado con éxito.") from _call_updateconsole_15
    call updateconsole ("os.eliminar(\"game/menu.rpy\")", "menu.rpy eliminado con éxito.") from _call_updateconsole_16
    call updateconsole ("os.eliminar(\"game/script.rpy\")", "script.rpy eliminado con éxito.") from _call_updateconsole_17
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole from _call_hideconsole_3
    show credits_ts
    show credits_text "Hecho con amor por":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
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
