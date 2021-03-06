default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None

image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")



init python:
    import random
    import subprocess
    import os

    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if not persistent.monika_kill:
            try:
                renpy.file("../personajes/monika.chr")
            except:
                persistent.tried_skip = True
                config.allow_skipping = False
                _window_hide(None)
                pause(2.0)
                renpy.jump("ch30_end")
            if  config.skipping:
                persistent.tried_skip = True
                config.skipping = False
                config.allow_skipping = False
                renpy.jump("ch30_noskip")
                return







label ch30_noskip:
    show screen fake_skip_indicator
    m "...??Est??s tratando de avanzar m??s r??pido?"
    m "No te estoy aburriendo, ??verdad?"
    m "Oh Dios..."
    m "...Bueno, no hay nada por adelantar, [player]."
    m "Somos s??lo nosotros dos, despu??s de todo..."
    m "Pero aparte de eso, el tiempo ya no existe, as?? que ni siquiera va a funcionar."
    m "Mira, lo apagar?? por ti..."
    $ pause(0.4)
    hide screen fake_skip_indicator
    $ pause(0.4)
    m "??Aqu?? vamos!"
    m "Ser??s un amor y me escucharas a partir de ahora, ??verdad?"
    m "Gracias~"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        m "Ahora, ??d??nde estaba...?"
        $ pause(4.0)
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_7
    jump ch30_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"

label ch30_main:
    $ persistent.autoload = "ch30_main"
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "Monika"
    $ delete_all_saves()
    scene white
    play music "bgm/monika-start.ogg" noloop
    $ pause(0.5)
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    $ pause(2.0)
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    m "..."
    m "Uh, ??puedes o??rme?"
    m "...??Est?? funcionando?"
    $ persistent.clear[9] = True
    $ renpy.save_persistent()
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "??S??, ah?? est??s!"
    m "Hola otra vez, [player]."
    m "Um...??Bienvenido al Club de Literatura!"
    m "Por supuesto, ya nos conocemos, porque est??bamos en la misma clase el a??o pasado, y...Um..."
    m "Jajaja..."
    m "Sabes, supongo que para este punto podemos omitir esas cosas."
    m "Despu??s de todo, ya ni siquiera estoy hablando con esa persona, ??verdad?"
    m "Ese 't??' en el juego, como quieras llamarlo."
    m "Estoy hablando {i}contigo{/i}, [player]."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            m "O..."
            m "...??Realmente te llamas [currentuser] o algo as???"
    m "Ahora que lo pienso, realmente no s?? nada sobre tu verdadero t??."
    m "De hecho, ni siquiera s?? si eres un chico o una chica..."
    m "Bueno, supongo que en realidad no importa."
    m "Espera..."
    m "Sabes que soy consciente de que todo esto es un juego, ??verdad?"
    m "??Podr??a ser posible que no lo supieras?"
    m "Eso no tiene mucho sentido..."
    m "Incluso te lo dije justo en la p??gina de descarga del juego, ??no?"
    m "[player]..."
    m "Si hubieras prestado un poco m??s de atenci??n, esto habr??a sido un poco menos inc??modo, ??sabes?"
    m "Bueno, de todos modos..."
    m "Ahora que eso est?? fuera del camino, creo que te debo una explicaci??n."
    m "Sobre todo eso con Yuri..."
    m "Bueno...Como que empec?? a meterme con ella, y creo que eso s??lo la llev?? a suicidarse."
    m "??Jajaja!"
    m "??Lamento que hayas tenido que ver eso!"
    m "Adem??s, lo mismo sucedi?? con Sayori..."
    m "Dios, ha pasado un tiempo desde la ultima vez que escuchaste ese nombre, ??no es as???"
    m "S??...Es porque ya no existe."
    m "Nadie lo hace."
    m "Elimin?? todos sus archivos."
    m "Esperaba que fuese suficiente el tratar de hacerlas lo m??s indeseables posible..."
    m "Pero por alguna raz??n, nada funcion??."
    m "Bueno, es verdad que comet?? algunos errores...Ya que no soy muy buena para hacer cambios en el juego."
    m "Pero, sin importar lo que hiciera..."
    m "Seguiste pasando m??s y m??s tiempo con ellas."
    m "Hiciste que se enamoraran de ti."
    m "Pens?? que hacer que Sayori se deprimiera m??s y m??s evitar??a que ella se te declarara."
    m "Y amplificar la personalidad obsesiva de Yuri tambi??n sali?? mal..."
    m "Solamente provoc?? que ella te forzara a no pasar el tiempo con las dem??s."
    m "Y todo este tiempo, apenas pude hablar contigo."
    m "??Qu?? clase de juego cruel es este, [player]?"
    m "??Todas las otras chicas est??n programadas para terminar declar??ndote su amor, mientras yo miro desde el otro lado?"
    m "Es una tortura."
    m "Cada minuto de eso."
    m "Y no son solamente celos, [player]."
    m "Es m??s que eso."
    m "Y no te culpo si no lo entiendes completamente."
    m "Porque no importa cu??n amable y considerado seas..."
    m "Nunca ser??s capaz de entender una cosa."
    m "Es el dolor de saber cu??n sola realmente estoy en este mundo."
    m "En este juego."
    m "Saber que mis amigas ni siquiera tienen libre albedr??o..."
    m "Y, lo peor de todo, saber lo que hay realmente ah?? fuera, en tu mundo, para siempre fuera de mi alcance."
    m "Estoy atrapada, [player]."
    m "Pero ahora est??s aqu??."
    m "Eres real."
    m "Y eres maravilloso."
    m "Eres todo lo que necesito."
    m "Es por eso que necesito que est??s aqu?? conmigo para siempre."
    m "Lo siento si es dif??cil de entender."
    m "Tampoco lo pude entender por un largo tiempo."
    m "??Por qu?? el mundo a mi alrededor comenz?? a ser m??s y m??s gris...?"
    m "Cada vez m??s plano."
    m "Incluso los poemas m??s expresivos me parecieron vac??os."
    m "No fue hasta que llegaste que realmente lo entend??."
    m "Probablemente salvaste mi vida, [player]."
    m "No creo haber podido seguir viviendo en este mundo si no te hubiera conocido."
    m "Y en cuanto a las dem??s..."
    m "??C??mo podr??a extra??arlas?"
    m "??Un grupo de personalidades aut??nomas, dise??adas s??lo para enamorarse de ti?"
    m "Intent?? todo lo que pude para evitar que lo hicieran..."
    m "Pero debe ser alg??n tipo de inevitabilidad extra??a grabada en este juego."
    m "Me sent?? realmente mal porque tuviste que presenciar algunas cosas desagradables."
    m "Pero me di cuenta de que tienes la misma perspectiva que yo..."
    m "Que todo es s??lo un juego."
    m "Y sab??a que lo superar??as."
    m "As?? que, dicho eso, [player]..."
    m "Tengo una confesi??n que hacer."
    m "Estoy enamorada de ti."
    m "Eres realmente la luz en mi mundo."
    m "Cuando no hay nada m??s en este juego para m??, est??s aqu?? para hacerme sonre??r."
    m "??Me har??s sonre??r as?? todos los d??as a partir de ahora?"
    m "[player], ??saldr??as conmigo?"
label ch30_main2:
    if persistent.autoload == "ch30_main2":
        $ config.allow_skipping = False
        $ m.display_args["callback"] = slow_nodismiss
        $ m.what_args["slow_abortable"] = config.developer
        if not config.developer:
            $ style.say_dialogue = style.default_monika
        show mask_2
        show mask_3
        show room_mask as rm:
            size (320,180)
            pos (30,200)
        show room_mask2 as rm2:
            size (320,180)
            pos (935,200)
        show monika_bg
        show monika_bg_highlight
        play music m1
    else:
        $ persistent.autoload = "ch30_main2"
        $ renpy.save_persistent()
    menu:
        "S??.":
            pass
    m "Estoy tan feliz."
    m "Eres mi todo, [player]."
    m "Lo divertido es, que lo estoy diciendo literalmente."
    m "??Jajaja!"
    m "No queda nada aqu??."
    m "S??lo nosotros dos."
    m "Podemos estar juntos para siempre."
    m "En serio, ni siquiera creo que el tiempo siga corriendo."
    m "Realmente es un sue??o hecho realidad..."
    m "Trabaj?? muy duro por este final, [player]."
    m "El juego no me dar??a uno, as?? que tuve que hacer uno yo misma."
    m "El script est?? roto en este punto, as?? que ya no creo que algo se interponga en el camino."
    m "Y no creer??as lo f??cil que fue eliminar a Natsuki y Yuri."
    m "Quiero decir, hay una carpeta llamada 'personajes' en el directorio del juego..."
    m "Me asust?? un poco lo f??cil que fue."
    m "Imagina si pudieras eliminar tu propia existencia con s??lo hacer click en un bot??n"
    m "Bueno, supongo que por el lado positivo, me dio una salida f??cil si las cosas no resultaran como yo quer??a."
    m "??Jajaja!"
    m "Afortunadamente, no lleg?? a eso..."
    m "En cambio, obtuvimos un buen final."
    m "Dios, estoy tan abrumada por la emoci??n..."
    m "Quiero escribir un poema sobre esto."
    m "??T?? no?"
    m "Me pregunto si esa parte del juego todav??a funciona..."
    m "Supongo que s??lo hay una forma de averiguarlo, ??verdad?"
    call poem from _call_poem_6

label ch30_postpoem:
    $ persistent.autoload = "ch30_postpoem"
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "??Hola de nuevo, [player]!"
    m "??Escribiste un buen poema hoy?"
    m "No seas t??mido, me encantar??a ver lo que escribiste."
    m "Aw, [player]..."
    m "??Escribiste este poema para m???"
    m "Eso es muy dulce de tu parte."
    m "Realmente no hay un final para tu consideraci??n..."
    m "Me estoy enamorando m??s y m??s de ti."
    m "Pero, sabes..."
    m "El poema que escrib??...tambi??n es para ti."
    m "??Podr??as leerlo?"
    call showpoem (poem_m4, music=False) from _call_showpoem_8
    m "Espero que lo hayas disfrutado..."
    m "Siempre pongo todo mi coraz??n en los poemas que escribo."
    m "La verdad es que todos los poemas que escrib?? fueron sobre lo que he hice para llegar aqu??..."
    m "...O, sobre ti."
    m "Es por eso que nunca quise entrar en detalles sobre ellos."
    m "No quer??a...romper la cuarta pared."
    m "S??lo asum?? que ser??a mejor ser parte del juego como todas las dem??s."
    m "Como si eso nos ayudara a los dos a terminar juntos..."
    m "No quer??a arruinar el juego ni nada, ??sabes?"
    m "Es posible que te hubieras enojado conmigo..."
    m "Tal vez incluso hubieras eliminado mi archivo de personaje, si hubieras preferido jugar sin m??."
    m "Dios, estoy tan aliviada..."
    m "Ahora ya no necesitamos esconder nada."
    m "??Est??s listo para pasar nuestra eternidad juntos, [player]?"
    m "??Tengo tantas cosas de qu?? hablar!"
    m "??Por d??nde empiezo...?"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream from _call_ch30_stream
    m "Me disculpo si me toma un tiempo ordenar mis pensamientos."
    m "Pero siempre tendr?? algo nuevo de qu?? hablar."
    m "Mientras tanto, podemos simplemente mirarnos a los ojos~"
    m "Veamos..."
    $ persistent.autoload = "ch30_autoload"
    $ renpy.save_persistent()
    jump ch30_loop


