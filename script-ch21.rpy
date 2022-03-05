label ch21_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t2g3
    show monika 5 zorder 2 at t11
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "¡Hola de nuevo, [player]!"
    m "Me alegra ver que no huiste de nosotras. ¡Jajaja!"
    mc "Nah, no te preocupes."
    mc "Esto puede ser un poco extraño para mí, pero al menos mantengo mi palabra."
    show monika zorder 1 at thide
    hide monika
    "Bueno, estoy de vuelta en el Club de Literatura."
    "Fui el último en entrar, por lo que todas las demás ya están pasando el rato."
    show yuri glitch2 zorder 2 at t32
    y "Gracias por cumplir tu promesa, [player]."
    y 1a "Espero que esto no sea demasiado abrumador como compromiso para ti."
    y 1u "Haciéndote zambullir de cabeza en la literatura cuando no estás acostumbrado a ella..."
    show natsuki glitch1 zorder 2 at i33
    n "Oh, ¡vamos! Como si lo mereciera."
    n 4e "Tuviste que ser arrastrado aquí por Monika."
    n "No sé si planeas venir y pasar el rato, o qué..."
    n "Pero si no nos tomas en serio, entonces no verás el final de esto."
    show monika 2b onlayer front at l41
    m "Natsuki, ciertamente tienes una gran boca para alguien que guarda su colección de manga en el salón del club."
    n 4o "¡¡M-M-M...!!"
    show monika onlayer front at lhide
    hide monika onlayer front
    "Natsuki se encuentra atrapada entre decir \"Monika\" y \"Manga\"."
    show natsuki at h33
    n 1v "¡¡El Manga es literatura!!"
    show natsuki zorder 1 at thide
    hide natsuki
    "Rápidamente derrotada, Natsuki vuelve a su asiento."
    show yuri 2s zorder 2 at t11
    y "Lo siento, [player]..."
    y "Nos aseguraremos de poner tu comodidad primero, ¿de acuerdo?"
    show yuri 2g
    "Yuri le dispara a Natsuki con una mirada de decepción."
    y 1a "Um, de todos modos..."
    y "Ahora que estás en el club y todo..."
    y "...¿Quizás tengas interés en leer un libro?"
    mc "Bueno..."
    mc "No puedo decir que no."
    mc "Como dijiste, estoy en este club ahora."
    mc "Entonces me parece correcto hacer algo así, si me preguntas."
    y 4b "E-Espera..."
    y "¡No quise decir eso!"
    y "Uu..."
    y "Si realmente no quieres, entonces olvida que dije algo..."
    mc "Ah - No, no es eso, Yuri."
    mc "Quiero intentar ser parte de este club."
    mc "Así que incluso si no leo a menudo, estaría feliz de escoger un libro si así lo quieres."
    y 3t "¿E-Estás seguro...?"
    y "Simplemente me sentí como..."
    y 3u "...Bueno, como vicepresidente y todo..."
    y "...Que debería ayudarte a comenzar con algo que te pueda gustar."
    "Yuri busca en su bolso y saca un libro."
    y 1s "No quería que te sintieras excluido..."
    y "Así que escogí un libro que pensé que podrías disfrutar."
    y "Es una lectura breve, por lo que debe mantener tu atención, incluso si no sueles leer."
    y "Y podríamos, ya sabes..."
    show yuri at sink
    y 4b "Discutirlo...Si quieres..."
    "E-Esto es..."
    "¿Cómo es que esta chica es tan linda por accidente?"
    "Incluso eligió un libro que cree que me va a gustar, a pesar de que no leo mucho..."
    mc "Yuri, ¡gracias! Definitivamente leeré esto!"
    "Entusiasmadamente tomo el libro."
    show yuri 2m zorder 2 at t11
    y "Uff..."
    y 2a "Bueno, puedes leerlo a tu propio ritmo."
    y "Quiero escuchar lo que piensas."
    show yuri zorder 1 at thide
    hide yuri
    show layer master


    "Ahora que todas se han acomodado, esperaba que Monika iniciara algunas actividades programadas para el club."
    "Pero eso no parece ser el caso."
    "La cara de Yuri ya está enterrada en un libro."
    "No puedo dejar de notar su intensa expresión, como si estuviera esperando esta oportunidad."
    "Mientras tanto, Natsuki está hurgando en el armario."


    $ nextscene = poemwinner[0] + "_exclusive2_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_25

    return

