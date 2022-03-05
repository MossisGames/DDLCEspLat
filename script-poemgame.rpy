init python:
    import random


    class PoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.glitch = glitch


    POEM_DISLIKE_THRESHOLD = 29
    POEM_LIKE_THRESHOLD = 45


    poem_lines="""#File format: word,sPoint,nPoint,yPoint

#Sayori's winning words
felicidad,3,2,1
tristeza,3,2,1
muerte,3,1,2
tragedia,3,1,2
soledad,3,1,2
amor,3,2,1
aventura,3,2,1
dulce,3,2,1
emoción,3,2,1
pirotecnia,3,2,1
romance,3,2,1
lágrimas,3,1,2
depresión,3,1,2
corazón,3,2,1
matrimonio,3,2,1
pasión,3,2,1
infancia,3,2,1
diversión,3,2,1
color,3,2,1
esperanza,3,1,2
amigos,3,2,1
familia,3,2,1
fiesta,3,2,1
vacaciones,3,2,1
perezoso,3,2,1
sueño,3,1,2
dolor,3,1,2
fiesta,3,2,1
cama,3,2,1
pluma,3,2,1
vergüenza,3,1,2
miedo,3,1,2
cálido,3,2,1
flor,3,2,1
comodidad,3,2,1
baile,3,2,1
canto,3,2,1
llanto,3,1,2
risa,3,2,1
oscuridad,3,1,2
soleado,3,2,1
nube,3,2,1
calma,3,1,2
tonto,3,2,1
volando,3,2,1
maravilloso,3,2,1
incorrespondido,3,1,2
rosa,3,1,2
juntos,3,2,1
promesa,3,2,1
encanto,3,2,1
belleza,3,2,1
animar,3,2,1
sonrisa,3,2,1
roto,3,1,2
precioso,3,2,1
oración,3,1,2
torpe,3,2,1
perdonar,3,1,2
naturaleza,3,2,1
océano,3,2,1
deslumbrar,3,2,1
especial,3,2,1
música,3,2,1
suerte,3,2,1
desgracia,3,1,2
ruidoso,3,2,1
pacífico,3,1,2
alegría,3,1,2
atardecer,3,2,1
luciérnagas,3,2,1
arcoíris,3,2,1
lastimado,3,1,2
juego,3,2,1
chispa,3,2,1
cicatrices,3,1,2
vacío,3,1,2
increíble,3,2,1
pena,3,1,2
abrazo,3,1,2
extraordinario,3,2,1
impresionante,3,2,1
derrota,3,1,2
desesperanzado,3,1,2
miseria,3,1,2
tesoro,3,2,1
dicha,3,2,1
recuerdos,3,2,1

#Natsuki's words
lindo,2,3,1
esponjoso,2,3,1
puro,1,3,2
caramelos,2,3,1
compras,2,3,1
cachorro,2,3,1
gatito,2,3,1
nubes,2,3,1
labial,1,3,2
parfait,2,3,1
fresa,2,3,1
rosado,2,3,1
chocolate,2,3,1
latido,1,3,2
beso,1,3,2
melodía,2,3,1
cinta,2,3,1
nervioso,2,3,1
doki-doki,2,3,1
kawaii,2,3,1
falda,2,3,1
mejillas,2,3,1
email,2,3,1
pegajoso,2,3,1
rebotable,2,3,1
brillante,2,3,1
mordisquear,2,3,1
fantasía,1,3,2
azúcar,2,3,1
risita,2,3,1
malvavisco,2,3,1
saltito,2,3,1
saltote,2,3,1
paz,2,3,1
rodar,2,3,1
giro,2,3,1
piruleta,2,3,1
poof,2,3,1
burbujas,2,3,1
susurro,2,3,1
verano,2,3,1
cascada,1,3,2
bikini,2,3,1
vainilla,2,3,1
auriculares,2,3,1
juegos,2,3,1
calcetines,2,3,1
cabello,2,3,1
parque,2,3,1
camisón,1,3,2
manta, 1,3,2
leche,2,3,1
puchero,2,3,1
ira,2,3,1
papá,2,3,1
valentín,2,3,1
ratón,1,3,2
silbato,2,3,1
boop,2,3,1
conejito,2,3,1
anime,2,3,1
saltar,2,3,1

#Yuri's words
determinación,1,1,3
suicidio,2,1,3
imaginación,2,1,3
reservado,2,1,3
vitalidad,1,1,3
existencia,2,1,3
refulgente,1,1,3
carmesí,1,1,3
torbellino,1,1,3
imagen residual,1,1,3
vértigo,1,1,3
desorientado,1,1,3
esencia,2,1,3
ambiente,2,1,3
estrellas,2,1,3
desorden,1,1,3
contaminación,1,1,3
intelectual,1,1,3
análisis,1,1,3
entropía,1,1,3
vivaz,1,1,3
asombroso,2,1,3
incongruente,1,1,3
furia,2,1,3
celestial,2,1,3
masacre,2,1,3
filosofía,1,1,3
voluble,1,1,3
tenaz,1,1,3
aura,2,1,3
inestable,1,1,3
infierno,2,1,3
incapaz,2,1,3
destino,2,1,3
infalible,1,1,3
agonizante,2,1,3
varianza,1,1,3
incontrolable,2,1,3
extrema,1,1,3
huir,2,1,3
sueño,2,2,3
desastre,2,1,3
vívido,2,1,3
vibrante,1,2,3
pregunta,1,2,3
inflamación,2,1,3
juicio,1,1,3
jaula,1,2,3
explotar,1,2,3
placer,1,2,3
lujuria,1,2,3
sensación,1,2,3
clímax,1,2,3
electricidad,1,2,3
repudiar,1,1,3
despreciar,2,1,3
infinito,2,1,3
eternidad,2,1,3
tiempo,2,1,3
universo,2,1,3
interminable,2,1,3
lluvioso,2,1,3
codiciar,1,1,3
desenfrenado,1,1,3
paisaje,2,1,3
retrato,2,1,3
viaje,2,1,3
pobre,1,1,3
ansiedad,2,1,3
aterrador,2,1,3
horror,2,1,3
melancolía,2,1,3
perspicacia,2,1,3
expiar,2,1,3
respirar,1,2,3
cautivo,2,1,3
deseo,1,2,3
cementerio,2,1,3"""
    full_wordlist = []  

    for line in poem_lines.splitlines():
        
        line = line.strip()
        
        if line == '' or line[0] == '#': continue
        
        
        x = line.split(',')
        full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3])))

    seen_eyes_this_chapter = False
    sayoriTime = renpy.random.random() * 4 + 4
    natsukiTime = renpy.random.random() * 4 + 4
    yuriTime = renpy.random.random() * 4 + 4
    monikaTime = renpy.random.random() * 4 + 4
    sayoriPos = 0
    natsukiPos = 0
    yuriPos = 0
    monikaPos = 0
    sayoriOffset = 0
    natsukiOffset = 0
    yuriOffset = 0
    monikaOffset = 0
    sayoriZoom = 1
    natsukiZoom = 1
    yuriZoom = 1
    monikaZoom = 1

    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMonika(trans, st, at):
        if st > monikaTime:
            global monikaTime
            monikaTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0

    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0

    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0

    def randomMoveMonika(trans, st, at):
        global monikaPos
        global monikaOffset
        global monikaZoom
        if st > .16:
            if monikaPos > 0:
                monikaPos = renpy.random.randint(-1,0)
            elif monikaPos < 0:
                monikaPos = renpy.random.randint(0,1)
            else:
                monikaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaPos > 5: monikaPos *= -1
            return None
        if monikaPos > 0:
            trans.xzoom = -1
        elif monikaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaPos
        monikaOffset = trans.xoffset
        monikaZoom = trans.xzoom
        return 0