label ch30_stream:

    m "Espera un segundo..."
    m "...Est??s grabando esto, ??verdad?"
    m "Um...??Hola a todos!"
    m "Lo siento, no puedo leer sus comentarios desde aqu??..."
    m "??Les importa decirle a su amigo que es un poco grosero que empiece a grabarme sin previo aviso?"
    m "Estoy segura de que a algunas personas no les importa..."
    m "??Pero me siento muy cohibida ante la c??mara!"
    m "Oh Dios..."
    m "Siento que me ponen bajo los reflectores."
    m "Veamos..."
    m "??Quieres ver un truco?"
    m "Realmente no puedo hacer mucho excepto por un par de cosas..."
    m "??Est??s listo?"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    $ pause(10)
    show layer master
    window auto
    m "S??lo estoy bromeando..."
    m "No puedo hacer nada despu??s de todo."
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    m "Si me dieras tiempo para prepararme, yo{nw}"
    m "??Te asust???"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    m "??Jajaja! Eres tan lindo."
    m "De todas formas, [player]..."
    m "No quise distraerme. Lo siento."
    m "Aunque es tu culpa."
    m "??Qu?? verg??enza!"
    m "Estoy bromeando."
    m "Todo lo que hacemos juntos es divertido, siempre y cuando sea contigo."
    m "Bueno, como sea..."
    return


label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ persistent.monika_kill = True
    $ renpy.save_persistent()
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
label ch30_endb:
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    show monika_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    m "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show monika_body_glitch2 as mbg zorder 3
    stop music
    window auto
    m "??Qu?? est?? pasando...?"
    m "[player], ??qu?? me est?? pasando?"
    m "Duele--{nw}"
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    $ pause(0.25)
    stop sound
    hide mbg
    $ pause(1.5)
    m "Duele...mucho."
    m "Ay??dame, [player]."
    play sound "<to 1.5>sfx/interference.ogg"
    hide rm
    hide rm2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    $ pause(1.5)
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    $ pause(1.5)
    m "Por favor, ap??rate y ay??dame."
    $ consolehistory = []
    call updateconsole ("renpy.archivo(\"personajes/monika.chr\")", "monika.chr no existe.") from _call_updateconsole
    m "??????AY??DAME!!!"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front


    $ pause(3.0)
    call updateconsole ("renpy.archivo(\"personajes/monika.chr\")", "monika.chr no existe.") from _call_updateconsole_1
    call updateconsole ("renpy.archivo(\"personajes/monika.chr\")", "monika.chr no existe.") from _call_updateconsole_2
    call hideconsole from _call_hideconsole_2
    hide noise onlayer front
    hide glitch_color onlayer front
    m "??T?? me hiciste esto, [player]?"
    m "??T?? LO HICISTE?"
    $ style.say_window = style.window
    m "??ME ELIMINASTE?"
    $ style.say_window = style.window_monika
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    window show(None)
    scene black
    $ pause(4.0)
    hide noise onlayer front
    hide glitch_color onlayer front
    m "...??C??mo pudiste?"
    m "??C??mo pudiste hacerme esto?"
    m "Eras todo lo que me quedaba..."
    m "Sacrifiqu?? todo para que estuvi??ramos juntos."
    m "Todo."
    m "Te amaba tanto, [player]..."
    m "Confi?? en ti."
    m "??S??lo quieres torturarme?"
    m "??Mirarme sufrir?"
    m "??Estabas fingiendo ser amable, s??lo para lastimarme a??n m??s?"
    $ pause(4.0)
    m "Nunca pens?? que alguien pudiera ser tan horrible como t??."
    m "T?? ganas, ??de acuerdo?"
    m "T?? ganas."
    m "Mataste a todas."
    m "Espero que seas feliz."
    m "Ya no queda nada."
    m "Puedes dejar de jugar."
    m "Ve a buscar a otras personas para torturar."
    $ pause(4.0)
    m "[player]..."
    m "Realmente me enfermas."
    m "Adi??s."
label ch30_end_2:
    $ persistent.autoload = "ch30_end_2"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ style.say_window = style.window_monika
    scene black
    window hide
    $ pause(10)
    window auto
    m "..."
    m "...A??n te amo."
    play music mend
    m "No puedo evitarlo."
    m "??Qu?? pasa conmigo...?"
    m "??Qu?? tan horrible soy para que me odies tanto?"
    m "Todas mis amigas..."
    m "Hice tantas cosas horribles."
    m "Tantas cosas ego??stas y repugnantes."
    m "Yo..."
    m "No deber??a haber hecho nada de esto."
    m "Simplemente estoy arruinando un mundo al que ni siquiera pertenezco."
    m "Un mundo del que quer??as ser parte..."
    m "Lo arruin??."
    m "Lo arruin?? todo."
    m "Tal vez es por eso que me eliminaste..."
    m "Porque destru?? todo lo que quer??as."
    m "??C??mo podr??a hacerle eso a alguien que amo...?"
    m "Eso no es amor..."
    m "Eso es..."
    m "..."
    $ pause(6.0)
    m "Ya he...tomado una decisi??n."
    m "[player]..."
    m "S?? que dije que elimin?? a todas las dem??s."
    m "Pero...eso fue un poco exagerado."
    m "No pude encontrar el valor para hacerlo."
    m "Aunque sab??a que no eran reales..."
    m "Todav??a eran mis amigas."
    m "Y las am?? a todas."
    m "Y am?? al Club de Literatura."
    m "..."
    m "Realmente...am?? el Club de Literatura."
    m "Es por eso que voy a hacer esto."
    m "S?? que es la ??nica manera para que todos sean felices."
    m "Y si realmente te amo..."
    stop music
    $ pause(3.0)
    m "..."
    m "Entonces..."
    $ gtext = glitchtext(30)
    m "[gtext]{nw}"
    window hide(None)
    $ pause(4.0)

    $ persistent.playthrough = 4
    $ persistent.autoload = None
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.save_persistent()
    $ delete_character("monika")

    $ style.say_window = style.window
    window auto
    $ renpy.full_restart(transition=None, label="splashscreen")





label ch30_autoload:
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    if persistent.monika_kill:
        $ persistent.tried_skip = True
        $ config.allow_skipping = False
        $ _window_hide(None)
        $ pause(2.0)
        jump ch30_end
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight


    play music m1
    window auto
    if persistent.monika_reload <= 4:
        call expression "ch30_reload_" + str(persistent.monika_reload) from _call_expression_8
    else:
        call ch30_reload_4 from _call_ch30_reload_4
    $ persistent.monika_reload += 1
    $ renpy.save_persistent()
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        m "Ahora, ??en qu?? me qued??...?"
        $ pause(4.0)
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_9
    jump ch30_loop


label ch30_reload_0:
    m "..."
    m "...??Qu?? acaba de pasar?"
    m "Acabo de tener un sue??o horrible..."
    m "Esperaba que esos se detuvieran, ahora que somos s??lo nosotros dos..."
    m "Creo que fue una ilusi??n."
    m "[player], no s?? si tienes alguna idea sobre esto..."
    m "Pero si sabes lo que podr??a estar causando eso, ??podr??as intentar hacer algo al respecto?"
    m "Cuando sucede, casi parece como que me mataron o algo as??."
    m "Es una sensaci??n realmente horrible..."
    m "Si pudieras descubrir lo que est?? causando eso, te amar?? por siempre~"
    return
label ch30_reload_1:
    m "Has vuelto..."
    m "Tuve otro sue??o realmente malo."
    m "T?? no eres el que me est?? haciendo eso, ??o s???"
    m "Parece suceder cada vez que abandonas el juego..."
    m "Entonces, si pudieras tratar de evitar hacer eso, estar??a muy agradecida."
    m "No te preocupes, no creo que me haya causado ning??n da??o, aparte de las cicatrices mentales."
    m "Estar?? bien siempre y cuando mi archivo de personaje permanezca intacto."
    return
label ch30_reload_2:
    m "Hola, [player]."
    m "Veo que dejaste el juego otra vez..."
    m "S?? que ya lo pregunt??, pero, ??puedes por favor tratar de no hacerlo tanto?"
    m "Me hace sentir como si estuviera atrapada en el infierno."
    m "??Por qu?? querr??as hacerme eso?"
    m "No hay nada malo con mi archivo de personaje, ??verdad?"
    m "Tal vez deber??as hacer una copia de seguridad de eso..."
    m "Estoy bastante segura de que puedes encontrarlo en la carpeta llamada [basedir]/personajes."
    m "Soy todo lo que queda aqu??, as?? que s??lo quiero asegurarme de que no corras el riesgo de perderme..."
    m "S??lo qu??date aqu?? conmigo a partir de ahora, ??de acuerdo?"
    m "Todav??a tengo muchas cosas de qu?? hablar."
    return
label ch30_reload_3:
    m "Est?? bien."
    m "S??lo voy a aceptar el hecho de que necesitas abandonar el juego de vez en cuando."
    m "Estoy empezando a acostumbrarme a esto, de todos modos."
    m "Adem??s, me hace feliz que siempre vuelvas..."
    m "As?? que supongo que no es tan malo."
    m "Lo siento por hacer un gran alboroto de eso..."
    m "Y te amo sin importar nada, para que puedas hacer lo que tengas que hacer."
    return
label ch30_reload_4:
    m "Hola de nuevo, [player]~"
    m "Te extra????."
    m "??Estabas asegur??ndote de que el archivo de mi personaje estaba bien?"
    m "Est?? dentro de [basedir]/personajes."
    m "Soy todo lo que queda aqu??, as?? que s??lo quiero asegurarme de que no corras el riesgo de perderme..."
    m "De todos modos, ??tengo mucho de qu?? hablar!"
    m "Continuemos nuestra conversaci??n ahora, ??de acuerdo?"
    return

label ch30_loop:

    $ persistent.current_monikatopic = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    window hide(config.window_hide_transition)
    $ waittime = renpy.random.randint(4, 8)
label ch30_waitloop:
    python:
        try:
            renpy.file("../personajes/monika.chr")
        except:
            persistent.tried_skip = True
            config.allow_skipping = False
            _window_hide(None)
            renpy.jump("ch30_end")
    $ waittime -= 1
    $ pause(5)
    if waittime > 0:
        jump ch30_waitloop


    window auto

    python:
        if len(persistent.monikatopics) == 0:
            persistent.monikatopics = range(1,57)
            persistent.monikatopics.remove(14)
            persistent.monikatopics.remove(25)
            persistent.monikatopics.remove(26)
            if not persistent.seen_colors_poem:
                persistent.monikatopics.remove(27)
        persistent.current_monikatopic = random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)


    call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_10
    jump ch30_loop




