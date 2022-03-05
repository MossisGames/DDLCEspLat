image yuri half = "images/yuri/1l.png"
image yuri_half2:
    "images/yuri/1r.png"
    block:
        xoffset -360
        linear 0.2 xoffset -280
        repeat

label ch22_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t6
    "Otro día pasa, y es hora de la reunión del club."
    "Me he vuelto un poco más cómodo aquí en los últimos días."
    "Al entrar en el salón del club, la escena habitual me saluda."
    if renpy.random.randint(0,2) == 0:
        show yuri half zorder 2 at i11
        show yuri_half2 zorder 1 at i11
    else:
        show yuri 1s zorder 2 at t11
    y "Bienvenido de vuelta, [player]..."
    hide yuri_half2
    mc "Ah, hola, Yuri..."
    "No estoy seguro si soy yo, o si es la expresión de Yuri..."
    "Pero el peso de la pelea de ayer todavía cuelga en el aire un poco."
    y 2v "U-Um..."
    "Yuri mira por encima del hombro, mirando alrededor del salón."
    "Natsuki está leyendo un manga en un escritorio."
    "Y sorprendentemente, Monika no ha llegado todavía."
    "De repente, Yuri me toma del brazo y me lleva a la esquina del salón."
    show bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "Sobre lo que pasó ayer..."
    y "Yo..."
    y 2v "Realmente necesito disculparme."
    y "Nada como eso ha sucedido antes..."
    y 2t "Y...Algo simplemente vino sobre mí, supongo..."
    y "No estaba actuando bien mentalmente."
    y 2w "¡Por favor no pienses que usualmente somos así!"
    y "No sólo yo, sino Natsuki tampoco..."
    show yuri 2t
    mc "Yuri..."
    mc "Estoy feliz de que hayas sido considerada y te hayas disculpado."
    mc "No tienes que preocuparte demasiado."
    mc "A pesar de que llevo aquí sólo un par de días, podría decir que algo salió ayer..."
    mc "Tal vez fuimos un poco más sensibles porque era la primera vez que compartíamos poemas."
    mc "Pero lo que sea..."
    mc "No me hizo pensar menos de ti."
    mc "Ya había decidido que no hay manera de que puedas ser una mala persona."
    mc "Y ahora que te estás disculpando, sé que realmente no lo has querido hacer."
    y 3t "A-Ah..."
    y "[player]..."
    y 3u "No digas ese tipo de cosas tan francamente..."
    y "Me hacen un poco feliz."
    y 1s "Estoy muy contenta de que seas una persona tan comprensiva..."
    y "Y estoy muy contenta de que te hayas unido a este club."
    y "Todo es un poco más brillante contigo, y--"
    y 1t "Ah--"
    y 4c "Perdón, ¿qué estoy diciendo ahora...?"
    y "Yo sólo--"
    show natsuki 2c zorder 3 at f33
    n "Oigan, ¿han visto a Monika?"
    show natsuki zorder 2 at t33
    show yuri 3n at h32
    y "¡Ah--!"
    mc "No, yo no..."
    mc "También me preguntaba dónde estaba."
    show natsuki zorder 3 at f33
    n 5g "Cielos..."
    n 5c "Yuri, supongo que tu tampoco"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 4a "..."
    "Yuri está claramente desconcertada por la calma con que Natsuki se dirige a ella."
    y "N-No, yo no..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1u "Por Dios, esto no es típico de ella en absoluto."
    n "Sé que es estúpido, pero no puedo evitar preocuparme un poco..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2t "..."
    show yuri zorder 2 at t32
    show natsuki 1h zorder 3 at f33
    n "¿Qué?"
    n "¿Por qué me miras así?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "U-Um..."
    y "Natsuki, sobre ayer..."
    y 3w "¡Y-Yo sólo quería disculparme!"
    y "¡Prometo que no quise decir ninguna de las cosas que dije!"
    y 3t "Y haré todo lo posible para mantenerme bajo control a partir de ahora..."
    y "Entonces--"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2c "Yuri, ¿De qué diablos estás hablando?"
    n "¿Hiciste algo ayer?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3f "...¿Eh?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    $ style.say_dialogue = style.normal
    n 2a "Caray..."
    $ style.say_dialogue = style.edited
    n "Lo que sea que tengas en mente, estoy segura de que no fue nada."
    n "Ni siquiera recuerdo que haya sucedido algo malo."
    n "Eres el tipo de persona que se preocupa demasiado por las pequeñas cosas, ¿verdad?"
    $ style.say_dialogue = style.normal
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2o "..."
    y "P-Pero..."
    show yuri zorder 2 at t32
    if renpy.random.randint(0, 3) == 0:
        $ style.say_dialogue = style.edited
        show natsuki mouth as nm zorder 3 at i33
        show n_moving_mouth zorder 3:
            xoffset 400
        n 2a ""
        hide nm
        hide n_moving_mouth
        $ style.say_dialogue = style.normal
    show natsuki zorder 3 at f33
    n 2j "Aceptaré tu disculpa de todos modos, si te ayuda a sentirte mejor al respecto."
    n "Además, es agradable de escuchar, ya que siempre tuve miedo de que en secreto me odiaras o algo así."
    n 2z "Jejeje."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3q "N-No, ¡en lo absoluto...!"
    y "No te odio..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2l "Jajaja."
    n "Bueno, eres un poco rara, pero yo tampoco te odio."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3t "..."
    "Natsuki se gira hacia mí."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2a "Tú aún estás a prueba."
    show natsuki zorder 2 at t33
    mc "¡Oye...!"
    "De repente, la puerta se abre."
    show monika 1g at l41
    m "¡Lo siento! ¡Lo siento mucho!"
    mc "Ah, ahí estás..."
    show monika zorder 3 at f41
    m "No quise llegar tarde..."
    m "¡Espero que no estuvieran preocupados o algo por el estilo!"
    show monika zorder 2 at t41
    mc "Nah..."
    mc "Bueno, Natsuki si."
    show natsuki zorder 3 at f33
    n 1p "¡¡C-Claro que no!!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1k "Jajaja."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 1s "...¿Qué te tomó tanto tiempo, de todos modos?"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1e "Ah..."
    m "Bueno, mi última clase fue en la sala de estudio."
    m "Para ser honesta, como que perdí la noción del tiempo..."
    m "Jajaja..."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2c "Eso no tiene sentido."
    n "Habrías escuchado la campana sonar, al menos."
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1m "No debí haberla oído, ya que estaba practicando piano..."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1e "¿Piano...?"
    y "No sabía que también tocas música, Monika."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 1l "Ah, no me den más crédito de lo que merezco."
    m 1m "Supongo que he estado practicando por un tiempo, pero todavía no lo hago realmente bien."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1a "Aún así..."
    y "Eso debe requerir mucha dedicación."
    y "Así que, estoy impresionada."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 5 "Aw, bueno, gracias, Yuri~"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2d "¡Deberías tocar algo para nosotros alguna vez!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m "Jajaja, eso es..."
    "Monika me mira."
    m 1a "Bueno, estoy escribiendo una canción, pero aún no está lista..."
    m "Tal vez ya que mejore un poco, lo haré."
    show monika zorder 2 at t41
    mc "Eso suena genial."
    mc "La espero con ansias."
    show monika zorder 3 at f41
    m 1b "¿Ah sí?"
    m "En ese caso..."
    m "No te decepcionaré, [player]."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show monika 5 zorder 2 at t11
    "Monika sonríe dulcemente."
    mc "Ah..."
    mc "¡No quise poner presión ni nada de eso!"
    m 1a "Jajaja, no te preocupes."
    m "Esperaba poder compartirla contigo."
    m "Supongo que es por eso que he estado practicando tanto recientemente."
    mc "Ya veo..."
    "No estoy seguro si Monika lo dijo de broma o de verdad se interesa en mi..."
    mc "En ese caso, la mejor de las suertes."
    m 1j "¡Gracias~!"
    m 1a "Entonces, no me perdí de nada, ¿verdad?"
    mc "No...En realidad no."
    show monika zorder 1 at thide
    hide monika
    "Elijo no mencionar nada de lo que los tres hablamos."
    "Además, Natsuki ya se ha escapado al armario."
    show yuri 2q zorder 2 at t11
    y "[player]..."
    y "Um..."
    y "Como tus cumplidos me pusieron de buen humor..."
    y "Me preguntaba si te gustaría pasar el tiempo juntos hoy."
    y 3o "Quiero decir - ¡En el club!"
    if poemwinner[0] == "natsuki":
        $ y_appeal = 1
        mc "Ah, supongo que sí."
        mc "No creo poder decirte que no, después de que me diste ese libro."
        mc "Bueno, supongo que necesito asegurarme de que Natsuki no me está esperando."
        mc "Después de que terminamos de leer ayer, ella--"
        if n_appeal >= 2:
            y 3r "¡Ella está bien!"
            $ style.say_dialogue = style.normal
            y 3h "Ella está leyendo allí. ¿Ves?"
            $ style.say_dialogue = style.edited
            y 3f "No pienses tanto en ella."
            y "Ella está acostumbrada a ser ignorada."
            y "Ven."
            $ style.say_dialogue = style.normal
            window hide(None)
            $ currentpos = get_pos()
            stop music
            scene black
            window auto
            $ pause (2.0)
            play music "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
            jump ch22_main2
        else:
            y 3r "¡E-Ella está bien!"
            y 3h "Ella está leyendo allí. ¿Ves?"
            y 3y6 "Así que está bien, ¿vale?"
            mc "Ah--"
            mc "En ese caso, no veo el problema..."
    else:
        $ y_appeal = 2
        mc "Sí, definitivamente."
        mc "Lo planeaba de todos modos."
    show yuri zorder 2 at h11
    y 3y5 "¡Está bien!"
    y "¿Podemos comenzar ahora?"
    y "Encontremos un lugar para senta--"
    y 3n "A-Ah--"
    y "Estoy siendo un poco enérgica, ¿verdad...?"
    y 4c "¡Lo siento!"
    y "Mi corazón...simplemente no deja de latir, por alguna razón..."
    mc "No te preocupes por eso."
    mc "En todo caso, es agradable ver que tienes tanta energía."
    y 3q "¡S-sí!"
    y "Pero..."
    y 3j "Necesito tratar de calmarme."
    y "No podré enfocarme en leer así..."
    mc "Tómate tu tiempo."
    "Yuri respira profundamente, luego saca una copia del libro de su bolso."
