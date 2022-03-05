label ch2_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    "Otro día pasa, y es hora de la reunión del club."
    "Me he sentido un poco más cómodo en los últimos días."
    "Al entrar en el salón del club, la escena habitual me da la bienvenida."
    show sayori 2x zorder 2 at t11
    s "Hola [player]~"
    mc "Hola, Sayori."
    mc "Parece que estás de buen humor hoy."
    s 1q "Jejeje~"
    s "Es sólo que aún no me acostumbro a que estés en el club."
    mc "Ya veo..."
    mc "...Eso es algo muy simple como para ponerte de buen humor."
    mc "Pero supongo que contigo las cosas siempre son simples."
    s 1d "Hablando de..."
    s "Estoy un poco hambrienta..."
    s "¿Vendrías conmigo a comprar un bocadillo?"
    mc "No, gracias."
    s 4h "¿¿Eh??"
    s "¡¡U-Usualmente no me dices eso!!"
    mc "Tengo mis razones."
    mc "¿Por qué no echamos un vistazo a tu monedero, Sayori?"
    s 4l "¿E-Eh?"
    show sayori at s11
    s "¿Por qué pides eso...tan repentino?"
    mc "No tengo una razón realmente."
    mc "Sólo quería verlo."
    s 1l "A-Ah..."
    show sayori zorder 2 at t11
    "Sayori nerviosamente saca su monedero."
    "Ella forcejea con el cerrojo y lo abre."
    "Luego, lo pone boca abajo y deja que su contenido caiga sobre el escritorio."
    "Sólo dos monedas pequeñas aparecen."
    s 5a "Ah-Jajaja..."
    mc "Lo sabía..."
    mc "Puedo ver a través de ti, Sayori."
    s 5c "¡No es justo!"
    s "¿Cómo lo sabías?"
    mc "Es sencillo."
    mc "Si desde el inicio hubieras tenido suficiente dinero, habrías comprado un bocadillo antes de llegar al salón del club."
    mc "Entonces, o no tienes hambre y quieres una excusa para dar un paseo..."
    mc "O bien, planeaste olvidarte convenientemente de que gastaste todo tu dinero, ¡para que yo te prestara un poco!"
    mc "Pero hay una cosa más..."
    mc "...¡Siempre tienes hambre!"
    mc "Y entonces, ¡eso sólo deja una opción!"
    s 4p "¡Uwaaa~!"
    s "¡Me rindo!"
    s "¡No me hagas sentir culpable!"
    mc "Si te sientes culpable, eso significa que mereces sentirte culpable..."
    show yuri 1c zorder 2 at t33
    y "Jajaja."
    "Yuri de repente se ríe."
    show sayori 4g
    mc "¿Eh?"
    "No noté que estaba escuchando."
    "Su rostro está en su libro, como siempre."
    show yuri 3n at h33
    y "¡A-Ah!"
    y "¡No estaba escuchando ni nada--!"
    y 3o "Era sólo...algo en mi libro..."
    show sayori zorder 3 at f32
    s 1h "Yuriiii..."
    s "Dile a [player] que me preste algo de dinero..."
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3h "¡Eso es--!"
    y "No me involucres así, Sayori..."
    y "Además..."
    y 1k "Sólo debes comprar lo que puedas pagar con responsabilidad..."
    y "Y, francamente, después de hacer un pequeño truco malicioso como ese, tu sufrimiento es una justa retribución."
    show sayori 1b
    mc "..."
    y 3n "¡Ah--!"
    y "¿Acabo de..."
    y 4c "¡¡Y-Yo no quise decir eso!!"
    y "Me absorbí demasiado en mi libro..."
    y "Uu..."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1r "¡Jajaja!"
    s 3x "Me gusta mucho cuando hablas sin pensar, Yuri..."
    s "No sucede a menudo, ¡pero es un lado divertido de ti!"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3v "Eso es..."
    y "No hay forma de que puedas pensar eso..."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1x "Aunque tienes razón..."
    s "Hice algo malo y ahora tengo que aceptar la revolución."
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3h "Retribución..."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1l "¡Eso!"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y "Aún así, viniendo de ti, Sayori..."
    y 1a "Supongo que hay un pequeño demonio dentro de nosotros, ¿no es así?"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1q "Jejeje..."
    show sayori zorder 2 at t32
    mc "No dejes que te engañe."
    mc "Sayori sabe exactamente lo que está haciendo."
    mc "Después de todo, les dijo que me iba a traer al club antes de que ella incluso me lo propusiera..."
    show sayori zorder 3 at f32
    s 1h "¡P-Pero...!"
    s "No hubieras venido si no fuese por los pastelitos..."
    s "¡Así que tuve que engañar a Natsuki para que los hiciera!"
    show sayori zorder 2 at t32
    mc "Vamos, dame más crédito que eso, Sayori."
    show sayori zorder 3 at f32
    s 1l "Jejeje..."
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 4p zorder 3 at hf32
    "{i}¡Pwap!{/i}"
    hide white
    s 4p "¡Kyaa--!"
    "De la nada, algo golpea a Sayori en la cara y cae sobre el escritorio."
    s 4j "Ow..."
    s "¿Qué fue--"
    s 4n "¿¿Eh??"
    s "¡U-Una galleta!"
    "Efectivamente, es una galleta gigante envuelta en plástico."
    "Sayori mira alrededor."
    s 4m "¿¿E-Es un milagro??"
    s "¡Es porqué acepté mi restitución!"
    show sayori zorder 2 at t32
    mc "Retribución..."
    show sayori 4n
    show yuri zorder 3 at f33
    y 1u "De hecho, eso es casi parecido..."
    show yuri zorder 2 at t33
    show natsuki 3z zorder 3 at f31
    n "¡Jajaja!"
    n "Yo {i}iba{/i} a dártela."
    n 3d "Pero luego te escuché chismosear sobre los pastelitos."
    n "Sin embargo, valió la pena ver tu reacción. ¡Jajaja!"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 4m "¡N-Natsuki!"
    s "¡Es tan lindo de tu parte!"
    s 4s "Estoy tan feliz..."
    "Sayori abraza la galleta."
    show sayori zorder 2 at t32
    mc "Caray, sólo cómetela..."
    "Sayori rápidamente rompe la envoltura y toma una gran mordida."
    show sayori zorder 3 at f32
    s 4q "Twaaaan bwueeeeno..."
    show sayori zorder 3 at hf32
    s 4o "¡Mmf--!"
    "Sayori repentinamente se tapa la boca."
    s 4p "Me mordí la lengua..."
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3a "Jejeje."
    n "Estás haciendo mucho escándalo por una galleta."
    "Natsuki toma un bocado de su propia galleta."
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1c "¡Ah, la tuya también se ve muy bien, Natsuki!"
    s "¿Puedo probar?"
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "Caraaay..."
    n "¡A caballo regalado no se le ve el colmillo!"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1h "Pero la tuya es de chocolate..."
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4c "Sí, ¿por qué crees que te di esa?"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1g "Bueno..."
    s 1q "Aún así, estoy muy feliz de que hayas compartido esta conmigo."
    s "Jejeje~"
    show sayori behind natsuki zorder 2 at t21
    "Sayori se levanta de su asiento y va detrás de Natsuki, luego la abraza."
    n 12c "Ah-- Caray..."
    n "Lo sé, lo sé."
    "Todavía con la galleta en mano, Natsuki intenta empujar a Sayori."
    show sayori 1n at h21
    s "...{i}Om.{/i}"
    "Sayori de repente se inclina y le da un mordisco a la galleta de Natsuki."
    n 1p "{i}¡¡O-Oye!!{/i}"
    n "¡¿En serio hiciste eso?!"
    s 1q "¡Jujuju!"
    show sayori at lhide
    hide sayori
    "Con la boca llena, Sayori trota lejos hacia la seguridad."
    show yuri 1c
    "Yuri y yo nos reímos."
    show yuri 1a
    show natsuki zorder 3 at f31
    n 1w "¡Caray! ¡Eres tan infantil a veces!"
    n 1h "¡Monika! Dile a Sayori--"
    n 1c "--¿Eh?"
    "Natsuki mira alrededor."
    "Monika no está en el salón."
    n 4q "Ugh..."
    n "¿Dónde está Monika?"
    show natsuki zorder 2 at t31
    show yuri 2f zorder 3 at f33
    y "Buena pregunta..."
    y "¿Alguno sabe por qué se ha retrasado su llegada?"
    show sayori 1b zorder 3 at f32
    show yuri zorder 2 at t33
    s "Yo no..."
    show sayori zorder 2 at t32
    mc "Ajá, yo tampoco."
    show yuri zorder 3 at f33
    y 2l "Hm..."
    y "Eso es inusual."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1g "Espero que esté bien..."
    show sayori zorder 2 at t32
    show natsuki 3k zorder 3 at f31
    n "Claro que está bien."
    n "Probablemente sólo tenía algo que hacer."
    n 3t "Ella es muy popular, después de todo..."
    show natsuki zorder 2 at t31
    show sayori 4m zorder 3 at f32
    s "¿Eh?"
    s "No crees que ella..."
    s "¡Ella tiene un...!"
    show sayori zorder 2 at t32
    show yuri 1a zorder 3 at f33
    y "Jajaja. No estaría sorprendida."
    y "Ella es probablemente más deseable que todos nosotros combinados."
    show yuri zorder 2 at t33
    show sayori 1r zorder 3 at f32
    s "Jejeje, es cierto..."
    show sayori zorder 2 at t32
    show natsuki 1p zorder 3 at f31
    n "¡¿Disculpa?!"
    hide natsuki
    hide sayori
    hide yuri
    with wipeleft
    "De repente, la puerta se abre."
    show monika 1g at l41
    m "¡Lo siento! ¡Lo siento mucho!"
    mc "Ah, allí estás..."
    m "No era mi intención llegar tarde..."
    m "¡Espero que no estuvieran preocupados ni nada por el estilo!"
    show sayori 4n zorder 3 at f42
    s "¿¿Eh??"
    s "¡Monika eligió al club en vez de su novio!"
    s "¡Eres muy obstinada!"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m 1l "¿N-Novio...?"
    m "¿De qué estás hablando?"
    "Monika me mira burlonamente."
    show monika zorder 2 at t41
    mc "Ah, no importa..."
    mc "¿Qué fue lo que te detuvo?"
    show monika zorder 3 at f41
    m 1e "Ah..."
    m "Bueno, mi última clase la pasé en la sala de estudio."
    m "Para ser honesta, como que perdí la noción del tiempo..."
    m "Jajaja..."
    show monika zorder 2 at t41
    show natsuki 2c zorder 3 at f43
    n "Eso no tiene sentido."
    n "Al menos habrías escuchado la campana sonar."
    show natsuki zorder 2 at t43
    show monika zorder 3 at f41
    m 1m "No la debí haber oído, ya que estaba practicando piano..."
    show monika zorder 2 at t41
    show yuri 1e zorder 3 at f44
    y "¿Piano...?"
    y "No sabía que también tocas música, Monika."
    show yuri zorder 2 at t44
    show monika zorder 3 at f41
    m 1l "¡Ah, no lo hago, realmente...!"
    m "Hace poco que empecé."
    m 1m "Siempre quise aprender a tocar piano."
    show monika zorder 2 at t41
    show sayori 4x zorder 3 at f42
    s "¡Eso es tan genial!"
    s "¡Deberías tocar algo para nosotros, Monika!"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m "Eso..."
    "Monika me mira."
    m 1a "Tal vez, cuando mejore un poco, lo haga."
    show monika zorder 2 at t41
    show sayori zorder 3 at f42
    s 4q "¡Yay~!"
    show sayori zorder 2 at t42
    mc "Eso suena genial."
    mc "También me gustaría verlo."
    show monika zorder 3 at f41
    m 1b "¿Ah si?"
    m "En ese caso..."
    m "No te decepcionaré, [player]."
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    show monika 5 zorder 2 at t11
    hide sayori
    hide natsuki
    hide yuri
    "Monika sonríe dulcemente."
    mc "Ah..."
    mc "¡No quise causarte ninguna presión ni nada de eso!"
    m 1a "Jajaja, no te preocupes."
    m "He estado practicando mucho últimamente."
    m "Y realmente me encantaría compartirlo una vez que esté lista."
    mc "Ya veo..."
    mc "En ese caso, la mejor de las suertes."
    m 1j "¡Gracias~!"
    m 1a "Entonces, no me perdí nada, ¿verdad?"
    mc "No...no realmente."
    show monika zorder 1 at thide
    hide monika
    "Elijo dejar de lado la travesura de Sayori."
    "Estoy seguro de que Natsuki terminará quejándose con ella, de todos modos."
    "Parece que todas ya se han relajado."
    "Sayori de alguna manera ya se terminó su galleta entera."
    "Yuri ha vuelto a su libro, y Natsuki desapareció en el armario."



    $ nextscene = poemwinner[1] + "_exclusive_" + str(eval(poemwinner[1][0] + "_appeal"))
    call expression nextscene from _call_expression_21



    return