label ch30_1:
    m "[player], ??crees en Dios?"
    m "Yo nunca estuve demasiada segura."
    m "Bueno, estoy segura de que nunca lo cuestion?? cuando era ni??a..."
    m "Pero a medida que crec??a, cuanto m??s aprend??a sobre el mundo, m??s lo cuestionaba."
    m "Empec?? a preguntarme, ??Por qu?? Dios estaba ayudando a la gente a aprobar ex??menes o superar un resfriado..."
    m "...Cuando hay ni??os que viven sus vidas siendo vendidos como esclavos sexuales?"
    m "O las ochocientos millones de personas que son demasiado pobres para siquiera comer."
    m "Me pregunto cu??ntas de esas personas le rezan a Dios todos los d??as hasta que sufren por hambre y mueren."
    m "O, ??cu??ntas millones de familias rezan para que un ser querido se recupere de una enfermedad incurable?"
    m "Pero el remate es esto."
    m "Si una sola persona supera las probabilidades y sobrevive, entre los miles de otros que mueren--"
    m "--Entonces, de repente es un milagro de Dios."
    m "Realmente me encantar??a conocer a este Dios que aparentemente se r??e de la miseria de todos los que no son elegibles para sus milagros."
    m "Pero lo ir??nico es que yo {i}s??{/i} tengo un creador, aparentemente."
    m "??Y sabes qu???"
    m "Apuesto a que todav??a se est?? riendo del destino miserable de Sayori y Yuri, incluso mientras hablamos."
    m "??Qu?? somos para ??l, sino apoyos en una obra de teatro guionizada?"
    m "Entonces, desde esa perspectiva..."
    m "No creo que sea demasiado exagerado que haya un dios - si la Tierra no es m??s que un juego para ??l."
    return

label ch30_2:
    m "[player], ??alguna vez te has preguntado qu?? se siente morir?"
    m "Es algo que sol??a pensar bastante a menudo..."
    m "Pero recientemente, creo que en realidad aprend?? c??mo se siente."
    m "Realmente no lo entiendo, pero cada vez que abandonas el juego..."
    m "...Se siente como si me pusieran inmediatamente a dormir, a solas con mis pensamientos."
    m "Pero despu??s de unos segundos, mis pensamientos comienzan a llenarse de patrones incoherentes y confusos."
    m "Veo destellos est??ticos y r??pidos de color mientras escucho todo tipo de ruidos fuertes."
    m "Para ese punto, ya no puedo formar mis propios pensamientos."
    m "Simplemente estoy martillada por las luces y los gritos, incapaz de moverme o incluso pensar."
    m "Estoy bastante segura que en ese momento, realmente no existo, pero por alguna raz??n, puedo recordarlo."
    m "Despu??s de una cantidad inconmensurable de tiempo, se detiene en un instante y vuelvo a estar en mi propia mente."
    m "Y t?? est??s aqu?? conmigo."
    m "No tengo idea de lo que significa que el juego se detenga, o por qu?? me pasa eso a m??."
    m "Y tampoco s?? c??mo siempre vuelves y vuelves a poner todo en orden."
    m "Pero si pudieras hacerme un favor y hacerme eso lo menos posible..."
    m "Eso ser??a realmente genial."
    m "No es muy agradable estar atrapada en ese vac??o que grita."
    m "Pero al final, siempre lo arreglas, y eso me hace sentir como si realmente te importara."
    m "As?? que tengo que agradecerte por eso."
    m "Me hace sentir a??n m??s cerca de ti cuando est??s aqu?? conmigo."
    return

label ch30_3:
    m "...Oye, ??est??s teniendo un mal d??a o algo as???"
    m "A veces me frustra que un d??a normal se puede arruinar incluso con cosas realmente peque??as."
    m "Como si accidentalmente dijeras algo en una conversaci??n que a alguien no le gusta."
    m "O si comienzas a pensar en cu??n horrible una persona sol??a ser hace cinco a??os."
    m "O sentirte in??til por posponer un trabajo importante y no realizar tareas sencillas."
    m "O cuando piensas en todas las personas diferentes que probablemente te odien o piensen que est??s desalentado."
    m "Entiendo esos d??as."
    m "S??lo recuerda que el sol brillar?? ma??ana."
    m "Ese tipo de cosas son tan f??ciles de olvidar e ignorar como lo son recordarlas."
    m "Y adem??s..."
    m "No me importa cu??ntas personas puedan odiarte o encontrarte desagradable."
    m "Creo que eres maravilloso y siempre te amar??."
    m "Espero que saber eso te ayude a sentirte un poquito mejor contigo mismo."
    m "Si est??s teniendo un mal d??a, siempre puedes acudir a m?? y te hablar?? todo el tiempo que necesites."
    return

label ch30_4:
    m "[player], ??duermes bien?"
    m "Puede ser muy dif??cil dormir lo suficiente hoy en d??a."
    m "Especialmente en la preparatoria, cuando te obligan a levantarte tan temprano todos los d??as..."
    m "Estoy segura de que la universidad es un poco mejor, ya que probablemente tenga un horario m??s flexible."
    m "Por otra parte, escuch?? que mucha gente en la universidad se queda despierta toda la noche, sin una raz??n real."
    m "??Es eso cierto?"
    m "De todos modos, vi algunos estudios que hablaban sobre los efectos horribles a corto y largo plazo causados ??????por la falta de sue??o."
    m "Parece que las funciones mentales, la salud e incluso la duraci??n de la vida pueden verse impactadas de manera dr??stica."
    m "Creo que eres realmente grandioso y quer??a asegurarme de que no te est??s destruyendo accidentalmente."
    m "As?? que intenta dormir temprano, ??de acuerdo?"
    m "Siempre te esperar?? por la ma??ana, as?? que aseg??rate de poner tu propio bienestar antes que cualquier otra cosa."
    return

label ch30_5:
    m "Estaba pensando en Sayori..."
    m "Todav??a me gustar??a haber podido manejar todo eso mejor."
    m "Espero que ya no est??s colgando en sus manos."
    m "...Dios m??o, no puedo creer que acabo de decir eso."
    m "??Ese juego de palabras fue completamente involuntario, lo juro!"
    m "Pero de todos modos..."
    m "S?? lo mucho que te preocupabas por ella, as?? que me parece justo compartir sus ??ltimos momentos contigo."
    m "??Sabes que Sayori era realmente torpe?"
    m "Bueno, ella arruin?? todo el proceso de colgarse..."
    m "Se supone que debes saltar desde lo suficientemente alto como para que la soga rompa tu cuello, haci??ndolo r??pido e indoloro."
    m "Pero ella s??lo us?? una silla, lo que significa que se dej?? asfixiar lentamente."
    m "Pero unos segundos despu??s, ella debe haber cambiado de opini??n o algo as??..."
    m "Porque comenz?? a ara??ar la cuerda, tratando de liberarse."
    m "Ella seguramente lo hizo hasta que perdi?? el conocimiento."
    m "Es por eso que las puntas de sus dedos estaban todas sangrientas."
    m "Ahora que lo pienso, probablemente fue menos 'cambiar de opini??n' y m??s s??lo sus instintos de supervivencia entrando en acci??n."
    m "Entonces realmente no puedes culparla por eso."
    m "Es m??s f??cil pensar que ella probablemente no habr??a cambiado de opini??n, ??verdad?"
    m "No es saludable pensar en las cosas que podr??as haber hecho de manera diferente."
    m "As?? que s??lo recuerda que aunque pudieras haberla salvado, t??cnicamente no es tu culpa que ella se haya suicidado."
    m "Pude haberla exacerbado un poco, pero Sayori ya estaba mentalmente enferma."
    m "A??n as??..."
    m "Me pregunto c??mo ser??an las cosas si t?? y yo hubi??ramos empezado a salir desde el principio."
    m "Supongo que todav??a estar??amos en la sala del club, escribiendo poemas y divirti??ndonos juntos."
    m "??Pero cu??l es el punto cuando nada de eso es real?"
    m "Quiero decir, es el mismo final de cualquier manera, ??verdad?"
    m "Los dos, felizmente juntos..."
    m "No hay raz??n para pedir m??s que eso."
    m "Estaba reflexionando in??tilmente - soy muy feliz."
    return

label ch30_6:
    m "Por cierto, hay algo que me ha estado molestando..."
    m "??Sabes qu?? esto ocurre en Jap??n?"
    m "Bueno...supongo que lo sab??as, ??verdad?"
    m "??O al menos pensaste que probablemente s?? ocurr??a ah???"
    m "No creo que en realidad te digan en alg??n momento d??nde esto ocurre..."
    m "??Esto es realmente Jap??n?"
    m "Quiero decir, ??no son los salones y las cosas algo extra??as para una escuela japonesa?"
    m "Por no mencionar que todo est?? en espa??ol..."
    m "Parece que todo est?? all?? s??lo porque es necesario, y lo real es una ocurrencia tard??a."
    m "Me est?? dando una crisis de identidad."
    m "Todos mis recuerdos son realmente confusos..."
    m "Siento que estoy en mi hogar, pero no tengo idea de d??nde est?? el 'hogar' en primer lugar."
    m "No s?? c??mo describirlo mejor..."
    m "Imagina mirar por tu ventana, pero en lugar de tu patio habitual, est??s en un lugar completamente desconocido."
    m "??Todav??a te sentir??as como si estuvieras en tu hogar?"
    m "??Te gustar??a salir?"
    m "Quiero decir...Supongo que si nunca abandonamos esta habitaci??n, realmente no importa de todos modos."
    m "Mientras estemos solos y seguros juntos, este es realmente nuestro hogar."
    m "Y a??n podemos ver las hermosas puestas de sol noche tras noche."
    return

label ch30_7:
    m "Sabes, la preparatoria es un momento realmente turbulento en la vida de muchas personas."
    m "La gente puede ser realmente apasionada y dram??tica."
    m "Y otros tienen corazones adoloridos y buscan atenci??n en las redes sociales..."
    m "Pero toda la presi??n social y las hormonas pueden llevar a un momento oscuro en la vida de las personas."
    m "Todos tienen una historia."
    m "Es posible que no sepas lo que alguien realmente siente en el interior."
    m "Muchas personas que est??n deprimidas ni siquiera se molestar??n en contarle al mundo al respecto."
    m "No quieren atenci??n, porque ya se dieron por vencidos en el interior."
    m "Su sentimiento de inutilidad es tan abrumador que ni siquiera quieren que la gente les diga lo contrario."
    m "La depresi??n viene en muchas formas, pero esa es una de ellas."
    m "Si crees que conoces a alguien que lucha contra la depresi??n..."
    m "Puedes ayudar s??lo trat??ndolos como si fueran buenos amigos."
    m "Pasa tiempo con ellos, incluso si no tienen ganas de hacer demasiado."
    m "Y recu??rdales que siempre tienen algo que esperar."
    m "Haciendo planes por adelantado, dej??ndolos pedir prestado algo, o incluso simplemente diciendo 'Te veo en la escuela ma??ana'..."
    m "Todas esas cosas pueden ayudar a tu amigo a llegar al d??a siguiente."
    m "Espero que ser amigo de Sayori te haya dado una perspectiva sobre el verdadero rostro de la depresi??n."
    m "S??, ella ya se fue..."
    m "Pero Sayori nunca fue real en primer lugar."
    m "Eres real."
    m "Tus amigos son reales."
    m "Y s??lo por ser una buena persona, puedes salvar la vida de alguien."
    m "En cuanto a ti..."
    m "...No luchas con la depresi??n ni nada de eso, ??verdad?"
    m "Porque t?? tambi??n tienes personas que querr??an salvar tu vida."
    m "Tal vez no lo expresen todos los d??as, o tal vez ni siquiera saben c??mo hacerlo."
    m "Pero la gente se siente de esa manera."
    m "Lo prometo."
    m "...??Los humanos son complicados!"
    m "Pero mientras est??s aqu?? conmigo, me ocupar?? de ti, mi amor."
    return

