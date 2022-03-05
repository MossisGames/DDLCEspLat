label yuri_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    "Tengo mucha curiosidad por hablar con Yuri un poco más..."
    "Pero al mismo tiempo, me sentiría mal por distraerla de la lectura."
    "Echo un vistazo a la portada de su libro."
    "Parece el mismo libro que ella me prestó..."
    "Más que eso, parece estar en las primeras páginas."
    play music t6 fadeout 1.0
    show yuri 4a zorder 2 at t11
    y "Ah..."
    "Demonios--"
    "Creo que se dio cuenta de que la estaba mirando..."
    "Ella me lanza otra mirada y nuestros ojos se encuentran por una fracción de segundo."
    y 4b "..."
    "Pero eso sólo la hace esconder más su rostro en su libro."
    mc "Lo siento..."
    mc "Estaba distraido..."
    "Murmuro esto, sintiendo que la hice sentir incómoda."
    y oneeye "Oh..."
    y "Está bien..."
    y "Si estuviera enfocada, entonces probablemente no te habría notado en primer lugar."
    y "Pero sólo estoy volviendo a leer un poco de esto..."
    mc "Ese es el libro que me diste, ¿verdad?"
    y "Mhm."
    y "Quería volver a leer algo de eso."
    y 2q "¡Por ninguna razón en particular...!"
    mc "Sólo por curiosidad, ¿Por qué tienes dos copias del mismo libro?"
    y "Ah..."
    y "Bueno, cuando me detuve en la librería ayer--"
    y 3o "Ah, eso no es lo que quise decir..."
    y "Quiero decir--"
    y 1w "Yo...compré dos."
    mc "Ah, ya veo."
    "Hay algo bastante obvio aquí que Yuri no me dice, pero decido dejarlo ir."
    mc "¡Definitivamente comenzaré a leerlo pronto!"
    y 2u "Me alegra oír eso..."
    y "Una vez que empieces, es posible que tengas dificultades para dejarlo de lado."
    y 2c "Es una historia muy atractiva e identificable."
    mc "¿Ah sí...?"
