image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47

label ch23_main:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        $ pause(7)
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 zorder 2 at i11
    else:
        scene bg club_day2
        with dissolve_scene_half

    play music t6
    show yuri 2y5 zorder 2 at t11
    y "¡Hola, [player]!"
    y "Te he estado esperando."
    y 2d "¿Estás listo para seguir leyendo?"
    y "Traje mi mejor té hoy--"
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "¡Monika!"
    n "Te dije que no..."
    n 1g "Ugh..."
    n "¿Otra vez no ha llegado a tiempo?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1h "Desconsiderada como siempre, Natsuki."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "¿Disculpa?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1r "¿Siempre debes interrumpir mis conversaciones con tus gritos incesantes?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1o "¡¿De qué estás hablando?!"
    n 1q "Dices eso como si lo hiciera regularmente o algo así."
    n "Simplemente no estaba prestando atención, ¿de acuerdo?, Lo siento."
    n 4u "En serio...¿Qué te ha pasado últimamente?"
    if n_appeal >= 2:
        n "Mira..."
        n "Pensé un poco sobre ayer."
        n 2q "Fui un poco más hostil de lo que pretendía ser..."
        n 1q "Creo que realmente me sentí amenazada o algo así."
        n 1h "Pero sé que esto es algo que estamos haciendo juntos."
        n 1q "Otro miembro nuevo no estaría mal, siempre y cuando sea genial..."
        n 5w "Y creo que otra chica estaría bien esta vez..."
        n 5u "Entonces..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y 2u "Natsuki..."
        $ style.say_dialogue = style.edited
        y 1f "A nadie le importa."
        y "¿Por qué no vas a buscar algunas monedas debajo de las máquinas expendedoras o algo así?"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 1p "¡--!"
        n 1r "..."
        n 12f "..."
        show natsuki at thide
        hide natsuki
        $ pause(1.0)
        show monika 1g at l31
        m "Aw,rayos..."
        m "¡Soy la ultima aquí otra vez!"
        show yuri zorder 3 at f32
        y 1f "¿Practicabas piano otra vez?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Si..."
        m "Jajaja..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "Debes tener mucha determinación."
        y "Comenzando en este club, y aún tratando de hacer tiempo para el piano..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Bueno, tal vez no determinación..."
        m 3a "Supongo que es pasión."
        m "También me motiva trabajar duro para el festival."
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2n "¿Yo?"
        y 2o "N-Nada..."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "¿Es realmente tan malo...?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2m "Miralo, sí {i}es{/i} algo."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 3p "¡Lo superaré!"
        y 3y6 "No es nada digno de mención..."
        y 3o "Me he sentido un poco al borde últimamente..."
        y 3n "D-De todos modos, ¡no necesitamos hablar de eso!"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2q "Bueno, sentí que tenía que mencionarlo."
        n 5q "No es que realmente me importe ni nada..."
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31
        m "Aw, rayos..."
        m "¡Soy la última aquí otra vez!"
        show natsuki zorder 3 at f33
        n 2c "Bueno, [player] acaba de entrar también."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 1f "¿Practicabas piano otra vez?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Si..."
        m "Jajaja..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "Debes tener mucha determinación."
        y "Comenzando en este club, y aún tratando de hacer tiempo para el piano..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Bueno, tal vez no determinación..."
        m 3a "Supongo que es pasión."
        m "También me motiva trabajar duro para el festival."
        m 3n "Um..."
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33
        n 5s "..."
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31
        m 1l "Cierto..."
        m "L-Lo había olvidado..."
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32
        y 2v "Um, sobre eso, Natsuki..."
        y "Todos estuvimos hablando ayer, y..."
        y 2t "Bueno...Decidimos que nos gustaría apoyar el festival también."
        y 2l "¡Sin embargo...!"
        y 2h "Entiendo cómo te sientes acerca de no querer que el club cambie."
        y "Creo que todos nos sentimos así."
        y 2f "Así que mientras trabajemos todos juntos, este club nunca se convertirá en algo que no queremos."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "Um, también..."
        y "Si nos ayudas con el festival..."
        y 3r "...¡Entonces te compraré un nuevo manga!"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33
        n 5h "..."
        n 2z "¡Jajajaja!"
        n "Lo siento, esa última parte fue realmente divertida."
        n 2c "Mira..."
        n "Pensé un poco sobre ayer."
        n 2q "Fui un poco más hostil de lo que pretendía ser..."
        n 1q "Creo que realmente me sentí amenazada o algo así."
        n 1h "Pero sé que esto es algo que estamos haciendo juntos."
        n 1q "Otro miembro nuevo no estaría mal, siempre y cuando sea genial..."
        n 5w "Y creo que otra chica estaría bien esta vez..."
        n 5e "...¡Pero más importante, odiaría ver el evento fallar sólo porque decidí echarme atrás!"
        n "Soy una profesional, ¿saben?"
        n 5c "Así que voy a ayudar también, y nos aseguraremos de que se haga bien."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2s "Gracias a Dios..."
        y "¿No es genial, Monika?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2k "...¿Monika?"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31
        m "Ah--"
        m 1n "Sí, eso es maravilloso!"
        m "No sería lo mismo sin ti, Natsuki."
    m 5 "Como sea, [player]..."
    m "¿Qué quieres hacer hoy?"
    m "Estaba pensando que podríamos--"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1l "Ya tenemos planes para hoy."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "Ah..."
    m "¿Es cierto, Yuri?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1y6 "Eso es correcto."
    y "[player] ya está ocupado con una novela que estamos leyendo juntos."
    y 1y5 "¿No te alegra que ya lo haya metido en la literatura, Monika?"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 2l "Yo..."
    m "Supongo..."
    m "Estaba sólo--"
    m 1r "En realidad, no importa."
    m 1i "No realmente."
    m "Ustedes pueden hacer lo que quieran."
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y 2y1 "{i}(¡SI!){/i}{w=0.5}{nw}"
    y 2u "Um...Gracias por entender, Monika."
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ y_appeal += 1

    scene bg club_day2
    show yuri 3 zorder 2 at t11
    with wipeleft_scene
    call yuri_exclusive2_2_ch22 from _call_yuri_exclusive2_2_ch22

    return