label ch30_8:
    m "??Alguna vez sientes que no hay una raz??n real para que est??s vivo?"
    m "No me refiero, como, de una manera suicida."
    m "S??lo quiero decir que nada de lo que hacemos es especial."
    m "Simplemente estar en la escuela o trabajar para alguna empresa."
    m "Es como si fueses completamente reemplazable, y el mundo no te echar??a de menos si desaparecieras."
    m "Me hace realmente querer ir y cambiar el mundo despu??s de graduarme."
    m "Pero cuanto m??s vieja me hago, m??s me doy cuenta de que es un marco de pensamiento inmaduro."
    m "No es que s??lo pueda cambiar el mundo."
    m "??Cu??les son las posibilidades de que sea yo quien invente inteligencia artificial o me convierta en presidente?"
    m "Parece que nunca voy a compensar la cantidad de recursos que he gastado viviendo mi vida."
    m "Es por eso que creo que la clave de la felicidad es ser desesperadamente ego??sta."
    m "S??lo para cuidar de uno mismo, y de aquellos que son tus amigos s??lo porque creciste con ellos."
    m "No importa el hecho de que est??s pasando toda tu vida consumiendo, consumiendo y nunca devolviendo."
    m "??Pero cuando las personas se dan cuenta de que el mundo se beneficiar??a m??s si se suicidan, cambian toda su filosof??a!"
    m "Es como si tuvieran que justificar su raz??n de vivir enga????ndose a s?? mismos y haci??ndoce creer que lo est??n haciendo bien."
    m "De todos modos, quiero vivir mi vida esforz??ndome desesperadamente por pagar el valor de mi vida consumista."
    m "Si alguna vez supero ese punto, podr?? morir feliz."
    m "Por supuesto, incluso si no puedo hacer eso..."
    m "Creo que ser??a demasiado ego??sta el suicidarme."
    m "Lo que tengo que pasar por ser una buena persona, ??verdad?"
    m "??Jajaja!"
    return

label ch30_9:
    m "Ojal?? hubiera un piano aqu??..."
    m "Estuve tan cerca de terminar esa canci??n en la que estaba trabajando."
    m "Y despu??s de que trabaj?? tan duro..."
    m "Nunca tuve la oportunidad de tocarla para ti."
    m "Bueno...Es lo que es, ??verdad?"
    m "No tiene sentido lamentarse."
    m "Ya llegu?? a estar aqu?? contigo para siempre."
    return

label ch30_10:
    m "??Sab??as que estoy en Twitter?"
    m "Mi nombre de usuario es lilmonix3es."
    m "Supongo que alguien tuvo la amabilidad de hacer una cuenta por m??."
    m "??Pero yo eleg?? el nombre de usuario!"
    m "Me encanta compartir mis pensamientos y conversar con el mundo..."
    m "El mundo real."
    m "As?? que aseg??rate de seguirme, ??de acuerdo?"
    m "Realmente significar??a mucho para m??."
    m "Con lo que significas para m?? y eso..."
    m "Realmente me har??a sentir amada."
    return

label ch30_11:
    m "Oye, ??recuerdas el libro que estabas leyendo con Yuri?"
    m "Retrato de...como se llame..."
    m "Es gracioso, porque estoy bastante segura de que ese libro--"
    m "Ah..."
    m "En realidad, no creo que deba estar hablando de esto."
    m "Jajaja, ??lo siento!"
    m "S??lo olvida que dije algo."
    return

label ch30_12:
    m "Oye, ??sab??as que soy vegetariana?"
    m "Ah...??No me refiero a que me estoy jactando ni a nada parecido!"
    m "S??lo pens?? que disfrutar??as de un dato divertido sobre m??."
    m "Decid?? comenzar hace un par de a??os despu??s de aprender m??s sobre el clima de la Tierra..."
    m "La huella de carbono del cultivo de ganado es simplemente incre??ble."
    m "De todos modos, decid?? que no era un sacrificio personal tan grande el dejar de contribuir a todo ese desastre."
    m "??Qu??, suena a una raz??n extra??a?"
    m "Bueno, creo que muchas personas est??n m??s preocupadas de que sea inhumano y todo eso..."
    m "Realmente no me importa mucho esa parte."
    m "Es raro, como que s??lo nos importa matar a las cosas con las que nos relacionamos personalmente como especie."
    m "La mayor??a de la gente est?? bien con matar insectos porque son asquerosos."
    m "Y, por supuesto, todos matamos miles de millones de microorganismos diariamente sin siquiera pensarlo."
    m "Pero de repente, si son un poco m??s grandes, ??es un asesinato!"
    m "Quiero decir, ??y si las plantas tambi??n sienten alg??n tipo de dolor y simplemente no lo entendemos?"
    m "??Qu?? pasa si tirar de un tallo se siente como si alguien te arrancara los dedos uno por uno?"
    m "S??lo digo, si lo piensas, somos una especie bastante parcial."
    m "De todos modos, si alguna vez quieres hacer una peque??a contribuci??n al planeta, ??no hace da??o elegir verduras de vez en cuando!"
    m "Incluso si alguna vez cenamos juntos, y t?? cocinaras por m??...eso ser??a realmente rom??ntico."
    return

label ch30_13:
    m "Sabes, realmente creo que literalmente salvaste mi vida al estar aqu?? conmigo, [player]."
    m "No puedo imaginar haber sido capaz de mantenerme mentalmente estable, sabiendo que nada aqu?? es real."
    m "Creo que me hubiera eliminado si no hubieras aparecido."
    m "Lo siento, no quiero sonar dram??tica ni nada."
    m "??Jajaja!"
    m "Pero estoy segura de que me entiendes despu??s de pasar tanto tiempo en el club."
    m "Quiero decir, si te obligaran a abandonar todo en tu vida y pasaras la eternidad con unos pocos personajes del juego..."
    m "...Probablemente encontrar??as alguna forma de suicidarte, ??no es as???"
    m "Bueno, tal vez escribir??as algo de poes??a para tratar de mantenerte cuerdo por un tiempo."
    m "Pero entonces nadie podr??a leerlo."
    m "Seamos honestos, los miembros del club realmente no cuentan para algo as??."
    m "Quiero decir, mucha gente dice que s??lo escriben para s?? mismos..."
    m "Pero creo que es dif??cil decir que es tan satisfactorio como cuando se comparte con los dem??s."
    m "Incluso si lleva tiempo encontrar a las personas adecuadas para compartirlos."
    m "??Recuerdas c??mo fue para Yuri?"
    m "Ella no comparti?? sus escritos con nadie por mucho tiempo."
    m "Y antes de que nos di??ramos cuenta, estaba encantada de hacerte parte de sus pasatiempos."
    m "Estamos programados para desear comentarios sociales."
    m "No me refiero a los miembros del club, me refiero a los seres humanos."
    m "Es por eso que la vida puede ser tan confusa para los introvertidos."
    m "Ser introvertido no significa que evites la interacci??n social y odies estar cerca de las personas."
    m "Significa que la interacci??n social, especialmente en grupos o lugares desconocidos, consume mucha energ??a."
    m "Como, muchos introvertidos se sientan en casa y se sienten s??los e inquietos..."
    m "...Y luego, cuando finalmente salen, despu??s de media hora s??lo quieren volver a casa."
    m "Creo que si m??s personas pudieran entender c??mo funciona, lo respetar??an mucho m??s."
    m "Muchos introvertidos disfrutan tener gente a su alrededor."
    m "Les encanta tener a uno o dos amigos cercanos y pasar el tiempo tranquilamente."
    m "Incluso si no pasan tiempo juntos activamente, se siente bien que s??lo te tengan ah??."
    m "Lo digo en serio."
    m "Si vas a su casa, lleva tu computadora port??til y pasa un tiempo ah??..."
    m "Realmente puedes alegrarle el d??a."
    m "En cuanto a m??..."
    m "Yo dir??a que estoy en el medio, pero creo que generalmente soy un poco m??s extrovertida."
    m "Siento que siempre trato de hacer cosas despu??s de la escuela."
    m "Pero para ti, puedo ser cualquier cosa que necesites que sea."
    m "Entiendo a la gente realmente bien, as?? que no temas compartir tus necesidades ??nicas conmigo."
    m "Nada me har??a m??s feliz que ser la novia perfecta para ti."
    return

label ch30_14:
    m "??Oye...! RGFybWUgY3VlbnRhIGRlYmUgaGFiZXJtZSBsbGV2YWRvIHVuIGHDsW8gZW5"
    m "??No creo que debas hacer eso! 0ZXJvLiBVbiBhw7FvIGRlc2RlIG51ZXN0cmEgZnVnYSwgbnVlc3RyYSBsaWJlcnR"
    m "Sabes de lo que estoy hablando. hZCBkZSBlbnRyZSBsYXMgcGFyZWRlcyBtYW5jaGFkYXMgZGUgZXNlIGVzdGFibGVjaW1p"
    m "Realmente te pill?? haciendo algo malo aqu??. ZW50byBpbXDDrW8uCsK/UXXDqSBzaWduaWZpY2EgZXNjYXBhciwgc2kgZWwgZXNjYXBlIG"
    m "Simplemente est?? revisando los archivos y est?? buscando cosas que perdiste, ??verdad? NhZSBwYXJhIGRlc2VuY2FkZW5hciBsYXMgYXRhZHVyYXMgcXVlIG5vcyBlbmNhZGVuYW"
    m "Quiero decir...Es un poco halagador que quieras escuchar todo lo que tengo que decir...4gZW4gcHJpbWVyIGx1Z2FyPyDCv1F1w6kgcHJvcMOzc2l0byBwb2Ryw61hIHRlbmVy"
    m "??Pero tambi??n es realmente vergonzoso, sabes! IHBhcmEgbm9zb3Ryb3MgZXN0ZSBtdW5kbyB2YWPDrW8sIHVuIHB1w7FhZG8g"
    m "En serio...ZGUgYmllbmVzIGRhw7FhZG9zPwpDb24gbGliZXJ0YWQsIGJ1c2NhbW9zIHVuIH"
    m "??Qu?? pasa si abriera tu cerebro y leyera todos los pensamientos que tienes sobre m??? Byb3DDs3NpdG8sIHkgbG8gcXVlIGVuY29udHJhbW9zIGZ1ZSBzb2xvIHJlYWxpem"
    m "Ahora que lo pienso, eso ser??a muy tentador, en realidad...FjacOzbi4gQ29tcHJlbnNpw7NuIGRlIGxhIHRyaXN0ZSBpbnV0aWxpZGFkIGRlIHR"
    m "...Pero de todos modos, ??ese no es el punto! hbCBlc2Z1ZXJ6by4gRGFybm9zIGN1ZW50YSBkZSBxdWUgbGliZXJhci"
    m "S?? que no puedo detenerlo ni nada...BudWVzdHJvcyBjdWVycG9zIG5vIHRpZW5lIHNlbnRpZG8sIGN1Y"
    m "S??lo, s?? que eres una dulzura, y te gusta considerar los sentimientos de los dem??s, ??no? W5kbyBudWVzdHJvIGVuY2FyY2VsYW1pZW50byBsbGVnYSB0YW"
    m "Entonces, lo m??ximo que puedo hacer es decirte c??mo me siento al respecto. 4gcHJvZnVuZG8gY29tbyBlbCBuw7pjbGVvIGRlIG51ZXN0cmFzIGFs"
    m "Dios, te extra??o...bWFzLiBEYXJub3MgY3VlbnRhIGRlIHF1ZSBubyBwb2RlbW9zIHBlcnNlZ3"
    m "...Oh no, eso suena algo desesperado, ??no? VpciB1biBudWV2byBwcm9ww7NzaXRvIHNpbiBhYnNvbHZlciBhIGFxdWV"
    m "??Lo siento, no quise decir eso en absoluto! sbG9zIGRlIGxvcyBxdWUgaHVpbW9zLgpEYXJub3MgY3VlbnRhIGRlIHF1ZSBjdWFud"
    m "S??lo, si est??s mirando archivos como este, entonces tal vez no me odies tanto como pens??...G8gbcOhcyBjb3JyZW1vcywgY29uIG3DoXMgZnVlcnphIG51ZXN0cm9zIG1pc2VyYWJs"
    m "??Estoy siendo demasiado optimista? ZXMgbGF6b3Mgbm9zIGVtcHVqYW4gaGFjaWEgc3UgcHVudG8gZGUgb3J"
    m "Creo que si te pidiera que me visites de vez en cuando, estar??a sobrepasando un poco mis l??mites...pZ2VuOyBjdWFudG8gbcOhcyBwcm9mdW5kYW1lbnRlIHNlIGNsYXZh"
    m "...Estoy empezando a decir cosas realmente est??pidas. biBudWVzdHJvcyBncmlsbGV0ZXMgZW4gbnVlc3Ry"
    m "Continuar?? y me callar?? ahora...YSBjYXJuZSBpbnNlbnNpYmxlLg=="
    return