label ch2_end:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "¡Muy bien, todos!"
    m "Hemos terminado de leer los poemas de los demás, ¿verdad?"
    m "Tengo algo extra planificado para hoy, así que si todos pudieran venir a sentarse al frente..."
    show natsuki 3c zorder 3 at f31
    n "¿Es sobre el festival?"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "Bueno, algo así~"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "Ugh. ¿Realmente tenemos que hacer algo para el festival?"
    n "No es como si pudiéramos hacer algo bueno en sólo unos pocos días."
    n "Terminaremos humillados en lugar de conseguir nuevos miembros."
    show yuri 2g zorder 3 at f33
    show natsuki zorder 2 at t31
    y "También tengo esa preocupación."
    y "Realmente no me va bien con los preparativos de último minuto..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "¡No se preocupen tanto!"
    m "Vamos a mantenerlo simple, ¿de acuerdo?"
    m 1a "No necesitaremos mucho más que algunas decoraciones."
    m "Sayori ha estado trabajando en carteles, y he diseñado algunos folletos que podemos distribuir durante el evento."
    show monika zorder 2 at t32
    show natsuki 3c zorder 3 at f31
    n "Está bien, eso es genial y todo..."
    n "Pero eso no nos dice lo que vamos a hacer realmente para el evento."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1d "¡Ah, lo siento! Creí que ya lo habías escuchado."
    m 1b "¡Vamos a recitar!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3h "¿Recitar?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3n "R..."
    y 3o "Um, Monika..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1k "¡Sí! Vamos a recitar poesía."
    m 1b "Cada uno elegirá un poema para recitar durante el evento."
    m "Pero lo genial es que también vamos a dejar que alguien más suba y recite poemas."
    m 1a "Sayori lo está poniendo en todos los carteles por si alguien quiere prepararse antes de tiempo."
    show yuri zorder 2 at t44
    show monika zorder 2 at t43
    show natsuki zorder 2 at t42
    show sayori 4q at l41
    s "Jejeje~"
    "Sayori, que ha estado pintando un cartel, lo levanta para que lo veamos."
    show natsuki 4w zorder 3 at f42
    n "¿Estás bromeando, Monika?"
    n "No...no has puesto esos carteles todavía, ¿o sí?"
    show natsuki zorder 2 at t42
    show monika zorder 3 at f43
    m 1d "¿Eh? Bueno, ya lo hice..."
    m "¿De verdad crees que es una idea tan mala...?"
    show monika zorder 2 at t43
    show natsuki 1s zorder 3 at f42
    n "Bueno, no."
    n "No es una mala idea."
    n 1w "¡Pero no me inscribí para esto, sabes!"
    n 1x "¡{i}No{/i} hay manera de que vaya a actuar frente a un grupo de personas así!"
    show natsuki zorder 2 at t42
    show yuri zorder 3 at f44
    y 3r "¡Yo...estoy de acuerdo con Natsuki!"
    y 3w "Nunca podría...en mi vida...hacer algo así..."
    "Imaginando, Yuri sacude la cabeza con miedo."
    show yuri zorder 2 at t44
    show sayori 1g zorder 3 at f41
    s "Chicas..."
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m 1g "No, Sayori..."
    m "Entiendo por qué lo dicen."
    m "Recuerda que Natsuki y Yuri nunca compartieron sus poemas con nadie hasta hace apenas un par de días..."
    m "Es mucho pedirles que reciten sus poemas en voz alta en una sala llena de gente."
    m 1r "Creo que pasé por alto eso."
    m "Entonces, lo siento."
    show monika zorder 2 at t43
    show natsuki 5g zorder 3 at f42
    n "..."
    show natsuki zorder 2 at t42
    show monika zorder 3 at f43
    m 1i "...¡Pero!"
    m "¡Aún así creo que debemos dar lo mejor de nosotros!"
    m 1d "Somos los únicos responsables del destino de este club."
    m "Si comenzamos el evento y cada uno realiza un buen desempeño..."
    m 3a "¡Entonces inspirará a otros a hacer lo mismo!"
    m "¡Cuantas más personas reciten, mejor será la demostración de lo que trata la literatura!"
    show monika zorder 2 at t43
    show sayori 1r zorder 3 at f41
    s "¡Sí!"
    s 1x "Se trata de expresar tus sentimientos..."
    s "Tener intimidad contigo mismo..."
    s "Encontrar nuevos horizontes..."
    s "¡Y divertirse!"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m 4b "¡Así es!"
    m "Y esas son las razones por las que todos estamos en este club hoy."
    m 4e "¿No quieren compartir eso con los demás?"
    m "¿Para inspirarlos a encontrar los mismos sentimientos que las trajeron aquí en primer lugar?"
    m 1e "Sé que lo hacen."
    m "Sé que todos lo hacemos."
    m 1b "Y si todo lo que se necesita es pararse al frente durante dos minutos y recitar un poema..."
    m "...¡Entonces sé que pueden hacerlo!"
    show monika 1a zorder 2 at t43
    show natsuki 5s zorder 3 at f42
    n "..."
    show natsuki zorder 2 at t42
    show yuri 4b zorder 3 at f44
    y "..."
    show yuri zorder 2 at t44
    show sayori 1g
    "Natsuki y Yuri permanecen en silencio."
    "Sayori parece preocupada."
    "Supongo que eso no me deja otra opción..."
    mc "Estoy de acuerdo..."
    mc "No creo que sea demasiado pedir."
    mc "Creo que Sayori y Monika realmente han estado intentando conseguir nuevos miembros."
    mc "Lo menos que podemos hacer es ayudarlas un poco."
    show natsuki zorder 3 at f42
    n 5h "Bueno...tal vez, pero..."
    n "..."
    "Parece que a Natsuki no le quedan argumentos."
    n "Uu..."
    n 1q "...¡Vale, está bien!"
    n "Supongo que tendré que soportarlo."
    show natsuki zorder 2 at t42
    show sayori zorder 3 at f41
    s 4r "¡Muy bien~!"
    show sayori 4a zorder 2 at t41
    show monika zorder 3 at f43
    m 1e "Uff..."
    m "Gracias, Natsuki."
    m "¿Y tú, Yuri...?"
    show monika zorder 2 at t43
    show yuri zorder 3 at f44
    y "..."
    "Yuri mira con abatimiento las caras expectantes de todos."
    y "*Suspiro*..."
    y "S-Supongo que realmente no tengo otra opción..."
    show yuri zorder 2 at t44
    show sayori zorder 3 at f41
    s 4r "¡Jajaja! ¡Ya aceptamos todos!"
    s "Eres la mejor, Yuri~"
    show sayori 4a zorder 2 at t41
    show yuri zorder 3 at f44
    y "Seriamente este club va a ser mi muerte..."
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 1l "Oh Dios..."
    m 1n "Estarás bien, Yuri."
    m "Pero de todos modos..."
    m 1b "¡Vamos a pasar al evento principal!"
    m "Quiero que cada uno de ustedes elija un poema suyo."
    m "Vamos a practicar recitar frente a nosotros."
    show monika 1a zorder 2 at t43
    show natsuki zorder 3 at f42
    n 1p "¡¡D-D-De ninguna manera!!"
    show natsuki zorder 2 at t42
    show yuri 3n zorder 3 at f44
    y "¡Monika...!"
    y "¡Esto es muy repentino...!"
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 2a "Bueno, si no pueden recitar su poema frente al club, ¿cómo esperan hacerlo frente a extraños?"
    show monika zorder 2 at t43
    show yuri 4c zorder 3 at f44
    show natsuki 1o
    y "Oh no..."
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 2a "No te preocupes."
    m "Lo haré primero para ayudar a que todos se sientan un poco más cómodos."
    show monika zorder 2 at t43
    show sayori 1r zorder 3 at f41
    s "¿¿Puedo ir después??"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m "Jajaja. Claro."
    m 2d "Ahora, veamos..."
    "Monika hojea su cuaderno buscando el poema específico que tiene en mente."
    "Luego se para detrás del podio."
    show monika zorder 2 at t11
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide natsuki
    hide yuri
    m 1a "El titulo de este poema es {i}La Forma En Que Vuelan{/i}."
    m 1r "Ahem..."
    show monika 1a
    "Monika comienza a recitar su poema."
    "Su voz clara y segura llena el salón."
    "Más que eso, su inflexión es prístina."
    "Ella sabe exactamente cómo aplicar la emoción detrás de cada línea que recita, haciendo que las palabras cobren vida."
    "¿Esto es algo que ya hizo antes o simplemente es natural?"
    "Miro a mi alrededor."
    "Todos tienen sus ojos puestos en Monika."
    "Sayori se ve sorprendida."
    "Yuri tiene una expresión intensa en su rostro que no entiendo."
    show monika 1j
    "Finalmente, Monika termina de recitar."
    "Los cuatro aplaudimos."
    "Monika toma aliento y sonríe."
    show monika 1a
    show sayori 4m zorder 3 at f33
    s "Eso...¡eso fue tan bueno, Monika!"
    show sayori zorder 2 at t33
    show monika zorder 3 at f32
    m 1j "Jajaja, muchas gracias."
    m 1a "Sólo esperaba dar un buen ejemplo."
    m "¿Estás lista para seguir, Sayori?"
    show monika zorder 2 at t32
    show yuri 2r at l31
    y "¡¡Yo...yo iré después!!"
    show sayori at h33
    s 1n "¡Uwah! ¡Yuri se encendió de repente!"
    "Yuri agarra una hoja de papel entre sus manos y se levanta."
    "Manteniendo la cabeza agachada, camina rápidamente hacia el podio."
    show monika zorder 1 at thide
    show sayori zorder 1 at thide
    show yuri zorder 2 at t11
    hide monika
    hide sayori
    y 2v "¡Este poema se llama--!"
    "Yuri mira ansiosamente a cada uno de nosotros."
    s "Puedes hacerlo, Yuri..."
    y "Se...se llama...{i}Remanente de un Ojo Carmesí{/i}."
    "La voz de Yuri tiembla cuando comienza a leer el poema."
    "Hace apenas un momento que prácticamente se negaba a hacer esto."
    "¿Por qué está de repente poniendo tanto esfuerzo?"
    show yuri 2l
    "Cuando Yuri pasa las primeras líneas, su voz cambia."
    "Es casi como lo que pasa cuando Yuri se absorbe en sus libros."
    "Sus palabras temblorosas se transforman en las afiladas sílabas de una mujer feroz y segura de sí misma."
    "El poema está lleno de giros y vueltas en su estructura que ella enuncia con un ritmo perfecto."
    "¡Este debe ser un raro vistazo al fuego giratorio que Yuri esconde dentro de su cabeza...!"
    show yuri 2t
    "De repente termina."
    "Todos están aturdidos."
    "Yuri vuelve a la realidad y mira a su alrededor, como si ella misma se desconcertara."
    y 3o "Yo..."
    "...Depende de mí salvar esta situación."
    "Soy el primero en comenzar a aplaudir."
    "Todas se unen a mí después, y le damos a Yuri el reconocimiento que merece."
    "No es que no quisiéramos aplaudirle."
    "Pero nos atrapó tan desprevenidos que debimos haberlo olvidado."
    "Mientras aplaudimos, Yuri sostiene el poema contra su pecho y se apresura a regresar a su asiento."
    show yuri at lhide
    hide yuri
    show monika 1a zorder 2 at t11
    m "Yuri, eso fue realmente bueno."
    m "Gracias por compartirlo."
    y "..."
    "Parece que Yuri está fuera de combate..."
    show sayori 1q zorder 2 at t31
    s "Vaaaale~"
    s "¡Supongo que soy la siguiente!"
    "Sayori se levanta de la silla y camina alegremente hacia el podio."
    show sayori zorder 2 at t11
    show monika zorder 1 at thide
    hide monika
    s 1x "Este se llama...{i}Mi prado{/i}."
    s "Ah..."
    s 1s "...¡Jajaja!"
    s 4s "Lo siento, me reí tontamente..."
    s 4q "Jejeje..."
    mc "Sayori..."
    s 1l "¡Es mucho más difícil de lo que pensaba!"
    s "¿Cómo lo hicieron tan fácilmente?"
    show monika 3a zorder 2 at t31
    show sayori 1b
    m "Ah..."
    m "Trata de no pensar en que se lo estás recitando a otras personas."
    m "Imagina que te lo estás recitando, como frente a un espejo o en tu propia cabeza."
    m "Es tu poema, así saldrá de la mejor manera."
    show sayori 1i
    s "Ya veo, ya veo..."
    s "Está bien, entonces..."
    show monika zorder 1 at thide
    hide monika
    show sayori 1c
    "Sayori comienza."
    "De alguna manera, parece que su voz suave fue hecha como una pareja perfecta a su poema."
    "El poema no es tan alegre como Sayori."
    "Es sereno y agridulce."
    "Si tuviera que leer esto en papel, probablemente no lo analizaría demasiado..."
    "Pero escuchar la voz de Sayori casi le da un significado completamente nuevo."
    "Quizás esto es a lo que Sayori se refería cuando dijo que le gustan mis poemas."
    "Es como si llegara a lo más profundo de alguien que creía conocer desde el principio."
    "Sayori termina y aplaudimos."
    s 3q "¡Lo hice~!"
    mc "Buen trabajo, Sayori."
    s "Jejeje, incluso a [player] le gustó."
    s "Supongo que es una buena señal~"
    mc "¿Eso qué significa...?"
    show monika 2b zorder 3 at f31
    m "Salió muy bien, Sayori."
    m "La atmósfera del poema te queda muy bien."
    m "Pero podría ser que otros poemas no funcionen tan bien con ese tipo de entrega..."
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1g "¿Eh? Realmente no entiendo..."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "En otras palabras, he visto poemas tuyos donde ese tipo de entrega suave no funcionaría tan bien."
    m "Quizás necesiten un poco más de fuerza en ellos, dependiendo de lo que estés leyendo..."
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1x "¡Oh, ya sé lo que quieres decir!"
    s "Eso...bueno, he estado practicando ese tipo de cosas..."
    s 5 "Me da vergüenza hacerlo frente a todos..."
    s "Ejeje..."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 4a "Entonces, la próxima vez, te haré elegir un poema que te desafíe un poco más."
    m "No tenemos mucho tiempo antes del festival, ¿Sabes?"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1q "Vaaaaale."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "Ahora, ¿quién sigue...?"
    m "¿Natsuki?"
    show natsuki 5s zorder 3 at f33
    show monika zorder 2 at t31
    n "Hmph."
    n "No me hagan ir antes de [player]."
    n "No es como si pudiera compararme con ustedes..."
    n "Podríamos dejar que [player] baje un poco la vara antes de que sea mi turno."
    show natsuki zorder 2 at t33
    show sayori zorder 3 at f32
    s 1g "Natsuki..."
    show sayori zorder 2 at t32
    mc "Está bien, está bien."
    mc "Me gustaría terminar con esto."
    mc "Pero no es como si tuviera mucha elección de qué leer..."
    mc "Tendré que hacerlo con lo que escribí hoy."
    "Me levanto y paso frente al podio."
    show natsuki 2c zorder 2 at t44
    show sayori 1a zorder 2 at t43
    show monika 1a zorder 2 at t42
    show yuri 1e zorder 2 at t41
    "Todas tienen sus ojos puestos en mí y me hacen sentir terriblemente incomodo."
    "Recito mi poema."
    "Dado que no estoy exactamente seguro de mi propia escritura, es difícil ponerle energía."
    "A pesar de eso, una vez que termino, recibo aplausos."
    mc "Lo siento, no soy tan bueno como ustedes..."
    show monika zorder 3 at f42
    m 1a "No te preocupes tanto por eso."
    m "Creo que se trata menos de tus habilidades y más de la falta de confianza en tu escritura."
    m "Eso es algo que mejorará con el tiempo."
    show monika zorder 2 at t42
    mc "Sí...puede ser que sí."
    show monika zorder 3 at f42
    m 1j "¡Entonces, todo bien!"
    m 1a "Sólo quedas tú, Natsuki."
    show monika zorder 2 at t42
    show natsuki zorder 3 at f44
    n 2g "Sí, sí."
    n "Ya voy."
    "Natsuki sale a regañadientes de su asiento y se dirige al podio."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 2 at t11
    hide sayori
    hide monika
    hide yuri
    n 2c "El poema se llama..."
    n 2q "Se llama..."
    n 1x "¡¿P-Por qué todos me miran?!"
    m "Porque estás presentando..."
    n 2x "Hmph..."
    n 2h "De todos modos...El poema se llama {i}Salto{/i}."
    "Natsuki respira."
    show natsuki 2c
    "Una vez que comienza a recitar el poema, su actitud agria desaparece un poco."
    "Mientras ella todavía está un poco desinteresada, su poema tiene un ritmo y una rima."
    "Es el estilo de marca registrada de Natsuki, y funciona sorprendentemente bien cuando se lee en voz alta."
    "Las palabras se sienten como si rebotaran hacia arriba y hacia abajo, como dando vida al poema."
    show natsuki 2s
    "Natsuki termina y todos aplauden."
    "Ella resopla a su asiento."
    show monika 2a zorder 3 at f31
    m "Eso no estuvo tan mal, ¿verdad?"
    show monika zorder 2 at t31
    show natsuki 5w zorder 3 at f32
    n "Para ti es fácil decirlo..."
    n "Será mejor que no me hagas volver a hacer eso."
    show natsuki zorder 2 at t32
    show monika 1d zorder 3 at f31
    m "Ah, bueno..."
    m "¿Por lo menos te sientes lo suficientemente preparada para recitar un poema frente a otras personas?"
    show monika zorder 2 at t31
    show natsuki 2c zorder 3 at f32
    n "Osea, ¡hacerlo delante de otras personas será mucho más fácil!"
    n "Puedo poner cualquier cara para otras personas."
    n 2q "Pero cuando sólo son mis amigos..."
    n "Es simplemente...vergonzoso."
    show natsuki zorder 2 at t32
    show sayori 1b zorder 3 at f33
    s "Eso es una sorpresa, Natsuki..."
    s "Creo que sería al revés para mí."
    show sayori zorder 2 at t33
    show natsuki zorder 3 at f32
    n "Bueno, así es como es, entonces..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "Bueno, supongo que en ese caso..."
    m "No tendrás que preocuparte de más por el festival."
    m 2b "Dicho esto, quiero agradecerles a todos por haberlo intentado."
    m "Podría ser difícil, pero espero que ahora tengan una idea de cómo se hace."
    m 4b "Asegúrense de elegir un poema y practicar lo suficiente antes del festival, ¿de acuerdo?"
    m "Haré panfletos, así que avísenme de antemano lo que van a recitar."
    show monika zorder 2 at t31
    mc "Caray..."
    mc "Probablemente debería encontrar otro poema para recitar."
    show monika zorder 3 at f31
    m 1j "¡Eso está bien!"
    m 1a "No tiene que ser tuyo."
    m "Ya estoy gratamente sorprendida de que estés poniendo todo este esfuerzo para el club."
    m 5 "Me hace muy feliz."
    show monika zorder 2 at t31
    mc "Ah...sí, no hay problema..."
    play music t8 fadeout 1.0
    show monika zorder 2 at t11
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    hide sayori
    hide natsuki
    m 4b "¡Muy bien, todos!"
    m "Creo que eso es todo por hoy."
    m "Sé que se acerca el festival, pero intentemos también escribir poemas para mañana."
    m "Ha estado funcionando muy bien hasta ahora, así que me gustaría continuar con eso."
    m "En cuanto al festival, terminaremos de planificar mañana, y luego tendremos el fin de semana para prepararnos."
    m "¡El lunes es el gran día!"
    show sayori 4r zorder 2 at t31
    s "¡No puedo esperar~!"
    show yuri 4b zorder 2 at t33
    y "Puedo hacerlo...puedo hacerlo..."
    mc "Muy bien--"
    hide sayori
    hide monika
    hide yuri
    with wipeleft
    "Me paro."
    "No hay forma de que pueda encontrar el mismo entusiasmo que Sayori y Monika, pero haré todo lo posible para lograrlo."
    "Si es por el bien del club..."
    "Y para impresionar a Monika..."
    "Entonces tendré que hacer mi mejor esfuerzo."
    show sayori 1a zorder 2 at t32
    mc "¿Lista para irnos, Sayori?"
    show sayori at h32
    s 1x "¡Sip!"
    show natsuki 2d zorder 3 at f33
    n "Miren a estos dos, siempre yendo a casa juntos."
    show monika 5 zorder 3 at f31
    show natsuki zorder 2 at t33
    m "Es adorable, ¿no?"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1q "Jejeje~"
    show sayori zorder 2 at t32
    mc "Caray, chicas..."
    mc "No hagan un gran alboroto con esto."
    show natsuki zorder 2 at t44
    show sayori zorder 2 at t43
    show monika zorder 2 at t42
    show yuri 1u zorder 3 at f41
    y "Debe ser agradable..."
    show yuri zorder 2 at t41
    mc "Bueno..."
    mc "Ah..."
    "¿Cómo se supone que debo responder a eso?"
    show sayori zorder 3 at f43
    s 1d "Está bien, [player], no tienes que decirlo."
    show sayori zorder 2 at t43
    mc "...Como sea. Ya vámonos."
    scene bg residential_day
    with wipeleft_scene
    $ ch2_winner = poemwinner[1].capitalize()
    if ch2_winner == "Sayori":
        $ ch2_winner = "Yuri"
    "Camino a casa con Sayori una vez más."
    "Aunque sólo han pasado unos días, muchas cosas ya han cambiado."
    "Pero hoy, Sayori está un poco más tranquila de lo normal en el camino a casa."
    mc "Oye, Sayori..."
    show sayori 1k at t11
    s "..."
    s 1n "...¡Perdón! ¡Estaba distraída!"
    mc "Ah, no te preocupes..."
    s 1d "Um..."
    s "Estaba...pensando en algo."
    s "Me gusta cómo llegamos a..."
    s 1y "Q-Quiero decir..."
    "Sayori se tropieza con sus palabras."
    s 1a "Entonces...digamos que un día, [ch2_winner] te pide caminar con ella..."
    mc "¡¿Huh?!"
    s "¿Qué harías?"
    mc "¿Qué clase de pregunta es esa...?"
    mc "Me estás poniendo en una situación incomoda..."
    s 1y "Jejeje..."
    menu:
        "Bueno..."
        "Iría a casa con [ch2_winner].":
            if ch2_winner == "Natsuki":
                call ch2_end_natsuki from _call_ch2_end_natsuki
            else:
                call ch2_end_yuri from _call_ch2_end_yuri
        "Seguiría caminando a casa con Sayori.":
            call ch2_end_sayori from _call_ch2_end_sayori

    "Por otra parte, el festival está a sólo unos días..."
    "¿Quién sabe lo que sucederá para entonces?"
    return