label ch22_main2:
    if n_poemappeal[1] == 1:
        $ n_poemappeal[1] = 0
    $ poemwinner[1] = "yuri"


    scene bg club_day2
    show yuri 3a at i11
    with wipeleft
    $ nextscene = "yuri_exclusive2_" + str(eval("y_appeal")) + "_ch22"
    call expression nextscene from _call_expression_1

    return

label ch22_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("Has desbloqueado un poema especial.\n¿Quieres leerlo?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[1]) from _call_expression_2
        scene black with Dissolve(1.0)
    else:
        pass
    if not faint_effect and renpy.random.randint(0,2) == 0:
        $ faint_effect = True
    else:
        $ faint_effect = None
    scene bg club_day2
    show monika 4b zorder 2 at t32
    if faint_effect:
        show layer master at dizzy(0.5, 1.0)
        show layer screens at dizzy(0.5, 1.0)
        show expression Solid("ff0000") as i1 onlayer front:
            additive 1.0
        show expression Solid("#440000") as i2 onlayer front:
            additive 0.4
        show veins onlayer front:
            additive 0.5
    with wipeleft_scene
    if faint_effect:
        play music t3g3
    else:
        play music t3
    if renpy.random.randint(0,2) == 0:
        $ config.mouse = {"default": [
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ]}



    m "¡Muy bien, todos!"
    m "Hemos terminado de leer los poemas de los demás, ¿verdad?"
    $ config.mouse = None
    m "Tenemos algo que repasar hoy, así que si todos pudieran venir a sentarse al frente de la sala..."
    show natsuki 3c zorder 3 at f31
    n "¿Es sobre el festival?"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "Bueno, algo así~"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "Ugh. ¿Realmente tenemos que hacer algo para el festival?"
    n "No es como si pudiéramos armar algo bueno en sólo unos pocos días."
    n "Terminaremos avergonzándonos en lugar de conseguir nuevos miembros."
    if faint_effect:
        $ currentpos = get_pos() + 2.0
        stop music fadeout 2.0
        show black onlayer front:
            alpha 0.0
            linear 2.0 alpha 1.0
    show natsuki zorder 2 at t31
    show yuri 2g zorder 3 at f33
    y "Esa es una preocupación mía también."
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    y "Realmente no me va bien con los preparativos de último minuto..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "¡No te preocupes tanto!"
    m "Vamos a mantenerlo simple, ¿de acuerdo?"
    m 2a "Mira..."
    m 2m "Sé que todo el mundo ha estado un poco más...animado...desde que [player] se unió y comenzamos con algunas actividades del club."
    m 2d "Pero este no es el momento para que nos volvamos complacientes."
    m "Todavía tenemos cuatro miembros..."
    m 2a "Y el festival es nuestra única oportunidad real de encontrar más, ¿saben?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5g "¿Qué hay de bueno en conseguir nuevos miembros, de todos modos?"
    n "Ya tenemos suficientes para ser considerados un club oficial."
    n "Más miembros sólo significará que todo se vuelve más ruidoso y más difícil de manejar."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "Natsuki..."
    m "No creo que lo estés viendo de la manera correcta."
    m "¿No quieres compartir tu pasión con tanta gente como puedas?"
    m 3e "¿Para inspirarlos a encontrar los mismos sentimientos que te trajeron aquí en primer lugar?"
    m "El Club de Literatura debe ser un lugar donde las personas puedan expresarse como no pueden hacerlo en ningún otro lado."
    m "Debería ser un lugar tan íntimo que nunca quieras irte."
    m 2e "Sé que tú también te sientes así."
    m 2b "¡Sé que todos lo hacemos!"
    m "Así que es por eso que debemos trabajar duro y preparar algo para el festival...¡Incluso si es algo pequeño!"
    m "¿No es así, [player]?"
    show monika 2a zorder 2 at t32
    mc "Ah..."
    show natsuki zorder 3 at f31
    n 42c "Oh, ¡vamos!"
    n "No puedes aprovecharte de [player] para que esté de acuerdo contigo sólo porque no sabe cómo decir no a nada."
    stop music fadeout 1
    n 1c "Mira, Monika."
    n "¿De verdad crees que alguno de nosotros aquí se unió al club con otras personas en mente?"
    n "Yuri nunca habló hasta que [player] se unió."
    n 2b "En cuanto a mí, me gusta más aquí que mi casa."
    n "Y [player] ni siquiera es apasionado por la literatura en primer lugar."
    n "Y esos son todos."
    n 4w "Lo siento, pero en realidad eres la única que está tan interesada en encontrar nuevos miembros."
    n "El resto de nosotros estamos bien así."
    n 4q "Sé que eres presidenta y todo eso, pero deberías considerar nuestras opiniones por una vez."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "..."
    "Monika está claramente sorprendida por las palabras de Natsuki."
    play music t9
    m 1m "Eso...no es cierto en absoluto."
    m 2m "Estoy segura de que Yuri y [player] quieren conseguir más miembros también..."
    m 2p "...¿Cierto?"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 4b "..."
    show yuri zorder 2 at t33
    mc "..."
    "No sé sobre Yuri, pero yo soy un poco indiferente."
    "Si mostrara tanto entusiasmo como Monika quería, entonces probablemente estaría mintiendo."
    "Aún así, si depende de mí rescatar esta situación..."
    mc "Um--"
    show monika zorder 3 at f32
    m 1i "No."
    m "Natsuki tiene razón, ¿verdad?"
    m 1g "Este club..."
    m "No es más que un lugar para que algunas personas pasen el rato."
    m 1r "¿Por qué creí que todos aquí lo vieron de la misma manera que yo?"
    show monika zorder 2 at t32
    mc "Pero eso no significa que estemos en contra de conseguir nuevos miembros o cualquier cosa..."
    show monika zorder 3 at f32
    m 1i "[player], ¿por qué te uniste a este club?"
    m "¿Qué esperabas obtener de él?"
    show monika zorder 2 at t32
    mc "Bueno--"
    "Eso no es realmente algo de lo que puedo ser honesto, ¿verdad?"
    show monika zorder 3 at f32
    m 1p "De hecho..."
    m "Si lo recuerdo, ni siquiera te dimos la opción de no unirte."
    show monika zorder 1 at thide
    hide monika
    "Monika se sienta y mira su escritorio."
    m "¿De qué sirve todo esto, de todos modos?"
    m "¿Qué pasa si comenzar este club fue un error?"
    mc "..."
    show yuri zorder 3 at f33
    y 2g "Ahora sí que lo has hecho, Natsuki..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1p "¿Qué, yo?"
    n 1s "Sólo dije lo que pienso..."
    n "¿Es un crimen ser honesta?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2l "No se trata de ser honesta."
    y "Se trata de elección de palabras."
    y 2h "Además, no tienes derecho a hablar por todos los demás en el club así..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1e "¡No lo entiendes para nada!"
    n 5s "Yo sólo..."
    n "Sólo quiero un lugar agradable para pasar el rato con algunos amigos."
    n 5u "¿Hay algún problema con que el club sea eso para mí?"
    n "No hay...No hay muchos otros lugares así para mí..."
    n 5x "¡Y ahora Monika quiere quitármelo!"
    show natsuki zorder 2 at t31
    mc "Ella no se está llevando nada--"
    show natsuki zorder 3 at f31
    n 1g "No, [player]."
    n "No es lo mismo."
    n 1q "No será lo mismo con la dirección que quiere tomar."
    n "Si quisiera eso, entonces podría haberme unido a cualquier otro club estúpido."
    n 12d "Pero este..."
    n "Quiero decir..."
    n 12e "Al menos por un ratito de tiempo..."
    n "Las cosas estuvieron bien."
    "Natsuki comienza a empacar sus cosas."
    n 12d "Me voy a casa."
    n "Siento que...no pertenezco aquí ahora."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3t "Natsuki..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Natsuki ignora a Yuri y sale del aula."
    show yuri zorder 2 at t11
    y 3v "..."
    y "Esto es malo..."
    y "No sé qué hacer..."
    mc "Bueno..."
    mc "¿Tienes alguna opinión sobre el festival?"
    y 4b "Y-Yo no lo sé..."
    $ style.say_dialogue = style.normal
    y "Soy un poco indiferente, supongo..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "¿A quién le importa esa odiosa mocosa?"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    y "Quiero decir, me gusta lo agradable y tranquilo que es el club en este momento..."
    y "Y yo sólo estoy...feliz contigo aquí..."
    y 2t "¡Pero aún así!"
    y "Soy la vicepresidenta..."
    y "No es correcto que ignore mis responsabilidades así..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "Nadie lloraría si se suicida."
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    stop music
    $ pause(0.5)
    play sound "sfx/stab.ogg"
    show blood_eye zorder 3:
        pos (710,380) zoom 2.5
    $ pause(0.75)
    stop sound
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    hide blood_eye
    y 2l "Debo hacer mi mejor esfuerzo para considerar la perspectiva de todos y tomar la decisión correcta para el club."
    y 1t "Pero, ¿y tú, [player]?"
    y "¿Qué quieres de este club?"
    "Yuri repite la misma pregunta que Monika."
    "Decido que dar una respuesta indirecta es mejor que nada."
    mc "...Creo que lo más importante es que todos se lleven bien..."
    mc "...Y que el club proporcione algo que no puedes conseguir en ningún otro lado."
    mc "No creo que se trate de cuántos miembros, sino de la calidad de cada miembro."
    mc "Eso es lo que terminará convirtiendo al Club de Literatura en un lugar especial."
    y 1u "Ya veo..."
    y "Realmente estoy de acuerdo contigo."
    show blood_eye2 zorder 3:
        pos (568, 165)
    y 1f "Cada miembro aporta sus propias cualidades de una manera especial."
    y "Con cada cambio en los miembros, la identidad del club como un todo también cambiará."
    y 1h "No creo que sea necesariamente algo malo."
    y "Al salir de tu zona de confort de vez en cuando..."
    y 1a "Entonces, si quisieras ayudar a Monika en el festival, yo también estoy de tu lado."
    hide blood_eye2
    mc "Bien."
    mc "Bueno, tal vez todos podamos hablar con Natsuki mañana..."
    "Yuri asiente."
    show monika 1g zorder 3 at f21
    show yuri zorder 2 at t22
    m "Oye, Yuri..."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1t "¿Eh?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1p "Um, sé que las cosas estuvieron un poco incómodas ayer..."
    m "Pero siento que mereces saber que todavía creo que eres una vicepresidenta maravillosa."
    m 1e "Y también, un amiga maravillosa."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3s "M-Monika..."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 2e "Quiero hacer todo lo posible para que este sea el mejor club de todos los tiempos."
    m "¿Está bien?"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y "...Yo también."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Sí..."
    m "Vámonos todos a casa por hoy."
    m "Hablaremos sobre el festival mañana."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1m "Está bien."
    y "Lo espero con ansias."
    y 1a "¿Nos vamos, [player]?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1d "Um--"
    m 1p "Por favor no tomes esto de la manera incorrecta, pero..."
    m "Voy a conversar un poco con [player] antes de irnos."
    m 1d "Sólo para ver lo que piensa de su tiempo aquí y todo eso..."
    m "Es importante para mí, como presidenta."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 2v "..."
    "Yuri se ve un poco preocupada, pero ella no protesta."
    y 2t "Está bien."
    y 2s "Confío en tu juicio, Monika."
    y "En ese caso, los veré a los dos mañana."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1j "Te veo mañana~"
    show yuri zorder 1 at thide
    hide yuri
    "Monika la despide mientras Yuri sale del aula."

    show monika 2a zorder 2 at t11
    m "Uff..."
    m 2e "Las cosas han estado un poco agitadas últimamente, ¿No?"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player], sólo quería asegurarme de que estés disfrutando de tu tiempo en este club."
    m "Realmente odiaría verte triste."
    m 2m "Me siento como si fuera la responsable de eso, como presidenta..."
    stop music
    m 4e "Y realmente me importas...¿sabes?"
    m "No me gusta ver que las otras chicas te hagan pasar un mal rato."
    m 4r "Con lo mala que es Natsuki y eso..."
    m 4m "Y Yuri es un poco...ya sabes."
    m 5a "Jajaja..."
    m "A veces parece que tú y yo somos las únicas personas reales aquí."
    m "¿Sabes lo que quiero decir?"
    m 1g "Pero es extraño, porque en todo el tiempo que has estado aquí, apenas hemos llegado a pasar tiempo juntos."
    m 1n "Ah...Quiero decir..."
    m "Supongo que técnicamente sólo han pasado un par de días..."
    m 1l "¡Lo siento, no quise decir algo raro!"
    m 1e "Hay algunas cosas de las que he estado esperando hablar..."
    m "Cosas que sé que sólo tú podrías entender."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "Así que es por eso que--\"{space=5000}{w=0.75}{nw}"
    m 1g "Espera, ¡todavía no!\"{space=5000}{w=0.5}{nw}"
    m "¡No!\"{space=5000}{w=0.5}{nw}"
    m "¡Alto!\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front





    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