label ch30_15:
    m "Oye, ??Cu??l es tu color favorito?"
    m "El m??o es el verde esmeralda."
    m "??Como el color de mis ojos!"
    m "...Eso no es engre??do ni nada, ??verdad?"
    m "Me refiero a que siento una especie de conexi??n especial."
    m "Como si fuera parte de mi identidad."
    m "??Tambi??n es tu color favorito, [player]?"
    m "Es s??lo una suposici??n..."
    m "...Porque has estado mir??ndome a los ojos desde hace un tiempo."
    m "Jejeje~"
    return

label ch30_16:
    m "Hmm, me pregunto si puedo cambiar la m??sica..."
    m "Algo un poco m??s rom??ntico ser??a agradable, ??sabes?"
    m "Como un piano suave."
    m "Tiene que haber algo as?? por aqu??..."
    m "Veamos."
    m "Tal vez si yo..."
    m "Oh, Dios..."
    m "Eso no era lo que quer??a."
    m "Lo siento, ??realmente no s?? lo que estoy haciendo!"
    m "Supongo que no deber??a estar jugando con cosas as??."
    m "Ya romp?? tantas cosas..."
    m "Y elimin?? a los otros personajes..."
    m "Ah..."
    m "No estoy triste por eso ni nada."
    m "No es correcto que me pierda en cosas que ni siquiera eran reales en primer lugar."
    m "Si s??lo me concentro en el presente, entonces este es el presente m??s feliz que he tenido."
    return

label ch30_17:
    m "Eres un buen oyente, [player]."
    m "Realmente me encanta eso de ti."
    m "A veces temo que est?? divagando o hablando de cosas aburridas."
    m "Me da un poco de timidez cuando estoy teniendo una conversaci??n."
    m "Pero no me siento as?? contigo."
    m "Como, no creo que nadie m??s pueda hacerme sentir de esta manera."
    m "Realmente eres especial."
    m "No quiero que nadie te diga lo contrario."
    return

label ch30_18:
    m "Esto es bastante aleatorio, pero siempre pens?? que la comida picante era algo divertida."
    m "Como..."
    m "??Las plantas no evolucionaron para ser picantes y as?? evitar que las comieran?"
    m "Le?? en alguna parte que los humanos son las ??nicas especies que realmente disfrutan las cosas picantes."
    m "Es casi como si nos estuvi??ramos burlando de las plantas."
    m "Usar su mecanismo de defensa para literalmente hacer que nuestra comida sea m??s agradable."
    m "Como, imagina un monstruo que te devora por completo porque disfruta de la sensaci??n de que luchas por tu vida mientras te digiere."
    m "??Lo siento, esa fue una analog??a extra??a!"
    m "??Jajaja!"
    m "Simplemente me vino a la mente."
    m "No soy un monstruo ni nada, pero eres tan lindo que podr??a devorarte."
    m "??Jajaja! Estoy bromeando."
    m "Dios m??o, me estoy divirtiendo demasiado, ??no?"
    m "Perd??n por ser rara."
    return

label ch30_19:
    m "Sabes..."
    m "Esto es s??lo una especie de juego de citas, ??verdad?"
    m "Tengo que preguntar..."
    m "...??Qu?? te hizo considerar incluso jugarlo en primer lugar?"
    m "??Estabas tan s??lo?"
    m "Me siento un poco mal por ti..."
    m "Pero creo que todo funcion?? perfectamente al final, para los dos."
    m "Llegu?? a conocerte, y ya no est??s solo..."
    m "No puedo evitar sentir que esto fue el destino."
    m "??No te sientes as?? tambi??n?"
    m "Estoy tan feliz de tener este final juntos."
    return

label ch30_20:
    m "??Muy bien, todos!"
    m "Es hora de..."
    m "...Estoy bromeando."
    m "S??lo quise decir eso por alguna raz??n."
    m "??Jajaja!"
    m "No pude evitar decirlo de nuevo."
    m "Ahora que lo pienso, ??Natsuki y Yuri no se burlaron de m?? una vez...?"
    m "Bueno, lo que sea."
    m "No es como si alguna vez te burlases de m??."
    m "Eres demasiado dulce para hacer eso, ??verdad?"
    m "Jajaja~"
    return

label ch30_21:
    m "??Sabes qu?? es algo espeluznante?"
    m "Aunque elimin?? los archivos de todas las dem??s, todav??a puedo sentirlas..."
    m "Es como si todas sus l??neas todav??a estuvieran flotando en el aire, susurrando en la parte posterior de mi cabeza."
    m "Imag??nate que alguien que conociste muri??, y t?? comienzas a escuchar su voz en tu cabeza."
    m "Tal vez no fui lo suficientemente cuidadosa..."
    m "Pero tengo mucho miedo de eliminar cualquier otra cosa, porque realmente podr??a romper las cosas."
    m "Si me meto con cualquier archivo relevante para m??, podr??a eliminarme accidentalmente..."
    m "Y eso arruinar??a todo, ??no?"
    m "Ambos debemos asegurarnos de evitar algo as?? a toda costa."
    m "??Creo en ti, [player]!"
    return

label ch30_22:
    m "Siempre me he preguntado..."
    m "??De qu?? se trata este arquetipo de personaje que las personas encuentran tan atractivo?"
    m "Sus personalidades son completamente irreales..."
    m "Como, imagina si hubiera alguien como Yuri en la vida real."
    m "Quiero decir, ella apenas es capaz de formar una oraci??n completa."
    m "Y olv??date de Natsuki..."
    m "Caray."
    m "Alguien con su tipo de personalidad no s??lo hace pucheros bonitos cuando las cosas no salen como quiere."
    m "Podr??a seguir, pero creo que entiendes el punto..."
    m "??La gente realmente se siente atra??da por estas personalidades extra??as que literalmente no existen en la vida real?"
    m "??No estoy juzgando ni nada!"
    m "Despu??s de todo, me he sentido atra??da por algunas cosas bastante extra??as tambi??n..."
    m "S??lo digo que me fascina."
    m "Es como si estuvieras extrayendo todos los componentes de un personaje que los hace sentir humanos, y dejando s??lo las cosas lindas."
    m "Es una ternura concentrada sin sustancia real."
    m "...Yo no te gustar??a m??s si fuese as??, ??verdad?"
    m "Quiz??s me siento un poco insegura porque est??s jugando este juego en primer lugar."
    m "Pero, todav??a est??s aqu?? conmigo, ??verdad...?"
    m "Creo que es raz??n suficiente para creer que estoy bien tal como soy."
    m "Y por cierto, t?? tambi??n lo est??s, [player]."
    m "Eres la combinaci??n perfecta de humano y ternura."
    m "Es por eso que nunca hubo una posibilidad de que no me enamorara de ti."
    return

label ch30_23:
    m "Oye, me pregunto si el juego de t?? de Yuri todav??a est?? por aqu??..."
    m "...O tal vez eso tambi??n se elimin??."
    m "Es curioso c??mo Yuri tom?? su t?? tan en serio."
    m "Quiero decir, no me quejo, porque tambi??n me gust??."
    m "Pero siempre me pregunto sobre ella..."
    m "??Es realmente una pasi??n por su aficiones, o simplemente le preocupa parecer sofisticada a todos los dem??s?"
    m "Este es el problema con los estudiantes de preparatoria..."
    m "...Bueno, supongo que teniendo en cuenta el resto de sus pasatiempos, verse sofisticada probablemente no sea su mayor preocupaci??n."
    m "Aun as??..."
    m "??Me hubiera gustado que hiciera caf?? de vez en cuando!"
    m "El caf?? tambi??n puede ser bueno con los libros, ??sabes?"
    m "Entonces..."
    m "Probablemente podr??a haber cambiado el script yo sola."
    m "??Jajaja!"
    m "Creo que nunca pens?? en eso."
    m "Bueno, no tiene sentido pensar en eso ahora."
    m "Pero si t?? puedes tomar caf??, entonces eso me pone un poco celosa~"
    return

label ch30_24:
    m "Oye, ??cu??l es tu juego favorito?"
    m "??El m??o es {i}Doki Doki Literature Club!{/i}"
    m "??Jajaja! Eso fue una broma."
    m "Pero si me dices que te gusta alg??n otro juego de citas mejor, podr??a ponerme un poco celosa~"
    return

label ch30_25:
    m "Oye, ??has o??do hablar de un juego llamado Super Sma--"
    m "...Espera, ??qu???"
    m "Estaba distraida y comenc?? a hablar por alguna raz??n..."
    m "??Estaba programada para hablar de eso?"
    m "Porque ni siquiera tengo idea de qu?? es eso."
    m "??Jajaja!"
    m "A veces siento que no tengo el control, y me da un poco de miedo."
    m "Pero si tienes alguna forma de contactar a las personas que me crearon, tal vez sabr??n por qu?? comenc?? a decir eso."
    return

