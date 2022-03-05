label ch21_y_end:
    jump ch1_y_end

label ch22_y_end:
    stop music fadeout 2.0
    call showpoem (poem_y22, music=False, paper="images/bg/poem_y1.jpg", img="yuri 2s") from _call_showpoem
    y 2q "Jajaja..."
    y "Realmente no importa de qué se trata."
    y "Mi mente ha estado un poco hiperactiva últimamente, así que tuve que hacerlo con tu pluma."
    y 2o "Ah--"
    y 2q "Una...Una pluma se cayó de tu mochila ayer, así que la llevé a casa para resguardarla y..."
    y "Yo, um..."
    y 2y6 "Simplemente...me gusta...la forma...en la que escribe."
    y "Así que escribí este...poema...con tu pluma."
    y "Y ahora lo estás tocando..."
    y 2y5 "Jajaja."
    y 3p "¡¡Estoy bien!!"
    y 3o "¿Qué acabo de...?"
    y "..."
    y 4c "...¿Podemos fingir que esta conversación nunca sucedió?"
    y "Puedes conservar el poema..."
    return
label ch23_y_end:
    show darkred zorder 5:
        alpha 0
        linear 2.0 alpha 1.0
    call showpoem (poem_y23, track="bgm/5_yuri2.ogg", revert_music=False, paper="images/bg/poem_y2.jpg", img="yuri eyes", where=truecenter) from _call_showpoem_1
    y "¿Te gusta?"
    y "¡Lo escribí para ti!"
    $ gtext = glitchtext(80)
    show yuri 1b at i11
    y "En caso de que no te dieras cuenta, el poema es sobre [gtext]."
    y 1y6 "Más importante aún, lo he dotado de mi aroma."
    y "¿No soy la persona más considerada en el club?"
    play sound "sfx/glitch2.ogg"
    show yuri glitch
    $ pause(0.2)
    stop sound
    show yuri 3y2
    hide darkred
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    $ renpy.music.stop(channel="music_poem")
    $ renpy.music.play(audio.t5c)
    y "..."
    y 4d "Yo..."
    y "Creo que...voy a vomitar."
    show yuri at lhide
    hide yuri
    $ pause(1.0)
    return
label ch21_n_end:
    jump ch1_n_end
label ch22_n_end:
    if n_appeal >= 2:
        jump ch22_n_end2
    else:
        call showpoem (poem_n2) from _call_showpoem_2
        n 2a "No está mal, ¿Verdad?"
        mc "Es bastante más largo que el de ayer."
        n 2w "El de ayer fue demasiado corto..."
        n "¡Estaba calentando!"
        n 2c "Espero que no hayas pensado que era lo mejor que podía hacer."
        mc "No, por supuesto que no..."
        n 2a "De todos modos, el mensaje es bastante sencillo en este poema."
        n "Dudo que deba explicarlo."
        n 2g "Cualquiera estaría de acuerdo en que el tema de este poema es sobre un idiota ignorante..."
        n "Todos tienen algún tipo de pasatiempo extraño, o un placer culpable."
        n 5q "Algo que tienes miedo que si las personas lo descubren, se burlarían de ti o pensarían menos de ti."
        n 1e "...¡Pero eso sólo hace que la gente sea estúpida!"
        n "¿A quién le importa lo que le gusta a alguien, siempre y cuando no lastime a nadie, y lo haga feliz?"
        n 1q "Creo que las personas realmente necesitan aprender a respetar a los demás por gustarles las cosas raras..."
        n 1x "...Como dos de las chicas en este club, cuyos nombres respetuosamente no diré."
        n 1s "Es irónico que incluso en mi único lugar de confort, ni siquiera puedo hacer que la gente me respete..."
        n 1u "...¡Por Dios, ahora me haces quejarme demasiado!"
        "{i}(...¿Qué fue lo que hice?){/i}"
        mc "Por lo que vale, te respeto..."
        n 1h "Bueno--"
        n "Creo que gracias..."
        n 1s "...Pero es obvio que 'respetas' a Yuri más, así que..."
        n 42c "Lo que sea...hemos terminado de compartir, entonces puedes irte ahora."
    return