label ch2_end_sayori:
    mc "Sayori..."
    mc "¿Realmente crees que te abandonaría por [ch2_winner]?"
    s 1e "¡¿Eh?!"
    s "P-Pero..."
    if ch2_winner == "Natsuki":
        s "Ella es muy linda y divertida..."
    else:
        s "Ella es tan hermosa e inteligente..."
    mc "Caray..."
    mc "Ya la veo en el club todos los días."
    mc "Además, parece que siempre te gusta ir a casa juntos..."
    mc "No lo arruinaría por ti."
    s 1y "Eres un tontito, [player]..."
    s "Piensas demasiado en mí a veces."
    s "[ch2_winner] lo merecería si ella lo quisiera..."
    mc "Sayori, ya me he decidido."
    mc "Realmente no puedo entenderte a veces..."
    s "Lo siento..."
    mc "Además, ¿qué sentido tiene especular con algo que nunca va a suceder?"
    s 1k "Hm..."
    show sayori at thide
    hide sayori
    "La conversación se apaga."
    "Es algo raro que Sayori se preocupe tanto por eso..."
    "Pero quiero respetarla y mantenerla feliz también."
    return

label ch2_end_natsuki:
    mc "Caminaría a casa con Natsuki, eh..."
    "¿Por qué esa idea hace que mi corazón palpite...?"
    mc "Quiero decir..."
    mc "Creo que le tengo miedo a lo que ella me haría si la rechazo..."
    s 1x "¿No es tan linda y divertida?"
    jump ch2_end_shared

