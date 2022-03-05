label ch10_main:
    $ delete_all_saves()
    $ persistent.deleted_saves = True
    $ gtext = glitchtext(48)
    stop music
    $ config.window_hide_transition = None
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2

    s "[gtext]"
    $ s_name = glitchtext(12)
    "Desde lejos, veo a una fastidiosa chica corriendo hacia mí, agitando los brazos en el aire como si fuera totalmente ajena a cualquier atención que pudiera atraer."
    "Esa chica es [s_name], mi vecina y buena amiga desde que eramos niños."
    "Ya sabes, el tipo de amiga que nunca te verías haciendo, pero funciona porque nos conocemos desde hace mucho tiempo."
    "Solíamos caminar a la escuela juntos en días como este, pero a partir de la secundaria se ha quedado dormida frecuentemente, y yo me cansé de esperar."
    "Pero si ella va a perseguirme así, casi me siento mejor huyendo."
    "Sin embargo, sólo suspiro y me paro frente al paso de peatones dejando que [s_name] me alcance."

    show sayori glitch zorder 2 at t11
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    $ pause(1.0)
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    $ pause(1.0)
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.5)
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ delete_all_saves()
    $ persistent.playthrough = 2
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ anticheat = persistent.anticheat
    $ renpy.save_persistent()

    jump ch20_from_ch10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