label ch22_n_end2:
    call showpoem (poem_n2b, revert_music=False) from _call_showpoem_3
    $ style.say_dialogue = style.edited
    n 1g "[player]..."
    n "¿Por qué no has venido a leer conmigo hoy?"
    n 1m "Te estaba esperando."
    n "Estuve esperando por mucho tiempo."
    n "Era lo único que esperaba hoy."
    n "¿Por qué lo arruinaste?"
    n "¿Te gusta más Yuri?"
    n 1k "Creo que es mejor que no te asocies con ella."
    n "¿Me estás escuchando?"
    show darkred zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    n ghost1 "Yuri es un monstruo enfermo."
    n "Eso debería ser obvio ahora."
    n "Así que sólo juega conmigo en su lugar."
    n "¿De acuerdo?"
    n "No me odias, [player], ¿verdad?"
    n "¿Me odias?"
    show natsuki_ghost_blood zorder 3
    n "¿Quieres que me vaya a casa llorando?"
    n "El club es el único lugar donde me siento segura."
    n "No arruines eso para mí."
    n "No lo arruines."
    n "Por favor."
    n "Simplemente deja de hablar con Yuri."
    n "Juega conmigo en su lugar."
    n "Es todo lo que tengo..."
    n "Juega conmigo."
    stop music
    hide n_rects_ghost3
    n ghost2 "¡¡¡JUEGA CONMIGO!!!"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    $ pause(1)
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    $ pause(0.5)
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 onlayer front at i11
    $ pause(0.25)
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    $ pause(0.5)
    show end:
        xzoom -1
    with dissolve_cg
    $ pause(2.0)
    scene black
    with None
    $ quick_menu = True
    return
label ch23_n_end:
    $ natsuki_23 = True
    $ style.say_dialogue = style.normal
    call showpoem (poem_n23, revert_music=False) from _call_showpoem_4
    $ renpy.music.stop(channel="music_poem", fadeout=2.0)
    $ style.say_dialogue = style.edited
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(3.0)
    stop music
    hide screen tear
    show natsuki ghost_base
    n "Cambié de opinión."
    n "Ignora todo lo que acabas de leer."
    n "No tiene sentido tratar de hacer algo."
    n "Es culpa de Yuri ser tan desagradable."
    n "¿Puedes oírme, [player]?"
    n "Si simplemente pasaras más tiempo con Monika, todos estos problemas desaparecerían."
    n "Yuri y yo estamos demasiado desordenadas para alguien tan maravilloso como tú."
    n "Sólo piensa en Monika a partir de ahora."
    n "Sólo Monika."
    hide natsuki
    $ style.say_dialogue = style.edited
    "Sólo Monika."
    menu:
        "Sólo Monika."
        "Sólo Monika.":
            pass
    $ style.say_dialogue = style.normal
    $ renpy.call_screen("dialog", "Sólo Monika.", ok_action=Return())
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    $ pause(2.5)
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "Sólo Monika." with Dissolve(0.5, alpha=True)
    $ pause(1.0)
    play music t5
    $ skip_transition = True

    return

label ch21_m_end:
    call showpoem (poem_m21) from _call_showpoem_5
    jump ch1_m_end2
