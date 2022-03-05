image sayori end-glitch:
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    1.00
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"

label ch40_main:
    $ s_name = "Sayori"
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    python:
        if not persistent.monika_back:
            try:
                renpy.file("../personajes/monika.chr")
                renpy.call_screen("dialog", message="Por favor, deja de jugar con mi corazón.\nNo quiero regresar.", ok_action=Return())
                persistent.monika_back = True
            except:
                pass

    $ delete_character("monika")
    play music t2
    "Es un día escolar normal, como cualquier otro."
    "Como de costumbre, estoy rodeado de parejas y grupos de amigos caminando juntos hacia la escuela."
    "Siempre me digo que es hora de conocer a algunas chicas o algo así..."
    show sayori 1a at t11
    s "Oye, [player]..."
    "...Bueno, ya hay una chica."
    "Esa chica es Sayori, mi vecina y buena amiga desde que éramos niños."
    "Solíamos caminar juntos a la escuela todos los días..."
    "...Y recientemente, retomamos ese hábito una vez más."
    s "[player], ¿estás orgulloso de mí?"
    mc "¿Eh? ¿Por qué?"
    s 1c "Ya sabes..."
    s "¡Por despertarme a tiempo!"
    mc "Bueno, has estado haciendo eso por un tiempo..."
    s "¡Ajá!"
    s 4h "¡Pero nunca dijiste nada al respecto!"
    show sayori at s11
    s "Aunque caminamos juntos a la escuela todos los días..."
    mc "Bueno, sí..."
    mc "Siempre pensé que estaba implícito."
    mc "Es vergonzoso decirlo en voz alta."
    s 1d "Vamos, ¿por favor?."
    s "Es una buena motivación~"
    mc "Bien, bien..."
    mc "Estoy orgulloso de ti, Sayori."
    show sayori at t11
    s 1q "Jejeje~"
    show sayori zorder 1 at thide
    hide sayori
    "Cruzamos la calle juntos y nos dirigimos a la escuela."
    "A medida que nos acercamos, las calles se llenan cada vez más con otros estudiantes haciendo su viaje diario."
    show sayori 3a zorder 2 at t11
    s "Por cierto, [player]..."
    s "¿Ya has decidido un club para unirte?"
    mc "¿Un club?"
    mc "Ya te lo dije, realmente no estoy--"
    "Comienzo a decir lo que siempre digo, que no estoy interesado en unirme a ningún club."
    "Pero algo me dice que Sayori ahora se ofendería más si digo eso."
    "Después de todo, ¿cómo podría decirle que los clubs son una pérdida de tiempo..."
    "...Cuando está comenzando un club por su cuenta?"
    mc "...En realidad, sí."
    mc "Creo que me he decidido por un club."
    show sayori at h11
    s 1m "¿De verdad?"
    s 1r "¿Cuál? ¡Dime!"
    mc "Hmm..."
    mc "Creo que lo mantendré como sorpresa."
    s 5d "Boo..."
    s "Eres malo."
    mc "Ten paciencia, pronto lo sabrás."
    "Solía​​ preguntarme por qué me dejaba ser sermoneado por una chica tan despreocupada."
    "Pero comencé a darme cuenta de que de alguna manera, la envidio."
    "Cuando Sayori pone su mente en algo, puede lograr grandes cosas."
    "Así que es por eso que siento que debería hacer algo especial por ella."

    scene bg class_day
    with wipeleft_scene

    "El día escolar fue tan común como siempre, y se acabó antes de que me diera cuenta."
    "Después de empacar mis cosas, me pongo de pie, juntando motivación."
    mc "Veamos..."
    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene
    "Recuerdo el número de salón del club por un volante que vi."
    "Camino a través de la escuela y al piso de arriba, una sección de la escuela que rara vez visito, generalmente utilizada para clases y actividades de tercer año"
    "En poco tiempo, encuentro el salón."
    "Tímidamente abro la puerta frente a mí."
    scene bg club_day
    with wipeleft
    play music t3
    mc "¿Hola...?"
    show sayori 1m at t32
    s "¡Ah!"
    s "¡¿[player]...?!"
    s 1c "¿Q-qué estás haciendo aquí?"
    mc "Bueno...Yo sólo--"
    "¿Eh? Miro alrededor de la habitación."
    show natsuki 3a at f31
    n "Huh."
    n "¿Así que tu eres [player]? ¿El chico del que Sayori habla tanto?"
    show natsuki at t31
    show yuri 2t at f33
    y "¡G-Gracias por pasar!"
    y 2m "Es un placer conocerte, [player]."
    y "Somos el Club de Literatura."
    y 3v "¡E-Espero que disfrutes tu visita!"
    show yuri at t33
    show natsuki at f31
    n 3g "Vamos, Yuri..."
    n "No es necesario ser tan formal."
    n "Él va a pensar que somos realmente estrictas o algo..."
    show natsuki at t31
    $ y_name = "Yuri"
    $ n_name = "Natsuki"
    show yuri at f33
    y 3q "Ah..."
    y "Perdón, Natsuki..."
    show yuri at t33
    "La alta, cuyo nombre aparentemente es Yuri, parece ser bastante tímida comparada con las demás."
    "En comparación, la chica llamada Natsuki - a pesar de su tamaño - parece ser la más asertiva."
    mc "Bueno, es un placer conocerlas a las dos."
    mc "Espero con interés trabajar con ustedes."
    show sayori at f32
    s 1n "¡T-Trabajar...?"
    s 1b "[player], no me digas que..."
    s "Tu vas a..."
    show sayori at t32
    mc "Es correcto."
    mc "El club al que he decidido unirme es el tuyo, Sayori."
    mc "El club de literatura."
    "Los ojos de Sayori se iluminan."
    show sayori at f32
    s 1n "...No puede ser."
    s 1s "¡No puede ser!"
    show sayori at hf32
    s 4s "¡Aaaahhhhhh!"
    "Sayori me rodea con sus brazos, saltando de arriba a abajo."
    show sayori at t32
    mc "O-Oye--"
    show natsuki at f31
    n 3y "Jejeje."
    n "Bueno, si Sayori está así de feliz, entonces estoy segura de que no será tan malo tenerte cerca."
    show natsuki 3a at t31
    show yuri at f33
    y 1s "Sin mencionar que somos cuatro ahora."
    y "Eso significa que podemos convertirnos en un club oficialmente reconocido."
    show yuri at t33
    show sayori at f32
    s 1x "¡No sé qué decir!"
    s "¡Tenemos que celebrar!"
    show sayori at t32
    show yuri at f33
    y 1m "Juju."
    y "Qué día apropiado para eso, ¿no es así?"
    show yuri 1a at t33
    show sayori at f32
    s 1r "¡Sí!"
    s 1x "Después de todo, Natsuki decidió--"
    show sayori at t32
    show natsuki at f31
    n 1w "Hey, ¡no arruines la sorpresa!"
    show natsuki at t31
    show sayori at f32
    s 5a "Jejeje, perdón..."
    show sayori at t32
    show natsuki at f31
    n 1k "Todos sientense en la mesa, ¿de acuerdo?"
    show natsuki at t31
    show yuri at f33
    y 1a "¿Qué tal si hago un poco de té también?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "Las chicas tienen algunos escritorios acomodados para formar una mesa."
    "Natsuki y Yuri caminan hacia la esquina del salón, donde Natsuki toma una bandeja envuelta y Yuri abre el armario."
    "Aún incómodo, tomo asiento al lado de Sayori."
    "Natsuki regresa con orgullo a la mesa, con la bandeja en la mano."
    show natsuki 2z zorder 2 at t22
    n "Bieeen, ¿están listos?"
    n "...¡Ta-daa!"
    show sayori 4m zorder 2 at t21
    s "¡Uwooooah!"
    "Natsuki levanta el papel de aluminio de la bandeja para revelar una docena de pastelitos blancos y esponjosos decorados para que parezcan pequeños gatos."
    "Los bigotes están dibujados con glaseado, y pequeños trozos de chocolate se utilizaron para hacer las orejas."
    show sayori at f21
    s 4r "¡Qué lindooooo~!"
    show sayori at t21
    mc "Wow, se ven geniales."
    show natsuki at f22
    n 2d "Jejeje. Bueno, ya sabes."
    n "¡Sólo apúrense y tomen uno!"
    show natsuki at t22
    "Sayori agarra uno, luego yo."
    show sayori at f21
    s 4q "¡Está delicioso!"
    show sayori at t21
    "Sayori habla con la boca llena y ya ha logrado mancharse de glaseado en la cara."
    "Giro el pastelito con los dedos, buscando el mejor ángulo para tomar un bocado."
    show sayori zorder 1 at thide
    hide sayori
    show natsuki 1c zorder 2 at t32
    "Natsuki está callada."
    "No puedo evitar notar su mirada furtiva en mi dirección."
    "¿Está esperando a que lo muerda?"
    "Finalmente lo hago."
    "El glaseado es dulce y lleno de sabor - Me pregunto si lo hizo por su cuenta."
    mc "Está muy bueno."
    mc "Gracias, Natsuki."
    n 42c "B-Bueno...¡Por supuesto que sí!"
    n "¡Soy una profesional, después de todo!"
    n 42a "No hay necesidad de agradecerme ni nada..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Mientras Natsuki lucha por aceptar el cumplido, Yuri regresa a la mesa, cargando un juego de té."
    "Ella coloca cuidadosamente una taza de té en frente de cada uno antes de colocar la tetera al lado de la bandeja de pastelitos."
    show yuri 1a zorder 2 at t11
    mc "¿Guardan un juego de té completo en este salón?"
    y "No te preocupes, los profesores nos dieron permiso."
    y "De todas formas, ¿una taza de té caliente no ayuda a disfrutar más de un buen libro?"
    mc "Ah...Y-Yo supongo..."
    show natsuki 2y at f31
    n "Jejeje. ¿Ya estamos tratando de impresionar a nuestro nuevo miembro, Yuri?"
    show natsuki at t31
    show yuri at f11
    y 3n "¿Eh?! E-Esa no es mi..."
    show yuri at t11
    show natsuki at thide
    hide natsuki
    "Insultada, Yuri aleja la mirada."
    y 4b "Esa no es mi intención, sabes..."
    mc "Te creo."
    mc "Bueno, el té y la lectura pueden no ser un pasatiempo para mi, pero al menos disfruto el té."
    y 2u "Me alegro..."
    "Yuri sonríe débilmente en alivio."
    y "Así que, [player], ¿qué tipo de cosas te gusta leer?"
    mc "Bueno...Ah..."
    "Teniendo en cuenta lo poco que he leído estos últimos años, realmente no tengo una buena manera de responder eso."
    mc "...Manga..."
    "Murmuro en voz baja, medio en broma."
    show natsuki 1c zorder 2 at t41
    "De repente, la cabeza de Natsuki se levanta en mi dirección."
    "Parece que quiere decir algo, pero se queda callada."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "N-No lees mucho, supongo..."
    mc "...Bueno, eso puede cambiar..."
    "¿Qué estoy diciendo?"
    "Hablé sin pensar después de ver la sonrisa triste de Yuri."
    mc "De todas formas, ¿qué hay de ti, Yuri?"
    y 1l "Bueno, veamos..."
    "Yuri traza el borde de la taza de té con su dedo."
    y 1a "Mis favoritos generalmente son novelas que construyen mundos de fantasía profundos y complejos."
    y "El nivel de creatividad y artesanía detrás de ellos es increíble para mí."
    y 1f "Y contar una buena historia en un mundo tan extraño es igualmente impresionante."
    "Yuri continúa, claramente apasionada por su lectura."
    "Parecía tan reservada y tímida desde el momento en que entré, pero es obvio por la forma en que sus ojos brillan que encuentra su comodidad en el mundo de los libros, no en las personas."
    y 2m "Pero ya sabes, me gustan muchas cosas."
    y 2a "No te sientas intimidado si no lees mucho, ¿de acuerdo?"
    y "Estoy segura de que podemos encontrar algo que tengamos en común."
    show yuri at t22
    show natsuki 2c at f21
    n "Oye, Yuri..."
    show natsuki at t21
    show yuri at f22
    y 2f "¿Eh?"
    show yuri at t22
    show natsuki at f21
    n 2h "Bueno, sobre...ya sabes, lo primero que dijo..."
    show natsuki at t21
    mc "¿Manga?"
    show yuri at f22
    y 2i "Así es..."
    y "Natsuki tiende a leer manga en el salón del club--"
    show yuri at t22
    show natsuki at f21
    n 1r "¡¡N-No lo digas en voz alta!!"
    "Por alguna razón, Natsuki parece avergonzada."
    n 1q "Además..."
    n "El manga...es literatura también, ¿sabes?"
    n 1w "Entonces...si [player] quiere leer algo de mi manga, ¡no intentes detenerlo!"
    show natsuki 1i at t21
    show yuri at f22
    y 1l "Natsuki..."
    y "Yo no haría tal cosa."
    y 1i "Sin embargo, también podría ser bueno para nosotros diversificarnos un poco..."
    y "Él puede aprovechar esta oportunidad para probar algo nuevo."
    y 1s "¿No estas de acuerdo, [player]?"
    show yuri at t33
    show natsuki at t32
    show sayori 1l at f31
    s "Q-Quizás--"
    "Sintiendo la tensión, Sayori salta."
    s 1x "¡Quizás todos podamos probar algo nuevo!"
    s 1l "Creo que podría ser divertido..."
    s 1c "¡Y todos nos conoceremos un poco mejor!"
    s 1l "Quiero decir..."
    s "Ese es el tipo de cosas que hacen los clubs de literatura...¿verdad?"
    show sayori at t31
    show yuri at f33
    y 1v "..."
    y "Y-Yo no estoy en desacuerdo..."
    show yuri at t33
    show natsuki at f32
    n 2j "Sí..."
    n "Tienes razón, como siempre, presidenta."
    show natsuki at t32
    show sayori at f31
    s 1q "Jejeje~"
    show sayori at t31
    show natsuki at f32
    n 2c "Supongo que eso significa que debería intentar buscar una novela o algo, ¿verdad...?"
    show natsuki at t32
    mc "Bueno, ya somos dos..."
    mc "No me molesta hacerlo si no soy el único."
    show sayori at thide
    hide sayori
    show natsuki at f21
    show yuri at t22
    n 2y "Entonces en cuanto a Yuri..."
    show natsuki at t21
    show yuri at f22
    y 2n "¿Eh...?"
    y "¿T...Tengo que leer manga...?"
    show yuri at t22
    show natsuki at f21
    n 4i "Caray..."
    n 4h "¡Fuiste tú quien sugirió que nos diversificáramos!"
    n "Deberías ser un poco más abierta de mente..."
    n 4u "Es un poco hiriente..."
    show natsuki at t21
    show yuri at f22
    y 2t "¿Hiriente...?"
    y 2v "Y-Yo no me di cuenta..."
    y "..."
    "Con una expresión culpable, Yuri se pone a pensar."
    y 2w "Lo siento por faltarle el respeto a tus intereses, Natsuki."
    y "Si...Si te gusta, entonces estoy segura de que es una forma digna de literatura."
    show yuri at t22
    show natsuki at f21
    n 5q "...¿Estás sólo diciendo eso sin razón?"
    show natsuki at t21
    show yuri at f22
    y "No..."
    y "Me he dado cuenta de mi error."
    y 2t "Entonces, si estás dispuesta a considerar comenzar una novela..."
    y 2u "...ofreceré mi gratitud encontrando un manga para leer también."
    show yuri at t22
    show natsuki at f21
    n 1l "¿De verdad?"
    n 12c "Q-Quiero decir..."
    n "...Me hace feliz que hagas eso por mí, Yuri."
    n 2c "Puedes confiar en mí para encontrar algo que realmente te guste, ¿de acuerdo?"
    show natsuki at t21
    show yuri at f22
    y 1m "Lo mismo digo..."
    y 1h "Quizás visitaré la librería después de la reunión del club."
    show yuri at t22
    show natsuki at f21
    n 1q "¿Sola...Solamente tú?"
    show natsuki at t21
    show yuri at f22
    y 3q "A-Ah--"
    y 4a "¿Te gustaría...Venir conmigo?"
    show yuri at t22
    show natsuki at f21
    n 5s "Um..."
    n "Si no te importa..."
    show natsuki at t21
    show yuri at f22
    y 3t "¡Para nada!"
    y "Siempre voy sola, así que..."
    show yuri at t22
    show natsuki at f21
    n "Si, yo tambien..."
    show natsuki at t21
    show sayori 4s at l41
    s "¡Esto es tan lindo~!"
    mc "Sayori, cállate..."
    show sayori at lhide
    hide sayori
    show natsuki at f21
    n 2j "Te mostraré algunos mangas ahí también, ¿de acuerdo?"
    show natsuki at t21
    show yuri at f22
    y 1a "Sí."
    y "Espero con ansias."
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri
    "Natsuki y Yuri comienzan a limpiar la comida."
    $ config.skipping = False
    $ config.allow_skipping = False
    show sayori 1q at t11
    s "Jejeje~"
    s 1x "Supongo que la reunión ha terminado, ¿eh?"
    mc "Sí, eso parece..."
    mc "Es agradable ver a todos llevarse bien."
    s 1q "¿No es así?"
    s 1d "Creo que a las dos les caes bien, [player]."
    mc "¿Eso crees...?"
    mc "Bueno, parece que todos se llevan un poco mejor contigo cerca, Sayori."
    s 1y "Aww, [player]~"
    s "¡No digas algo así, es vergonzoso!"
    mc "Bueno, lo que sea."
    mc "Me sorprendió cuando me dijiste que estabas comenzando un club..."
    mc "Pero creo que lo estás haciendo bien."
    s 1r "¡Vamos a convertirlo en el mejor club de todos los tiempos!"
    s 1x "Ahora que te uniste, todos los días serán muy divertidos."
    stop music fadeout 2.0
    s 1a "Oye, [player]..."
    s "Realmente quiero agradecerte."
    s "Quiero decir, estoy muy feliz de que te hayas unido al club y eso..."
    s "Pero la verdad es que ya sabía que ibas a hacerlo."
    s 1q "Jejeje~"
    s 1a "En realidad hay algo más."
    $ if all(clear for clear in persistent.clear): persistent.clearall = True
    if persistent.clearall:
        call ch40_clearall from _call_ch40_clearall
    else:
        call ch40_clearnormal from _call_ch40_clearnormal
    window hide(None)
    window auto
    $ quick_menu = False
    return

    label ch40_clearnormal:
        show sayori 1a zorder 2 at t11
        s "Quería agradecerte por haber eliminado a Monika."
        play music hb
        show black:
            alpha 0.5
            parallel:
                0.36
                alpha 0.5
                repeat
            parallel:
                0.49
                alpha 0.475
                repeat
        show layer master at heartbeat
        s 1b "Así es..."
        s "Sé todo lo que ella hizo."
        s 1x "Tal vez sea porque ahora soy la presidenta."
        s "Pero realmente sé todo, [player]."
        s 1q "Jejeje~"
        s 1d "Sé lo mucho que intentaste hacer felices a todas."
        s "Conozco todas las cosas horribles que Monika hizo para hacer a todos realmente tristes..."
        s 1b "Pero nada de eso importa más."
        s "Sólo somos nosotros ahora. {nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        show room_glitch zorder 1:
            xoffset -5
            0.1
            xoffset 5
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 0
        s "Sólo somos nosotros ahora.{fast}"
        hide room_glitch
        s 1d "Y me hiciste la chica más feliz del mundo."
        s "No puedo esperar para pasar todos los días así..."
        s "Contigo."
        play sound "sfx/s_kill_glitch1.ogg"
        show room_glitch zorder 1:
            xoffset -10
            0.1
            xoffset 0
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 1.0
        $ pause(0.3)
        stop sound
        s 1q "Por siempre y para siempre..."
        hide sayori
        show sayori 1a onlayer screens zorder 101 at face
        s "P"
        s "o"
        s "r"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        s "S"
        s "i"
        s "e"
        s "m"
        s "p"
        s "r"
        window show(None)
        stop music
        call screen dialog("No...", ok_action=Return())
        show layer master
        hide black
        show sayori end-glitch onlayer screens
        s "...¿Eh?"
        s "¿Q-Qué está pasando...?"
        call screen dialog("No dejaré que lo lastimes.", ok_action=Return())
        s "¿Quién..."
        s "D-Duele--"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        hide sayori onlayer screens
        $ pause(0.35)
        stop sound
        hide screen tear
        window show(None)
        s "Ah--"
        call screen dialog("Lo siento...Me equivoqué.", ok_action=Return())
        call screen dialog("No hay felicidad aquí después de todo...", ok_action=Return())
        call screen dialog("Adiós, Sayori.", ok_action=Return())
        call screen dialog("Adiós, [player].", ok_action=Return())
        call screen dialog("Adiós, Club de Literatura.", ok_action=Return())
        $ gtext = glitchtext(120)
        s "[gtext]{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.35)
        stop sound
        hide screen tear
        scene black
        $ pause(3.0)
        return

    label ch40_clearall:
        s "Quería agradecerte por pasar tanto tiempo con nosotras."
        play music mend
        s 2d "Trabajaste tan duro para hacernos felices a todas y cada una."
        s "Nos confortaste durante nuestros tiempos más difíciles."
        s "Y nos ayudaste a llevarnos bien la una con la otra."
        s 1a "¿Lo entiendes, [player]?"
        s "Como soy presidenta ahora, lo entiendo todo."
        s 1q "Realmente no querías perder ni una sola cosa de este juego, ¿o sí?"
        s 1a "Has guardado y cargado tantas veces, solo para asegurarte de poder pasar tiempo con todas."
        s "Sólo alguien que realmente se preocupe por el Club de Literatura llegaría tan lejos."
        s "Pero..."
        s 4d "Todo el tiempo, eso es todo lo que siempre quise."
        s "Para que todos sean felices y se preocupen el uno por el otro."
        s 4q "Jajaja..."
        s 1t "Es un poco triste, ¿sabes?"
        s "Después de todo lo que has hecho por nosotras, no hay mucho que pueda hacer por ti a cambio."
        s "Ya hemos llegado al final del juego."
        s 1y "Entonces..."
        s "Aquí es donde decimos adiós."
        s 1d "Gracias por jugar {i} Doki Doki Literature Club {/i}."
        s "Te voy a extrañar, [player]."
        s "Ven a visitarnos alguna vez, ¿de acuerdo?"
        s "Siempre estaremos aquí para ti."
        s 1t "Nosotras..."
        scene black with dissolve_cg
        s "Te amamos."
        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
