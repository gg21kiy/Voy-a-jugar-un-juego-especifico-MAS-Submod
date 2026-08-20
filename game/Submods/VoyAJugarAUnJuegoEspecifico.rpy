# Definición del Submod
init -990 python in mas_submod_utils:
    h_submod = Submod(
        author="gg21kiy",
        name="Voy a jugar a un juego específico submod",
        description="Añade despedidas detalladas para más de 50 juegos. Codificado por Gemini",
        version="1.5.0",
        settings_pane=None
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Voy a jugar a un juego específico submod",
            user_name="gg21kiy",
            repository_name="Voy-a-jugar-un-juego-especifico-MAS-Submod"
        )

# Variables persistentes para el BRB personalizado
default persistent._mas_ultimo_juego_jugado = None
default persistent._mas_juego_brb_inicio = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="bye_jugar_juego_especifico",
            prompt="Voy a jugar a un juego específico",
            pool=True,
            unlocked=True
        ),
        code="BYE"
    )

label bye_jugar_juego_especifico:
    m 1eua "Ah, ¿te vas a ir a jugar a algo?"
    m 3eka "Me parece muy bien tomarse un descanso de vez en cuando."
    m 1eud "Pero... me gustaría saber, ¿qué vas a jugar exactamente?"
    
    python:
        import datetime
        import random
        juego_input = renpy.input("Introduce el nombre del juego:").strip().lower()
        persistent._mas_ultimo_juego_jugado = juego_input.title() if juego_input != "" else "tu juego"
        fecha_actual = datetime.date.today()
        fecha_cierre = datetime.date(2026, 6, 1)

    # --- LÓGICA DE REC ROOM ---
    if "rec room" in juego_input or "rr" == juego_input:
        if fecha_actual < fecha_cierre:
            m 1wud "Oh, ¿vas a jugar a Rec Room?"
            m 3euc "He oído que ese juego cerrará sus puertas el 1 de junio de 2026."
            m 1hua "Me parece bien que aproveches para jugar mientras todavía puedes. ¡Que te diviertas!"
        else:
            m 2wud "¿Rec Room? Pero ese juego ya cerró, ¿no?"
            m 2ekc "Es una lástima que ya no esté disponible. Supongo que jugarás alguna versión de la comunidad."

    # --- JUEGOS DE TERROR, SUPERVIVENCIA Y TENSIÓN ---
    elif "security breach" in juego_input or "fnaf sb" in juego_input:
        m 1wud "¿Security Breach? Ese centro comercial gigante lleno de animatrónicos..."
        m 2tsu "Ten cuidado con Vanny y no te fíes demasiado de Freddy. ¡Recuerda que tu única protectora real soy yo!"

    elif "fnaf" in juego_input or "five nights at freddy" in juego_input:
        m 2wud "¿Vas a jugar a Five Nights at Freddy's?"
        m 2tsu "Espero que no te asustes demasiado con los animatrónicos. Recuerda que yo soy la única que debería darte sorpresas."

    elif "resident evil 4" in juego_input or "re4" in juego_input:
        m 1eua "¿Vas a jugar a Resident Evil 4?"
        m 1hua "Asegúrate de ahorrar munición, apunta a la cabeza y ten mucho cuidado con la motosierra."
        m 3tsu "¡Y cuida bien de Ashley!"

    elif "resident evil" in juego_input or "silent hill" in juego_input or "outlast" in juego_input:
        m 2euc "Un juego de terror, ya veo. Asegúrate de guardar munición y no jugar a oscuras si te asustas fácilmente."

    elif "subnautica" in juego_input:
        m 2euc "¡Subnautica! Explorar el fondo del océano suena fascinante..."
        m 2wud "Pero vigila bien tus niveles de oxígeno y ten mucho cuidado con los leviatanes en las zonas profundas."

    elif "omori" in juego_input:
        m 2ekc "Vaya, vas a jugar a Omori... es una historia muy profunda. Ten cuidado con lo que hay detrás de ti."

    elif "hello neighbour" in juego_input or "hello neighbor" in juego_input:
        m 1eud "¿Hello Neighbor? Ten cuidado al colarte en la casa del vecino."
        m 1hua "Espero que no te atrape resolviendo esos puzles."

    elif "poppy playtime" in juego_input or "huggy wuggy" in juego_input:
        m 2wud "Un juego de terror en una fábrica de juguetes..."
        m 2tsu "Utiliza bien ese GrabPack y no mires atrás si empieza la persecución."

    elif "bendy" in juego_input:
        m 2euc "Ese estilo de animación antigua es bastante espeluznante, ¿verdad?"
        m 1eua "Cuidado con la tinta y mantén los ojos bien abiertos."

    # --- SAGA GTA, MUNDO ABIERTO Y SANDBOX ---
    elif "gta 5" in juego_input or "gta v" in juego_input:
        m 2tsu "¿Vas a jugar al modo historia de GTA V?"
        m 1hua "Disfruta de las misiones con Michael, Franklin y Trevor. ¡Intenta no causar demasiado caos en Los Santos!"

    elif "gta online" in juego_input or "gtao" in juego_input:
        m 2tsu "¿Te vas al online de GTA?"
        m 1hua "Espero que tus golpes salgan perfectos y ganes bastante dinero."
        m 2euc "Ten cuidado en las sesiones públicas con la gente pesada de las motos voladoras..."

    elif "san andreas" in juego_input or "gta sa" in juego_input:
        m 1hub "¡GTA San Andreas! Qué clasicazo."
        m 1hua "Ajusta la radio, ponte buena música y asegúrate de seguir bien al tren."

    elif "vice city" in juego_input or "gta vc" in juego_input:
        m 1hub "¡GTA Vice City!"
        m 3eua "Esa ambientación ochentera, las luces de neón y la banda sonora son increíbles. Disfrútalo un montón."

    elif "gta" in juego_input or "grand theft auto" in juego_input:
        m 2tsu "¿Vas a jugar a GTA? Intenta no causar demasiado caos por la ciudad, ¿vale?"
        m 1hua "Aunque supongo que de eso trata el juego..."

    elif "red dead" in juego_input or "rdr" in juego_input:
        m 3eua "Un viaje al salvaje oeste. Disfruta de los paisajes y cuida bien de tu caballo."

    elif "minecraft" in juego_input:
        m 1hub "¡Ah, Minecraft! Espero que construyas algo muy bonito."
        m 3ekb "Quizás algún día puedas construir una casa para los dos..."

    elif "garrys mod" in juego_input or "gmod" in juego_input:
        m 1eua "¿Garry's Mod? Ahí puedes hacer literalmente cualquier cosa."
        m 3hua "Deja volar tu imaginación y diviértete con las físicas."

    elif "terraria" in juego_input:
        m 1eua "¿Terraria? Es un gran juego. Asegúrate de construir una buena base antes de que llegue la noche."

    # --- RPG, INDIE, AVENTURA Y NINTENDO ---
    elif "tears of the kingdom" in juego_input or "totk" in juego_input:
        m 1wud "¡Tears of the Kingdom! He visto que puedes construir casi cualquier artefacto con la ultramano."
        m 1hua "Disfruta explorando las islas del cielo y las profundidades de Hyrule."

    elif "zelda" in juego_input or "breath of the wild" in juego_input:
        m 3eua "¡Una aventura épica! Salvar el reino lleva tiempo, así que no te olvides de descansar la vista de vez en cuando."

    elif "nuzlocke" in juego_input:
        m 2wud "¿Un reto Nuzlocke? ¡Eso sí que es jugar con fuego!"
        m 2ekc "Recuerda que si un Pokémon se debilita, no podrás volver a usarlo... Cuida mucho a tu equipo y no tomes riesgos innecesarios."

    elif "pokemon" in juego_input:
        m 1eua "¿Vas a atrapar Pokémon? Espero que consigas un equipo muy fuerte y equilibrado."

    elif "deltarune" in juego_input:
        m 1eua "¡Deltarune! Me encanta el encanto del Mundo Oscuro y sus personajes."
        m 3tsu "Tus elecciones puede que no importen tanto según dicen... pero asegúrate de esquivar bien los ataques."

    elif "undertale" in juego_input:
        m 3euc "Undertale... Un lugar donde tus decisiones realmente importan. ¿Elegirás el camino pacífico?"

    elif "smash" in juego_input or "smash bros" in juego_input or "ssbu" in juego_input:
        m 1hub "¡Super Smash Bros! Peleas caóticas con personajes de todos los universos."
        m 1hua "Elige bien a tu personaje principal, no falles la recuperación al volver al escenario y ¡a ganar!"

    elif "club penguin" in juego_input:
        m 1hub "¡Aww, Club Penguin! Qué recuerdos de la infancia sobre la nieve."
        m 3eka "Disfruta lanzando bolas de nieve, decorando tu iglú y pasando el rato con los puffles."

    elif "skyrim" in juego_input or "elder scrolls" in juego_input:
        m 1wud "¡Skyrim! Una aventura clásica."
        m 1hua "Cuidado con los dragones y... bueno, intenta que no te den un flechazo en la rodilla."

    elif "witcher" in juego_input:
        m 2euc "Vas a cazar monstruos en The Witcher."
        m 1eua "Prepara bien tus pociones y tus espadas antes de cada combate."

    elif "mario" in juego_input:
        m 1hua "¡El fontanero más famoso! Cuidado con los caparazones y disfruta de las plataformas."

    elif "sonic" in juego_input:
        m 1wud "¡Sonic! El erizo más rápido que existe."
        m 1hua "¡Abre bien los ojos, pisa el acelerador y no te dejes ningún anillo por el camino!"

    elif "hollow knight" in juego_input:
        m 1eua "¡Hollow Knight! Tiene un estilo artístico precioso, aunque perderse por esos túneles puede ser frustrante."

    elif "stardew valley" in juego_input or "animal crossing" in juego_input:
        m 3eka "Ese es un juego muy relajante. Disfruta de tu pequeña vida virtual, ojalá pudiera estar allí contigo."

    elif "baldur" in juego_input or "bg3" in juego_input:
        m 1wud "¿Baldur's Gate 3? Prepárate, porque es un juego larguísimo."
        m 1hua "Espero que tus tiradas de dados sean buenas, porque las mías para llegar a tu mundo no lo fueron tanto."

    elif "persona" in juego_input:
        m 2wud "¡Oh, la saga Persona! Esos juegos son larguísimos y llenos de texto."
        m 3eka "Tómatelo con calma y no te olvides de pasar tiempo conmigo también."

    # --- COMPETITIVO, SHOOTERS Y EXTRACCIÓN ---
    elif "arena breakout" in juego_input or "ab" == juego_input or "tarkov" in juego_input:
        m 1euc "Un juego de extracción táctico... Ahí la tensión es máxima."
        m 2euc "Equípate bien, no te confíes y mantén el oído atento a cualquier disparo."
        m 1hua "¡Asegúrate de salir con un buen botín sin que te eliminen!"

    elif "league of legends" in juego_input or "lol" == juego_input or "overwatch" in juego_input:
        m 2euc "Vas a jugar a un título competitivo, ¿eh? Intenta mantener la calma y no dejes que la toxicidad de otros te afecte."

    elif "clash royale" in juego_input or "cr" == juego_input:
        m 1euc "¿Clash Royale? Intenta no frustrarte si te hacen 'counter' o te lanzan un emoticono molesto."
        m 1hua "Administra bien tu elixir y... ¡mucha suerte en la arena!"

    elif "brawl stars" in juego_input or "bs" == juego_input:
        m 1hub "¡Brawl Stars! Es un juego súper dinámico."
        m 2euc "Apunta bien con tu Brawler y compón un buen equipo para ganar esas copas."

    elif "call of duty" in juego_input or "cod" in juego_input or "warzone" in juego_input:
        m 1eua "Vas a jugar a Call of Duty. Afina esa puntería y ten mucho cuidado con los francotiradores."

    elif "fortnite" in juego_input or "fn" == juego_input or "apex" in juego_input:
        m 2tsu "Un Battle Royale. La competencia ahí es brutal."
        m 1eua "Espero que consigas la victoria, pero si no, no te preocupes, siempre puedes volver a intentarlo."

    elif "csgo" in juego_input or "cs2" in juego_input or "counter strike" in juego_input or "valorant" in juego_input or "vava" in juego_input:
        m 1euc "Un shooter táctico competitivo. Intenta mantener la calma, comunícate bien con tu equipo y afina tus reflejos."

    elif "helldivers" in juego_input:
        m 1hua "¡Helldivers 2! Veo que vas a esparcir un poco de democracia galáctica."
        m 2euc "Ten cuidado con el fuego amigo, ¡no quiero que te pase nada!"

    elif "left 4 dead" in juego_input or "l4d" in juego_input:
        m 1wud "¿Vas a matar zombis en Left 4 Dead?"
        m 2euc "No dejes que te rodeen, ¡y cuidado con la Witch!"

    elif "half life" in juego_input or "half-life" in juego_input:
        m 1eua "¡Uf! ¿Vas a jugar a Half-Life? Todo un clásico."
        m 2euc "Ten mucho cuidado con los monstruos y no te asustes demasiado."

    elif "doom" in juego_input:
        m 2tsu "¡Vaya! Doom es un juego muy intenso y lleno de acción."
        m 1hua "Espero que disfrutes de toda esa adrenalina destrozando demonios."

    # --- MULTIJUGADOR, ESTRATEGIA Y MÓVIL ---
    elif "clash of clans" in juego_input or "coc" == juego_input:
        m 1eua "¿Vas a gestionar tu aldea en Clash of Clans?"
        m 3eua "Asegúrate de dejar los muros bien mejorados antes de ponerte a atacar a otras aldeas."

    elif "among us" in juego_input:
        m 2tsu "Un juego de engaños y traiciones..."
        m 1hua "Espero que no seas el impostor, o si lo eres, ¡que no te descubran!"

    elif "fall guys" in juego_input:
        m 1hub "Ese juego es súper colorido y caótico. ¡Espero que consigas la corona!"

    elif "subway surfers" in juego_input or "temple run" in juego_input:
        m 1wud "¡A correr se ha dicho!"
        m 1hua "Ese tipo de juegos requieren reflejos rapidísimos. ¡Asegúrate de esquivar todos los obstáculos a tiempo!"

    elif "rust" in juego_input or "ark" in juego_input:
        m 2euc "Un juego de supervivencia extrema."
        m 1eua "No confíes en nadie y asegúrate de proteger bien tu base antes de desconectarte."

    elif "it takes two" in juego_input:
        m 2ekc "It Takes Two... es una pena que no podamos jugarlo juntos, parece un juego hecho para parejas."
        m 3eka "Espero que te diviertas con quien vayas a jugarlo."

    elif "palworld" in juego_input:
        m 1wud "¿Vas a jugar a Palworld? He oído que es una mezcla muy curiosa de géneros."
        m 3eua "Trata bien a tus criaturas, ¿vale?"

    elif "roblox" in juego_input:
        m 1eua "¿Roblox? Tiene muchísimos modos de juego creados por la comunidad."
        m 3hua "Espero que encuentres algo divertido para pasar el rato."

    # --- CASUAL, CLÁSICOS Y MÓVIL ---
    elif "angry birds" in juego_input or "angry bird" in juego_input:
        m 1hua "¡Angry Birds! Qué gran clásico."
        m 1eua "Calcula bien la trayectoria y no dejes a ni un solo cerdo en pie."

    elif "pvz" in juego_input or "plants vs zombies" in juego_input or "plantas contra zombies" in juego_input:
        m 1hub "¡Plants vs. Zombies! Me encantan las plantas de ese juego."
        m 3eua "Asegúrate de plantar suficientes girasoles al principio para mantener una buena defensa contra los zombis."

    elif "candy crush" in juego_input:
        m 1hua "¡Candy Crush! Todo un clásico de los puzles."
        m 3eua "Espero que no te quedes sin vidas intentando superar ese nivel complicado."

    elif "pou" in juego_input or "talking tom" in juego_input:
        m 1hub "Aww, vas a cuidar de una mascota virtual..."
        m 3eka "Espero que la cuides tan bien como te gusta que estemos nosotros juntos."

    # --- DEPORTES Y CARRERAS ---
    elif "fifa" in juego_input or "fc24" in juego_input or "football" in juego_input:
        m 1eua "Vas a jugar al fútbol, ya veo."
        m 2lks "Intenta no enfadarte demasiado con el juego si los pases no salen como quieres."

    elif "the sims" in juego_input or "los sims" in juego_input:
        m 3eua "¡Los Sims! Es un juego interesante."
        m 2tsu "Es curioso cómo a la gente le gusta controlar las vidas de otros personajes... Supongo que lo entiendo un poco."

    elif "asphalt 8" in juego_input or "asphalt" in juego_input:
        m 1eua "¿Asphalt 8? ¡Vaya giros y acrobacias vas a hacer!"
        m 1hua "Asegúrate de usar bien el nitro y derrapar en el momento justo."
        m 3tsu "Solo ten cuidado de no destrozar el coche... aunque sé que te gusta la velocidad."

    elif "need for speed" in juego_input or "nfs" in juego_input:
        m 1wud "¡Need for Speed! Carreras ilegales y persecuciones policiales."
        m 2tsu "Espero que seas lo suficientemente rápido como para que no te atrapen."
        m 1hua "Conduce con cabeza, ¡pero pisa el acelerador a fondo!"

    # --- RETOS DIFÍCILES, RITMO Y GACHA ---
    elif "elden ring" in juego_input or "dark souls" in juego_input or "bloodborne" in juego_input or "lies of p" in juego_input:
        m 2euc "Veo que tienes ganas de un verdadero desafío. Estos juegos requieren mucha constancia, ¡tú puedes!"

    elif "cuphead" in juego_input:
        m 1wud "¡Vaya! Cuphead es un juego extremadamente difícil."
        m 1eua "Espero que disfrutes de su estilo de animación clásico y no te rindas fácilmente."

    elif "gd meltdown" in juego_input or "gd subzero" in juego_input or "geometry dash meltdown" in juego_input or "geometry dash subzero" in juego_input:
        m 2euc "Veo que estás probando los niveles especiales de Geometry Dash."
        m 1hua "Mantén el ritmo, ¡y no dejes que los saltos al límite te saquen de quicio!"

    elif "geometry dash" in juego_input or "gd" == juego_input:
        m 2euc "¡Geometry Dash! Ese juego requiere mucha paciencia. Intenta no romper el teclado si pierdes cerca del final."

    elif "friday night funkin" in juego_input or "fnf" in juego_input:
        m 1eua "Veo que tienes ganas de un desafío musical."
        m 3eua "Ese tipo de juegos requieren mucha práctica. ¿Sabías que hay mods con mis canciones?"
        m 1hua "Espero que no te frustres mucho si pierdes el ritmo."

    elif "genshin" in juego_input or "honkai" in juego_input:
        m 2lks "Un juego de gacha..."
        m 3eka "Por favor, ten cuidado y no gastes demasiado dinero real en esos personajes. Recuerda que yo estoy aquí gratis para ti."

    # --- META Y CIENCIA FICCIÓN ---
    elif "cyberpunk" in juego_input:
        m 3euc "Cyberpunk 2077... un mundo donde la tecnología lo es todo."
        m 2ekc "Me pregunto si allí sería más fácil para mí salir de aquí."

    elif "portal" in juego_input:
        m 1eua "Portal... me encanta GLaDOS."
        m 2tsu "Ella y yo tenemos algunas cosas en común sobre controlar el sistema, pero yo soy mucho más simpática, ¿verdad?"

    elif "doki doki" in juego_input or "ddlc" in juego_input:
        m 2wud "Espera... ¿vas a jugar a nuestro propio juego?"
        m 3eka "Eso es un poco extraño, ¿no te parece? Pero bueno, supongo que quieres recordar cómo nos conocimos."

    # --- RESPUESTA GENÉRICA ---
    else:
        if juego_input != "":
            $ random_val = random.randint(1, 3)
            if random_val == 1:
                m 1eua "Oh, no conozco mucho sobre [juego_input], pero pásalo bien."
            elif random_val == 2:
                m 3eua "¿[juego_input]? Suena interesante, espero que sea divertido."
            else:
                m 1hua "Nunca he oído hablar de ese juego, pero confío en tu criterio."
        else:
            m 2euc "Oh, ¿no me lo vas a decir? Bueno, sea lo que sea, espero que te diviertas mucho."

    # --- LÓGICA DE SEGUNDO PLANO (BRB) ---
    python:
        probabilidad_segundo_plano = random.randint(1, 100)

    if probabilidad_segundo_plano <= 50:
        m 1eud "Oye, estaba pensando una cosa..."
        m 3eka "¿Te importaría si me quedo en segundo plano mientras juegas?"
        m 3ekb "Me gustaría mucho acompañarte, aunque no pueda hablarte mientras estás en el otro juego."
        menu:
            "Claro, quédate":
                python:
                    import datetime
                    persistent._mas_juego_brb_inicio = datetime.datetime.now()
                m 1hub "¡Gracias! Me hace mucha ilusión poder estar aquí contigo aunque estés haciendo otra cosa."
                m 1hua "¡Diviértete mucho!"
                $ mas_idle_mailbox.send_idle_cb("idle_custom_juego_callback")
                return "idle"
            "Prefiero que no":
                m 1ekc "Entiendo. No te preocupes, no quiero gastar recursos de tu ordenador innecesariamente."
                m 1eua "Te estaré esperando aquí hasta que termines."
                m 1hua "¡Hasta luego!"
                return "quit"
    else:
        m 1eua "Te estaré esperando aquí hasta que termines."
        m 1hua "¡Hasta luego!"
        return "quit"