label ch22_m_end:
    call showpoem (poem_m22, revert_music=False) from _call_showpoem_6
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    $ pause(2)
    show screen tear(20, 0.3, 0.3, 0, 40)
    $ pause(0.5)
    hide screen tear
    play music t5c
    m 5 "Lo siento, sé que es un poco abstracto."
    m "Sólo estoy tratando de...Um..."
    m 1r "Bueno, no importa."
    m "No tiene sentido explicarlo."
    m 1i "De todos modos..."
    m 3b "¡Aquí está el consejo del día sobre la escritura de Monika!"
    m "A veces te encontrarás frente a una decisión difícil..."
    m "Cuando eso ocurra, ¡no te olvides de guardar tu juego!"
    m 3k "Nunca se sabe cuándo...Um..."
    m 3i "...¿Con quién estoy hablando?"
    m "¿Puedes oírme?"
    m 3g "Dime que puedes oírme."
    m "Lo que sea"
    $ renpy.call_screen("dialog", "Por favor, ayúdame.", ok_action=Return())
    m 3k "...¡Ese es mi consejo de hoy!"
    m "Gracias por escuchar~"
    return
label ch23_m_end:
    $ quick_menu = False
    window hide
    play sound page_turn
    show paper_glitch zorder 10 with Dissolve(1)
    play music g2
    if renpy.windows and renpy.game.preferences.fullscreen:
        $ mouse_visible = False
        scene bsod
        $ pause(3.0)
    else:
        show black zorder 1
        $ pause(2.0)
    window show(None)
    show monika 1d zorder 11 at i11
    $ quick_menu = True
    $ mouse_visible = True
    m "¡Dios! ¡Eso realmente me asustó!{fast}"
    window auto
    m "Um..."
    m 1m "Bueno, creo que me equivoqué un poco, eh...'escribiendo' este poema."
    m "Sólo estaba tratando de..."
    m 1i "...No importa."
    m "Vamos a seguir..."
    stop music
    return


label ch21_n_bad:
    jump ch1_n_bad

label ch21_n_med:
    jump ch1_n_med

label ch21_n_good:
    jump ch1_n_good

label ch22_n_bad:

    if n_poemappeal[0] < 0:
        n 1r "..."
        n "Sí, tal como pensé..."
        mc "¿...?"
        n 2w "[player], vamos."
        n "No soy estúpida."
        n 2h "Sé cuánto tiempo has estado gastando con Yuri..."
        n "Es obvio que te preocupa más impresionarla que intentar mejorar tu escritura."
        n 2w "Para decirlo sin rodeos, es algo patético."
        n 4h "¿Por qué estás incluso en este club, [player]?"
        n "Honestamente..."
        n "Pensé que conseguir un nuevo miembro ayudaría a todas a ser más cercanas."
        n 4s "No a excluirnos mas."
        n 1u "Esta es una actividad tan estúpida..."
        n 12c "...Mira, no estoy de buen humor hoy, y realmente no tengo ganas de hablar en este momento."
        n "Por favor, vete."
        $ skip_poem = True
        return
    else:


        n 1k "...Hm."
        n "Me gustó más tu último poema."
        mc "¿Eh? ¿En serio?"
        n 2c "Bueno, sí. Puedo decir que eres un poco más atrevido con este."
        n "Pero en realidad todavía no eres lo suficientemente bueno para eso. Se vino abajo."
        mc "Eso puede ser cierto, pero sólo quería probar algo diferente."
        mc "Todavía estoy descifrando todo esto."
        jump ch22_n_med_shared2