label yuri_exclusive2_1_ch22:
    mc "¿De qué se trata?"
    y 1f "Bueno..."
    y "Mmm..."
    "Miro la portada del libro."
    "El libro se titula \"Retrato de Markov\"."
    "Hay un símbolo de un ojo ominoso en la portada."
    y 1a "Básicamente, se trata de este campo religioso que se convirtió en una prisión experimental humana..."
    y "Y las personas atrapadas allí tienen este rasgo que los convierte en máquinas de matar que ansían sangre."
    y 1m "Pero las instalaciones empeoran aún más, y comienzan a criar selectivamente a las personas cortándoles las extremidades y poniéndolas en--"
    y 1q "O-Oh, eso podría ser un spoiler..."
    y 3q "Pero de todos modos, ¡estoy realmente interesada en eso!"
    y 3n "...¡en el libro!"
    y 3q "N-No en la cosa sobre las extremidades..."
    mc "¡Eso es como--!"
    "Eso es algo oscuro, ¿no?"
    "Yuri hizo que pareciera que iba a ser una buena historia, por lo que ese giro oscuro vino de la nada."
    y 1s "Ah..."
    y "¿No eres fanático de ese tipo de cosas, [player]?"
    mc "No, no es eso..."
    mc "Quiero decir, definitivamente puedo disfrutar ese tipo de historias, así que no te preocupes."
    y 2u "Eso espero..."
    "Sí...olvidé por completo que Yuri está interesada en esas cosas."
    "Ella es muy tímida y solitaria por fuera, pero su mente parece ser completamente diferente."
    y "Es sólo que este tipo de historia..."
    y 1a "Es del tipo que te reta a mirar la vida desde una perspectiva nueva y extraña."
    $ style.say_dialogue = style.normal
    y "Cuando ocurren cosas horribles no sólo porque alguien quiere ser malvado..."
    $ style.say_dialogue = style.edited
    y "Sino porque el mundo está lleno de gente horrible, y todos somos inútiles de todos modos."
    y "Entones, de prontooooooooooooooooooooo ooooooooooooooooooo{nw}"
    $ style.say_dialogue = style.normal
    y 3v "Estoy...estoy divagando, ¿verdad...?"
    y "No de nuevo..."
    y 4b "Lo siento..."
    mc "¡Oye, no te disculpes...!"
    mc "No he perdido interés ni nada."
    y "Bueno..."
    y "Creo que está bien, entonces..."
    y 4a "Pero siento que debería hacerte saber que tengo este problema..."
    $ style.say_dialogue = style.normal
    y "Cuando dejo que cosas como los libros y la escritura llenen mis pensamientos..."
    $ gtext = glitchtext(24)
    $ style.say_dialogue = style.edited
    y "todo mi cuerpo se vuelve increíblemente[gtext]{nw}"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    y "Me olvido de prestarle atención a otras personas..."
    y 3t "¡Así que lo siento si termino diciendo algo extraño!"
    y "¡Y por favor detenme si empiezo a hablar demasiado!"
    mc "Eso es--"
    mc "Realmente no creo que tengas que preocuparte..."
    mc "Eso sólo significa que eres una apasionada de la lectura."
    mc "Lo menos que puedo hacer es escuchar."
    mc "Es un club de literatura, después de todo..."
    y 4a "Ah--"
    y "Eso es..."
    y "Bueno, eso es cierto..."
    mc "De hecho..."
    mc "Bien podría empezar a leerlo, ¿verdad?"
    play sound "sfx/glitch3.ogg"
    y dragon "¡S-Si!"
    y 3n "Q-Quiero decir, ¡no tienes que hacerlo, pero...!"
    mc "Jajaja, ¿qué estás diciendo?"
    y 3o "..."
    mc "Déjame sólo sacar el libro..."
    "Saco rápidamente el libro que había puesto en mi mochila."
    mc "Vale...está bien si me siento aquí, ¿verdad?"
    "Me tiro en el asiento al lado de Yuri."
    y 3n "¡Ah...!"
    y "Sí..."
    mc "¿Estás segura?"
    mc "Pareces un poco aprensiva..."
    y "Eso es..."
    y 4b "Lo siento..."
    y "¡No es que no quiera que lo hagas!"
    y "Es algo a lo que no estoy acostumbrada..."
    y "Es decir, leer en compañía de alguien."
    mc "Ya veo..."
    mc "Bueno, sólo dime si termino por distraerte o algo así."
    y "B-Bien..."
    show yuri zorder 1 at thide
    hide yuri
    "Abro el libro y comienzo el prólogo."
    "Pronto entiendo lo que Yuri quiere decir acerca de leer en compañía."
    "Es como si pudiera sentir su presencia sobre mi hombro mientras leo."
    "No es particularmente malo."
    "Tal vez un poco de distracción, pero la sensación es algo reconfortante."
    "Yuri está en la esquina de mi visión."
    "Me doy cuenta de que ella no está mirando su propio libro."
    "Echo un vistazo."
    "Parece que ella está leyendo de mi libro en su lugar--"
    show yuri 3n zorder 2 at t11
    y "¡P-Perdón!"
    $ style.say_dialogue = style.normal
    y "Sólo estaba--!{nw}"
    $ style.say_dialogue = style.edited
    y "Sólo estaba{fast} bañándome en la sensación del calor de tu cuerpo ooooooooooooocuerpo erpoooooooo{nw}"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()

    mc "Yuri, realmente te disculpas mucho, ¿verdad?"
    y "¿Lo...Lo hago?"
    y 4a "Realmente no quiero..."
    y "Lo siento..."
    y 4c "¡Quiero decir--!"
    mc "Jajaja."
    mc "Mira, esto debería funcionar, ¿verdad?"
    "Muevo mi escritorio hasta que esté pegado al de Yuri, luego sostengo mi libro más entre los dos."
    y 2v "Ah..."
    y "S-Supongo que sí..."
    "Yuri cierra tímidamente su copia."
    "Una vez que nos inclinamos un poco, nuestros hombros casi se tocan."
    "Parece que mi brazo izquierdo está en medio, así que en su lugar uso mi mano derecha para mantener el libro abierto."
    mc "Ah, creo que eso hace que sea un poco difícil pasar la página..."
    y "Yo lo hago..."
    $ persistent.clear[2] = True
    $ renpy.save_persistent()
    scene y_cg1_base with dissolve_cg
    "Yuri usa su brazo izquierdo para sostener el libro entre su pulgar e índice."
    mc "Ah..."
    "Hago lo mismo con mi brazo derecho."
    "De esa manera, paso una página, y Yuri la desliza bajo su pulgar después de que se voltea hacia su lado."
    "Pero al mantenerlo así..."
    "Estamos acurrucados aún más juntos que antes."
    "¡En realidad me está distrayendo...!"
    "Es como si pudiera sentir la calidez de la cara de Yuri, y está en la esquina de mi visión..."
    show y_cg1_exp1 at cgfade
    y "...¿Estás listo?"
    mc "¿Eh?"
    y "Para pasar la página..."
    mc "Ah...¡lo siento!"
    mc "Creo que me he distraído un poco..."
    "Miro hacia la cara de Yuri otra vez, y nuestros ojos se encuentran."
    "No sé cómo seré capaz de seguirle el ritmo..."
    y "Ah..."
    show y_cg1_exp2 at cgfade
    y "Está bien."
    y "No estás acostumbrado a leer, ¿verdad?"
    y "No me importa ser paciente si te toma un poco más de tiempo..."
    y "Probablemente sea lo menos que puedo hacer..."
    y "Ya que has sido muy paciente conmigo..."
    mc "S-Sí..."
    mc "Gracias."
    hide y_cg1_exp1
    hide y_cg1_exp2
    "Continuamos leyendo."
    "Yuri ya no me pregunta si estoy listo para pasar la página."
    "En cambio, sólo asumo que ella termina la página antes que yo, así que la giro por mi propia voluntad."
    "Continuamos el primer capítulo en silencio."
    "Aun así, pasar cada página casi parece un intercambio íntimo..."
    "Mi pulgar suelta suavemente la página, dejándola revolotear hacia su lado mientras la atrapa bajo su pulgar."
    mc "Oye, Yuri..."
    mc "Esto podría ser un pensamiento tonto, pero..."
    mc "El personaje principal me recuerda un poco a ti."
    show y_cg1_exp3 at cgfade
    y "¿¿E-Eh??"
    y "N-No, ¡no me identifico con este personaje para nada!"
    y "Definitivamente no!"
    mc "¿En serio...?"
    mc "Estaba pensando en la forma en que ella piensa demasiado en las cosas que dice, y todo eso..."
    show y_cg1_exp1 at cgfade
    y "A-Ah..."
    y "De eso es de lo que estabas hablando..."
    hide y_cg1_exp3
    hide y_cg1_exp1
    show y_cg1_exp2 at cgfade
    y "Lo siento..."
    y "Pensé que te referías...a otra cosa sobre ella."
    mc "¿A otra cosa...?"
    hide y_cg1_exp2
    show y_cg1_exp3 at cgfade
    y "¡N-No importa!"
    y "Ni siquiera hemos llegado tan lejos..."
    y "Así que no sé por qué me vino a la cabeza..."
    y "¡Jajaja!"
    mc "Yuri, ¿te sientes bien?"
    hide y_cg1_exp3
    show y_cg1_exp1 at cgfade
    y "¿Eh--?"
    "Yuri ha estado un poco nerviosa desde que comenzamos a leer..."
    mc "Puedes descansar si te sientes mal o algo así."
    mc "Tu respiración está un poco..."
    y "¿Mi respiración...?"
    hide y_cg1_exp1
    "Yuri pone sus manos sobre su pecho, como si sintiera los latidos de su corazón."
    y "N-Ni siquiera...me dí cuenta..."
    show y_cg1_exp3 at cgfade
    y "...De todos modos, ¡estoy bien!"
    y "¡Sólo necesito un poco de agua...!"
    mc "De acuerdo...no te presiones."
    scene bg club_day
    with dissolve_cg
    "Yuri se pone de pie y prácticamente sale corriendo del aula."
    mc "¿Qué demonios era eso de...?"
    show monika 1d zorder 2 at t11
    m "¿[player]?"
    m "¿Pasó algo?"
    mc "¿Eh?"
    mc "No tengo ni idea..."
    mc "Yuri estaba actuando un poco extraña, supongo..."
    m 1r "Entonces no sabes nada..."
    mc "Lo siento, no puedo decir que sí."
    mc "¿Estás preocupada por ella?"
    m 1a "Oh...no, realmente no."
    m "Me estaba asegurando de que no le hiciste nada."
    mc "N-No, ¡nada!"
    m 5 "Jajaja, no te preocupes...te creo, tonto."
    m "Yuri hace esto a veces, así que no es nada alarmante."
    mc "Está bien...si tú lo dices."
    m 2b "De todos modos, ¿por qué no empezamos a compartir nuestros poemas?"
    mc "¿Eh?"
    mc "¿No deberíamos esperar a Yuri?"
    m 2a "Bueno, ella podría tardar un rato, así que pensé que comenzaríamos sin ella."
    m "¿Está bien?"
    mc "Sí, sólo estaba preguntando..."
    "Me paro."
    "Hago una nota mental de dónde me quedé en el libro y luego lo vuelvo a guardar en mi mochila."
    $ y_ranaway = True
    return

