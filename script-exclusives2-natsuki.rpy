init python:
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight
            
            for i in range(self.numRects):
                self.add(self.displayable)
        
        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)
        
        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0

image n_rects_ghost1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost4:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -250

image n_rects_ghost5:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -100

label natsuki_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    n "¡Ugh...!"
    "Escucho a Natsuki lanzando un suspiro exasperado desde el armario."
    "Parece estar molesta por algo."
    "Me acerco a ella, en caso de que necesite ayuda."
    play music t6 fadeout 1
    scene bg closet
    show natsuki 4r zorder 2 at t11
    with wipeleft_scene
    $ style.say_dialogue = style.normal
    mc "¿Estás buscando algo allí?"
    $ style.say_dialogue = style.edited
    n 4x "jodida monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Tonta Monika..."
    n "¡Ella nunca vuelve a poner mis cosas en el lugar correcto!"
    n "¿De qué sirve mantener organizada tu colección si alguien más la estropea?"
    "Natsuki desliza un montón de libros apilados y cajas en el estante."
    mc "Manga..."
    n 2c "Lees manga, ¿verdad?"
    mc "Ah--"
    mc "...A veces..."
    "El manga es una de esas cosas que no puedes admitir que realmente te interesa hasta que descubres la opinión de la otra persona."
    mc "...¿Cómo lo supiste?"
    n 2k "Escuché que lo mencionaste en algún momento."
    n "Además, está escrito en tu cara."
    "¿Que se supone que significa eso...?"
    mc "Ya veo..."
    "Hay un volumen solitario de manga en medio de una pila de varios libros en el lateral de uno de los estantes."
    "Con curiosidad, lo saco de la pila."
    n 1b "¡{i}Ahí{/i} esta!"
    "Natsuki me lo arrebata de la mano."
    "Luego se dirige a una caja de mangas y desliza el volumen justo en el medio del resto."
    n 4d "¡Aah, mucho mejor!"
    n "Ver una caja con un libro perdido es probablemente la vista más irritante del mundo."
    mc "Sé lo que se siente..."
    "Observo más de cerca la caja que está admirando."
    mc "¿Chicas Parfait...?"
    "Es una serie de la que nunca había oído hablar en mi vida."
    "Eso probablemente significa que está fuera de mi demografía, o simplemente es terrible."
    n 5g "Si vas a juzgar, puedes hacerlo a través del vidrio en esa puerta."
    "Señala la puerta del salón."
    mc "¡H-Hey, yo no estaba juzgando...!"
    mc "Ni siquiera dije nada."
    n 5c "Fue el tono de tu voz."
    $ style.say_dialogue = style.normal
    n "Pero te diré una cosa, [player]."
    n 4l "Considera esta una lección directa del Club de Literatura: {nw}"
    $ _history_list[-1].what = "Considera esta una lección directa del Club de Literatura: ¡No juzgues un libro por su portada!"
    $ style.say_dialogue = style.edited
    n "¡No juzgues un librrrrrrrrrrrrrrrrr rrrrr rr{space=20}r{space=40}r{space=120}r{space=160}r{space=200}r"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    n "De hecho--"
    "Natsuki saca el primer volumen de Chicas Parfait de la caja."
    n "¡Te voy a mostrar exactamente por qué!"
    "Ella me da el libro directamente en mis manos."
    mc "Ah..."
    "Miro la portada."
    "Presenta a cuatro chicas con atuendos coloridos y sorprendentes poses femeninas animadas."
    "Es...Excedentemente \"moe\"."
    n 4b "¡No te quedes ahí parado!"
    mc "Uwa--"
    show natsuki zorder 1 at thide
    hide natsuki
    "Natsuki me agarra del brazo y me saca del armario."
    "Luego se sienta contra la pared, debajo de una ventana."
    "Ella palmea en el suelo junto a ella, indicando que me siente allí."
    show bg club_day
    show natsuki 2a zorder 2 at t11
    with wipeleft
    mc "¿Las sillas no estarían más cómodas...?"
    "Tomo mi asiento."
    n 2k "Las sillas no funcionarían."
    n "No podríamos leer al mismo tiempo en las sillas."
    mc "¿Eh?, ¿a qué te refieres?"
    mc "Ah...creo que es más fácil estar juntos así..."
    n 2o "¡-!"
    n 5r "¡N-No digas eso!"
    n "¡Me harás sentir rara!"
    "Natsuki se cruza de brazos y se separa un poco de mí."
    mc "Lo siento..."
    show natsuki 5g
    "Tampoco esperaba exactamente estar tan cerca de ella..."
    "No es que pueda decir que es particularmente malo."
    "Abro el libro."
    "Son sólo unos segundos antes de que Natsuki una vez más se acerque, reclamando el espacio adicional mientras espera que no me de cuenta."
    "Puedo sentirla mirando por encima de mi hombro, mucho más ansiosa por comenzar a leer que yo."
    n 1k "Wow, ¿hace cuánto tiempo que no leo el principio...?"
    mc "¿Hm?"
    mc "¿No lees los volúmenes más viejos de vez en cuando?"
    n 2k "No realmente."
    n "Quizás a veces después de que ya terminé la serie."
    n 2c "Oye, ¿estás prestando atención?"
    mc "Uh..."
    "Lo estoy, pero todavía no ha pasado nada, así que puedo hablar al mismo tiempo."
    "Parece que se trata de un grupo de amigas en la escuela secundaria."
    "Algo común en los 'slice-of-life'."
    "Usualmente me alejo de estos, ya que es raro que la escritura sea lo suficientemente entretenida como para compensar la falta de argumento."
    $ persistent.clear[0] = True
    $ renpy.save_persistent()
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "...¿Estás segura de que esto no es aburrido para ti?"
    n "¡No lo es!"
    mc "¿Aunque sólo me estás viendo leer?"
    n "¡Bueno...!"
    n "Estoy...bien con eso."
    mc "Si tú lo dices..."
    mc "...Creo que es divertido compartir algo que te gusta con alguien más."
    mc "Siempre me emociono cuando convenzo a cualquiera de mis amigos para que lea una serie que disfruto."
    mc "¿Sabes lo que quiero decir?"
    n "¿...?"
    mc "¿Hm?"
    mc "¿No?"
    show n_cg1_exp2 at cgfade
    n "Um..."
    n "Eso no es..."
    n "Bueno, realmente no lo sé."
    mc "...¿Qué quieres decir?"
    mc "¿No compartes tu manga con tus amigos?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "¿Podrías no restregármelo en la cara?"
    n "Caray..."
    mc "Ah...lo siento..."
    n "Hmph."
    n "Como si alguna vez pudiera hacer que mis amigos leyeran esto..."
    n "Simplemente piensan que el manga es para niños."
    n "Ni siquiera puedo mencionarlo sin que todos sean como..."
    n "'¿Eh? ¿Todavía lees eso?'"
    n "Me dan ganas de golpearlos en la cara..."
    mc "Urgh, conozco ese tipo de personas..."
    mc "Honestamente, cuesta mucho esfuerzo encontrar amigos que no juzguen, y mucho más trabajo amigos que también los lean..."
    mc "Ya soy un perdedor, así que creo que gravité hacia los otros perdedores con el tiempo."
    mc "Pero probablemente sea más difícil para alguien como tú..."
    hide n_cg1_exp3
    n "Hm"
    n "Sí, eso es bastante preciso."
    "{i}...Espera, ¿¿qué parte??{/i}"
    $ style.say_dialogue = style.normal
    n "Quiero decir, siento que ni siquiera puedo guardarlo en mi propia habitación..."

    $ style.say_dialogue = style.edited
    n "Mi papá me sacaría la mierda a golpes si descubriera esto."
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Ni siquiera sé lo que haría mi papá si encontrara esto."
    n "Al menos está seguro aquí en el salón del club."
    show n_cg1_exp3 at cgfade
    n "Excepto cuando Monika es un poco idiota al respecto..."
    n "¡Uff! Simplemente no puedo ganar, ¿verdad?"
    mc "Bueno, valió la pena al final, ¿no?"
    mc "Quiero decir, aquí estoy, leyéndolo."
    n "Bueno, no es como que eso resuelva ninguno de mis problemas."
    mc "Tal vez..."
    mc "Pero al menos te estás divirtiendo, ¿verdad?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    n "..."
    n "...¿Y qué?"
    mc "Jajaja."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "¡Dios mío, es suficiente!"
    n "¿Vas a seguir leyendo, o qué?"
    mc "Sí, sí..."
    "Paso la página."
    show black with dissolve_cg
    "..."
    "..."
    "....."
    "......."
    "........."
    "El tiempo pasa."
    hide n_cg1_exp3
    show n_cg1_exp4 behind black at cgfade
    "Natsuki está extrañamente callada ahora."
    "La miro."
    hide black with dissolve_cg
    "Parece que ella comenzó a quedarse dormida."
    mc "Oye, Natsuki..."
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "¿S-Sí...?"
    "De repente, Natsuki se derrumba directamente contra mí."
    play sound fall
    $ style.say_dialogue = style.normal
    mc "O-Oye--"
    show n_cg1_exp5
    hide n_cg1_exp5

    show n_cg1b
    hide n_cg1_base

    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    play music t6g
    $ ntext = glitchtext(96)
    $ style.say_dialogue = style.edited
    n "{color=#000}[ntext]{/color}"
    $ ntext = glitchtext(96)
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal

    stop music
    window hide(None)
    window auto
    scene bg club_day
    show monika 1r zorder 2 at t11
    m "Oh cielos..."
    m 1d "Natsuki, ¿estás bien?"
    show monika zorder 2 at t21
    show natsuki 12b zorder 3 at f22
    n "..."
    show natsuki zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Toma..."
    show monika zorder 2 at t21
    "Monika toma su bolso y saca una especie de barra de proteína."
    "Ella lo arroja en la dirección de Natsuki."
    "Los ojos de Natsuki de repente se iluminan de nuevo."
    "Ella arrebata la barra del suelo y de inmediato arranca el envoltorio."
    show natsuki zorder 3 at f22
    n 1s "Te dije que no me dieras mmph..."
    show natsuki zorder 2 at t22
    "Ella ni siquiera termina su oración antes de metérsela en la boca."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 3b zorder 2 at t11
    m "No te preocupes, [player]."
    m "Ella está bien."
    m "Simplemente sucede de vez en cuando."
    m 1a "Es por eso que siempre tengo un bocadillo en mi bolsa para ella."
    m 5a "¡De todos modos...!"
    m "¿Por qué no compartimos poemas ahora?"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
