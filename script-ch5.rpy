image exception_bg = "#dadada"
image fake_exception = Text("Un error ha ocurrido.", size=40, style="_default")
image fake_exception2 = Text("Archivo \"game/script-ch5.rpy\", linea 307\nVe reporte.txt para los detalles del error.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


label ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "Es el día del festival."
    "De todos los días, era el que más esperaba para ir a la escuela con Sayori."
    "Pero Sayori no está respondiendo su teléfono."
    "Consideré ir a su casa para despertarla, pero decidí que era demasiado."
    "Mientras tanto, los preparativos para el evento deberían estar casi completos."
    if ch4_scene == "natsuki":
        "Me las arreglé para llevar todos los pastelitos con cuidado apilando las dos bandejas."
        "Natsuki ya me está escribiendo una tormenta de mensajes, pero no puedo responder, gracias a que tengo las manos ocupadas."
    else:
        "La pancarta que Yuri y yo pintamos está seca, y la enrollé suavemente para llevarla conmigo."
        "Me envió un mensaje agradable recordándome que no olvidara nada, y la tranquilicé."
    "Curiosamente, es probable que me sienta de la misma manera que Natsuki sobre el evento."
    "Me emociona más que termine, así podré pasar tiempo con Sayori y [ch4_name] en el festival."
    "Pero conociendo a Monika, estoy seguro de que el evento también será grandioso."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "¡[player]!"
    m "Eres el primero aquí."
    m "¡Gracias por llegar temprano!"
    mc "Es gracioso, pensé que al menos Yuri estaría aquí temprano."
    "Monika está colocando pequeños folletos en cada uno de los escritorios del salón."
    "Deben ser los que ella preparó, los cuales tienen todos los poemas que vamos a recitar."
    "Al final, encontré un poema al azar en línea que pensé que le gustaría a Monika, y se lo envié."
    "Entonces, ese es el que voy a recitar."
    m 1d "Me sorprende que no hayas traído a Sayori contigo."
    mc "Sí, ella se quedó dormida otra vez..."
    mc "Esa tontita."
    mc "Uno pensaría que en días tan importantes, ella lo intentaría un poco más..."
    "Digo eso, pero de repente recuerdo lo que Sayori me dijo ayer..."
    "Y de repente me siento mal, sabiendo que no es tan fácil para ella"
    "Sólo lo dije porque es la manera en que estoy acostumbrado a pensar."
    "Pero..."
    "¿Tal vez debería haber ido a despertarla después de todo?"
    m 1k "Jajaja."
    m 4b "¡Deberías tomar un poco de responsabilidad por ella, [player]!"
    m "Quiero decir, especialmente después de lo que pasó ayer entre ustedes dos..."
    m "De alguna manera la dejaste colgada esta mañana, ¿sabes?"
    show monika 4a
    mc "¿Lo que pasó ayer...?"
    mc "Monika-- ¿Sabes de eso?"
    m 2a "Por supuesto que sí."
    m "Soy la presidenta del club, después de todo."
    mc "¡Pero...!"
    "Tartamudeo, avergonzado."
    "¿Sayori realmente le habló de eso tan rápido?"
    if sayori_confess:
        "Que ahora somos...¿Una pareja?"
        "Realmente no planeaba decírselo a nadie todavía..."
    else:
        "¿Sobre cómo básicamente rechacé su confesión?"
        "Eso me hace parecer realmente el tipo malo aquí..."
        "Pero yo soy el que sabe lo que es mejor para ella, ¿verdad?"
    mc "Caray..."
    mc "No conoces la historia completa, así que..."
    m 2j "No te preocupes."
    m "Probablemente sé mucho más de lo que piensas."
    mc "¿Eh...?"
    "Monika está siendo tan amigable como de costumbre, pero por alguna razón sentí un escalofrío por mi espina dorsal después de escuchar eso."
    m 5 "Oye, ¿quieres ver los folletos?"
    m "¡Salieron muy bien!"
    mc "Sí, claro."
    "Agarro uno de los folletos puestos en los escritorios."
    mc "Oh sí, realmente lo hicieron."
    mc "Algo como esto definitivamente ayudará a las personas a tomarse más en serio el club."
    m "Sí, ¡yo también pensé eso!"
    show monika zorder 1 at thide
    hide monika
    "Hojeo las páginas."
    "El poema de cada uno está cuidadosamente impreso en su propia página, dándole una sensación casi profesional."
    "Reconozco los poemas de Natsuki y Yuri, son los que interpretaron durante nuestra práctica."
    mc "¿Qué es esto...?"
    "Paso al poema de Sayori."
    "Es diferente al que ella practicó."
    "Es uno que no he leído antes..."
    call showpoem (poem_s3, music=False) from _call_showpoem_7
    mc "Ah--"
    "¿Qué es esto...?"
    "Al leer el poema, siento un vacío en el estomago."
    show monika 1d zorder 2 at t11
    m "¿[player]?"
    m "¿Qué pasa?"
    mc "Ah, nada..."
    "Este poema se siente completamente diferente de todo lo demás que Sayori ha escrito."
    "Pero más que eso..."
    mc "¡Y-Yo cambié de opinión!"
    mc "Voy a buscar a Sayori, así que..."
    m "Ah--"
    m 1b "¡Vale, está bien!"
    m "Trata de no tomar demasiado tiempo, ¿de acuerdo?"
    scene bg corridor with wipeleft
    "Salgo rápidamente del salón."
    m "No te tenses demasiado~"
    "Monika lo dice después de que me voy."
    "Apresuro mi ritmo."

    scene bg residential_day with wipeleft_scene
    "¿Qué estaba pensando?"
    "Debería haberlo intentado un poco más por Sayori."
    "No es gran cosa al menos esperar por ella o ayudarla a despertar."
    "Incluso el simple gesto de llevarla a la escuela la hace muy feliz."
    "Además..."
    "Ayer le dije que las cosas serían las mismas que siempre han sido."
    "Eso es todo lo que ella necesita y es lo que quiero darle."

    scene bg house with wipeleft
    "Llego a la casa de Sayori y toco la puerta."
    "No espero una respuesta, ya que tampoco contesta su teléfono."
    "Como ayer, abro la puerta y entro."
    scene black with wipeleft
    mc "¿Sayori?"
    "Ella realmente tiene el sueño pesado..."
    "Trago saliva"
    "No puedo creer que terminé haciendo esto después de todo."
    "Despertarla en su propia casa..."
    if sayori_confess:
        "Eso realmente es algo que un novio haría, ¿no?"
    else:
        "¿No es eso más como algo que un novio haría?"
    "En todo caso..."
    "Simplemente se siente bien."

    "Fuera de la habitación de Sayori, toco su puerta."
    mc "¿Sayori?"
    mc "Despierta, tontita..."
    "No hay respuesta."
    "Realmente no quería tener que entrar en su habitación así..."
    "¿No es una especie de violación a la privacidad?"
    "Pero ella realmente no me deja otra opción."
    "Abro la puerta suavemente."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    $ persistent.playthrough = 1
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.save_persistent()
    $ delete_character("sayori")
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    $ pause(3.75)
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    $ pause(0.01)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show white zorder 2
    show splash_glitch zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ pause(4.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    $ pause(0.75)
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: renpy.file(config.basedir + "/reporte.txt")
        except: open(config.basedir + "/reporte.txt", "wb").write(renpy.file("reporte.txt").read())
    $ pause(6.0)


    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "¿Qué demonios...?"
    "{i}¿¿Qué demonios??{/i}"
    "¿Es esto una pesadilla?"
    "Tiene...que serlo."
    "Esto no es real."
    "No hay forma de que esto pueda ser real."
    "Sayori no haría esto."
    "Todo estaba tranquilo hace unos días."
    "¡Es por eso que no puedo creer lo que mis ojos me están mostrando...!"
    scene black with dissolve_cg
    "Reprimo el impulso de vomitar."
    "Tan sólo ayer..."
    "Le dije a Sayori que estaría allí para ella."
    "Le dije que sabía lo que es mejor, y que todo estaría bien."
    "Entonces, ¿por qué...?"
    "¿Por qué ella haría esto...?"
    "¿Por qué no la ayudé?"
    "¿Qué hice mal?"
    if sayori_confess:
        "Confesarme..."
        "No debería haberme confesado."
        "Eso no es lo que Sayori necesitaba en absoluto."
        "Incluso me dijo lo doloroso que es para ella que otros se preocupen."
        "Entonces, ¿por qué le confesé mi amor y la hice sentir aún peor?"
    else:
        "Rechazar su confesión..."
        "Eso tiene que haber sido lo que la empujó al límite."
        "Su grito de agonía aún resuena en mis oídos."
        "¿Por qué le hice eso cuando más me necesitaba?"
    "¿Por qué fui tan egoísta?"
    "¡Esto es mi culpa--!"
    "Mis enjambres de pensamientos me siguen diciendo todo lo que pude haber hecho para evitar esto."
    "Si sólo hubiera pasado más tiempo con ella."
    "Acompañarla a la escuela."
    if sayori_confess:
        "Y seguir siendo su amigo, como siempre lo he sido..."
    else:
        "Y darle lo que sé que ella quería de nuestra relación..."
    "...Entonces podría haber evitado esto."
    "¡Sé que podría haber evitado esto!"
    "Que se pudra el Club de Literatura."
    "Que se pudra el festival."
    "Simplemente...perdí a mi mejor amiga."
    "Alguien con quien crecí."
    "Ella se ha ido para siempre."
    "Nada de lo que haga puede traerla de vuelta."
    "Este no es un juego en el que puedo reiniciar y probar algo diferente."
    "Sólo tuve una oportunidad, y no fui lo suficientemente cuidadoso."
    "Y ahora llevaré esta culpa conmigo hasta que muera."
    "Nada en mi vida vale más que la de ella..."
    "Pero aún así no pude hacer lo que ella necesitaba de mí."
    "Y ahora..."
    "Nunca podré recuperarla."
    "Nunca."
    "Nunca."
    "Nunca."
    "Nunca."
    "Nunca..."
    $ in_sayori_kill = False


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