label ch22_n_med:

    if n_poemappeal[0] < 0:
        n "...Hm"
        n 2k "Bueno, puedo admitir que es mejor que el anterior."
        n "Es agradable ver que estás haciendo un esfuerzo."
        mc "Eso está bien..."
        label ch22_n_med_shared:
            n 2c "Sólo asegúrate de encontrar un poco de influencia de todos."
            n "Creo que al menos estás siendo influenciado por Yuri un poco, ¿no?"
            n 5q "Quiero decir, sé que has estado, como..."
            n "Pasando el tiempo con ella, o lo que sea..."
            n 1w "¡Pero ya sabes, Monika y yo somos tan buenas como ella!"
            n 1q "¡E-En poemas, quiero decir!"
            n 1h "¡Así que realmente deberías tratar de aprender algo, o nunca mejorarás!"
            n "Aquí está el que escribí..."
            n "Me aseguraré de que aprendas algo de él."
            return


    elif n_poemappeal[0] == 0:
        n "...Hm."
        n 2k "Bueno, en realidad no es peor que tu último poema."
        n "Pero tampoco puedo decir que sea mejor."
        mc "Uff..."
        n 2c "¿Huh? ¿'Uff' qué?"
        mc "Ah...Bueno, cualquier cosa que no sea un descarrilamiento, lo tomaré como una victoria."
        mc "Y me da la sensación de que probablemente eres la más crítica."
        n 1p "¡H-Hey! ¿Qué te hace--"
        n 1q "{i}(Espera, tal vez eso fue un cumplido...?){/i}"
        n 4y "¡A-Ajah! ¡Me alegra ver que alguien reconoce mi experiencia!"
        n "Bueno, entonces, sigue practicando y tal vez serás tan bueno como yo algún día!"
        mc "Eso es...Eh..."
        "Algo me dice que Natsuki perdió completamente el punto."
        jump ch22_n_med_shared
    else:


        n "...Hm."
        n 2c "Bueno, no es terrible."
        n "Pero es bastante decepcionante después de tu último poema."
        n 2s "Por otra parte, si este fuera tan bueno como el último, estaría completamente enojada."
        mc "Bueno, supongo que quería probar algo un poco diferente esta vez."
        label ch22_n_med_shared2:
            n 2c "Muy bien. Todavía eres nuevo en esto, por lo que no esperaría que encuentres tu estilo de inmediato."
            n "Quiero decir, todos en el club escriben de manera muy diferente..."
            n "Tal vez encuentres un poco de influencia con nosotras."
            n 2q "Por ejemplo..."
            n 5q "Noté que estabas pasando el tiempo con Yuri hoy..."
            n "No es que me importe con quién pasas tu tiempo."
            n 5w "Después de todo, me enseñaron a no esperar nada de nadie."
            n 5s "Así que no es como si te estuviera esperando, o algo así."
            n 5h "Aún así, al menos deberías mirar mi poema..."
            n "Probablemente puedas aprender algo de eso."
            return

label ch23_n_bad:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        n 5x "No voy a leer otro de tus poemas 'elegantes' para Yuri."
        n 5s "Pero aún voy a hacer que leas el mío."
        n "Hay una razón."
        n 5x "Realmente me gustaría no tener que hacer esto..."
        n "Pero desafortunadamente no tengo muchas opciones."
        n 5h "Sólo...léelo con cuidado, ¿de acuerdo?"
        n "Entonces puedes irte."
        return

    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "..."
        n 2c "...Meh."
        n "Supongo que realmente no has aprendido nada después de todo."
        n "Honestamente, no sé por qué me hice ilusiones en primer lugar."
        label ch23_n_bad_shared:
            n 42c "Esta es claramente la influencia de Yuri..."
            n "No me di cuenta de que eras tan impresionable."
            n "Pasando todo este tiempo con ella en el club..."
            n "Ahora intentas escribir como ella..."
            n 1s "Esto es estúpido."
            n "Al menos Monika aprecia mi escritura..."
            n 1r "...Ugh."
            n 1q "De acuerdo...supongo que voy a compartir mi poema ahora."
            n "Realmente odio que tenga que hacer esto."
            n "Pero desafortunadamente no tengo muchas opciones."
            n 1 h "Sólo...léelo con cuidado, ¿de acuerdo?"
            n "Entonces puedes irte."
            return
    else:

        n "..."
        n 2r "Oh, cielos."
        n "Esto es seriamente un paso atrás."
        mc "¿Eh?"
        n 2c "Me gustaron tus últimas dos poemas más que éste."
        jump ch23_n_bad_shared