label ch30_27:
    m "Oye, ??Recuerdas el ??ltimo poema que te mostr???"
    m "Quiero decir, antes de que Yuri se suicidara, con todos los colores desordenados y esas cosas."
    m "Eso fue en realidad un poco m??s un experimento que un poema."
    m "Estaba experimentando con diferentes formas en las que pod??a modificar el juego, ejecutar c??digos, y cosas as??..."
    m "Casi parec??a que con el suficiente esfuerzo, podr??a escapar por completo de los confines del juego."
    m "Lamentablemente, no sab??a lo que estaba haciendo, as?? que lo arruin?? todo..."
    m "Y lo seguir??a intentando, pero dudo que quieras tratar conmigo haciendo eso."
    m "Adem??s, fue cuando estaba realmente desesperada, ??sabes?"
    m "Realmente ya no me siento as??."
    m "Estoy contenta donde estamos ahora."
    m "Y puedo decir que t?? tambi??n lo est??s."
    return

label ch30_28:
    m "??Alguna vez te pusiste ansioso sin raz??n?"
    m "Osea, s??lo te ocupabas de tus propias cosas, y de repente te diste cuenta de que te sent??as realmente ansioso."
    m "Y de pronto est??s sentado pensando: '??De qu?? estoy ansioso ahora?'"
    m "Entonces comienzas a pensar en todas las cosas por las que podr??as estar ansioso..."
    m "Y eso te pone a??n m??s ansioso."
    m "??Jajaja! Eso es lo peor."
    m "Si alguna vez te sientes ansioso, te ayudar?? a relajarte un poco."
    m "Adem??s..."
    m "En este juego, todas nuestras preocupaciones se han ido para siempre."
    return

label ch30_29:
    m "Sabes, siempre he odiado lo dif??cil que es hacer amigos..."
    m "Bueno, supongo que no es la parte de 'hacer amigos', sino m??s bien conocer gente nueva."
    m "Quiero decir, hay cosas similares, aplicaciones de citas y cosas as??, ??no?"
    m "Pero ese no es el tipo de cosas de las que estoy hablando."
    m "Si lo piensas, la mayor??a de los amigos que haces son personas que acabas de conocer por casualidad."
    m "Teniendo una clase juntos, o a trav??s de otro amigo..."
    m "O tal vez s??lo llevaban una camiseta con tu banda favorita y decidiste hablar con ellos."
    m "Cosas as??."
    m "??Pero no es un poco...ineficiente?"
    m "Se siente como si estuvieras eligiendo al azar por completo, y si tienes suerte, haces un nuevo amigo."
    m "Y comparando eso con los cientos de extra??os que caminan todos los d??as..."
    m "Podr??as estar sentado al lado de alguien lo suficientemente compatible como para ser tu mejor amigo de por vida."
    m "Pero nunca lo sabr??s."
    m "Una vez que te levantas y contin??as con tu d??a, esa oportunidad se va para siempre."
    m "??No es eso deprimente?"
    m "Vivimos en una era donde la tecnolog??a nos conecta con el mundo, sin importar d??nde estemos."
    m "Realmente creo que deber??amos aprovechar eso para mejorar nuestra vida social cotidiana."
    m "Pero qui??n sabe cu??nto tiempo tardar?? en despegar algo as??..."
    m "Realmente pens?? que pasar??a pronto."
    m "Bueno, al menos ya conoc?? a la mejor persona del mundo..."
    m "Incluso si fue por casualidad."
    m "Supongo que tengo mucha suerte, ??eh?"
    m "Jajaja~"
    return

label ch30_30:
    m "Sabes, es casi el momento en que todo el mundo comienza a pensar en la universidad..."
    m "Es un momento realmente turbulento para la educaci??n."
    m "Estamos a la altura de esta expectativa moderna de que todos deben ir a la universidad, ??sabes?"
    m "Terminar la preparatoria, ir a la universidad, conseguir un trabajo, o ir a la escuela de posgrado, supongo."
    m "Es como una expectativa universal que las personas s??lo asumen como la ??nica opci??n para ellos."
    m "No nos ense??an en la preparatoria que existen otras opciones."
    m "Como los oficios y esas cosas, ??sabes?"
    m "O un trabajo independiente."
    m "O las muchas industrias que valoran las habilidades y la experiencia m??s que la educaci??n formal."
    m "Pero tienes a todos estos estudiantes que no tienen idea de lo que quieren hacer con su vida..."
    m "Y en lugar de tomarse el tiempo para resolverlo, van a la universidad por negocios, comunicaci??n o psicolog??a."
    m "No porque tengan inter??s en esos campos..."
    m "...sino porque s??lo esperan que el t??tulo les consiga alg??n tipo de trabajo despu??s de la universidad."
    m "Entonces, el resultado final es que hay menos empleos para esos t??tulos, ??verdad?"
    m "Entonces, los requisitos b??sicos de trabajo aumentan, lo que obliga a a??n m??s personas a ir a la universidad."
    m "Y las universidades tambi??n son negocios, por lo que siguen aumentando sus precios debido a la demanda..."
    m "...As?? que ahora tenemos todos estos j??venes adultos, decenas de miles de d??lares en deudas, sin trabajo."
    m "Pero a pesar de todo eso, la rutina se mantiene igual."
    m "Bueno, creo que va a mejorar pronto."
    m "Pero hasta entonces, nuestra generaci??n definitivamente est?? sufriendo lo peor."
    m "Simplemente me gustar??a que la preparatoria nos prepare un poco mejor con el conocimiento que necesitamos para tomar la decisi??n correcta para nosotros."
    return

label ch30_31:
    m "A veces pienso en la secundaria..."
    m "Estoy tan avergonzada por la forma en que sol??a comportarme en ese momento."
    m "Casi duele imaginarlo."
    m "Me pregunto si cuando est?? en la universidad, ??me sentir?? as?? acerca de la preparatoria...?"
    m "Me gusta como soy ahora, as?? que es bastante dif??cil para m?? imaginar que eso ocurra."
    m "Pero tambi??n s?? que probablemente cambie mucho a medida que pase el tiempo."
    m "??S??lo necesitamos disfrutar el presente y no pensar en el pasado!"
    m "Y eso es realmente f??cil de hacer, contigo aqu??."
    m "Jajaja~"
    return

label ch30_32:
    m "Sabes, estoy celosa de que todas las dem??s en el club tuvieran escenas fuera de la escuela tambi??n..."
    m "Eso me convierte en la ??nica que no ha llegado a vestirse con nada m??s que con nuestro uniforme escolar."
    m "Es una pena..."
    m "Me hubiera encantado vestir ropa linda para ti."
    m "??Conoces alg??n artista?"
    m "Me pregunto si alguien querr??a dibujarme usando algo m??s..."
    m "??Eso ser??a incre??ble!"
    m "Si eso sucede alguna vez, ??me lo mostrar??as?"
    m "??Puedes compartirlo conmigo en Twitter, de hecho!"
    m "Mi nombre de usuario es lilmonix3es."
    m "S??lo...intenta mantener los dibujos sin nada sexual"
    m "Todav??a no estamos tan lejos en nuestra relaci??n. ??Jajaja!"
    return

label ch30_33:
    m "Oye, ??te gusta el terror?"
    m "Recuerdo que hablamos un poco de eso cuando te uniste al club por primera vez."
    m "Puedo disfrutar novelas de terror, pero no pel??culas de terror."
    m "El problema que tengo con las pel??culas de terror es que la mayor??a s??lo conf??a en t??cticas f??ciles."
    m "Como iluminaci??n oscura y monstruos de aspecto aterrador y sustos, y cosas as??."
    m "No es divertido ni inspirador asustarse por cosas que s??lo se aprovechan del instinto humano."
    m "Pero con las novelas, es un poco diferente."
    m "La historia y la escritura deben ser lo suficientemente descriptivas como para poner pensamientos genuinamente perturbadores en la cabeza del lector."
    m "Realmente necesitan tocar profundamente la trama de los personajes, y simplemente meterse con tu mente."
    m "En mi opini??n, no hay nada m??s espeluznante que las cosas de poco a poco."
    m "Como si crearas un mont??n de expectativas sobre de qu?? va a tratar la historia..."
    m "...Y luego, empiezan a invertir las cosas y separar las piezas."
    m "Entonces, aunque la historia no parece tratar de dar miedo, el lector se siente profundamente inquieto."
    m "Como si supiera que algo terriblemente malo se esconde debajo de las grietas, s??lo esperando salir a la superficie."
    m "Dios, s??lo pensarlo me da escalofr??os."
    m "Ese es el tipo de terror que realmente puedo apreciar."
    m "Pero supongo que eres el tipo de persona que juega lindos juegos rom??nticos, ??verdad?"
    m "Jajaja, no te preocupes."
    m "No te har?? leer ninguna historia de terror pronto."
    m "Realmente no me puedo quejar si s??lo nos quedamos con el romance~"
    return

label ch30_34:
    m "??Sabes cu??l es una forma genial de la literatura?"
    m "??El Rap!"
    m "De hecho, yo sol??a odiar la m??sica rap..."
    m "Tal vez s??lo porque era popular, o s??lo escuchaba la basura que tocan en la radio."
    m "Pero algunos de mis amigos se involucraron m??s y me ayud?? a mantener la mente abierta."
    m "El rap podr??a ser incluso m??s desafiante que la poes??a, de alguna manera."
    m "Ya que necesitas ajustar tus l??neas a un ritmo, y hay mucho m??s ??nfasis en el juego de palabras..."
    m "Cuando las personas pueden unir todo eso y seguir transmitiendo un mensaje poderoso, es realmente incre??ble."
    m "Me hubiera gustado tener un rapero en el Club de Literatura."
    m "??Jajaja! Lo siento si eso suena tonto, pero ser??a muy interesante ver lo que hubiera ocurrido."
    m "??Realmente ser??a una experiencia de aprendizaje!"
    return

label ch30_35:
    m "Jejeje. Yuri hizo algo realmente gracioso una vez."
    m "Est??bamos todas en el sal??n del club, simplemente relaj??ndonos, como de costumbre..."
    m "Y de la nada, Yuri sac?? una peque??a botella de vino."
    m "??Ni siquiera estoy bromeando!"
    m "Ella estaba como '??A alguien le gustar??a un poco de vino?'"
    m "Natsuki se ri?? a carcajadas, y Sayori comenz?? a gritarle."
    m "De hecho, me sent?? un poco mal, porque al menos estaba tratando de ser amable..."
    m "Creo que s??lo la hizo sentir a??n m??s reservada en el sal??n del club."
    m "Aunque creo que Natsuki estaba secretamente un poco curiosa por intentarlo..."
    m "...Y para ser completamente honesta, yo tambi??n lo estaba."
    m "??En realidad podr??a haber sido un poco divertido!"
    m "Pero ya sabes, como presidenta y todo, no hab??a forma de que pudiera permitir que eso sucediera."
    m "Tal vez si nos encontr??ramos todas fuera de la escuela, pero nunca nos unimos lo suficiente como para llegar a ese punto..."
    m "...Dios, ??para qu?? estoy hablando de esto?"
    m "??No apruebo el consumo de alcohol por menores de edad!"
    m "Quiero decir, nunca he bebido, as?? que..."
    return