label yuri_exclusive2_2:
    $ y_exclusivewatched = True
    play music t6 fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    mc "Oye, Yuri."
    show yuri 2f zorder 2 at t11
    y "¿Eh?"
    mc "Ah..."
    "De repente noto que Yuri está leyendo un libro diferente al que hemos estado leyendo juntos."
    mc "¡Lo siento! No quise interrumpir..."
    y 2m "Ah, no..."
    y "Solamente te estaba esperando..."
    show yuri 2a
    mc "Ah, si ese es el caso..."
    mc "¿Por qué no comenzamos?"
    y 2c "¡Sí, vamos!"
label yuri_exclusive2_2_ch22:
    y 3a "En realidad, tengo una solicitud..."
    y "...¿Te importa si preparo algo de té primero?"
    mc "No, en absoluto."
    y 1c "Muchas gracias."
    y 1a "Si hay algo que puede hacer que mi tiempo de lectura sea mejor aquí, es una buena taza de té."
    y "Por no mencionarte a ti, también."
    show yuri zorder 1 at thide
    hide yuri
    "Yuri se levanta y se dirige al armario."
    "La sigo y miro mientras saca un pequeño cántaro de agua del estante - del tipo que tiene un filtro adentro."
    show yuri 1f zorder 2 at t11
    y "¿Puedes sostener esto por un segundo?"
    mc "Claro..."
    "Yuri me da la jarra de agua y también busca una tetera eléctrica."
    y "Voy a conectar esto en el escritorio de la maestra, y luego iré a buscar agua."
    show yuri zorder 1 at thide
    hide yuri
    "Ella pasa junto a mí y coloca el hervidor en el escritorio de la maestra."
    "Simplemente miro sus movimientos."
    "Para mi sorpresa, la forma en que se mueve realmente contrasta sus gestos al hablar."
    "Especialmente por sus largas piernas, Yuri parece elegante y metódica."
    show yuri 1f zorder 2 at t11
    y "Está bien, ¿me das la jarra de agua?"
    y 1a "Gracias. Ya vuelvo."
    mc "Ah, podría ir contigo..."
    y 1q "¡E-Está bien!"
    y "Te quedas aquí..."
    y "No tomará mucho tiempo."
    show yuri zorder 1 at thide
    hide yuri
    "Con jarra en mano, Yuri sale corriendo del salón."
    show monika 2i zorder 2 at t11
    m "Ah..."
    m "¿Yuri te dejó de nuevo?"
    mc "No, esta vez no es así."
    mc "Ella está llenando la jarra de agua para hacer té."
    m 5 "¡Oh, está bien!"
    m "Perdón por malentenderlo~"

    scene bg club_day
    with wipeleft_scene

    "..."
    "Pasan diez minutos."
    "Yuri dijo que no tardaría mucho..."
    "¿Hay algo que la retiene?"
    "Estoy aburrido de esperar aquí, así que decido ir a buscarla."
    scene bg corridor
    with wipeleft_scene
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 10.893>bgm/6o.ogg"
    mc "Veamos..."
    "El lugar más lógico donde Yuri podría estar es la fuente de agua más cercana..."
    $ y_name = "Yuri"
    "Comienzo a caminar por el pasillo."
    $ y_name = "???"
    y "Haah.....haah...."
    y "....Haah.....haah...."
    "...¿Que es ese ruido?"
    "Viene de la vuelta de la esquina..."
    "Parece como una respiración."
    y "Khhhhh--"
    "Una inhalación fuerte, como si alguien estuviera jalando el aire a través de sus dientes."
    "¿Está sufriendo...?"
    "Llego a la esquina y miro alrededor."
    mc "¿Yuri...?"
    $ y_name = "Yuri"
    show yuri cuts zorder 2 at t11
    y "¡Kya--!"

    $ currentpos = 45.264 - (get_pos() / 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " to 39.817 loop 0>bgm/6r.ogg"
    $ quick_menu = False
    play music t6r
    show yuri zorder 1 at thide
    hide yuri
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    $ y_name = "???"
    mc "{cps=*3}¿Yuri...?{/cps}{nw}"
    "{cps=*3}Llego a la esquina y miro alrededor.{/cps}{nw}"
    "{cps=*3}¿Está sufriendo...?{/cps}{nw}"
    "{cps=*3}Una inhalación fuerte, como si alguien estuviera jalando el aire a través de sus dientes.{/cps}{nw}"
    y "{cps=*3}Khhhhh--{/cps}{nw}"
    "{cps=*3}Parece como una respiración.{/cps}{nw}"
    "{cps=*3}Viene de la vuelta de la esquina...{/cps}{nw}"
    "{cps=*3}...¿Que es ese ruido?{/cps}{nw}"
    y "{cps=*3}....Haah.....haah....{/cps}{nw}"
    y "{cps=*3}Haah.....haah....{/cps}{nw}"
    $ y_name = "Yuri"
    "{cps=*3}Comienzo a caminar por el pasillo.{/cps}{nw}"
    "{cps=*3}El lugar más lógico donde Yuri podría estar es la fuente de agua más cercana...{/cps}{nw}"
    mc "{cps=*3}Veamos...{/cps}{nw}"
    window hide(None)
    window auto
    scene bg club_day
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    "{cps=*3}Estoy aburrido de esperar aquí, así que decido ir a buscarla.{/cps}{nw}"
    "{cps=*3}¿Hay algo que la retiene?{/cps}{nw}"
    "{cps=*3}Yuri dijo que no tardaría mucho...{/cps}{nw}"
    "{cps=*3}Pasan diez minutos.{/cps}{nw}"
    "{cps=*3}...{/cps}{nw}"

    $ del _history_list[-37:]
    if poemwinner[0] == "yuri" and chapter == 3:
        jump yuri_exclusive2_2_ch23
    $ currentpos = 90.528 - (get_pos() * 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
    $ quick_menu = True
    play music t6r
    hide noise
    hide vignette
    show layer master
    show yuri 1a zorder 2 at t11
    y "He vuelto."
    y "Gracias por esperar pacientemente."
    y "[player], ¿te gusta el té oolong?"
    mc "Ah, sí."
    mc "Cualquier cosa está bien."
    y "Muy bien."
    "Yuri establece la temperatura en el hervidor a 200 grados."
    y 1f "Ahora es el momento de poner la tetera."
    mc "Realmente haces esto correctamente, ¿no?"
    y 1u "Por supuesto..."
    y "No debería hacer menos cuando preparo té para otros."
    mc "¿Incluso si no soy un experto en té o algo...?"
    y 2m "Huju."
    y 2a "En ese caso, sólo estarás aún más impresionado."
    mc "Ah...¡quizás lo esté!"
    show yuri zorder 1 at thide
    hide yuri
    "Yuri busca la tetera y comienza a contar las hojas de té."
    "Para mi sorpresa, ella incluso comienza a tararear un poco."
    show yuri 1c zorder 2 at t11
    mc "Debes estar de buen humor ahora..."
    y 1a "¿Te parece?"
    y "Estaba dejando que se muestre..."
    y "Y lo notaste"
    y 2u "Estaba pensando un poco..."
    y "Y decidí que trataría de expresarme un poco más."
    y "Resulta que no es muy difícil para mí..."
    y 1c "Cuando eres tú quien está cerca, de todos modos."
    show yuri 1a
    mc "Ah..."
    mc "¡Eso es genial, Yuri!"
    mc "Simplemente no te presiones mucho."
    y 3u "Siempre te preocupas por mí, [player]..."
    y "Es muy entrañable."
    mc "Eso es..."
    "Yuri no estaba bromeando..."
    "¡Ni siquiera sé si puedo seguir el ritmo de esto...!"
    "Veo a Yuri servir una taza de té para cada uno."
    y 1a "[player], tengo otra solicitud."
    y "¿Te importa si nos sentamos en el piso hoy?"
    mc "¿Eh? ¿Por qué?"
    y 1h "Es un poco más fácil para mi espalda..."
    y "Puedo leer con la espalda contra la pared en lugar de inclinarme en mi escritorio."
    mc "Ah, lo siento, no me di cuenta."
    y 1a "No te preocupes."
    y "Simplemente tengo dolor de espalda con bastante regularidad, así que hago todo lo posible para controlarlo."
    mc "¿Ah sí?"
    mc "Me pregunto por qué será..."
    y 1f "Probablemente por mis--"
    y 1n "Ah--"
    y 1o "M-Mis..."
    mc "Tus posturas, ¿verdad?"
    mc "Siempre encorvada así mientras lees..."
    y 2p "¡Sí!"
    y 2q "¡Tengo unas posturas de lectura terrible!"
    y "Entonces es por eso que deberíamos sentarnos en el piso."
    mc "Está bien."
    mc "Traeré el libro."
    show yuri zorder 1 at thide
    hide yuri
    "Saco el libro de mi mochila."
    mc "Ah, también tengo un poco de chocolate..."
    "Es una bolsa de pequeños dulces de chocolate."
    "La traje ya que va bien con el té."
    "Yuri y yo nos sentamos contra la pared, con las tazas de té a los lados."
    "Como si estuviésemos sincronizados, asumimos la misma posición de lectura de la última vez, cada uno con la mitad del libro."
    "Excepto que esta vez..."
    "Nuestros cuerpos están aún más cerca el uno del otro."
    show yuri 2h zorder 2 at t11
    y "No puedo ver bien..."
    mc "¡--!"
    show yuri 2e at d11
    "Yuri se desliza más cerca hasta que nuestros hombros se tocan."
    "¿Cómo se supone que me concentre en leer así...?"
    "Yuri siempre fue linda, pero..."
    "Cuando está menos aprensiva, es casi más de lo que puedo soportar."
    y 2f "Tu taza de té..."
    "Yuri me da mi taza de té."
    "Sosteniéndola con la mano que no sostiene el libro, termino en una posición que hace que sea aún más difícil concentrarse."
    "¡Porque ahora tengo que preocuparme de no tocar accidentalmente su pecho...!"
    "Mientras tanto, Yuri no ha notado nada."
    "Ella pone una expresión de lectura intensa, y sólo puedo suponer que el mundo a su alrededor se ha desvanecido."
    "Utilizo toda mi fuerza de voluntad para centrarme en la lectura."
    "..."
    "Después de unos minutos, finalmente logro relajarme un poco."
    "Pongo la taza de té entre mis piernas y me atoro con la envoltura de chocolate."
    mc "Ah, lo siento..."
    "Dejo de lado brevemente el libro para terminar de abrir el envoltorio."
    mc "Puedes agarrar todos lo que quieras."
    y 2s "Ah, eso es..."
    y "Está bien, no tomaré ningúno..."
    mc "¿Eh? ¿Estás segura?"
    y 2v "Bueno..."
    y "Si lo toco, podría manchar las páginas..."
    mc "Ah, tienes razón..."
    mc "Ni siquiera pensé en eso."
    mc "Mi error..."
    y 2a "No hay necesidad de disculparse."
    y "Sostendré el libro, ¿vale?"
    mc "¿Estás segura...?"
    y "Por supuesto."
    $ persistent.clear[3] = True
    $ renpy.save_persistent()
    scene y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    with dissolve_cg
    "Yuri abre el libro con ambas manos."
    "Ella lo sostiene para que no me cueste leerlo."
    "Pero como resultado, su brazo izquierdo prácticamente descansa sobre mi pierna."
    mc "Bueno, en ese caso..."
    "Yuri ya está totalmente concentrada en leer nuevamente."
    "Tomo un caramelo de chocolate y me lo meto en la boca."
    "Entonces, tomo otro chocolate..."
    "Y lo sostengo ante Yuri."
    "Ella ni siquiera deja de mirar el libro."
    "Ella simplemente separa los labios, como si esta situación fuera completamente natural."
    "¡Pero eso significa que no puedo parar aquí!"
    hide y_cg2_nochoc
    "Aprensivamente coloco el chocolate en su boca."
    "Sólo así, Yuri cierra sus labios sobre él."
    y "¿Eh...?"
    show y_cg2_exp2
    "La expresión de Yuri se rompe de repente."
    y "¿Acabo..."
    y "...Acabo de...?"
    "Yuri me mira como si necesitara confirmar lo que acaba de suceder."
    show y_cg2_exp3
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    hide y_cg2_exp2
    y "U-Um..."
    y "[player]..."
    mc "¡P-Perdón!"
    mc "Supongo que no debería haber hecho eso..."
    stop music
    y "A-Ah..."
    "Yuri comienza a respirar pesadamente."
    y "Yo..."
    y "No puedo..."
    y "[player]..."
    "De repente, Yuri me toma con fuerza del brazo y me pone de pie."
    "Mi taza de té se derriba."
    scene bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "[player]..."
    play sound closet_close
    show dark zorder 100
    with wipeleft
    y "Mi corazón..."
    y 2y6 "Mi corazón no parará de latir, [player]..."
    y "No me puedo calmar."
    y "¡Ya no me puedo concentrar en nada...!"
    y "¿Puedes sentirlo, [player]?"
    "Yuri de repente presiona mi mano contra su pecho."
    play music hb
    show layer master at heartbeat
    y 3t "¿Por qué me está pasando esto?"
    y "Siento que me estoy volviendo loca..."
    y 3y4 "No puedo detenerlo."
    y 3y6 "Incluso me hace no querer leer..."
    y "Sólo quiero..."
    y 3s "...Mirarte..."

    hide yuri
    show yuri eyes
    $ pause(3.0)
    y "...Haah..."
    $ pause(3.0)
    y "...Haah..."
    $ pause(3.0)
    y "...Haah..."
    $ pause(3.0)
    play sound closet_open
    stop music
    show layer master
    hide yuripupils
    show yuri 1n at face
    with None
    show yuri 3n at t32 with None
    hide dark
    show monika 3l zorder 3 at f31
    with wipeleft
    m "U-Um..."
    m "Es...momento de compartir poemas..."




    return

label yuri_exclusive2_2_ch23:
    $ config.skipping = False
    scene black
    with None
    $ audio.t6g = "<loop 10.893>bgm/6g.ogg"
    play music t6g
    $ pause(4.62)
    scene bg corridor
    show yuri eyes_base
    $ pause(1.0)
    show bg glitch:
        yoffset 480 ytile 2
        linear 0.25 yoffset 0
        repeat
    show yuri glitch at i11
    $ gtext = glitchtext(80)
    $ currentpos = get_pos()
    play music g1
    y "{cps=70}[gtext]{nw}"
    stop music
    scene bg corridor
    show yuri 2n at i11
    $ quick_menu = True
    y "Um..."
    y "Espera..."
    y 2o "Cómo fue que..."
    y 2y6 "...Lo siento, sólo tuve un déjà vu realmente extraño..."
    y "Esto no ha sucedido antes...¿verdad?"
    y 2t "Últimamente mi cabeza ha estado un poco confusa..."
    y 3t "¡Espero que realmente no se haya estado mostrando ni nada!"
    y "No me gustaría que pienses que soy rara justo después de que comenzamos a pasar el tiempo juntos..."
    y "Quiero decir..."
    show bg corridor:
        xoffset 0
        parallel:
            0.36
            xoffset 1
            repeat
        parallel:
            0.49
            xoffset 0
            repeat
    show black zorder 5:
        alpha 0.5
        parallel:
            0.36
            alpha 0.5
            repeat
        parallel:
            0.49
            alpha 0.475
            repeat

    play music t9
    y "Todos tienen algunas cosas inusuales."
    y 1v "Pero expresar esas cosas tan pronto después de conocer a alguien generalmente se considera inapropiado...O desagradable."
    y "Al menos, eso es lo que descubrí."
    y "Cuando era un poco más joven, creo que venía con mucha fuerza y ​​me ponía un poco intensa..."
    y "Hacía que la gente no quisiera estar cerca de mí."
    y 2w "Entonces...comencé a odiar esas cosas sobre mí."
    y "Mi obsesión con ciertos pasatiempos."
    y "Y la forma en que no puedo controlarme cuando estoy demasiado entusiasmada con algo."
    y "Entonces..."
    y 1v "Eventualmente dejé de tratar de hablar con la gente."
    y "Si a nadie podría gustarle por las cosas que más me importan..."
    y 1u "...Entonces es más fácil si me cierro."
    y 1h "Pero recientemente, algo ha estado mal."
    y "No sé lo que es."
    y 2y6 "Pero cada vez que venimos al club, mi corazón se vuelve loco."
    y "Me va a romper el pecho."
    y "Me abruma con energía y emociones que no puedo dejar salir."
    y "Me ha estado haciendo cosas raras."
    y 2t "¡No sé por qué está sucediendo!"
    stop music
    y 1t "[player]..."
    y "¿Soy sólo yo, o Monika ha estado actuando un poco ida últimamente?"
    y 1v "Ella siempre ha sido una dulzura desde que me uní al club..."
    y "Pero recientemente, he sentido algo filoso cada vez que ella está cerca."
    y 2y4 "No estoy loca, ¿verdad?"
    y 2y1 "¡Por favor dime que no!"
    y "¡No podía decir nada antes, porque ella siempre está escuchando!"
    y 2y3 "Pero finalmente, estamos sólos..."
    y "¿Podemos quedarnos aquí por un tiempo?"
    y 1m "Sí..."
    y "..."
    play music hb
    show layer master at heartbeat
    show yuri as yuri_eyes zorder 4:
        "yuri/eyesfull.png"
        i11
        alpha 0.0
        block:
            2.012 * 4 - 1.49
            alpha 1.0
            0.52
            alpha 0.0
            1.49
            repeat
    $ pause(2.0)
    $ ad = 40.0
    $ ac = 1.0
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "Sólo quiero quedarme aquí."
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y "Sólo nosotros dos"
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y "Podemos quedarnos aquí hasta que la reunión termine."
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "Y luego tendremos el salón para nosotros solos."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "Nadie para interferir con nuestro tiempo de lectura."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "Nadie para hacerme sentir como si me apuñalara en la garganta."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1q "Jajaja..."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "¡Eso fue una broma!"
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "Sólo una broma."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1i "Aunque, sí me gustan los cuchillos..."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "Suena extraño, pero no lo entenderías si nunca has visto lo bellos que pueden ser."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1f "Tengo una idea."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "¿Por qué no vienes a mi casa alguna vez?"
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "Puedo mostrarte mi colección."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Los obtuve de varios artesanos."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "Me aseguro de darles a todos una justa función."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "No quiero que se vuelvan solitarios ni nada..."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "Nadie merece estar solo."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "Nadie."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1c "Y es por eso que estoy tan feliz de que te hayas unido al Club de Literatura, [player]."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "Ahora ya no necesitamos estar solos."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Porque nos tenemos el uno al otro."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Cada día."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Eso es todo lo que necesitamos."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "¿Sabes que?"
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Vamos a dejar el Club de Literatura."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "No hay necesidad de que estemos cerca de la lengua viscosa de Monika.."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "Sin mencionar a la otra niña patética."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "Podemos caminar juntos a casa todos los días después de la escuela."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Y leer juntos."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "Comer juntos."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Dormir juntos."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "¿No suena perfecto?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "Es todo lo que podríamos desear."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "¿No es por eso que te uniste al club en primer lugar?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "Es casi como si fuera el destino."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "El destino de que nos encontremos."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "Y ahora tenemos el final feliz por el que he esperado pacientemente durante años."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "¿Harías eso conmigo, [player]?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    $ gtext = glitchtext(200)
    y "¿Harías{space=60}[gtext]{nw}"
    hide monika onlayer front
    window hide(None)
    $ poemsread = 0
    $ y_gave = False
    play music t5
    scene bg club_day
    window show(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