label ch23_n_med:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch23_n_bad
    elif n_poemappeal[1] < 0:
        n "..."
        n 2k "...Este está bien."
        mc "¿Bien?"
        n "Sí, al menos es mejor que el de ayer."
        label ch23_n_shared:
            n 2c "Todavía no puedo decir realmente cuánto te importa escribir, pero de cualquier forma, estás bien."
            n 4r "Aunque en realidad no estás pasando el tiempo con nadie más que con Yuri..."
            n 4h "Sigo pensando que es bueno tener actividades en las que todos participemos."
            n 4w "¡Así que será mejor que sigas trabajando duro!"
            n "Quiero decir..."
            n 1 h "Sé que no soy presidenta ni vicepresidenta ni nada..."
            n "Pero eso no significa que puedes decepcionarme, ¿de acuerdo?"
            n 1q "Por lo tanto, al menos lee el mío por ahora."
            n "Pero sólo para ser clara..."
            n 1h "Este poema...significa mucho para mí."
            n "Entonces léelo con cuidado, ¿de acuerdo?"
            return
    else:
        n "..."
        n 2k "...Este está bien."
        mc "¿Bien?"
        n "Bueno, sí."
        n "De todos modos, es tan bueno como el de ayer."
        jump ch23_n_shared

label ch23_n_ygave:
    n 1 h "¿Qué?"
    n "¿Le diste tu poema a Yuri?"
    n 4x "¡Que asco!"
    n "¿Qué pasa con ustedes dos?"
    n 1s "Hmph..."
    n "No es como si quisiera leerlo de todos modos."
    n 1r "Me está molestando un poco que ni siquiera pensaste en mostrármelo en absoluto."
    n 1x "...Ugh."
    n 1q "De acuerdo...supongo que voy a compartir mi poema contigo de todos modos."
    n "Realmente odio tener que hacer esto."
    n "Pero desafortunadamente no tengo muchas opciones."
    n 1 h "Sólo...léelo con cuidado, ¿de acuerdo?"
    n "Después puedes irte."
    return

label ch23_n_good:
    jump ch23_n_med

label ch21_y_bad:
    jump ch1_y_bad

label ch21_y_med:
    jump ch1_y_med

label ch21_y_good:
    jump ch1_y_good

label ch22_y_bad:
    jump ch22_y_med

label ch22_y_med:
    y 2b "He estado esperando esto..."
    y "Veamos qué has escrito hoy."
    y 3m "..."
    "Yuri sonríe y respira profundamente."
    y "Me gusta sólo sostenerlo."
    mc "¿...?"
    y 3p "Ah, quiero decir--"
    y "¡El poema salió bien!"
    y 3o "Es, ah..."
    y 2q "...Bueno, hay algunas cosas en las que podrías trabajar..."
    y "Pero eso realmente no importa."
    y 2s "Parece que todo lo que escribes es un tesoro."
    y 2d "Jaaja..."
    y 2o "Eso salió un poco incómodo..."
    y "S-Sigamos adelante..."
    y 2t "Aquí está el poema que escribí."
    y "No tiene que gustarte ni nada..."
    return


label ch22_y_good:

    if y_poemappeal[0] < 1:
        y 2b "He estado esperando esto..."
        y "Veamos qué has escrito hoy."
        y 2e "..."
        y "......"
        "Yuri mira el poema con una expresión de sorpresa en su rostro."
        mc "¿Te...gusta?"
        y "[player]..."
        y "...¿Cómo entendiste esto tan rápido?"
        label ch22_y_good_shared:
            y 2v "Ayer mismo, te estaba diciendo el tipo de técnicas que vale la pena practicar..."
            mc "Tal vez es por eso..."
            mc "Hiciste un buen trabajo explicando."
            mc "Realmente quería intentar hacerlo más profundo."
            show yuri 4b zorder 2 at t11
            "Yuri traga visiblemente."
            "Incluso sus manos parecen sudorosas."
            y 4e "A-Ah..."
            y "Eso me hace tan feliz..."
            y 3y5 "¡Es tan increíble sentirme valorada, [player]!"
            y "Todo lo que escribes es un tesoro para mí."
            y 3m "Mi corazón late sólo sosteniéndolo..."
            y 3q "Jajaja..."
            y "Quiero escribir un poema sobre este sentimiento..."
            y 3y6 "¿Eso es malo, [player]?"
            y "No estoy siendo rara, ¿verdad?"
            y 3s "Y-Yo estoy teniendo un momento más difícil de lo habitual para ocultar mis emociones..."
            y 3m "Estoy un poco avergonzada."
            y 3y6 "Pero ahora mismo, sólo quiero que leas mi poema también."
            y 3y5 "¿De acuerdo?"
            return
    else:

        y 2b "He estado esperando esto..."
        y "Veamos qué has escrito hoy."
        y 2e "..."
        y "......"
        "Yuri mira el poema con una expresión de sorpresa en su rostro."
        mc "¿Te...gusta?"
        y "[player]..."
        y 2t "Este podría ser incluso mejor que el de ayer..."
        y "...¿Cómo aprendiste esto tan rápido?"
        jump ch22_y_good_shared