label ch2_end_yuri:
    mc "Caminaría a casa con Yuri, eh..."
    "¿Por qué esa idea hace que mi corazón palpite...?"
    mc "Quiero decir..."
    mc "Dado lo difícil que es para ella el socializar, me sentiría mal rechazándola, así que..."
    s 1x "¿No es tan hermosa e inteligente?"
    jump ch2_end_shared

label ch2_end_shared:
    mc "¡Eso no tiene nada que ver con lo que acabo de decir!"
    s 4s "¡Ajá! ¡Lo admitiste!"
    mc "Por Dios..."
    mc "Ni siquiera tiene sentido especular sobre algo que nunca va a suceder."
    s 1d "Bueno, tal vez..."
    s "Pero sólo me gusta pensar en eso."
    s 1y "No pasará mucho tiempo antes de que ya no me necesites más, ¿sabes?"
    mc "¿Necesitarte...?"
    mc "Sayori..."
    mc "No puedo entender cómo estás viendo las cosas en tu cabeza."
    s "Lo siento..."
    mc "Todos somos diferentes..."
    mc "Nadie en el club es un reemplazo para ti."
    s 1k "Hmm..."
    s "Si tú lo dices..."
    show sayori at thide
    hide sayori
    "La conversación se apaga, y me siento incómodo."
    "Pero fue su culpa haberme atrapado con una pregunta tan extraña..."
    "No puedo simplemente mentirle."
    "Pero si hay algo que la hace feliz, odiaría quitárselo."
    "Es por eso que dije que no tiene sentido especular."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
