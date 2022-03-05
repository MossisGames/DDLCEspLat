label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

label ch20_main2:
    "Es un día escolar normal, como cualquier otro."
    "Las mañanas suelen ser las peores, estar rodeado de parejas y grupos de amigos caminando juntos hacia la escuela."
    "Por mi parte, siempre he caminado sólo a la escuela."
    "Usualmente me digo que es hora de conocer a algunas chicas o algo así..."
    "Pero no tengo motivación para unirme a ningún club."
    "Estoy perfectamente contento con sólo ser un chico promedio mientras gasto mi tiempo libre en juegos y anime."
    "Está el club de anime, pero de todos modos no es como si hubiera chicas ahí."

    scene bg class_day
    with wipeleft_scene

    "El día escolar fue tan común como siempre, y se acabó antes de que me diera cuenta."
    "Después de empacar mis cosas, miro inexpresivamente a la pared, buscando un gramo de motivación."
    mc "Clubs..."
    "Realmente no hay ninguno que me interese."
    "Además, la mayoría probablemente serían demasiado exigentes para que yo quiera tratarlos."
    "Creo que no tengo más remedio que comenzar con el club de anime..."

    $ m_name = "???"

    m "...¿[player]?"
    window hide(None)
    show monika g2 zorder 2 at t11
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    show monika 1 zorder 2 at t11
    mc "...¿Monika?"
    $ m_name = "Monika"
    m 1b "¡Dios mío, no esperaba verte aquí!"
    m 5 "Ha pasado mucho tiempo, ¿verdad?"
    mc "Ah..."
    mc "Sí, lo ha hecho."
    "Monika sonríe dulcemente."
    "Nos conocemos - bueno, rara vez hablamos, pero estábamos en la misma clase el año pasado."
    "Monika era probablemente la chica más popular de la clase - inteligente, hermosa, atlética."
    "Básicamente, fuera de mi alcance."
    "Entonces, sonriéndome tan genuinamente se siente un poco..."
    mc "¿Por qué viniste aquí, de todos modos?"
    m 1a "Ah, estoy buscando algunos útiles para mi club."
    m 1d "¿Sabes si hay algún pliego de papel aquí?"
    m "¿O marcadores?"
    mc "Supongo que podrías revisar el armario."
    mc "...Estás en el club de debate, ¿verdad?"
    m 5 "Jajaja, sobre eso..."
    m "De hecho, dejé el club de debate."
    mc "¿En serio? ¿Lo dejaste?"
    m "Sí..."
    m 2e "Para ser honesta, no puedo soportar toda la política en torno a los principales clubs."
    m "Se siente como nada más que discutir sobre el presupuesto y la publicidad y cómo prepararse para los eventos..."
    m "Prefiero escoger algo que personalmente disfruto y hacer algo especial con él."
    mc "En ese caso, ¿a qué club decidiste unirte?"
    m 1b "¡En realidad, estoy empezando uno nuevo!"
    m "¡Un Club de Literatura!{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "¡Un Club de Literatura!{fast}"
    window auto
    mc "¿Literatura...?"
    "Eso suena...¿aburrido?"
    mc "¿Cuántos miembros tienes hasta ahora?"
    m 5 "Um..."
    m "Jajaja..."
    m "Es un poco vergonzoso, pero sólo somos tres hasta ahora."
    m "Es realmente difícil encontrar nuevos miembros para algo que suena tan aburrido..."
    mc "Bueno, puedo ver eso..."
    m 3d "Pero realmente no es nada aburrido, ¿sabes?"
    m "La literatura puede ser cualquier cosa. Lectura, escritura, poesía..."
    m 3e "Quiero decir, incluso hay alguien que guarda su colección de manga en el salón del club..."
    mc "Espera...¿de verdad?"
    m 2k "Sí, es gracioso, ¿no?"
    m 2e "Siempre insiste en que el manga es literatura."
    m "Quiero decir, ella no está equivocada, supongo..."
    m "Y además, un miembro es un miembro, ¿no es así?"
    "...¿Acaso Monika dijo \"ella\"?"
    "Hmm..."
    m 1a "Oye, [player]..."
    m "Por casualidad...¿todavía estás buscando un club para unirte?"
    mc "Ah--"
    mc "Quiero decir, supongo que sí, pero..."
    m "En ese caso..."
    m 5 "¿Hay alguna posibilidad de que me hagas un gran favor?"
    m "No te pediré que te unas, pero..."
    m "Si al menos pudieras visitar mi club, me haría muy feliz."
    m "¿Por favor?"
    mc "Um..."
    "Bueno, supongo que no tengo motivos para rechazar esa propuesta..."
    "Además, ¿cómo podría rechazar a alguien como Monika?"
    mc "Claro, supongo que podría darle un vistazo."
    m 1k "Aah, ¡increíble!"
    m 1b "Eres muy dulce, [player], ¿lo sabías?"
    mc "N-No es nada, realmente..."
    m 1a "¿Entonces nos vamos?"
    m "Buscaré los útiles en otra ocasión - tú eres más importante."

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "Y así, hoy marca el día en que vendí mi alma a Monika y su sonrisa irresistible."
    "Tímidamente sigo a Monika a través de la escuela y al piso de arriba, una sección de la escuela que rara vez visito, generalmente utilizada para clases y actividades de tercer año."
    "Monika, llena de energía, abre la puerta del salón."

    scene bg club_day2
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0:
        show monika g1 at l31
    else:
        show monika 3b at l31
    m "¡Estoy de vuelta~!"
    m "¡Y traje a un invitado conmigo!"
    show yuri 2t zorder 2 at t33
    if not config.skipping:
        show screen invert(0.15, 0.3)
    y "¿Eh?"
    y "¿Un...Un invitado?"
    show natsuki 4c zorder 2 at t32
    n "¿En serio? ¿Trajiste a un chico?"
    n "Que manera de matar la atmósfera."
    show monika 3m zorder 3 at f31
    m "No seas grosera, Natsuki..."
    m 3b "...De todas formas, ¡bienvenido al club, [player]!"
    show monika 3a zorder 2 at t31
    mc "..."
    "Todas las palabras se me escapan en esta situación."
    "Este club..."
    "{i}...¡¡Está lleno de chicas increíblemente lindas!!{/i}"

    show natsuki zorder 3 at f32
    n 5c "Así que, adivinaré..."
    n "Eres el novio de Monika, ¿verdad?"
    show natsuki zorder 2 at t32
    mc "¿Qué--"
    mc "¡No, No lo soy!"
    show yuri zorder 3 at f33
    y 2l "Natsuki..."
    $ n_name = 'Natsuki'
    "La chica con la actitud agria, cuyo nombre aparentemente es Natsuki, es una que no reconozco."
    "Su pequeña figura me hace pensar que probablemente es de primer año."

    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 2l "¡D-De todas formas! Esta es Natsuki, siempre llena de energía...."
    m 2b "Y esta es Yuri, ¡la Vicepresidenta!"
    $ y_name = 'Yuri'
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f33
    y 4 "E-Es un placer conocerte..."
    "Yuri, quien parece comparablemente más madura y tímida, parece tener dificultades para mantenerse al día con personas como Natsuki."
    show yuri zorder 2 at t33
    mc "Si...es un placer conocerlas a ambas."
    show monika zorder 3 at f31
    m 1a "Me encontré con [player] en un salón de clases, y él decidió venir a ver el club."
    m "¿No es genial?"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32
    n 4e "¡Espera, Monika!"
    n "¿No te dije que me avisaras con anticipación antes de traer a alguien nuevo?"
    n 4q "Iba a...bueno, ya sabes..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1e "¡Lo siento, lo siento!"
    m "No olvidé eso, pero casualmente me encontré con él."
    show monika zorder 2 at t31
    show yuri zorder 3 at f33
    y 1a "En ese caso, al menos debería hacer un poco de té, ¿verdad?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 1b "¡Sí, eso sería genial!"
    m "¿Por qué no te sientas, [player]?"
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "Las chicas tienen algunos escritorios acomodados para formar una mesa."
    "Yuri camina hacia la esquina de la habitación y abre el armario."
    "Mientras tanto, Monika y Natsuki se sientan frente a frente."
    "Aun incómodo, tomo asiento junto a Monika."
    show monika 1a zorder 2 at t11
    m "Entonces, sé que en realidad no planeaste venir aquí..."
    m "Pero nos aseguraremos de que se sienta como en casa, ¿vale?"
    m 1j "¡Como presidenta del Club de Literatura, es mi deber hacer que el club sea divertido y emocionante para todos!"
    mc "Entonces me sorprende que todavía no haya más personas en el club."
    mc "Debe ser difícil comenzar un nuevo club."
    m 3b "Podrías ponerlo de esa manera."
    m "No muchas personas están muy interesadas en poner todo su esfuerzo para comenzar algo nuevo..."
    m "Especialmente cuando es algo que no llama tu atención, como la literatura."
    m "Tienes que esforzarte para convencer a la gente de que es divertido y que vale la pena."
    m "Pero hace que los eventos escolares, como el festival, sean mucho más importantes."
    m 2k "¡Estoy segura de que todas podemos hacer crecer este club antes de graduarnos!"
    m "¿No es así, Natsuki?"
    show monika zorder 2 at t22
    show natsuki 4q zorder 2 at t21
    n "Bueno..."
    n "...Supongo."
    "Natsuki de mala gana está de acuerdo."
    "Estas chicas tan diferentes, todas interesadas en el mismo objetivo..."
    "Monika debe haber trabajado muy duro sólo para encontrar a estas dos."
    "Yuri regresa a la mesa, cargando un juego de té."
    "Ella coloca cuidadosamente una taza de té delante de cada uno antes de dejar la tetera en medio."
    show natsuki zorder 1 at thide
    show monika zorder 1 at thide
    hide natsuki
    hide monika
    show yuri 1a zorder 2 at t21
    mc "¿Guardan un juego de té completo en este salón?"
    y "No te preocupes, los profesores nos dieron permiso."
    y "De todas formas, ¿una taza de té no ayuda a disfrutar más de un buen libro?"
    mc "Ah...Y-Yo supongo..."
    show monika 4a zorder 3 at f22
    m "Jejeje, no te intimides, Yuri sólo está tratando de impresionarte."
    show monika zorder 2 at t22
    show yuri at hf21
    y 3n "¡¿Eh?! E-Esa no es..."
    "Insultada, Yuri mira hacia otro lado."
    y 4b "...Esa no es mi intención, sabes..."
    show yuri zorder 2 at t21
    mc "Te creo."
    mc "Bueno, el té y la lectura pueden no ser un pasatiempo para mi, pero al menos disfruto el té."
    show yuri zorder 3 at f21
    y 2u "Me alegro..."
    show yuri zorder 2 at t21
    "Yuri sonríe débilmente en alivio."
    show monika zorder 1 at thide
    hide monika
    show yuri 1a zorder 2 at t32
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
    m "Jajaja. Esperaba eso de ti, Yuri."
    m 1a "Encaja con tu personalidad."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "Oh, ¿eso crees?"
    y "En serio, si una historia me hace pensar o me lleva a otro mundo, entonces realmente no puedo dejarlo."
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
    show monika 1a zorder 2 at t33
    mc "Natsuki, ¿escribes tus propios poemas?"
    show natsuki zorder 3 at f31
    n 1c "¿Eh? Bueno, supongo que a veces."
    n "¿Por qué te importa?"
    show natsuki zorder 2 at t31
    mc "Creo que es impresionante."
    mc "¿Por qué no los compartes algún día?"
    show natsuki zorder 3 at f31
    n 5q "¡N-No!"
    "Natsuki desvía la mirada."
    n "No te...gustarían..."
    show natsuki zorder 2 at t31
    mc "Ah...¿Aun no eres una escritora confiada?"
    show yuri zorder 3 at f32
    y 2f "Entiendo lo que Natsuki siente."
    y "Compartir ese nivel de escritura toma más que seguridad."
    y 2k "La verdadera forma de escribir es hacerlo para ti mismo."
    y "Debes estar dispuesto a abrirte a tus lectores, exponiendo tus vulnerabilidades y mostrando incluso los alcances más profundos de tu corazón."
    show yuri zorder 2 at t32
    show monika 2a zorder 3 at f33
    m "¿También tienes experiencia escribiendo, Yuri?"
    m "Quizás si compartes parte de tu trabajo, puedes dar un ejemplo y ayudar a Natsuki a sentirse lo suficientemente cómoda como para compartir el de ella.."
    show yuri at s32
    y 3o "..."
    mc "Supongo que es lo mismo para Yuri..."
    "Nos sentamos en silencio por un momento."
    show monika zorder 3 at f33
    m 5a "Hey, ¡tengo una idea!"
    m "¿Qué les parece esto?"
    show monika zorder 2 at t33
    show natsuki 2k zorder 3 at f31
    show yuri 3e zorder 3 at f32
    ny "¿...?"
    "Natsuki y Yuri miran con curiosidad a Monika."
    show natsuki zorder 2 at t31
    show yuri zorder 2 at t32
    show monika zorder 3 at f33
    m 2b "¡Vámonos todos a casa y escribamos un poema!"
    m "Entonces, la próxima vez que nos veamos, los compartiremos entre nosotros."
    m "De esa forma, ¡todos estaremos a la par!"
    show monika 2a zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5q "U-Um..."
    show natsuki zorder 2 at t31
    show yuri 3v zorder 3 at f32
    y "..."
    show yuri zorder 2 at t32
    show monika 2m zorder 3 at f33
    m "Ah..."
    m "Quiero decir, pensé que sería buena idea..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 2l "Bueno..."
    y "...Creo que tienes razón, Monika."
    y 2f "Probablemente deberíamos comenzar a buscar actividades para que todos participemos juntos."
    y 2h "Decidí asumir la responsabilidad de Vicepresidenta, después de todo..."
    y "Necesito hacer mi mejor esfuerzo para nutrir tanto al club como a sus miembros."
    y 2a "Además, ahora que tenemos un nuevo miembro..."
    y "Parece un buen paso para nosotros."
    y "¿No estás de acuerdo, [player]?"
    show yuri zorder 2 at t32
    mc "Espera...Aún hay un problema."
    show monika zorder 3 at f33
    m 1d "¿Eh? ¿Cuál?"
    "Ahora que volvemos al tema original de mi incorporación al club, sin rodeos saco lo que he tenido en mente."
    show monika zorder 2 at t33
    mc "¡Nunca dije que me uniría a este club!"
    mc "Monika puede haberme convencido de pasar por aquí, pero nunca tomé ninguna decisión."
    mc "Todavía tengo otros clubs que mirar, y...Um..."
    show monika 1g
    show natsuki 4g
    show yuri 2e
    "Pierdo el hilo de mis pensamientos."
    "Las tres chicas me miran con ojos abatidos."
    show monika at s33
    m 1p "P-Pero..."
    show yuri at s32
    y 2v "Lo siento, pensé..."
    show natsuki at s31
    n 5s "Hmph."
    mc "¿Eh...?"
    "Las chicas intercambian miradas antes de que Monika se vuelva hacia mí."
    show monika zorder 3 at f33
    m 1m "Yo...Creo que necesito decirte la verdad, [player]."
    m "Lo que pasa es que..."
    m 1p "...Todavía no tenemos suficientes miembros para formar un club oficial."
    m "Necesitamos cuatro..."
    m "Y he estado tratando demasiado de encontrar nuevos miembros."
    m "Y si no encontramos uno más antes del festival..."
    show monika zorder 2 at t33
    mc "..."
    "Estoy...estoy indefenso contra estas chicas."
    "¿Cómo se supone que debo tomar una decisión clara cuando es así?"
    "Me sentiría mal por decepcionar a todas en esta situación..."
    "Y además, el club en sí parece bastante relajado..."
    "Bueno, si escribir poemas es el precio que tengo que pagar para poder pasar cada día con estas hermosas chicas..."
    mc "...Bien."
    mc "Vale, ya lo decidí."
    mc "Me uniré al Club de Literatura."
    show monika 1e zorder 2 at t33
    show yuri 3f zorder 2 at t32
    show natsuki 1k zorder 2 at t31
    "Los ojos de las chicas se iluminan."
    show monika zorder 3 at f33
    m "Oh Dios mio, ¿en verdad?"
    m "¿Lo dices en serio, [player]?"
    show monika zorder 2 at t33
    mc "Si..."
    mc "Será divertido, ¿no?"
    show yuri zorder 3 at f32
    y 1m "Realmente me asustaste por un momento..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5q "Si realmente sólo te hubieras ido después de esto, estaría muy enojada."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m "[player], estoy tan feliz..."
    m 1k "¡Ahora podemos convertirnos en un club oficial!"
    m 1e "Muchas gracias por esto. Eres realmente increíble."
    m "Haré todo lo que pueda para que pases un buen rato, ¿de acuerdo?"
    show monika zorder 2 at t33
    mc "Ah...gracias, supongo."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
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
    "Mientras tanto, las chicas continúan charlando mientras Yuri limpia la mesa."
    mc "Creo que ya me iré, entonces..."
    show monika 5a zorder 2 at t11
    m "¡Está bien!"
    m "Te veré mañana."
    m "¡No puedo esperar!"

    scene bg residential_day
    with wipeleft_scene

    "Con eso, me voy del salón del club y me dirijo a casa."
    "Durante todo el camino, mi mente vuela pensando en las tres chicas:"
    show natsuki 4a zorder 2 at t31
    "Natsuki,"
    show yuri 1a zorder 2 at t32
    "Yuri,"
    show monika 1a zorder 2 at t33
    "Y, por supuesto, Monika."
    "¿Realmente estaré feliz de pasar todos los días después de la escuela en un club de literatura?"
    "Quizás tendré la oportunidad de acercarme a una de estas chicas..."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "¡Muy bien!"
    "Sólo tendré que aprovechar al máximo mis circunstancias, y estoy seguro de que la buena suerte me encontrará."
    "Y supongo que eso comienza con escribir un poema esta noche..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    call screen confirm("Has desbloqueado un poema especial.\n¿Quieres leerlo?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[0]) from _call_expression_3
    else:
        pass

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