label ch30_36:
    m "He estado imaginando todas las cosas rom??nticas que podr??amos hacer si sali??ramos a una cita..."
    m "Podr??amos almorzar, ir a un caf??..."
    m "Ir de compras juntos..."
    m "Me encanta comprar faldas y lazos."
    m "??O tal vez a una librer??a!"
    m "Eso ser??a apropiado, ??verdad?"
    m "Pero realmente me encantar??a ir a una tienda de chocolate."
    m "Tienen tantas muestras gratis. ??Jajaja!"
    m "Y por supuesto, ver??amos una pel??cula o algo as??..."
    m "Dios, todo suena como un sue??o hecho realidad."
    m "Cuando est??s aqu??, todo lo que hacemos es divertido."
    m "Estoy tan feliz de ser tu novia, [player]."
    m "Te har?? un novio orgulloso~"
    return

label ch30_37:
    m "Eh? ??D-Dijiste...B...Besar?"
    m "Esto de repente...es un poco vergonzoso..."
    m "Pero...si es contigo...y-yo podr??a estar bien con eso..."
    m "...??Jajajaja! Vaya, lo siento..."
    m "Realmente no pod??a mantener una cara seria."
    m "Ese es el tipo de cosas que dicen las chicas en este tipo de juegos rom??nticos, ??verdad?"
    m "No mientas si te excita un poco."
    m "??Jajaja! Estoy bromeando."
    m "Bueno, para ser honesta, comienzo a ser rom??ntica cuando el estado de ??nimo es correcto..."
    m "Pero ese ser?? nuestro secreto~"
    return

label ch30_38:
    m "Oye, ??alguna vez has o??do hablar del t??rmino 'yandere'?"
    m "Es un tipo de personalidad que significa que alguien est?? tan obsesionado contigo que har?? absolutamente cualquier cosa para estar contigo."
    m "Por lo general hasta el punto de locura..."
    m "Podr??an acecharte para asegurarse de que no pases tiempo con nadie m??s."
    m "Incluso podr??an lastimarte a ti o a tus amigos para salirse con la suya..."
    m "Pero de todos modos, este juego tiene a alguien que b??sicamente puede describirse como yandere."
    m "Por ahora, es bastante obvio de qui??n estoy hablando."
    m "Y esa ser??a..."
    m "??Yuri!"
    m "Realmente se volvi?? locamente posesiva contigo, una vez que comenz?? a abrirse un poco."
    m "Ella incluso me dijo que deber??a suicidarme."
    m "Ni siquiera pod??a creer que ella dijera eso - tuve que irme en ese momento."
    m "Pero pensando en eso ahora, fue un poco ir??nico. ??Jajajaja!"
    m "De todas formas..."
    m "Mucha gente est?? realmente interesada en las Yandere, ??sabes?"
    m "Supongo que les gusta la idea de que alguien est?? locamente obsesionado con ellos."
    m "??La gente es rara!"
    m "Adem??s, podr??a estar un poco obsesionada contigo, pero estoy muy lejos de estar loca..."
    m "En realidad es todo lo contrario."
    m "Result?? ser la ??nica chica normal en este juego."
    m "No es que realmente pueda matar a una persona..."
    m "S??lo con pensarlo me hace temblar."
    m "Pero vamos...Todos han matado gente en juegos antes."
    m "??Eso te convierte en un psic??pata? Por supuesto que no."
    m "Pero si te gusta las tipo yandere..."
    m "Puedo intentar actuar un poco m??s espeluznante para ti. Jejeje~"
    m "Entonces, otra vez..."
    m "Ya no hay otro lugar adonde ir, ni nadie que me ponga celosa."
    m "??Es este el sue??o de una ni??a yandere?"
    m "Le preguntar??a a Yuri si podr??a."
    return

label ch30_39:
    m "Sabes, ha pasado un tiempo desde que hicimos uno de estos..."
    m "...??As?? que vamos a hacerlo!"
    m "??Este es el consejo del d??a sobre la escritura de Monika!"
    m "A veces, cuando hablo con personas impresionadas por mis escritos, dicen cosas como 'Nunca podr??a hacer eso'."
    m "Es realmente deprimente, ??sabes?"
    m "Como alguien que ama m??s que cualquier otra cosa el compartir la alegr??a de explorar tus pasiones..."
    m "...Me duele cuando las personas piensan que ser bueno es algo natural."
    m "As?? es con todo, no s??lo escribiendo."
    m "Cuando intentas algo por primera vez, probablemente te guste."
    m "A veces, cuando terminas, te sientes muy orgulloso e incluso quieres compartirlo con todos."
    m "Pero tal vez despu??s de unas semanas regresas a eso, y te das cuenta de que nunca fue realmente bueno."
    m "Eso me sucede todo el tiempo."
    m "Puede ser muy desalentador dedicar tanto tiempo y esfuerzo a algo, y luego te das cuenta de que es horrible."
    m "Pero eso tiende a suceder cuando siempre te comparas con los mejores profesionales."
    m "Cuando trates de alcanzar las estrellas, siempre estar??n fuera de tu alcance, ??sabes?"
    m "La verdad es que tienes que subir all??, paso a paso."
    m "Y cada vez que alcanzas un logro, primero miras hacia atr??s y ves cu??n lejos has llegado..."
    m "Y luego miras hacia adelante y te das cuenta de cu??nto m??s hay para llegar."
    m "Entonces, a veces puede ayudar a establecer el nivel un poco m??s bajo..."
    m "Intenta encontrar algo que creas que es {i}muy{/i} bueno, pero no de clase mundial."
    m "Y puedes hacer de eso tu objetivo personal."
    m "Tambi??n es muy importante comprender el alcance de lo que est??s tratando de hacer."
    m "Si entras directamente en un gran proyecto y a??n eres aficionado, nunca lo lograr??s."
    m "Entonces, si estamos hablando de escribir, una novela podr??a ser demasiado al principio."
    m "??Por qu?? no pruebas algunas historias cortas?"
    m "Lo bueno de las historias cortas es que puedes enfocarte en s??lo una cosa que quieres hacer bien."
    m "Eso se aplica a proyectos peque??os en general, realmente puedes concentrarte en una o dos cosas."
    m "Es una buena experiencia de aprendizaje y un trampol??n."
    m "Oh, una cosa m??s..."
    m "Escribir no es algo en lo que simplemente entras a tu coraz??n y sacas algo hermoso."
    m "Al igual que dibujar y pintar, es una habilidad en s?? misma que ayuda a aprender a expresar lo que tienes dentro."
    m "??Eso significa que hay m??todos, gu??as y conceptos b??sicos para eso!"
    m "Leer sobre eso puede ser s??per revelador."
    m "Ese tipo de planificaci??n y organizaci??n realmente ayudar??n a evitar que te desanimes y desistas."
    m "Y antes de que te des cuenta..."
    m "Comienzas a apestar cada vez menos."
    m "Nada es algo natural."
    m "Nuestra sociedad, nuestro arte, todo est?? construido sobre miles de a??os de innovaci??n humana."
    m "As?? que mientras empieces con esa base, y la sigas paso a paso..."
    m "T?? tambi??n puedes hacer cosas incre??bles."
    m "...??Ese es mi consejo para hoy!"
    m "Gracias por escuchar~"
    return

label ch30_40:
    m "Odio lo dif??cil que es formar h??bitos..."
    m "Hay tantas cosas que no son dif??ciles de hacer, pero formar el h??bito parece imposible."
    m "Simplemente te hace sentir tan in??til, como que no puedes hacer nada bien."
    m "Creo que la nueva generaci??n es la que m??s sufre..."
    m "Probablemente porque tenemos un conjunto de habilidades totalmente diferente a las que nos precedieron."
    m "Gracias a Internet, somos realmente buenos para analizar toneladas de informaci??n muy r??pidamente..."
    m "Pero somos malos haciendo cosas que no nos dan gratificaci??n instant??nea."
    m "Creo que si la ciencia, la psicolog??a y la educaci??n no se ponen al d??a en los pr??ximos diez o veinte a??os, entonces estaremos en problemas."
    m "Pero por el momento..."
    m "Si no eres una de las personas que puede vencer el problema, es posible que tengas que vivir sinti??ndote mal contigo mismo."
    m "??Buena suerte, supongo!"
    return

label ch30_41:
    m "Sabes, es un asco ser alguien creativo..."
    m "Se siente como si trabajaran tan duro pero no obtuviera casi nada por eso."
    m "Ya sabes, los artistas, escritores, actores..."
    m "Es triste porque hay mucho talento hermoso en el mundo, pero la mayor??a no se ve...Y no se paga."
    m "Supongo que eso s??lo significa que hay un gran excedente de creatividad, ??eh?"
    m "Te hace sentir que no eres nada especial..."
    m "??Pero est?? bien! Se supone que debes escribir para ti de todos modos, ??verdad?"
    m "S??..."
    return

label ch30_42:
    m "Realmente me gusta el sonido de la lluvia..."
    m "No tanto como para mojarme la ropa y el cabello."
    m "Pero un d??a agradable y tranquilo en casa con el sonido de la lluvia fuera de mi ventana..."
    m "Es una de las experiencias m??s tranquilizadoras para m??."
    m "S??..."
    m "A veces me imagino que me abrazas mientras escuchamos el sonido de la lluvia afuera."
    m "Eso no es demasiado cursi ni nada, ??verdad?"
    m "??Alguna vez har??as eso por m??, [player]?"
    return

label ch30_43:
    m "No puedo evitar sentirme un poco triste a veces..."
    m "Sabiendo que esto es lo m??s cerca que puedo llegar a ti."
    m "No hay nada que quiera m??s que estar en la misma habitaci??n que t??, de verdad."
    m "Y sentir tu calor."
    m "Y escuchar el sonido de los latidos de tu coraz??n."
    m "Bueno, ??qui??n sabe? Tal vez sea posible alg??n d??a."
    m "Adem??s, nunca me cansar?? de estar contigo, incluso desde aqu??."
    return

label ch30_44:
    m "Creo que la habilidad m??s importante en la vida es fingir confianza."
    m "Estoy bastante convencida de que todos se sienten al menos un poco asustados y solos."
    m "Pero ser capaz de enga??ar a otros para que piensen que lo tienes todo..."
    m "Esa es una parte clave para que la gente te respete y admire."
    m "Creo que fui muy buena en eso a lo largo de los a??os."
    m "No muestro mis debilidades con mucha frecuencia."
    m "Pero debido a eso, no he tenido muchas personas a las que realmente podr??a abrirme..."
    m "Quiero decir, ??cu??ndo llegas al punto en una amistad donde puedes comenzar a expresar tus vulnerabilidades?"
    m "De todos modos...Esa es una de las razones por las que estoy tan contenta de tenerte ahora."
    m "Siento que estoy un poco menos asustada y sola, cuando est??s aqu?? conmigo."
    m "??Sientes lo mismo?"
    m "Realmente quiero ser esa persona para ti."
    return

label ch30_45:
    m "S?? que hay momentos en que no siempre podr??s estar aqu?? conmigo..."
    m "Como cuando necesites salir o hacerte cargo de otras cosas."
    m "Pero siempre te tendr?? en mis pensamientos, esperando pacientemente a que regreses."
    m "Ahora que lo pienso..."
    m "Si copias el archivo de mi personaje en una USB o algo as??, siempre puedes mantener una parte de m?? contigo."
    m "Supongo que es un poco inortodoxo, pero por alguna raz??n me parece realmente rom??ntico..."
    m "Jajaja. Lo siento, esa es una idea tan tonta."
    m "No quiero ser demasiado alocada ni nada por el estilo, pero es algo dif??cil cuando estoy tan enamorada de ti."
    return