label poem(transition=True):
    stop music fadeout 2.0
    if persistent.playthrough == 3:
        scene bg notebook-glitch
    else:
        scene bg notebook
    show screen quick_menu
    if persistent.playthrough == 3:
        show m_sticker at sticker_mid
    else:
        if persistent.playthrough == 0:
            show s_sticker at sticker_left
        show n_sticker at sticker_mid
        if persistent.playthrough == 2 and chapter == 2:
            show y_sticker_cut at sticker_right
        else:
            show y_sticker at sticker_right
        if persistent.playthrough == 2 and chapter == 2:
            show m_sticker at sticker_m_glitch
    if transition:
        with dissolve_scene_full
    if persistent.playthrough == 3:
        play music ghostmenu
    else:
        play music t4
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    if persistent.playthrough == 0 and chapter == 0:
        call screen dialog("¡Es momento de escribir un poema!\n\nElige palabras que le gustarán a tu \nmiembro favorito. ¡Algo bueno pasará\ncon quien le guste más tu poema!", ok_action=Return())
    python:
        poemgame_glitch = False
        played_baa = False
        progress = 1
        numWords = 20
        sPointTotal = 0
        nPointTotal = 0
        yPointTotal = 0
        wordlist = list(full_wordlist)

        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1





        while True:
            ystart = 160
            if persistent.playthrough == 2 and chapter == 2:
                pstring = ""
                for i in range(progress):
                    pstring += "1"
            else:
                pstring = str(progress)
            ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
            for j in range(2):
                if j == 0: x = 440
                else: x = 680
                ui.vbox()
                for i in range(5):
                    if persistent.playthrough == 3:
                        s = list("Monika")
                        for k in range(6):
                            if random.randint(0, 4) == 0:
                                s[k] = ' '
                            elif random.randint(0, 4) == 0:
                                s[k] = random.choice(nonunicode)
                        word = PoemWord("".join(s), 0, 0, 0, False)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        word = PoemWord(glitchtext(80), 0, 0, 0, True)
                    else:
                        word = random.choice(wordlist)
                        wordlist.remove(word)
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                ui.close()
            
            t = ui.interact()
            if not poemgame_glitch:
                if t.glitch:
                    poemgame_glitch = True
                    renpy.music.play(audio.t4g)
                    renpy.scene()
                    renpy.show("white")
                    renpy.show("y_sticker glitch", at_list=[sticker_glitch])
                elif persistent.playthrough != 3:
                    renpy.play(gui.activate_sound)
                    if persistent.playthrough == 0:
                        if t.sPoint >= 3:
                            renpy.show("s_sticker hop")
                        if t.nPoint >= 3:
                            renpy.show("n_sticker hop")
                        if t.yPoint >= 3:
                            renpy.show("y_sticker hop")
                    else:
                        if persistent.playthrough == 2 and chapter == 2 and random.randint(0,10) == 0: renpy.show("m_sticker hop")
                        elif t.nPoint > t.yPoint: renpy.show("n_sticker hop")
                        elif persistent.playthrough == 2 and not persistent.seen_sticker and random.randint(0,100) == 0:
                            renpy.show("y_sticker hopg")
                            persistent.seen_sticker = True
                        elif persistent.playthrough == 2 and chapter == 2: renpy.show("y_sticker_cut hop")
                        else: renpy.show("y_sticker hop")
            else:
                r = random.randint(0, 10)
                if r == 0 and not played_baa:
                    renpy.play("gui/sfx/baa.ogg")
                    played_baa = True
                elif r <= 5: renpy.play(gui.activate_sound_glitch)
            sPointTotal += t.sPoint
            nPointTotal += t.nPoint
            yPointTotal += t.yPoint
            progress += 1
            if progress > numWords:
                break

        if persistent.playthrough == 0:
            
            if chapter == 1:
                exec(ch1_choice[0] + "PointTotal += 5")
            
            unsorted_pointlist = {"sayori": sPointTotal, "natsuki": nPointTotal, "yuri": yPointTotal}
            pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)
            
            
            poemwinner[chapter] = pointlist[2]
        else:
            if nPointTotal > yPointTotal: poemwinner[chapter] = "natsuki"
            else: poemwinner[chapter] = "yuri"


        exec(poemwinner[chapter][0] + "_appeal += 1")


        if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
        elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
        if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal[chapter] = -1
        elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal[chapter] = 1
        if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal[chapter] = -1
        elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal[chapter] = 1


        exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")

    if persistent.playthrough == 2 and persistent.seen_eyes == None and renpy.random.randint(0,5) == 0:
        $ seen_eyes_this_chapter = True
        $ quick_menu = False
        play sound "sfx/eyes.ogg"
        $ persistent.seen_eyes = True
        $ renpy.save_persistent()
        stop music
        scene black with None
        show bg eyes_move
        $ pause(1.2)
        hide bg eyes_move
        show bg eyes
        $ pause(0.5)
        hide bg eyes
        show bg eyes_move
        $ pause(1.25)
        hide bg eyes with None
        $ quick_menu = True
    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    $ pause(1.0)
    return

image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
image bg eyes:
    "images/bg/eyes.png"

image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset yuriOffset xzoom yuriZoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