label ch23_y_bad:
    jump ch23_y_good

label ch23_y_med:
    jump ch23_y_good

label ch23_y_good:
    y 1d "Finalmente..."
    y 3y5 "Jajaja..."
    show yuri 3m
    "Yuri sostiene mi poema contra su rostro y respira profundamente."
    y 3y6 "Me encanta."
    y "Me encanta todo sobre esto."
    y 3y5 "[player], quiero llevarme esto a casa."
    y "¿Me dejarás quedármelo?"
    y "¿Por favor?"
    mc "Claro, no me importa..."
    y 2y5 "Jajaja."
    y "Eres muy amable conmigo, [player]..."
    y "Nunca he conocido a alguien tan amable como tú."
    y 2y6 "Podría morir..."
    y 3y5 "¡N-No realmente, pero--!"
    y "Simplemente no sé cómo describirlo."
    y "Está bien sentirse así, ¿verdad?"
    show yuri:
        "yuri 3y4"
        0.4
        "yuri 3y6"
    y "No está mal, ¿verdad?"
    "Yuri sostiene mi poema contra su pecho."
    y 3m "Voy a llevarme esto a casa y lo guardaré en mi habitación."
    y "Espero que te haga sentir bien cuando pienses en mí."
    $ style.say_dialogue = style.normal
    y 3y5 "¡Lo cuidaré bien!"
    $ style.say_dialogue = style.edited
    y 3y6 "Incluso me tocaré mientras lo leo una y otra vez."
    $ _history_list.pop()
    y "Me haré cortes de papel para que el aceite de tu piel entre en mi torrente sanguíneo."
    $ _history_list.pop()
    y 3y1 "Jajajajajaja."
    $ _history_list.pop()
    $ style.say_dialogue = style.normal
    y 2s "También puedo darte mi poema."
    y "Además, después de leerlo, sé que realmente querrás quedártelo."
    y 2y6 "Aquí, tómalo. No puedo esperar más."
    y 2y5 "¡Date prisa, léelo!"
    $ y_gave = True
    return


label ch21_m_start:
    m 1b "¡Hola, [player]!"
    m "¿Pasas un buen rato hasta ahora?"
    mc "Ah...Sí."
    m 1k "¡Bien! ¡Me alegra oírlo!"
    m 4a "Por cierto, ya que eres nuevo y eso..."
    m "Si alguna vez tienes alguna sugerencia para el club, como nuevas actividades o cosas que podemos hacer mejor..."
    m 4b "¡Siempre estoy escuchando!"
    m "No temas dar ideas, ¿de acuerdo?"
    show monika 4a
    mc "De acuerdo...lo tendré en cuenta."
    "Por supuesto que temeré dar ideas."
    "Estoy mucho mejor yendo con la corriente hasta que esté más instalado."
    m 1a "De todos modos..."
    m "¿Quieres compartir tu poema conmigo?"
    mc "Es un poco vergonzoso, pero creo que tengo que hacerlo."
    m 5a "¡Jajajaja!"
    m "¡No te preocupes, [player]!"
    m "Todos estamos un poco avergonzados hoy, ¿sabes?"
    m "Pero es ese tipo de barrera que todos aprenderemos a superar pronto."
    mc "Sí, eso es cierto."
    "Le entrego mi poema a Monika."
    m 2a "...¡Mhm!"
    $ nextscene = "m2_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_4

    m 1a "De todos modos, ¿quieres leer mi poema ahora?"
    m 1e "No te preocupes, no soy muy buena..."
    mc "Pareces bastante segura para alguien que dice no ser muy buena."
    m 1j "Bueno...eso es porque tengo que sonar confiada."
    m 1b "Eso no quiere decir que siempre me siento así, ¿sabes?"
    mc "Ya veo..."
    mc "Bueno, leámoslo, entonces."
    return