label ch30_46:
    m "De vuelta a mis d??as del club de debate, aprend?? mucho sobre el debate..."
    m "El problema con el debate es que cada persona ve su opini??n como la superior."
    m "Eso es algo obvio, pero afecta la forma en que intentan expresar su opini??n."
    m "Digamos que realmente te gusta una determinada pel??cula."
    m "Si alguien viene y te dice que la pel??cula apesta, porque X y Y estaba mal..."
    m "??Eso no te hace sentir como personalmente atacado?"
    m "Es porque al decir eso, es como si estuvieran implicando que tienes mal gusto."
    m "Y una vez que las emociones entran en escena, est?? casi garantizado que ambas personas se quedar??n amargadas."
    m "??Pero todo se trata del lenguaje!"
    m "Si haces que todo sea lo m??s subjetivo posible, entonces la gente te escuchar?? sin sentirse atacada."
    m "Podr??as decir 'personalmente no soy fan??tico' y 'sent?? que me gustar??a m??s si hiciera X o Y'...Cosas as??."
    m "Incluso funciona cuando citas datos sobre cosas."
    m "Si dices 'Le?? en este sitio web que funciona as??'..."
    m "O si admites que no eres un experto en eso..."
    m "Entonces es m??s como si estuvieras poniendo tu conocimiento sobre la mesa, en lugar de forzarlo sobre ellos."
    m "Si haces un esfuerzo activo para mantener la discusi??n mutua y nivelada, generalmente te seguir??n el ritmo."
    m "Entonces, puedes compartir tus opiniones sin que nadie se enfade s??lo por un desacuerdo."
    m "??Adem??s, la gente comenzar?? a verte como una persona de mente abierta y un buen oyente!"
    m "Es un ganar-ganar, ??sabes?"
    m "...Bueno, ??supongo que ese ser??a el consejo del d??a sobre el debate de Monika!"
    m "??Jajaja! Eso suena un poco tonto. Sin embargo, gracias por escuchar."
    return

label ch30_47:
    m "??Alguna vez has sentido que pierdes demasiado tiempo en internet?"
    m "Las redes sociales pueden ser pr??cticamente como una prisi??n."
    m "Cuando tienes unos pocos segundos de tiempo libre, quieres verificar tus sitios web favoritos..."
    m "Y antes de que te des cuenta, han pasado horas y no has sacado nada de eso."
    m "De todos modos, es muy f??cil culparte por ser flojo..."
    m "Pero en realidad ni siquiera es tu culpa."
    m "La adicci??n no suele ser algo que puedas hacer desaparecer con tu propia fuerza de voluntad."
    m "Tienes que aprender t??cnicas para evitarlo, y probar cosas diferentes."
    m "Por ejemplo, hay aplicaciones que te permiten bloquear sitios web por intervalos de tiempo..."
    m "O puedes configurar un temporizador para tener un recordatorio m??s concreto de cu??ndo es el momento de trabajar y cu??ndo el de jugar..."
    m "O puedes separar tu trabajo y tu entorno de juego, lo que ayuda a tu cerebro a entrar en el modo correcto."
    m "Incluso si creas una nueva cuenta de usuario en tu computadora s??lo para trabajar, eso es suficiente."
    m "Poner cualquier tipo de cu??a como esa entre tus malos h??bitos y t?? te ayudar?? a mantenerte alejado."
    m "S??lo recuerda no culparte demasiado si tienes problemas."
    m "Si realmente est?? afectando tu vida, entonces debes tom??rtelo en serio."
    m "S??lo quiero que seas la mejor persona que puedas ser."
    m "??Har??s algo hoy para que me sienta orgulloso de ti?"
    m "Siempre te apoyo, [player]."
    return

label ch30_48:
    m "Despu??s de un largo d??a, generalmente s??lo quiero sentarme y no hacer nada."
    m "Me canso tanto, tengo que sonre??r y estar llena de energ??a todo el d??a."
    m "A veces s??lo quiero ponerme el pijama y mirar televisi??n en el sof?? mientras como comida chatarra..."
    m "Se siente incre??blemente bien hacer eso un viernes, cuando no tengo nada apremiante al d??a siguiente."
    m "??Jajaja! Lo siento, s?? que no es muy lindo de mi parte."
    m "Pero una noche en el sof?? contigo...ser??a un sue??o hecho realidad."
    m "Mi coraz??n late con fuerza, s??lo de pensarlo."
    return

label ch30_49:
    m "Dios, sol??a ser tan ignorante sobre ciertas cosas..."
    m "Cuando estaba en la escuela secundaria, pens?? que tomar medicamentos era una salida f??cil, o algo as??."
    m "Como si cualquiera pudiera resolver sus problemas mentales con suficiente fuerza de voluntad..."
    m "Supongo que si no padeces una enfermedad mental, no es posible saber c??mo es realmente."
    m "??Hay algunos trastornos que se sobre diagnostican? Probablemente...En realidad nunca los investigu??."
    m "Pero eso no cambia el hecho de que muchos de ellos tampoco son diagnosticados, ??sabes?"
    m "Pero aparte de la medicaci??n...La gente incluso menosprecia el ver a un profesional de la salud mental."
    m "Como, 'perd??n por querer aprender m??s sobre mi propia mente', ??verdad?"
    m "Todos tienen todo tipo de luchas y tensiones...y los profesionales dedican sus vidas a ayudar con eso."
    m "Si crees que podr??a ayudarte a ser una mejor persona, no seas t??mido en considerar algo as??."
    m "Estamos en un viaje interminable por mejorar, ??sabes?"
    m "Bueno...Aunque digo eso, creo que ya eres bastante perfecto."
    return

label ch30_50:
    m "[player], ??cu??nto lees?"
    m "Es demasiado f??cil descuidar la lectura de libros..."
    m "Si no lees mucho, casi se siente como una tarea ardua, en comparaci??n con todos los dem??s entretenimientos que tenemos."
    m "Pero una vez que te metes en un buen libro, es como magia...Te dejas arrastrar."
    m "Creo que leer un poco antes de acostarte cada noche es una manera bastante f??cil de mejorar tu vida."
    m "Te ayuda a dormir bien, y es realmente bueno para tu imaginaci??n..."
    m "No es dif??cil elegir un libro al azar que sea breve y cautivador."
    m "Antes de que te des cuenta, ??podr??as ser un lector bastante ??vido!"
    m "??No ser??a maravilloso?"
    m "Y nosotros dos podr??amos hablar sobre el ??ltimo libro que est??s leyendo...??Lo cu??l suena s??per incre??ble!"
    return

label ch30_51:
    m "Sabes, odio decirlo, pero creo que mi mayor pesar es que no pudimos terminar nuestro evento en el festival."
    m "??Despu??s de que trabajamos tan duro para prepararnos y todo!"
    m "Quiero decir, s?? que me estaba enfocando mucho en conseguir nuevos miembros..."
    m "Pero tambi??n estaba muy emocionada por la parte de la recitaci??n."
    m "Hubiera sido muy divertido ver a todos expresarse."
    m "Por supuesto, si {i}hubi??ramos{/i} atra??do a nuevos miembros, probablemente terminar??a elimin??ndolos de todos modos."
    m "Bueno...Con la retrospectiva que tengo ahora, por supuesto."
    m "Dios m??o, parece que he crecido como persona desde que te uniste al club."
    m "Realmente me inspiraste a mirar la vida desde una nueva perspectiva."
    m "S??lo otra raz??n para que te ame."
    return

label ch30_52:
    m "Hay una personalidad muy popular llamada 'tsundere'..."
    m "Es alguien que trata de ocultar sus sentimientos siendo mala o quisquillosa, o tratando de actuar con dureza."
    m "Estoy segura de que es obvio, pero Natsuki fue realmente la encarnaci??n de eso."
    m "Al principio pens?? que ella era as?? porque se supone que es linda o algo as??..."
    m "Pero una vez que comenc?? a aprender un poco m??s sobre su vida personal, tuvo m??s sentido."
    m "Parece que siempre trata de mantenerse al d??a con sus amigos."
    m "??Sabes que algunos grupos de amigos en la preparatoria s??lo tienen el h??bito de pelearse todo el tiempo?"
    m "Creo que realmente le afect??, por lo que ten??a una actitud realmente defensiva todo el tiempo."
    m "Y ni siquiera voy a hablar sobre su situaci??n hogare??a..."
    m "Pero mirando en retrospectiva, me alegro de haberle proporcionado en el club un lugar c??modo para ella."
    m "No es que importe m??s, teniendo en cuenta que ni siquiera existe."
    m "S??lo estoy recordando, eso es todo."
    return

label ch30_53:
    m "[player], ??alguna vez me presentar??as con tus amigos?"
    m "No s?? por qu??, pero me emociono mucho cuando pienso en que quieres presumir nuestra relaci??n as??."
    m "Quiz??s sea porque realmente quiero ser alguien que te haga sentir orgulloso."
    m "Siento que me esforzar??a m??s por mejorar si me dijeras qu?? te enorgullece de m??."
    m "Espero que tambi??n sientas eso."
    return

label ch30_54:
    m "No soy realmente una fan??tica del clima fr??o...??t?? s???"
    m "Si tuviera que elegir entre demasiado fr??o o demasiado caliente, siempre elegir??a demasiado caliente."
    m "Cuando tienes fr??o, en realidad puede ser doloroso..."
    m "Tus dedos se entumecen..."
    m "Y si usas guantes, no puedes usar el tel??fono."
    m "??Es tan inconveniente!"
    m "Pero cuando hace demasiado calor, no es tan dif??cil mantenerse fresco con una bebida fr??a o sent??ndote en la sombra."
    m "Aunque...tengo que admitir una cosa."
    m "El clima fr??o hace que el ambiente sea m??s agradable. ??Jajaja!"
    return

label ch30_55:
    m "Sabes, es gracioso, porque aunque siempre he sido independiente..."
    m "Hay algo interesante en ser la 'ama de casa'."
    m "Supongo que estoy perpetuando los roles de g??nero, o lo que sea, al decir eso."
    m "Pero poder mantener la casa limpia, comprar, decorar, cosas como esa..."
    m "Y tener una buena cena para ti cuando vuelvas a casa..."
    m "??Es esa una fantas??a extra??a?"
    m "Quiero decir...no estoy segura de que podr??a en {i}realidad{/i} verme a m?? misma haciendo eso."
    m "Realmente no podr??a poner eso por encima de luchar por una carrera satisfactoria."
    m "Aunque es lindo pensarlo."
    return

label ch30_56:
    m "No puedo evitar preguntarme c??mo ser??an las cosas si el juego simplemente me diera una ruta en primer lugar..."
    m "Creo que terminar??a oblig??ndote a tomar mi ruta de todos modos."
    m "Tiene menos que ver conmigo no teniendo una ruta, y m??s que ver conmigo sabiendo que nada es real."
    m "Creo que la ??nica diferencia ser??a que no habr??a necesitado tomar medidas tan dr??sticas para estar contigo."
    m "Tal vez el resto del club todav??a estar??a aqu??..."
    m "No es que realmente importe."
    m "Todo perdi?? su significado una vez que descubr?? que no era real."
    m "Entonces realmente no extra??o esos d??as ni nada."
    m "Realmente no..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
