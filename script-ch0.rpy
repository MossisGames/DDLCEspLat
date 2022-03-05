label ch0_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../personajes/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_all_characters()
    s "¡¡Oyeeeeeeeeee!!"
    "Desde lejos, veo a una fastidiosa chica corriendo hacia mí, agitando los brazos en el aire como si fuera totalmente ajena a cualquier atención que pudiera atraer."
    "Esa chica es Sayori, mi vecina y buena amiga desde que éramos niños."
    "Ya sabes, el tipo de amiga que nunca te verías haciendo, pero funciona porque nos conocemos desde hace mucho tiempo."
    "Solíamos caminar a la escuela juntos en días como este, pero a partir de la secundaria se ha quedado dormida frecuentemente, y yo me cansé de esperar."
    "Pero si ella va a perseguirme así, casi me siento mejor huyendo."
    "Sin embargo, sólo suspiro y me paro frente al paso de peatones dejando que Sayori me alcance."
    $ s_name = "Sayori"
    show sayori 4p zorder 2 at t11
    s 4p "Haaahhh...Haaahhh..."
    s "¡Otra vez me quedé dormida!"
    s "¡Pero esta vez te atrapé!"
    mc "Tal vez, pero sólo porque decidí detenerme y esperarte."
    show sayori at s11
    s 5c "Eeehhhhh, ¡dices eso como si pensaras en ignorarme!"
    s "¡Eso es grosero, [player]!"
    mc "Bueno, si la gente te mira por actuar raro entonces no quiero que piensen que somos pareja o algo así."
    show sayori zorder 2 at t11
    s 1a "Bien, bien."
    s "Pero de todas formas me esperaste."
    s "Supongo que no puedes ser malo aunque quieras~"
    mc "Como digas, Sayori..."
    s 1q "Jejeje~"
    show sayori zorder 1 at thide
    hide sayori
    "Cruzamos la calle juntos y nos dirigimos a la escuela."
    "A medida que nos acercamos, las calles se llenan cada vez más con otros estudiantes haciendo su viaje diario."
    show sayori 3a zorder 2 at t11
    s "Por cierto, [player]..."
    s "¿Ya has decidido un club para unirte?"
    mc "¿Un club?"
    mc "Ya te lo dije, realmente no estoy interesado en unirme a ningún club."
    mc "Y tampoco he estado buscando."
    show sayori at s11
    s 4h "¿Eh? ¡Eso no es verdad!"
    s "¡Me dijiste que te unirías a un club este año!"
    mc "¿Lo hice...?"
    "Estoy seguro de que es posible que lo haya hecho, en una de nuestras muchas conversaciones en las que le sigo la corriente."
    "A Sayori le gusta preocuparse por mí, cuando estoy perfectamente contento con ser un chico promedio mientras gasto mi tiempo libre en juegos y anime."
    s 4j "¡Uh-huh!"
    s "Estaba hablando acerca de cómo me preocupa que no aprendas a socializar o tener alguna habilidad antes de la universidad."
    s "Tu felicidad es realmente importante para mí, ¡sabes!"
    s "Y sé que eres feliz ahora, ¡pero moriría con sólo pensar que te convertirás en un NINI en unos pocos años porque no estás acostumbrado al mundo real!"
    s 4g "Confía en mí, ¿si?"
    s "No dejes que me siga preocupando por ti..."
    mc "Bien, bien..."
    mc "Voy a ver algunos clubs si eso te hace feliz."
    mc "Pero no prometo nada."
    s 1h "¿Al menos me prometes que intentarás un poco?"
    mc "Sí, supongo que te prometo eso."
    show sayori zorder 2 at t11
    s 4r "¡Yaay~!"
    "¿Por qué me dejo ser sermoneado por una chica tan despreocupada?"
    "Más que eso, me sorprende que incluso me haya permitido ceder a ella."
    "Supongo que verla preocuparse tanto por mí me da ganas de tranquilizarla un poco, incluso si exagera todo lo que tiene dentro de su cabeza."

    scene bg class_day
    with wipeleft_scene

    "El día escolar fue tan común como siempre, y se acabó antes de que me diera cuenta."
    "Después de empacar mis cosas, miro inexpresivamente a la pared, buscando un gramo de motivación."
    mc "Clubs..."
    "Sayori quiere que revise algunos clubs."
    "Creo que no tengo más remedio que comenzar con el club de anime..."

    s "¿Holaaaa?"
    show sayori 1b zorder 2 at t11
    mc "¿Sayori...?"
    "Sayori debe haber entrado al salón mientras yo estaba distraído."
    "Miro a mi alrededor y me doy cuenta de que soy el último que queda."
    s 1a "Pensé que podría alcanzarte saliendo del salón, pero te vi sentado aquí, así que entré."
    s "Honestamente, eres peor que yo algunas veces...¡estoy impresionada!"
    mc "No tienes que esperarme si eso te hará llegar tarde a tu club."
    s 1y "Bueno, pensé que tal vez necesitabas un poco de aliento, así que pensé, ya sabes..."
    mc "¿Qué cosa?"
    s 1a "Bueno, ¡que podrías venir a mi club!"
    mc "Sayori..."
    s 4r "¿¿Siii??"
    mc "...No hay manera de que vaya a tu club."
    show sayori at s11
    s 5d "¡¿Eeeehhhhh?! ¡Grosero!"
    "Sayori es Vicepresidenta del Club de Literatura."
    "No es que fuera consciente de que ella tenía algún interés en la literatura."
    "De hecho, estoy seguro de que ella sólo lo hizo porque pensó que sería divertido ayudar a comenzar un nuevo club."
    "Como ella fue la primera en mostrar interés después de la que propuso el club, heredó el título de \"Vicepresidenta\"."
    "Dicho esto, mi interés en la literatura es incluso menor."
    mc "Sí. Voy al club de anime."
    show sayori zorder 2 at t11
    s 1g "Vamos, ¿por favor?"
    mc "¿Por qué te importa tanto?"
    s 5b "Bueno..."
    s "Como que le conté ayer al club que traería un nuevo miembro..."
    s "Y Natsuki hizo pastelitos..."
    s "Jejeje..."
    mc "¡No hagas promesas que no puedes cumplir!"
    "No puedo adivinar si Sayori es realmente una cabeza hueca, o si ella es tan astuta como para haber planeado todo esto."
    "Dejo escapar un largo suspiro."
    mc "Bien...pasaré por un pastelito, ¿vale?"
    show sayori at h11
    s 4r "¡Sí! ¡Vamos~!"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "Y así, hoy marca el día en que vendí mi alma por un pastelito."
    "Abrumado, sigo a Sayori a través de la escuela y al piso de arriba, una sección de la escuela que rara vez visito, generalmente utilizada para clases y actividades de tercer año."
    "Sayori, llena de energía, abre la puerta del salón."

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "¡Chicas! ¡El nuevo miembro está aquí~!"
    mc "Ya te lo dije, no me llames 'nuevo miembro--'"
    show sayori at lhide
    hide sayori
    "¿Eh? Miro alrededor del salón."
    show yuri 1a zorder 2 at t11
    y "Bienvenido al Club de Literatura. Es un placer conocerte."
    y "Sayori siempre dice buenas cosas sobre ti."
    show yuri zorder 2 at t22
    show natsuki 4c zorder 2 at t21
    n "¿En serio? ¿Trajiste a un chico?"
    n "Qué manera de matar la atmósfera."
    show yuri zorder 2 at t33
    show natsuki zorder 2 at t32
    show monika 1k zorder 2 at t31
    m "Ah, ¡[player]! ¡Qué buena sorpresa!"
    m "¡Bienvenido al Club!"
    show monika 1a
    mc "..."
    "Todas las palabras se me escapan en esta situación."
    "Este club..."
    "{i}...¡¡Está lleno de chicas increíblemente lindas!!{/i}"

    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 3 at f32
    hide monika
    hide yuri

    n 2c "¿Qué estás mirando?"
    n "Si quieres decir algo, dilo."
    mc "L-Lo siento..."
    show natsuki zorder 2 at t32
    show yuri 2l zorder 3 at f33
    y "Natsuki..."
    $ n_name = 'Natsuki'
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f32
    n 5s "Hmph."
    show natsuki zorder 2 at t32

    "La chica con la actitud agria, cuyo nombre aparentemente es Natsuki, es una chica que no reconozco."
    "Su pequeña figura me hace pensar que probablemente es de primer año."
    "Ella es quien hizo los pastelitos, de acuerdo a Sayori."

    show sayori 2q zorder 3 at f31
    s "Puedes ignorarla cuando se pone de mal humor~"
    "Sayori dice eso en mi oído, luego se vuelve hacia las otras chicas."
    s 1x "Esta es Natsuki, siempre llena de energía."
    s "Y esta es Yuri, ¡la más lista del club!"
    $ y_name = 'Yuri'
    show sayori zorder 2 at t31
    show yuri zorder 3 at f33
    y 4b "N-No digas eso..."
    "Yuri, quien comparablemente parece más madura y tímida, parece tener dificultades para mantenerse al día con personas como Sayori y Natsuki."
    show yuri zorder 2 at t33
    mc "Ah...Bueno, es un placer conocerlas a las dos."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show sayori zorder 3 at f31
    s 1a "Y parece que ya conoces a Monika, ¿verdad?"
    $ m_name = 'Monika'
    show sayori zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "Así es."
    m "Es genial verte de nuevo, [player]."
    show monika 5a at hop
    "Monika sonríe dulcemente."
    "Nos conocemos - bueno, rara vez hablamos, pero estábamos en la misma clase el año pasado."
    "Monika era probablemente la chica más popular de la clase - inteligente, hermosa, atlética."
    "Básicamente, fuera de mi alcance."
    "Entonces, sonriéndome tan genuinamente se siente un poco..."
    mc "S-Sí, es genial, Monika."
    show monika zorder 1 at thide
    hide monika
    show sayori zorder 3 at f31
    s 4x "¡Siéntate, [player]! Hicimos sitio para ti en la mesa, para que te puedas sentar junto a mí o junto a Monika."
    s "Iré por los pastelitos~"
    show sayori zorder 2 at t31
    show natsuki 1e zorder 3 at f32
    n "¡Hey! Yo los hice, ¡yo voy por ellos!"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 5a "Perdón, me emocioné un poco~"
    show sayori zorder 2 at t31
    show yuri 1a zorder 3 at f33
    y "Entonces, ¿y si también hago té?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "Las chicas tienen algunos escritorios acomodados para formar una mesa."
    "Como Sayori mencionó, se ha ampliado para que haya un espacio al lado de Monika y un espacio al lado de Sayori."
    "Natsuki y Yuri caminan hacia la esquina del salón, donde Natsuki toma una bandeja envuelta y Yuri abre el armario."
    "Aún incómodo, tomo asiento al lado de Sayori."
    "Natsuki regresa con orgullo a la mesa, con la bandeja en la mano."
    show natsuki 2z zorder 2 at t32
    n "Bieeen, ¿están listos?"
    n "...¡Ta-daa!"
    show sayori 4m zorder 2 at t31
    show monika 2d zorder 2 at t33
    s "¡Uwooooah!"
    "Natsuki levanta el papel de aluminio de la bandeja para revelar una docena de pastelitos blancos y esponjosos decorados para que parezcan pequeños gatos."
    "Los bigotes están dibujados con glaseado, y pequeños trozos de chocolate se utilizaron para hacer las orejas."
    show sayori zorder 3 at f31
    s 4r "¡Qué lindooooo~!"
    show sayori zorder 2 at t31
    show monika zorder 3 at f33
    m 2b "¡No tenía idea de que fueras tan buena horneando, Natsuki!"
    show monika zorder 2 at t33
    show natsuki zorder 3 at f32
    n 2d "Jejeje. Bueno, ya sabes."
    n "¡Sólo apúrense y tomen uno!"
    "Sayori toma uno primero, luego Monika. Yo las sigo."
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 4q "¡Está delicioso!"
    "Sayori habla con la boca llena y ya ha logrado mancharse de glaseado en la cara."
    "Giro el pastelito con los dedos, buscando el mejor ángulo para tomar un bocado."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    show natsuki 1c zorder 2 at t32
    "Natsuki está callada."
    "No puedo evitar notar su mirada furtiva en mi dirección."
    "¿Está esperando a que lo muerda?"
    "Finalmente lo hago."
    "El glaseado es dulce y lleno de sabor - Me pregunto si lo hizo por su cuenta."
    mc "Está muy bueno."
    mc "Gracias, Natsuki."
    n 5h "¿P-por qué me agradeces? ¡No es como que..."
    "{i}(¿No he escuchado esto en algún lugar...?){/i}"
    show natsuki at s32
    n 5s "...Los haya hecho para ti o algo así!."
    mc "¿Eh? Creí que técnicamente lo hiciste. Sayori dijo--"
    show natsuki zorder 2 at t32
    n 12c "Bueno, ¡tal vez!"
    n "Pero no para, t-tú sabes, {i}¡no para ti!{/i} Tonto..."
    mc "Muy bien, muy bien..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Renuncio a la extraña lógica de Natsuki y descarto la conversación."
    "Yuri regresa a la mesa, cargando un juego de té."
    "Ella coloca cuidadosamente una taza de té en frente de cada uno antes de colocar la tetera al lado de la bandeja de pastelitos."
    show yuri 1a zorder 2 at t21
    mc "¿Guardan un juego de té completo en este salón?"
    y "No te preocupes, los profesores nos dieron permiso."
    y "De todas formas, ¿una taza de té no ayuda a disfrutar más de un buen libro?"
    mc "Ah...Y-Yo supongo..."
    show monika 4a zorder 2 at t22
    m "Jejeje, no te intimides, Yuri sólo está tratando de impresionarte."
    show yuri at h21
    y 3n "¡¿Eh?! E-Esa no es..."
    "Insultada, Yuri mira hacia otro lado."
    y 4b "...Esa no es mí intención, sabes..."
    mc "Te creo."
    mc "Bueno, el té y la lectura pueden no ser un pasatiempo para mi, pero al menos disfruto el té."
    y 2u "Me alegro..."
    "Yuri sonríe débilmente en alivio."
    "Monika levanta una ceja y luego me sonríe."
    show yuri zorder 1 at thide
    hide yuri
    show monika zorder 2 at t11
    m 1 "Así que, ¿qué te hizo considerar el Club de literatura?"
    mc "Um..."
    "Tenía miedo que me preguntaran eso."
    "Algo me dice que no debo decirle a Monika que fui prácticamente arrastrado aquí por Sayori."
    mc "Bueno, no me he unido a ningún club, y Sayori se ve realmente feliz aquí, así que..."
    m 1j "¡Está bien! ¡No te avergüences!"
    m 1b "Haremos que te sientas como en casa, ¿vale?"
    m "Como presidenta del Club de Literatura, ¡es mi trabajo hacer el club divertido y emocionante para todos!"
    show monika 1a
    mc "Monika, estoy sorprendido."
    mc "¿Cómo es que decidiste comenzar tu propio club?"
    mc "Probablemente podrías ser miembro de la junta de alguno de los clubs más importantes."
    mc "¿No eras líder del club de debate el año pasado?"
    m 5 "Jajaja, bueno, ya sabes..."
    m "Para ser honesta, no puedo soportar toda la política en torno a los principales clubs."
    m "Se siente como nada más que discutir sobre el presupuesto y la publicidad y cómo prepararse para los eventos..."
    m "Prefiero escoger algo que personalmente disfruto y hacer algo especial con eso."
    m 1b "Y si alienta a otros a entrar en la literatura, ¡entonces estoy cumpliendo ese sueño!"
    show monika 1a
    show sayori 3q zorder 2 at t31
    s "¡Realmente Monika es una gran líder!"
    show yuri 1 zorder 2 at t33
    "Yuri asiente con la cabeza."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide yuri
    mc "Entonces me sorprende que todavía no haya más personas en el club."
    mc "Debe ser difícil comenzar un nuevo club."
    m 3b "Podrías ponerlo de esa manera."
    m "No muchas personas están muy interesadas en poner todo su esfuerzo para comenzar algo nuevo..."
    m "Especialmente cuando es algo que no llama tu atención, como la literatura."
    m "Tienes que esforzarte para convencer a la gente de que es divertido y que vale la pena."
    m "Pero hace que los eventos escolares, como el festival, sean mucho más importantes."
    m 2k "¡Estoy segura de que todos podemos hacer crecer este club antes de graduarnos!"
    m "¿No es así, chicas?"
    show monika 2a zorder 2 at t22
    show sayori 4r zorder 2 at t21
    s "¡Sí!"
    show monika zorder 2 at t33
    show sayori zorder 2 at t32
    show yuri 1a zorder 2 at t31
    y "Haremos lo mejor."
    show monika zorder 2 at t44
    show sayori zorder 2 at t43
    show yuri zorder 2 at t42
    show natsuki 4d zorder 2 at t41
    n "¡Lo sabes!"
    "Todas con entusiasmo están de acuerdo."
    "Estas chicas tan diferentes, todas interesadas en el mismo objetivo..."
    "Monika debe haber trabajado muy duro sólo para encontrar a estas tres."
    "Tal vez es por eso que todas estaban tan encantadas con la idea de un nuevo miembro uniéndose."
    "Aunque todavía no sé si puedo seguir el ritmo de su entusiasmo por la literatura..."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 2 at t32
    hide sayori
    hide monika
    hide natsuki
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
    y "Las historias con profundos elementos psicológicos generalmente me sumergen también."
    y 2a "¿No es sorprendente cómo un escritor puede aprovecharse tan deliberadamente de tu propia falta de imaginación?"
    y "De todos modos, he estado leyendo mucho horror últimamente..."
    mc "Ah, leí un libro de horror una vez..."
    "Desesperadamente trato de tomar un tema con el que me puedo identificar a un nivel mínimo."
    "A este ritmo, Yuri podría estar teniendo una conversación con una roca."
    show monika 1d zorder 3 at f33
    m "¿De verdad? No hubiera esperado eso, Yuri."
    m "Para alguien tan gentil como tú..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "Creo que podrías decir eso."
    y "Pero si una historia me hace pensar o me lleva a otro mundo, entonces realmente no puedo dejarlo."
    y "El horror surrealista a menudo tiene mucho éxito en cambiar la forma de mirar el mundo, aunque sólo sea por un breve momento."
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "Ugh, odio el horror..."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "¿Oh? ¿Por qué?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "Bueno, yo sólo..."
    "Los ojos de Natsuki se vuelven hacia mí por una fracción de segundo."
    n 5q "No importa."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "Es cierto, usualmente te gusta escribir cosas lindas, ¿no es así, Natsuki?"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "¿Q-Qué?"
    n "¿Por qué dices eso?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "Dejaste un trozo de papel en la última reunión del club."
    m "Parecía que estabas trabajando en un poema llamado--"
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "¡¡No lo digas en voz alta!!"
    n "¡Y regrésalo!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "Bien, bien~"
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    hide monika
    hide yuri
    show natsuki 1r zorder 2 at t42
    show sayori 4q behind natsuki at l41
    s "Jejeje, tus pastelitos, tus poemas..."
    s "Todo lo que haces es tan lindo como tú~"
    show sayori behind natsuki at t21
    "Sayori se sienta detrás de Natsuki y pone las manos sobre sus hombros."
    show natsuki at h42
    n 1v "{i}¡¡No soy linda!!{/i}"
    show natsuki zorder 2 at t11
    show sayori zorder 1 at thide
    hide sayori
    mc "Natsuki, ¿escribes tus propios poemas?"
    n 1c "¿Eh? Bueno, supongo que a veces."
    n "¿Por qué te importa?"
    mc "Creo que es impresionante."
    mc "¿Por qué no los compartes algún día?"
    n 5q "¡N-No!"
    "Natsuki desvía la mirada."
    n "No te...gustarían..."
    mc "Ah...¿Aún no eres una escritora confiada?"
    show yuri 2f zorder 2 at t31
    y "Entiendo lo que Natsuki siente."
    y "Compartir ese nivel de escritura toma más que seguridad."
    y 2k "La verdadera forma de escribir es hacerlo para ti mismo."
    y "Debes estar dispuesto a abrirte a tus lectores, exponiendo tus vulnerabilidades y mostrando incluso los alcances más profundos de tu corazón."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 2a zorder 2 at t33
    m "¿Tambien tienes experiencia escribiendo, Yuri?"
    m "Quizás si compartes parte de tu trabajo, puedes dar un ejemplo y ayudar a Natsuki a sentirse lo suficientemente cómoda como para compartir el de ella."
    show yuri at s31
    y 3o "..."
    mc "Supongo que es lo mismo para Yuri..."
    show sayori 2g zorder 2 at t32
    s "Aww...Quería leer los poemas de todos..."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide yuri
    hide monika
    "Nos sentamos en silencio por un momento."
    show monika 5a zorder 3 at f32
    m "¡Muy bien!"
    m "Tengo una idea, chicos~"
    show yuri 3e zorder 2 at t31
    show natsuki 2k zorder 2 at t33
    ny "¿...?"
    "Natsuki y Yuri miran con curiosidad a Monika."
    m 2b "¡Vámonos todos a casa y escribamos un poema!"
    m "Entonces, la próxima vez que nos veamos, los compartiremos entre nosotros."
    m "De esa forma, ¡todos estaremos a la par!"
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f33
    n 5q "U-Um..."
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f31
    y "..."
    show natsuki zorder 2 at t44
    show monika zorder 2 at t43
    show yuri zorder 2 at t42
    show sayori 4r at l41
    s "¡Siiii! ¡Hagámoslo!"
    show monika zorder 3 at f43
    m 1a "Además, ahora que tenemos un nuevo miembro, creo que eso nos ayudará a sentirnos un poco más cómodos y fortalecer el vínculo del club."
    m "¿No es así, [player]?"
    show monika zorder 2 at t43
    "Monika me sonríe cálidamente una vez más."
    mc "Espera...Aún hay un problema."
    show monika zorder 3 at f43
    m 1d "¿Eh? ¿Cuál?"
    "Ahora que volvemos al tema original de mi incorporación al club, sin rodeos saco lo que he tenido en mente."
    show monika zorder 2 at t43
    mc "¡Nunca dije que me uniría a este club!"
    mc "Sayori puede haberme convencido de pasar por aquí, pero nunca tomé ninguna decisión."
    mc "Todavía tengo otros clubs que mirar, y...Um..."
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e
    "Pierdo el hilo de mis pensamientos."
    "Las cuatro chicas me miran con ojos abatidos."
    show monika at s43
    m 1p "P-Pero..."
    show yuri at s42
    y 2v "Lo siento, pensé..."
    show natsuki at s44
    n 5s "Hmph."
    show sayori at s41
    s 1k "[player]..."
    mc "T-Todas ustedes..."
    "Estoy...Estoy indefenso contra estas chicas."
    "¿Cómo se supone que debo tomar una decisión clara con ellas así?"
    "Bueno, si escribir poemas es el precio que tengo que pagar para poder pasar cada día con estas hermosas chicas..."
    mc "...Bien."
    mc "Vale, ya lo decidí."
    mc "Me uniré al Club de Literatura."
    show monika 1e zorder 2 at t43
    show yuri 3f zorder 2 at t42
    show natsuki 1k zorder 2 at t44
    show sayori 4b zorder 2 at t41
    "Los ojos de las chicas se iluminan."
    show sayori at h41
    s 4r "¡Síii! Estoy tan feliz~"
    "Sayori me rodea con sus brazos, saltando de arriba a abajo."
    mc "O-Oye--"
    show yuri zorder 3 at f42
    y 1m "Realmente me asustaste por un momento..."
    show yuri zorder 2 at t42
    show natsuki zorder 3 at f44
    n 5q "Si realmente sólo hubieras venido por los pastelitos, estaría muy enojada."
    show natsuki zorder 2 at t44
    show monika zorder 3 at f43
    m 5 "Entonces, ¡eso lo hace oficial!"
    m "¡Bienvenido al Club de Literatura!"
    show monika zorder 2 at t43
    mc "Ah...Gracias, supongo."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show sayori zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    hide sayori
    m 3b "¡Muy bien, todos!"
    m "Creo que con eso, podemos finalizar oficialmente la reunión de hoy con una buena nota."
    m "Recuerden la tarea de esta noche:"
    m "Escribir un poema para traer a la próxima reunión, ¡para que todos podamos compartir!"
    "Monika me mira una vez más."
    m 1a "[player], quiero ver cómo te expresas."
    show monika 5 at hop
    m "Jejeje~"
    mc "S-Siie..."
    show monika zorder 1 at thide
    hide monika
    "¿Realmente puedo impresionar a la estrella de la clase Monika con mis mediocres habilidades de escritura?"
    "Ya siento la ansiedad creciendo dentro de mí."
    "Mientras tanto, las chicas continúan charlando mientras Yuri y Natsuki limpian la comida."
    show sayori 1a zorder 2 at t11
    s "Oye, [player], ya que estamos aquí, ¿quieres caminar juntos a casa?"
    "Es cierto - Sayori y yo nunca volvíamos a casa juntos porque siempre se quedaba al terminar las clases."
    mc "Claro, podríamos hacerlo."
    s 4q "Yaay~"

    scene bg residential_day
    with wipeleft_scene

    "Con eso, los dos nos vamos del salón del club y nos dirigimos a casa."
    "Durante todo el camino, mi mente vuela pensando en las cuatro chicas:"
    show sayori 1 zorder 2 at t41
    "Sayori,"
    show natsuki 4 zorder 2 at t42
    "Natsuki,"
    show yuri 1 zorder 2 at t43
    "Yuri,"
    show monika 1 zorder 2 at t44
    "Y, por supuesto, Monika."
    "¿Realmente estaré feliz de pasar todos los días después de la escuela en un club de literatura?"
    "Quizás tendré la oportunidad de acercarme a una de estas chicas..."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "¡Muy bien!"
    "Sólo tendré que aprovechar al máximo mis circunstancias, y estoy seguro de que la buena suerte me encontrará."
    "Y supongo que eso comienza con escribir un poema esta noche..."

    return

label ch0_kill:
    $ s_name = "Sayori"
    show sayori 1b zorder 2 at t11
    s "..."
    s "..."
    s "¿Q-Qué..."
    s 1g "..."
    s "Esto..."
    s "¿Qué es esto...?"
    s "Oh no..."
    s 1u "No..."
    s "Esto no puede ser."
    s "Esto no puede ser todo lo que es."
    s 4w "¿Qué es esto?"
    s "¿Qué soy?"
    s "¡Hazlo parar!"
    s "¡POR FAVOR, DETENLO!"

    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