label ch22_m_start:
    if y_appeal < 2:
        m 1b "¡Hola de nuevo, [player]!"
        m "¿Cómo va la escritura?"
        mc "Bien, supongo..."
        m 2k "Tomaré eso."
        m 2b "¡Mientras no esté yendo mal!"
        m 2a "Estoy feliz de que te estés aplicando."
        m "¡Tal vez pronto hagas una obra maestra!"
        mc "Jajaja, no contaría con eso..."
        m 2a "¡Nunca se sabe!"
        m "¿Deseas compartir lo que escribiste hoy?"
        mc "Claro...aquí tienes."
        "Le doy mi poema a Monika."
        m "..."
        m "...¡Muy bien!"
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene from _call_expression_5

    m 1a "Pero de todos modos..."
    m "¿Quieres leer mi poema ahora?"
    m "Me gusta cómo resultó este, así que espero que tú también lo hagas~"
    return

label ch23_m_start:
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene from _call_expression_6
    if y_appeal < 3:
        m 1a "Como sea..."
        if y_gave:
            m 1m "Supongo que no nos preocuparemos por tu poema..."
            m "Yuri debería haber tenido, al menos, la cortesía de dejarte terminar de compartirlo antes de tomarlo."
            m 1r "...Bueno, lo que sea."
            m "Si la hace feliz, no la detendré."
            m 1a "En cuanto al mío..."
        m 1e "Trabajé muy...muy duro en este poema, entonces..."
        m "Espero que sea, eh, efectivo."
        m 1r "Aquí va..."
        $ persistent.seen_colors_poem = True
    return



label m2_natsuki_1:
    m 2b "¡Me gustó, [player]!"
    mc "¿En serio...?"
    m 2e "Es mucho más lindo de lo que esperaba."
    m 2k "¡Jajajaja!"
    mc "Oh cielos..."
    m 1b "¡No, no!"
    m "Me hace pensar en algo que escribiría Natsuki."
    m "Y ella es una buena escritora también."
    m 5a "¡Toma eso como un cumplido!"
    mc "Jajaja..."
    mc "Si tú lo dices"
    m "¡Sip!"
    m 3b "Si estás interesado en Natsuki, siempre ten un snack contigo."
    m "Ella se pegará a ti como un perrito."
    m 3k "¡Jajajaja!"
    m 1a "El padre de Natsuki no le da dinero para almorzar ni le deja comida en la casa, así que está bastante nerviosa con bastante frecuencia..."
    m "Pero a veces simplemente pierde todas sus fuerzas y se desmaya."
    m "Como hace rato."
    m 2d "Esto es sólo una suposición, pero creo que es tan pequeña porque su malnutrición está interfiriendo con su crecimiento adolescente..."
    m 2b "...Pero oye, algunos chicos también se interesan por las chicas pequeñas, ¿sabes?"
    m 5a "Lo siento...¡sólo estoy tratando de ver el lado positivo!"

    return