label ch23_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[2]) from _call_expression_24
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "¡Muy bien, todos!"
    m "Es hora de hablar sobre los preparativos del festival."
    m 1i "Démonos prisa y terminemos con esto."
    if n_appeal >= 2:
        show natsuki 4q zorder 3 at f31
        n "..."
    else:
        show natsuki 4q zorder 3 at f31
        n "Caray..."
        n "¿Por qué el estado de ánimo es tan extraño hoy?"
        n "Mira, incluso Yuri no es inmune a eso."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "Uu..."
    y "El estancamiento del aire es un presagio común de que algo terrible está a punto de suceder..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Mira, ¿podemos seguir con esto?"
    m 2d "Voy a imprimir y preparar todos los folletos de poesía."
    if n_appeal >= 2:
        m 2i "Natsuki, puedes hacer pastelitos."
        m "Sé que eres al menos buena en eso."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "..."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "Natsuki, yo estaba pensando--"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "¡Quiero hacer pastelitos!"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "...Si, eso."
        m "Me alegra que estemos en la misma página."
    m 1m "Yuri, puedes..."
    m 1r "...Bueno, no importa."
    m 1i "Haz lo que quieras, siempre y cuando creas que ayudará."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Monika..."
    y "No soy inútil, ¿sabes?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "¡L-Lo sé!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "Ya sé lo que me gustaría hacer."
    y 1h "No podemos llevar a cabo un evento de poesía exitoso sin tener la atmósfera adecuada para la ocasión."
    y "Así que voy a hacer decoraciones y establecer una buena iluminación ambiental."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "Eso, ¿ves?"
    m "¡Esa es una gran idea!"
    m 1a "Y eso nos da a todos algo que hacer."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "¿Eh?"
    y "¿Que hay de [player]?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "[player] va a ayudarme."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "¿Espera, a ti?"
    n "¡Tienes el trabajo más fácil, Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "Lo siento, pero así es como es."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 1f "¡Nada de 'así es como es'!"
    n "¿Qué estás tratando de hacer?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "¡Estoy de acuerdo con Natsuki!"
    y "No sólo tu trabajo es más adecuado para sólo una persona..."
    y 3l "Sino que mi tarea es lo suficientemente laboriosa como para beneficiarse de un par de manos adicionales."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "¡La mía también!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "¿Qué, tus pastelitos?"
    y "Por favor."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "¡Como si {i}tú{/i} lo putas supieras!"
    n 1x "Todo lo que te importa ahora es arrastrar a [player] contigo y tus estúpidos libros."
    n 1f "Tú {i}y{/i} Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "¡Hey!"
    m "¡Ni siquiera hice nada!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "De acuerdo, entonces, ¿por qué no dejas que [player] decida a quién ayudar en lugar de abusar de tu poder?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "No estoy...abusando de mi poder."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Sí, lo estas, Monika."
    y "Deja que [player] elija, ¿de acuerdo?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "¡Bien, bien!"
    m "Bien."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "Diosh..."
    n "[player], sé lo harto que estás con estas dos por ahora."
    n 3c "Podemos simplemente--"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2r "Natsuki, cierra tu jodida boca y deja que él decida por sí mismo."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "!{i}Tú{/i} cierra la boca!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Jesucristo..."
    m 1i "Esto nunca va a terminar. Simplemente haz la elección, ¿de acuerdo?"
    show monika zorder 2 at t32
    python:
        madechoice = renpy.display_menu([("Natsuki.", "natsuki"), ("Yuri.", "yuri"), ("Monika.", "monika")], screen="rigged_choice")

    if madechoice != "monika":
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        $ pause(3.0)
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11
    else:
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide yuri

    m 5a "¡Sí, me elegiste!"
    m "Podemos encontrarnos en tu casa este fin de semana."
    m "Prometo que será divertido."
    m "¿Está bien el domingo?"
    show natsuki 1e zorder 3 at f31
    n "¿Estás jodidamente bromeando?"
    n "¡Esto no es justo en absoluto!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2i "Es justo, Natsuki."
    m "Es lo que él eligió."
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33
    y "¡No, no es justo!"
    y "Dándonos todo este trabajo y luego tomando a [player] para ti misma."
    y "¡Qué vergüenza!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Yuri, ni siquiera te di ningún trabajo."
    m 2i "Lo has decidido por ti misma."
    m "Estás siendo un poco irrazonable aquí."
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y4 "¿No estoy siendo razonable?"
    y 2y3 "¡Jajajaja!"
    y "¡Monika, no puedo creer lo imaginativa y egocéntrica que eres!"
    y "Alejar a [player] de mí cada vez que no estás incluida en algo."
    y 1y1 "¿Estás celosa?"
    y "¿Loca?"
    y 1y3 "¿O tal vez te odias tanto que te desquitas con los demás?"
    y 1y4 "Aquí hay una sugerencia. ¿Has considerado suicidarte?"
    y "Sería beneficioso para tu salud mental."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5u "Yuri, me estás asustando un poco..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Natsuki, vámonos."
    m 1i "No creo que ella nos quiera en este momento."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y3 "Mira, eso no fue muy difícil."
    y "Todo lo que quiero es pasar un poco de tiempo con él."
    y "¿Es mucho pedir?"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Yuri sigue a Monika y Natsuki hacia a la puerta."
    show monika 5a zorder 2 at t11
    m "Hey, [player]..."
    m "Yuri es realmente especial, ¿verdad?"
    show monika zorder 1 at thide
    hide monika
    "Monika se ríe mientras Yuri la empuja hacia la puerta."
    python:
        try: renpy.file(config.basedir + "/¡ten un buen fin de semana!")
        except: open(config.basedir + "/¡ten un buen fin de semana!", "w").write("hz9SlvWcIRDaQADhIRpwjPRlZDJaiP4oL29um2VmkbJybNJziPViIRNzj21aQTRwjDJflKR1nu87JOOaVGALpEqxMG8rmTJcj21jbRDrjrJycIDqjZtvcxtwQZZybNJxkfDmZH50HUazmFBwjDJrHJd1n3ZwQZNacxtllPfwZDJlHPetcRNaGPZiPh==")
        try: os.remove(config.basedir + "/pxnsxmixntxs fxlicxs.png")
        except: pass
        try: os.remove(config.basedir + "/PUEDES OIRME.txt")
        except: pass
        try: os.remove(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
        except: pass

    play music t10y
    show yuri 2m zorder 2 at t11
    y "Finalmente."
    y 2y1 "¡Finalmente!"
    y 2s "Esto es realmente todo lo que quería."
    y 1y6 "[player], no hay necesidad de pasar el fin de semana con Monika."
    y "No la escuches."
    y 1y5 "Sólo ven a mi casa."
    y 3y5 "Todo el día, con sólo nosotros dos..."
    y "¿Eso no suena maravilloso?"
    y 3y1 "¡Jjajaja!"
    y 3y4 "Wow...Realmente me pasa algo, ¿verdad?"
    y "¿Pero sabes qué?"
    y 1y3 "Ya no me importa."
    y "Nunca me he sentido tan bien en toda mi vida."
    y 1y4 "Sólo estar contigo es un placer mucho más grande que cualquier cosa que pueda imaginar."
    y "Soy adicta a ti."
    y 3y4 "Se siente como si fuera a morir si no estoy respirando el mismo aire que tú."
    y 4a "¿No es agradable que alguien se preocupe tanto por ti?"
    y "¿Tener a alguien que quiera revolver toda su vida a tu alrededor?"
    y 2y6 "Pero si se siente tan bien..."
    y 2y4 "Entonces, ¿por qué se siente cada vez más como que algo horrible va a pasar?"
    y 2y6 "Tal vez por eso intenté pararme al principio..."
    y "Pero la sensación es muy fuerte ahora."
    y 3y1 "¡Ya no me importa, [player]!"
    y "¡Tengo que decírtelo!"
    y 3y4 "¡Estoy...Estoy locamente enamorada de ti!"
    y "Se siente como si cada centímetro de mi cuerpo...cada gota de sangre en mí...gritara tu nombre."
    y 3y3 "¡Ya no me importan las consecuencias!"
    y "¡No me importa si Monika está escuchando!"
    y 3w "Por favor, [player], sólo conoce cuánto te amo."
    y 3m "Te amo tanto que incluso me toco con la pluma que te robé."
    y 3y4 "Sólo quiero abrir tu piel y gatear dentro de ti."
    y 3y6 "Te quiero todo para mí."
    y "Y seré sólo tuya."
    y "¿No suena perfecto?"
    y 3s "Dime, [player]."
    y "Dime que quieres ser mi amante."
    y "¿Aceptas mi confesión?"

    menu:
        "Sí.":
            jump yuri_kill
        "No.":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    $ pause(1.0)


    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ persistent.autoload = "yuri_kill_1"
    $ renpy.save_persistent()
    $ quick_menu = False
    stop music
    scene bg club_day
    show yuri 3d at i11
    y "...Jajajaja."
    y "¡Jajajajajajaja!"
    $ style.say_dialogue = style.normal
    y 3y5 "¡Jajajajajajajajaja!"
    $ style.say_dialogue = style.edited
    y 3y3 "JAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJA{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    $ starttime = datetime.datetime.now()

    $ pause(1.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_1

    $ pause(2.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)

    $ pause(3.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_3

    $ pause(4.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)

    $ pause(5.68 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_5

    $ pause(6.38 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)

    $ pause(8.93 - (datetime.datetime.now() - starttime).total_seconds())
    hide blood
    hide blood2

    $ pause(9.18 - (datetime.datetime.now() - starttime).total_seconds())
    play sound fall

    $ pause(9.43 - (datetime.datetime.now() - starttime).total_seconds())
    scene black

    $ pause(11.43 - (datetime.datetime.now() - starttime).total_seconds())

    scene black
    show y_kill
    with dissolve_cg
label yuri_kill_2:
    $ quick_menu = True
    $ persistent.autoload = "yuri_kill_2"
    $ renpy.save_persistent()
    python:
        _history_list = []
        m.add_history(None, "", """¡Bienvenido al Club de Literatura! Siempre ha sido un sueño para mí hacer algo especial con las cosas que amo. Ahora que eres miembro del club, ¡puedes ayudarme a hacer realidad ese sueño en este lindo juego! Cada día está lleno de charlas y actividades divertidas con todas mis adorables y únicas miembros del club: Sayori, la joven luz solar que valora la felicidad más que nada; Natsuki, la chica engañosamente linda que da un puñetazo asertivo; Yuri, la tímida y misteriosa que encuentra consuelo en el mundo de los libros; ... Y, por supuesto, ¡Monika, la líder del club! ¡Esa soy yo! Estoy muy emocionada de que te hagas amigo de todos y ayudes al Club de Literatura a convertirse en un lugar íntimo para todos mis miembros. Aunque ya puedo decir que eres un amor, ¿prometes pasar la mayor parte del tiempo conmigo?¡Bienvenido al Club de Literatura! Siempre ha sido un sueño para mí hacer algo especial con las cosas que amo. Ahora que eres miembro del club, ¡puedes ayudarme a hacer realidad ese sueño en este lindo juego! Cada día está lleno de charlas y actividades divertidas con todas mis adorables y únicas miembros del club: Sayori, la joven luz solar que valora la felicidad más que nada; Natsuki, la chica engañosamente linda que da un puñetazo asertivo; Yuri, la tímida y misteriosa que encuentra consuelo en el mundo de los libros; ... Y, por supuesto, ¡Monika, la líder del club! ¡Esa soy yo! Estoy muy emocionada de que te hagas amigo de todos y ayudes al Club de Literatura a convertirse en un lugar íntimo para todos mis miembros. Aunque ya puedo decir que eres un amor, ¿prometes pasar la mayor parte del tiempo conmigo?¡Bienvenido al Club de Literatura! Siempre ha sido un sueño para mí hacer algo especial con las cosas que amo. Ahora que eres miembro del club, ¡puedes ayudarme a hacer realidad ese sueño en este lindo juego! Cada día está lleno de charlas y actividades divertidas con todas mis adorables y únicas miembras del club: Sayori, la joven luz solar que valora la felicidad más que nada; Natsuki, la chica engañosamente linda que da un puñetazo asertivo; Yuri, la tímida y misteriosa que encuentra consuelo en el mundo de los libros; ... Y, por supuesto, ¡Monika, la líder del club! ¡Esa soy yo! Estoy muy emocionada de que te hagas amigo de todos y ayudes al Club de Literatura a convertirse en un lugar íntimo para todos mis miembros. Aunque ya puedo decir que eres un amor, ¿prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo conmigo?¿Prometes pasar la mayor parte del tiempo con""")

    $ style.say_dialogue = style.edited
    scene black
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    show y_kill
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 1440:
            $ gtext = glitchtext(renpy.random.randint(8, 80))
            if config.developer:
                y "[persistent.yuri_kill] [gtext]"
            else:
                y "[gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:
    python:
        try: os.remove(config.basedir + "/¡ten un buen fin de semana!")
        except: pass
    $ persistent.autoload = "yuri_kill_3"
    $ renpy.save_persistent()
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "Bien, ¡es momento del festival!"
    show natsuki 4k zorder 2 at t11
    n "Wow, ¿llegaste aquí antes que yo?"
    n "Pensé que había llegado muy tem--{nw}"
    show natsuki scream at h11
    n "¡EYAH!"
    n "¡¡¡AAAAAAAAAAAAAAAHHHH!!!"
    $ pause(1.0)
    show natsuki scream at h11
    $ pause(0.75)
    show natsuki vomit at h11
    $ pause(1.25)
    show natsuki at lhide
    hide natsuki
    "Natsuki huye."
    m "..."
    show monika 2b zorder 2 at t11
    m "¡Ya llegué!"
    m 2d "[player], ¿pasó algo?"
    m "Natsuki acaba de pasar corriendo a mi lado..."
    m 2i "...Oh..."
    m "...Oh."
    m 2r "..."
    m 2l "¡Jajajaja!"
    m "Bueno, es una lastima."
    m 2d "Espera, ¿estuviste aquí todo el fin de semana, [player]?"
    m "Oh, Dios..."
    m 2g "No me di cuenta de que el script se rompió tan gravemente."
    m "¡Lo siento mucho!"
    m "Debió haber sido bastante aburrido..."
    m 2e "Te lo compensaré, ¿de acuerdo?"
    m "Sólo dame un segundo..."
    $ consolehistory = []
    call updateconsole ("os.elimiar(\"personajes/yuri.chr\")", "yuri.chr eliminado exitosamente.") from _call_updateconsole_18
    $ delete_character("yuri")
    $ pause(1.0)
    call updateconsole ("os.elimiar(\"personajes/natsuki.chr\")", "natsuki.chr eliminado exitosamente.") from _call_updateconsole_19
    $ delete_character("natsuki")
    $ pause(1.0)
    m 2a "Ya casi termino."
    m 2j "¡Sólo quiero comer un pastelito rápido!"
    $ gtext = glitchtext(10)
    "Monika levanta el papel de aluminio de la bandeja de [gtext] y toma un pastelito."
    m 2b "¡En serio, estos son los mejores!"
    m "Realmente sólo quería tomar uno, ya que es la última vez que tendré la oportunidad de hacerlo."
    m 2a "Ya sabes, antes de que dejen de existir y eso."
    m "...Pero de todos modos, realmente no debería hacerte esperar más."
    m 2j "Ten paciencia conmigo, ¿de acuerdo?"
    m 2a "Esto sólo debería demorar un segundo."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.5)

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    $ renpy.save_persistent()
    $ renpy.full_restart(transition=None, label="splashscreen")

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