label ch21_end:
    stop music fadeout 1.0
    scene bg club_day2
    with wipeleft_scene
    play music t3g
    queue music t3g2
    mc "Uff..."
    "Creo que esas son todas."
    "Miro alrededor."
    "Eso fue un poco más estresante de lo que esperé."
    "Es como si todas me juzgaran por mis mediocres habilidades de escritura..."
    "Incluso si tratan de ser amables, no hay forma de que mis poemas puedan hacer frente a los suyos."
    "Esto es un Club de Literatura, después de todo."
    "Suspiro."
    "Supongo que esto es en lo que me terminé metiendo."
    "Al otro lado de la sala, Monika está escribiendo algo en su libreta."
    "Mis ojos aterrizan en Yuri y Natsuki."
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "Con cautela intercambian hojas de papel, compartiendo sus respectivos poemas."
    show yuri 2i zorder 2 at t21
    "Mientras leen, miro cada una de sus expresiones cambiar."
    "Las cejas de Natsuki se fruncen en respuesta a su frustración."
    "Mientras tanto, Yuri sonríe tristemente."
    show natsuki zorder 3 at f22
    n 1q "{i}(¿Qué es este lenguaje...?){/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "¿Eh?"
    y "Um...¿Dijiste algo?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "Oh, no es nada."
    "Natsuki devuelve el poema al escritorio con una mano."
    n "Creo que se podría decir que es elegante."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2i "Ah-- Gracias..."
    y "El tuyo es...lindo..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "¿Lindo?"
    n 1h "¿Perdiste completamente el simbolismo o algo así?"
    n "Claramente se trata de la sensación de rendirse."
    n "¿Cómo eso puede ser lindo?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3f "¡E-Eso lo se!"
    y "Sólo me refería..."
    y 3h "Tu lenguaje, supongo..."
    y "Sólo trataba de decir algo amable..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "¿Eh?"
    n 4w "¿Quieres decir que te tienes que esforzar para encontrar algo amable que decir?"
    n "Gracias, ¡pero eso no salió nada amable!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1i "Um..."
    y "Bueno, tengo un par de sugerencias..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "Hmph."
    n "Si estuviera buscando sugerencias, le hubiera preguntado a alguien que si le guste mi poema."
    n "Y hay personas que {i}si lo hicieron{/i}, por cierto."
    n 5e "A Monika le gustó."
    n "¡Y a [player] también!"
    n "Así que basados en eso, me encantaría darte algunas sugerencias."
    n "Primero que nada--"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "Discúlpame..."
    y "Aprecio tu oferta, pero he pasado mucho tiempo estableciendo mi estilo de escritura."
    y 2h "No espero cambiarlo pronto, a menos, por supuesto, que me encuentre con algo particularmente inspirador."
    y "Lo cual no he hecho aún."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "¡Nn...!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "Y a [player] también le gustó mi poema, sabes."
    y "Incluso me dijo que lo impresionó."
    stop music fadeout 1.0
    "De repente Natsuki se para."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "¿Oh?"
    n "No me di cuenta de que estabas tan interesada en tratar de impresionar a nuestro nuevo miembro, Yuri."
    play music t7a
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "¡¿E-Eh?!"
    y "¡Eso no es lo que...!"
    y 1o "Uu..."
    y "Tú...Tú estás..."
    "Yuri también se para."
    y 2r "¡Tal vez estás celosa de que [player] aprecie más mis consejos que los tuyos!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "¡Huh! ¿Y como sabes que no prefiere {i}mis{/i} consejos más?"
    n "¿Tan engreída eres?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "¡Yo...!"
    y "No..."
    y "Si fuera engreída..."
    y 1r "...¡Deliberadamente haría lindo en extremo todo lo que tengo!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Uuuuuu...!"
    n "¡¿Sabes qué?!"
    n "¡¡Yo no fui a la que sus pechos de pronto le crecieron cuando [player] empezó a aparecer!!"
    show yuri 3p at h21
    show natsuki zorder 2 at t22
    y "¡¡N-Natsuki!!"
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show monika 3l behind yuri, natsuki at l41
    m "Um, Natsuki, eso es un poco--"
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "¡Esto no te involucra!"
    show monika at lhide
    hide monika
    show yuri 2h zorder 2 at f21
    show natsuki zorder 2 at t22
    queue music t7g
    $ timeleft = 12.453 - get_pos()
    show noise zorder 3 at noisefade(25 + timeleft)
    show vignette as flicker zorder 4 at vignetteflicker(timeleft)
    show vignette zorder 4 at vignettefade(timeleft)
    show layer master at layerflicker(timeleft)
    y "Poner tus propias inseguridades sobre otros así..."
    y "Realmente actúas tan inmadura como te ves, Natsuki."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4o "{i}¿Yo?{/i} ¡Mira quién habla, intento de perra edgy!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "¿Edgy...?"
    y 2r "¡Lo siento, mi estilo de vida es demasiado para que lo entienda alguien de tu edad!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4f "¿¿Ves??"
    n "¡Sólo decir eso demuestra mi punto!"
    n 4e "La mayoría de las personas aprenden a superarse después de graduarse de la preparatoria, sabes."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "¡Si quieres probar algo, entonces deja de hostigar a los demás con tu actitud enfermiza!"
    y "¿Crees que puedes contrarrestar tu personalidad tóxica simplemente vistiéndote y actuando linda?"
    y 1k "Lo único lindo de ti es lo duro que lo intentas."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2y "Wow, ten cuidado o podrías cortarte en ese borde, Yuri."
    n "Oh, mi error...Ya lo hiciste, ¿no?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "¿A-Acabas de acusarme de que me corto?"
    y 3r "¡¿Qué mierda le pasa a tu mente?!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "¡Si, vamos!"
    n "¡Dejemos que [player] escuche todo lo que en verdad piensas!"
    n "¡Estoy seguro de que va a estar loco por ti después de esto!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "¡A-Ah--!"
    show yuri zorder 2 at t21
    "De pronto Yuri se voltea hacia a mí, como si se acabara de dar cuenta que estaba aquí."
    show yuri zorder 3 at f21
    y 2n "¡[player]...!"
    y "¡Ella-- Ella sólo trata de hacerme ver mal...!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "¡No es cierto!"
    n "¡Ella empezó!"
    show yuri 1t zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    $ style.say_dialogue = style.normal
    mc "..."
    $ style.say_dialogue = style.edited
    "{cps=*2}¡¿Cómo fui arrastrado a esto en primer lugar?!{/cps}{nw}"
    "{cps=*2}No es como si supiera algo sobre escribir...{/cps}{nw}"
    "{cps=*2}Pero con quien esté de acuerdo, ¡probablemente piense mejor de mí!{/cps}{nw}"
    "{cps=*2}Entonces, ¡por supuesto que esa va a ser...!{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ menu_clicked = 0
    window hide(None)
    label ch21_end_menu:
        menu:
            "Natsuki.":
                jump menu_click
            "Yuri.":
                jump menu_click

    label menu_click:
        $ srf = screenshot_srf()
        show layer screens:
            truecenter
            zoom 1.00
        show screen tear(20, 0.1, 0.1, 0, 40, srf)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        hide screen tear
        stop sound
        $ menu_clicked += 1
        if menu_clicked < 9:
            show layer master:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            show layer screens:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            jump ch21_end_menu


    window show(None)
    stop music
    $ menu_clicked = 8
    $ quick_menu = False
    show layer master:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show layer screens:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show monika 1 onlayer front at i11:
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    show layer master
    show layer screens
    show monika 1 onlayer front at i11
    window auto
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    show monika 1m onlayer front at i11
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Um..."
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Oye, [player]..."
    show monika 1e onlayer front at i11
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "¿Por que no \nsalimos por un \nrato?"
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "¿Vale?"
    scene bg corridor
    hide monika onlayer front
    show monika 1n onlayer master at t11
    with wipeleft_scene
    $ quick_menu = True
    m "Lamento lo que pasó..."
    m "Realmente no deberían haber intentado involucrarte."
    m 1e "Probablemente sea mejor para nosotros permanecer fuera de esto..."
    m "Volveremos adentro una vez que terminen de gritar."
    m 5 "Jajaja..."
    m "Que buena presidenta soy, ¿verdad?"
    m 1m "Ni siquiera puedo enfrentarme a los miembros de mi propio club..."
    m "Ojalá pudiera ser un poco más asertiva a veces."
    m "Pero nunca tengo en mí poner mi pie en contra de los demás..."
    m 1e "Lo entiendes, ¿verdad?"
    m "De todas formas..."
    m 1a "Si esto hace que quieras pasar menos tiempo con las demás, está bien."
    m 1j "Me encantaría pasar el tiempo contigo en su lugar..."
    show monika zorder 1 at thide
    hide monika
    "De repente, Natsuki sale corriendo del salón."
    show natsuki 12h zorder 2 at t11
    n "..."
    show natsuki 12f at lhide
    $ pause(0.75)
    hide natsuki
    "Ella rápidamente huye."
    show monika 1l zorder 2 at t11
    m "Oh querida..."
    m "...Bueno, parece que ya terminaron..."
    scene bg club_day2
    with wipeleft_scene
    y "No quería..."
    y "No quería..."
    y "No quería..."
    "Yuri se balancea hacia adelante y hacia atrás en su escritorio con sus palmas en la frente."
    mc "¿Yuri...?"
    show yuri 4d zorder 2 at t11
    y "¡No quería!!"
    mc "T-Te creo..."
    "No tengo idea de lo que Yuri podría haberle dicho a Natsuki."
    "O hecho."
    y "[player]."
    y "Por favor, no me odies."
    y "¡Por favor!"
    y "¡No soy así!"
    y "Hay algo mal conmigo..."
    show monika 1d zorder 3 at f31
    m "Está bien, Yuri."
    m "Sabemos que no lo quisiste hacer."
    m 1j "Además, estoy segura de que Natsuki se olvidará de todo mañana."
    m 1a "Completamente."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    show yuri zorder 3 at t32
    show monika zorder 2 at f31
    m "De todos modos, la reunión ha terminado, así que puedes ir a casa ahora si quieres."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4a "..."
    show yuri zorder 2 at t32
    "Yuri me mira como si quisiera decir algo."
    "Pero ella sigue dirigiéndose a Monika."
    show yuri zorder 3 at f32
    y 2v "P-Puedes ir primero, Monika..."
    y "Me gustaría quedarme un poco más."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2k "Soy la presidenta, así que debería ser la última en salir."
    m "Esperaré a que termines."
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    y "..."
    y "Bueno-- soy Vicepresidenta, entonces..."
    y "Por favor, déjame tomar esa responsabilidad hoy."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2i "Suena como si no me quisieras cerca, Yuri."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 3p "¡No-No es eso!"
    y 3o "No es eso..."
    y 3n "Yo sólo..."
    y 3q "No tuve la oportunidad de discutir mi libro con [player]..."
    y "Sería...vergonzoso contigo escuchando..."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "{i}*Suspiro*{/i}"
    m 1d "Supongo que realmente no tengo otra opción, ¿verdad?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1t "L-Lo siento por causar problemas..."
    $ gtext = glitchtext(20)
    y 1s "Pero realmente aprecio tu compren{nw}"
    play music g1
    show monika 1 onlayer front at i31
    y glitch "Pero realmente aprecio tu compren{fast}[gtext] [gtext][gtext]{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