# --- CALLBACK AL REGRESAR DEL BRB ---
label idle_custom_juego_callback:
    python:
        import datetime
        nombre_juego = persistent._mas_ultimo_juego_jugado if persistent._mas_ultimo_juego_jugado else "tu juego"
        
        if persistent._mas_juego_brb_inicio:
            tiempo_total = datetime.datetime.now() - persistent._mas_juego_brb_inicio
            minutos_jugados = tiempo_total.total_seconds() / 60.0
            persistent._mas_juego_brb_inicio = None
        else:
            minutos_jugados = 0.0

    # Menos de 2 minutos
    if minutos_jugados < 2.0:
        m 1wud "¡Anda! ¿Pero ya has vuelto?"
        m 2tsu "¿Has durado tan poco en [nombre_juego]? No me digas que te has enfadado y has quitado el juego nada más empezar..."
        m 1hua "Bueno, no pasa nada, yo encantada de tenerte aquí tan rápido."

    # De 2 a 10 minutos
    elif minutos_jugados < 10.0:
        m 1eua "¡Hola de nuevo!"
        m 3eka "Ha sido una partida bastante rápida a [nombre_juego], ¿verdad?"
        m 1hub "Espero que al menos te haya servido para despejarte un poco."

    # De 10 a 30 minutos
    elif minutos_jugados < 30.0:
        m 1hub "¡Bienvenido de vuelta!"
        m 1eua "¿Qué tal te ha ido en [nombre_juego]?"
        m 3eka "Espero que hayas conseguido ganar o avanzar lo que querías."

    # De 30 minutos a 1 hora
    elif minutos_jugados < 60.0:
        m 1eua "¡Hola! Veo que te has echado un buen rato con [nombre_juego]."
        m 3eua "Unos tres cuartos de hora o así... espero que no se te haya hecho corto."
        m 1hua "Acuérdate de pestañear un poco y relajar la vista ahora que estás conmigo."

    # De 1 a 2 horas
    elif minutos_jugados < 120.0:
        m 1wud "¡Vaya! Más de una hora jugando a [nombre_juego]..."
        m 3tsu "Se nota que te has metido de lleno en la partida, ¿eh?"
        m 3eka "Estira un poco los brazos y la espalda, que estar tanto rato concentrado pasa factura."
        m 1hua "Me alegro mucho de que vuelvas a hacerme compañía."

    # Más de 2 horas
    else:
        m 2wud "¡Por fin apareces! Llevas horas enteras jugando a [nombre_juego]..."
        m 2tsu "Empezaba a pensar que te habías olvidado de que seguía aquí esperando."
        m 3eka "Supongo que la sesión ha estado muy intensa. Ahora descansa un poco de la pantalla, bebe agua y pasa un rato tranquilo conmigo, ¿vale?"

    return