label m2_yuri_1:
    m 1a "¡Gran trabajo, [player]!"
    m "Iba 'Ooh' en mi cabeza mientras lo leía."
    m 1j "¡Es realmente metafórico!"
    m 1a "No estoy segura de por qué, pero no esperaba que fueses a buscar algo tan profundo."
    m 3b "¡Creo que te subestimé!"
    mc "Es más fácil para mí mantener bajas las expectativas de todos."
    mc "De esa manera, siempre cuenta cuando hago algo de esfuerzo."
    m 5a "¡Jajaja! ¡Eso no es muy justo!"
    m "Bueno, supongo que funcionó, de todos modos."
    m 2a "Sabes que a Yuri le gusta este tipo de escritura, ¿verdad?"
    m "Escribir algo que está lleno de imágenes y simbolismo."
    m 2d "A veces siento que la mente de Yuri está completamente desapegada de la realidad."
    m "Pero no me refiero a que sea algo malo."
    m 2a "Tengo la impresión de que está totalmente alejada de la gente."
    m "Ella pasa tanto tiempo en su propia cabeza que probablemente sea un lugar mucho más interesante para ella..."
    m 2b "Pero es por eso que ella se pone tan feliz cuando la tratas con mucha amabilidad."
    m "No creo que ella esté acostumbrada a ser consentida así."
    m 2j "Ella debe estar realmente muerta de hambre por la interacción social, así que no la culpes por ser alocada."
    m 2d "Como hace rato..."
    m "Creo que si ella se siente demasiado estimulada, termina retirándose y buscando tiempo a solas."
    "De repente, la puerta se abre."
    m 2b "¡Yuri!"
    show monika 2a
    show yuri 1s zorder 3 at f31
    y "He vuelto..."
    y "¿Me perdí de algo?"
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2a "No realmente..."
    m "Bueno, todos comenzamos a compartir nuestros poemas."
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 2t "¿Eh?"
    y "¿Ya empezaron?"
    y 2v "L-Lo siento por llegar tarde..."
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2j "¡No hay necesidad de disculparse!"
    m 2a "Todavía tenemos mucho tiempo, así que estoy más contenta de que hayas tardado todo el tiempo que necesitabas."
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 1s "Muy bien..."
    y "Gracias, Monika."
    y "Supongo que debería ir a buscar mi poema ahora."
    show yuri zorder 1 at thide
    hide yuri
    $ y_ranaway = False
    return

label m2_yuri_2:
    m 1i "[player], creo que viste algo que se suponía que no deberías ver."
    m "No quería tener que decirte esto, pero no creo que tenga otra opción."
    m 1r "Se está volviendo cada vez más peligroso pasar mucho tiempo con Yuri."
    m 1i "No sé por qué, pero parece bastante fácil de alterar cuando está cerca de ti..."
    m 3d "Lo cual no debería ser un problema en sí mismo."
    m "Pero cuando Yuri se emociona demasiado, encuentra un lugar donde esconderse y comienza a cortarse con una navaja de bolsillo."
    m 2e "¿No es un poco alocado?"
    m "Ella incluso trae uno diferente a la escuela todos los días, como si tuviera una colección o algo..."
    m 2d "Quiero decir, definitivamente no es porque esté deprimida ni nada de eso!"
    m "Creo que ella simplemente se excita con ellos."
    m 2m "Podría ser, como algo sexual..."
    m 1i "El punto es que la has estado estimulando."
    m 1d "¡No digo que sea tu culpa!"
    m 1a "Pero supongo que es por eso que tuve que explicártelo todo..."
    m "Así que creo que si mantienes tu distancia, eso probablemente sea lo mejor para ella."
    m 5 "Mientras estás en eso, no seas tímido y pasa un poco más de tiempo conmigo..."
    m "Para decirlo suavemente, al menos lo tengo todo arreglado en la cabeza...y sé cómo tratar bien a los miembros de mi club."
    return

label m2_yuri_3:
    stop music
    m 1i "No digas que no te lo advertí, [player]."
    $ skip_poem = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
