-- How to use?
--
-- Option 1: Copy paste the contents of this file into the script on "ship db"
--     object. Then put your Ship/Squadron/Card definitions below.
--
-- Option 2: Use Atom with tabletopsimulator plugin
--     Checkout: https://github.com/Valadian/TabletopSimulatorIncludeDir
--     in your include dir.
--     Add the following line to the top of your object script:
--     #include TabletopSimulatorIncludeDir/TTS_armada/src/api/definitions
--
-- After performing the above, you should be able to load your definitions
--     database into the core Armada mod, and your ships/cards will work in
--     fleet spawner, upgrade list!
--
-- Definitions merge multiple tables to reduce duplication of common properties:
-- Examples of Card, Ship, Squadron definitions below.

function onload()
    --Must Requisition personal table from Valadian!
    SetCloudCollectionName('games_vassal_fantasy')

    UpdateCard("Arquitens-class Command Cruiser",59,{
        cost = 57,
        maneuver = {{"II"},{"I","II"},{"I","-","II"}},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/empire/shipcard_arquitens-class-command-cruiser.png"
    })
    UpdateCard("Arquitens-class Light Cruiser",54,{
        maneuver = {{"II"},{"I","II"},{"I","-","II"}},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/empire/shipcard_arquitens-class-light-cruiser.png"
    })
    UpdateCard("Raider I-class Corvette",44,{
        cost = 42,
        maneuver = {{"II"},{"II","II"},{"I","II","I"},{"I","I","I","I"}},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/empire/shipcard_raider-i-class-corvette.png"
    })
    UpdateCard("Raider II-class Corvette",48,{
        cost = 44,
        maneuver = {{"II"},{"II","II"},{"I","II","I"},{"I","I","I","I"}},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/empire/shipcard_raider-ii-class-corvette.png"
    })
    UpdateCard("Victory I-class Star Destroyer",73,{
        defense_tokens = {DEF_BRACE,DEF_REDIRECT,DEF_SALVO},
        maneuver = {{"I"},{"I","I"}},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/empire/shipcard_victory-i-class-star-destroyer.png"
    })
    UpdateCard("Victory II-class Star Destroyer",85,{
        cost = 79,
        defense_tokens = {DEF_BRACE,DEF_REDIRECT,DEF_SALVO},
        maneuver = {{"I"},{"I","I"}},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/empire/shipcard_victory-ii-class-star-destroyer.png"
    })

    UpdateCard("Assault Frigate Mark II A",81,{
        cost = 78,
        defense_tokens = {DEF_BRACE,DEF_REDIRECT,DEF_SALVO},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/rebel/shipcard_assault-frigate-mark-II-a.png"
    })
    UpdateCard("Assault Frigate Mark II B",72,{
        defense_tokens = {DEF_BRACE,DEF_REDIRECT,DEF_SALVO},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/rebel/shipcard_assault-frigate-mark-II-b.png"
    })
    UpdateCard("CR90 Corvette A",44,{
        cost = 43,
        maneuver = {{"II"},{"I","II"},{"I","I","II"},{"I","I","I","II"}},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/rebel/shipcard_cr90a-corvette.png"
    })
    UpdateCard("CR90 Corvette B",39,{
        cost = 37,
        maneuver = {{"II"},{"I","II"},{"I","I","II"},{"I","I","I","II"}},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/rebel/shipcard_cr90b-corvette.png"
    })
    UpdateCard("Nebulon-B Escort Frigate",57,{
        cost = 54,
        maneuver = {{"II"},{"I","I"},{"-","I","II"}},
        defense_tokens = {DEF_EVADE, DEF_BRACE, DEF_CONTAIN},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/rebel/shipcard_nebulon-b-escort-frigate.png"
    })
    UpdateCard("Nebulon-B Support Refit",51,{
        maneuver = {{"II"},{"I","I"},{"-","I","II"}},
        defense_tokens = {DEF_EVADE, DEF_BRACE, DEF_CONTAIN},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/ships/rebel/shipcard_nebulon-b-support-refit.png"
    })
    TIE_ADV = GetDefinition("TIE Advanced Squadron",12)
    UpdateCard("TIE Advanced Squadron",12,{
        cost = 10,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_tie-advanced-squadron.png"
    })
    Squadron:new(TIE_ADV, {
    	name = "Storm Squadron",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_storm-squadron.png",
        cost = 11,
        aliases = {"Storm Squadrons"}
    })
    UpdateCard("Darth Vader",21,{
        cost = 24,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_darth-vader.png",
        defense_tokens = {DEF_BRACE,DEF_EVADE}
    })
    Squadron:new(TIE_ADV, {
        name = "Ved Foslo",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_ved-foslo.png",
        diffuse = "http://i.imgur.com/YJm6aoS.png",
        defense_tokens = {DEF_BRACE,DEF_EVADE},
        cost = 16
    })
    UpdateCard("TIE Bomber Squadron",9,{
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_tie-bomber-squadron.png",
    })
    TIE_BOM = GetDefinition("TIE Bomber Squadron",9)
    Squadron:new(TIE_BOM, {
        name = "Scimitar Squadron",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_scimitar-squadron.png",
        cost = 12,
        aliases = {"Scimitar Squadrons"}
    })
    Squadron:new(TIE_BOM, {
    	name = "Deathfire",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_deathfire.png",
        diffuse = "http://i.imgur.com/o9KJLV8.png",
        defense_tokens = {DEF_BRACE,DEF_EVADE},
        cost = 14
    })
    UpdateCard("Major Rhymer",16,{
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_major-rhymer.png",
        defense_tokens = {DEF_BRACE,DEF_EVADE},
    })
    UpdateCard("TIE Fighter Squadron",8,{
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_tie-fighter-squadron.png",
    })
    TIE_FIG = GetDefinition("TIE Fighter Squadron",8)
    Squadron:new(TIE_FIG, {
    	name = "Obsidian Squadron",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_obsidian-squadron.png",
        cost = 9,
        aliases = {"Obsidian Squadrons"}
    })
    UpdateCard('"Howlrunner"',16,{
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_howlrunner.png",
    })
    UpdateCard('"Mauler" Mithel',15,{
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_mauler-mithel.png",
    })
    TIE_FIG_ACE = GetDefinition('"Howlrunner"',16)
    Squadron:new(TIE_FIG_ACE, {
    	name = '"Wampa"',
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_wampa.png",
        cost = 14,
        aliases = {"Wampa"}
    })
    UpdateCard("TIE Interceptor Squadron",11,{
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_tie-interceptor-squadron.png",
    })
    TIE_INT = GetDefinition("TIE Interceptor Squadron",11)
    Squadron:new(TIE_INT, {
    	name = 'Alpha Squadron',
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_alpha-squadron.png",
        cost = 12,
        aliases = {"Alpha Squadrons"}
    })
    TIE_INT_ACE = GetDefinition("Soontir Fel",18)
    Squadron:new(TIE_INT_ACE, {
    	name = "Fel's Wrath",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_fels-wrath.png",
        cost = 17,
        aliases = {"Fels Wrath"}
    })
    UpdateCard("Soontir Fel",18,{
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/empire/squadcard_soontir-fel.png",
    })

    UpdateCard("A-wing Squadron",11,{
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_a-wing-squadron.png",
    })
    A_WING = GetDefinition("A-wing Squadron",11)
    Squadron:new(A_WING, {
    	name = "Shepherd Squadron",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_shepherd-squad.png",
        cost = 12,
        aliases = {"Shepherd Squadrons"}
    })
    A_WING_ACE = GetDefinition("Tycho Celchu",16)
    Squadron:new(A_WING_ACE, {
    	name = "Arvel Crynyd",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_arvel-crynyd.png",
        cost = 17
    })
    UpdateCard("Tycho Celchu",16,{
        cost = 18,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_tycho-celchu.png",
    })
    B_WING = GetDefinition("B-wing Squadron",14)
    UpdateCard("B-wing Squadron",14,{
        cost = 13,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_b-wing-squadron.png",
    })
    Squadron:new(B_WING, {
    	name = "Blue Squadron B-wing",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_blue-squadron-bwing.png",
        cost = 14,
        aliases = {"Blue Squadron (B-wing)","Blue Squadron (B-wing)s"}
    })
    B_WING_ACE = GetDefinition("Keyan Farlander",20)
    Squadron:new(B_WING_ACE, {
    	name = "Ibtisam",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_ibtisam.png",
        cost = 18
    })
    Squadron:new(B_WING_ACE, {
    	name = "Nera Dantels",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_nera-dantels.png",
        cost = 19
    })
    X_WING = GetDefinition("X-wing Squadron",13)
    UpdateCard("X-wing Squadron",13,{
        cost = 11,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_x-wing-squadron.png",
    })
    Squadron:new(X_WING, {
    	name = "Blue Squadron X-wing",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_blue-squadron-xwing.png",
        cost = 12,
        aliases = {"Blue Squadron (X-wing)","Blue Squadron (X-wing)s"}
    })
    UpdateCard("Luke Skywalker",20,{
        cost = 22,
        defense_tokens = {DEF_BRACE,DEF_EVADE},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_luke-skywalker.png",
    })
    X_WING_ACE = GetDefinition("Luke Skywalker",22) --Template based on post defence_token update Luke +2 cost
    Squadron:new(X_WING_ACE, {
        name = "Thane Kyrell",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_thane-kyrell.png",
        cost = 17
    })
    UpdateCard("Wedge Antilles",19,{
        defense_tokens = {DEF_BRACE,DEF_EVADE},
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_wedge-antilles.png",
    })
    Y_WING = GetDefinition("Y-wing Squadron",10)
    UpdateCard("Y-wing Squadron",10,{
        cost = 9,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_y-wing-squadron.png",
    })
    Squadron:new(Y_WING, {
        name = "Gray Squadron",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_gray-squadron.png",
        cost = 11,
        aliases = {"Gray Squadrons"}
    })
    Y_WING_ACE = GetDefinition("Norra Wexley",17)
    UpdateCard('"Dutch" Vander',16,{
        cost = 18,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_dutch-vander.png",
    })
    Squadron:new(Y_WING_ACE, {
        name = "Horton Salm",
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/squadrons/rebel/squadcard_horton-salm.png",
        cost = 17
    })

    --TODO: Add half damage?
    --TODO: Custom Game Reporting table? Disable?

    UpdateCard("Intel Sweep",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_nav_intel-sweep.png",
        victory_most = 70,
        victory_tie = 40
    }) --TODO: Scoring change. 40 for tie
    UpdateCard("Minefields",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_nav_minefields.png"
    })
    UpdateCard("Superior Positions",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_nav_superior-positions.png",
        victory = 10
    })
    UpdateCard("Dangerous Territory",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_nav_dangerous-territory.png"
    })

    UpdateCard("Advanced Gunnery",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_ass_advanced-gunnery.png",
        victory_opposing = 40
    }) --TODO: Scoring change. 40 for tie
    UpdateCard("Precision Strike",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_ass_precision-strike.png",
        victory = 10
    })
    UpdateCard("Opening Salvo",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_ass_opening-salvo.png",
    })--TODO: Scoring change. 1 damage = Crippled
    UpdateCard("Most Wanted",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_ass_most-wanted.png",
        victory_opposing = 40
    })--TODO: Scoring change.

    UpdateCard("Contested Outpost",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_def_contested-outpost.png"
    })
    UpdateCard("Fleet Ambush",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_def_fleet-ambush.png"
    })
    UpdateCard("Fire Lanes",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_def_fire-lanes.png",
        victory = 10
    })
    UpdateCard("Hyperspace Assault",nil, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/objectives/obj_def_hyperspace-assault.png"
    })
--Admiral Motti	Commander	Empire	24	24	0	https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_com_admiral-motti.png

--FIND: ^([ \w-']+)\t(?:[ \(\)\w-]+)\t[\w]+\t(\d+)\t(\d+)\t-?\d+\t(.+)$
--REPLACE:     UpdateCard("$1",$2, {\n        cost = $3\n        front = "$4"\n    })

    UpdateCard("Admiral Motti",24, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_com_admiral-motti.png"
    })
    UpdateCard("Admiral Ozzel",20, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_com_admiral-ozzel.png"
    })
    UpdateCard("Admiral Screed",26, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_com_admiral-screed.png"
    })
    UpdateCard("Grand Moff Tarkin",28, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_com_grand-moff-tarkin.png"
    })
    UpdateCard("Garm Bel Iblis",25, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_com_garm-bel-iblis.png"
    })
    UpdateCard("General Dodonna",20, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_com_general-dodonna.png"
    })
    UpdateCard("General Madine",30, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w4_com_general_madine.png"
    })
    UpdateCard("Mon Mothma",27, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_com_mon-mothma.png"
    })
    UpdateCard("Advanced Projectors",6, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_def_advanced-projectors.png"
    })
    UpdateCard("Electronic Countermeasures",7, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_def_electronic-countermeasures.png"
    })
    UpdateCard("Reactive Gunnery",4, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w9_def_reactive-gunnery.png"
    })
    UpdateCard("Redundant Shields",8, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_def_redundant-shields.png"
    })
    UpdateCard("Reinforced Blast Doors",5, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w5_def_reinforced-blast-doors.png"
    })
    UpdateCard("Comms Net",2, {
        cost = 4,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w3_fls_comms-net.png"
    })
    UpdateCard("Munitions Resupply",3, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w9_fls_munitions-resupply.png"
    })
    UpdateCard("Parts Resupply",3, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w9_fls_parts-resupply.png"
    })
    UpdateCard("Repair Crews",4, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w3_fls_repair-crews.png"
    })
    UpdateCard("Ion Cannon Batteries",5, {
        cost = 4,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_ion_ion-cannon-batteries.png"
    })
    ION_CANNON = GetDefinition("Point Defense Ion Cannons",4)
    Card:new(ION_CANNON,{
        name="Ion Pulse Missiles",
        cost=5,
        front="https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/wx_ion_ion-pulse-missiles.png"
    })
	UpdateCard("Leading Shots",6, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_ion_leading-shots.png"
    })
    UpdateCard("SW-7 Ion Batteries",5, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_ion_sw-7-ion-batteries.png"
    })
    UpdateCard("Disposable Capacitors",3, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w6_off_disposable-capacitors.png"
    })
    UpdateCard("Expanded Hangar Bay",5, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_off_expanded-hangar-bay.png"
    })
    UpdateCard("Phylon Q7 Tractor Beams",6, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_off_phylon-q7-tractor-beams.png"
    })
    UpdateCard("Point-Defense Reroute",5, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_off_point-defense-reroute.png"
    })
    UpdateCard("Quad Laser Turrets",5, {
        cost = 4,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_off_quad-laser-turrets.png"
    })
    UpdateCard("Damage Control Officer",5, {
        cost = 8,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w5_cpt_damage-control-officer.png"
    })
    UpdateCard("Defense Liaison",3, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_cpt_defense-liaison.png"
    })
    UpdateCard("Veteran Captain",3, {
        cost = 2,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_cpt_veteran-captain.png"
    })
    UpdateCard("Weapons Liaison",3, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_cpt_weapons-liaison.png"
    })
    UpdateCard("Admiral Chiraneau",10, {
        cost = 8,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_cpt_admiral-chiraneau.png"
    })
    UpdateCard("Admiral Montferrat",5, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_cpt_admiral-montferrat.png"
    })
    UpdateCard("Director Isard",3, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_cpt_director-isard.png"
    })
    UpdateCard("Wulff Yularen",7, {
        cost = 5,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_cpt_wulff-yularen.png"
    })
    UpdateCard("Adar Tallon",10, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_cpt_adar-tallon.png"
    })
    UpdateCard("Lando Calrissian",4, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_cpt_lando-calrissian.png"
    })
    UpdateCard("Leia Organa",3, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_cpt_leia-organa.png"
    })
    UpdateCard("Raymus Antilles",7, {
        cost = 5,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_cpt_raymus-antilles.png"
    })
    UpdateCard("Assault Concussion Missiles",5, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_ord_assault-concussion-missiles.png"
    })
    UpdateCard("Assault Proton Torpedoes",4, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_ord_assault-proton-torpedoes.png"
    })
    UpdateCard("Expanded Launchers",13, {
        cost = 8,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_ord_expanded-launchers.png"
    })
    UpdateCard("Rapid Reload",8, {
        cost = 4,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_ord_rapid-reload.png"
    })
    UpdateCard("Auxiliary Shields Team",3, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w_rim_sup_auxiliary-shields-team.png"
    })
    UpdateCard("Engineering Team",5, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_sup_engineering-team.png"
    })
    UpdateCard("Nav Team",4, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_sup_nav-team.png"
    })
    UpdateCard("Projection Experts",6, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_sup_projection-experts.png"
    })
    ARQ_TITLE = GetDefinition("Centicore",3)
    Card:new(ARQ_TITLE,{
        name="Audacious",
        cost=4,
        front="https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/wx_ttl_audacious.png"
    })
    UpdateCard("Centicore",3, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w5_ttl_centicore.png"
    })
    UpdateCard("Hand of Justice",4, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w5_ttl_hand-of-justice.png"
    })
    RAIDER_TITLE = GetDefinition("Corvus",2)
    Card:new(RAIDER_TITLE,{
        name="Assailer",
        cost=4,
        front="https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/wx_ttl_assailer.png"
    })
    UpdateCard("Corvus",2, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w_rim_ttl_corvus.png"
    })
    UpdateCard("Impetuous",4, {
        cost = 3,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_ttl_impetuous.png"
    })
    UpdateCard("Corrupter",5, {
        cost = 3,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_ttl_corrupter.png"
    })
    UpdateCard("Dominator",12, {
        cost = 8,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_ttl_dominator.png"
    })
    UpdateCard("Harrow",3, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w_rim_ttl_harrow.png"
    })
    AF2_TITLE = GetDefinition("Gallant Haven",8)
    Card:new(AF2_TITLE,{
        name="Echelon",
        cost=4,
        front="https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/wx_ttl_echelon.png"
    })
    UpdateCard("Gallant Haven",8, {
        cost = 6,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_ttl_gallant-haven.png"
    })
    UpdateCard("Paragon",5, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_ttl_paragon.png"
    })
    UpdateCard("Dodonna's Pride",6, {
        cost = 4,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_ttl_dodonnas-pride.png"
    })
    UpdateCard("Jaina's Light",2, {
        cost = 3,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_ttl_jainas-light.png"
    })
    UpdateCard("Tantive IV",3, {
        cost = 2,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_ttl_tantive-iv.png"
    })
    UpdateCard("Salvation",7, {
        cost = 5,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_ttl_salvation.png"
    })
    UpdateCard("Vanguard",4, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w_rim_ttl_vanguard.png"
    })
    UpdateCard("Yavaris",5, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_ttl_yavaris.png"
    })
    UpdateCard("Dual Turbolaser Turrets",5, {
        cost = 4,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w5_trl_dual-turbolaser-turrets.png"
    })
    UpdateCard("Enhanced Armament",10, {
        cost = 8,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_trl_enhanced-armament.png"
    })
    UpdateCard("H9 Turbolasers",8, {
        cost = 6,
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_trl_h9-turbolasers.png"
    })
    UpdateCard("XI7 Turbolasers",6, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_trl_xi7-turbolasers.png"
    })
    UpdateCard("Flight Controllers",6, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_wpn_flight-controllers.png"
    })
    UpdateCard("Gunnery Team",7, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w0_wpn_gunnery-team.png"
    })
    WEAP_TEAM = GetDefinition("Gunnery Team",7)
    Card:new(WEAP_TEAM,{
        name="Ion Techs",
        cost=5,
        front="https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/wx_wpn_ion-techs.png"
    })
    UpdateCard("Local Fire Control",4, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w8_wpn_local-fire-control.png"
    })
    UpdateCard("Ordnance Experts",4, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w2_wpn_ordnance-experts.png"
    })
    UpdateCard("Sensor Team",5, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w1_wpn_sensor-team.png"
    })
    UpdateCard("Veteran Gunners",5, {
        front = "https://vassalwarlords.twilightpeaks.net/assets/cards/upgrades/w4_wpn_veteran-gunners.png"
    })

end

-- DO NOT MODIFY CODE BELOW THIS, OR MOD DB MAY NOT WORK!
function table.copy(orig)
    local orig_type = type(orig)
    local copy
    if orig_type == 'table' then
        copy = {}
        for orig_key, orig_value in pairs(orig) do
            copy[orig_key] = orig_value
        end
    else -- number, string, boolean, etc
    copy = orig
    end
    return copy
end
function findObjectByName(name)
    for i,obj in ipairs(getAllObjects()) do
        if obj.getName()==name then return obj end
    end
end
DEF_BRACE = '79d121'
DEF_CONTAIN = '68abfc'
DEF_EVADE = 'c09d88'
DEF_REDIRECT = '36f595'
DEF_SCATTER = '895e91'
DEF_SALVO = '5028b2'
Ship = { collider = "", convex = true, material = 3, maneuver = {}, type = nil, -- 1,
    defense_tokens = {}, shields = {1,1,1,1,1,1}, cost = 0, name = "",
    front = "", back = "", aliases = {}, faction = "" }
DefaultShip = table.copy(Ship)
function Ship:new (...)
    o = table.copy(DefaultShip)
    if ... ~= nil then
        for i,tab in ipairs({...}) do
            for k, v in pairs(tab) do
                o[k] = v
            end
        end
    end
    setmetatable(o, Ship)
    Ship.__index = Ship
    spawner = findObjectByName("Armada Spawner")
    if spawner~=nil then
        spawner.call("API_CacheShip",o)
    end
    return o
end
SmallShip = { collider = "http://paste.ee/r/eDbf1" }
MediumShip = { collider = "http://paste.ee/r/6LYTT" }
LargeShip = { collider = "http://paste.ee/r/a7mfW" }
HugeShip = { collider = "http://paste.ee/r/ClCL3" }
Squadron = { collider = "http://paste.ee/r/ZKM7E", convex = false, type = 1, --1, --http://paste.ee/r/nAMCQ
    material = 1, health = 0, move = 0, defense_tokens = {}, cost = 0,
    name = "", front = "", back = "", aliases = {}, faction = "" }
DefaultSquad = table.copy(Squadron)
function Squadron:new (...)
    o = table.copy(DefaultSquad)
    if ... ~= nil then
        for i,tab in ipairs({...}) do
            for k, v in pairs(tab) do
                o[k] = v
            end
        end
    end
    setmetatable(o, Squadron)
    Squadron.__index = Squadron
    spawner = findObjectByName("Armada Spawner")
    if spawner~=nil then
        spawner.call("API_CacheShip",o)
    end
    return o
end
Card = { cost = 0, name = "", type = "", front = "", back = "", aliases = {},
    iscard = true,  faction = nil
}
DefaultCard = table.copy(Card)
function Card:new (...)
    o = table.copy(DefaultCard)
    if ... ~= nil then
        for i,tab in ipairs({...}) do
            for k, v in pairs(tab) do
                o[k] = v
            end
        end
    end
    setmetatable(o, Card)
    Card.__index = Card
    spawner = findObjectByName("Armada Spawner")
    if spawner~=nil then
        spawner.call("API_CacheCard",o)
    end
    return o
end
function PurgeCard (name, cost)
    o = {}
    o['name'] = name
    o['cost'] = cost or 0
    spawner = findObjectByName("Armada Spawner")
    if spawner~=nil then
        spawner.call("API_PurgeCard",o)
    end
end
function UpdateCard(current_name, current_cost, o) -- MUST
    local update = {}
    update['name'] = current_name
    update['cost'] = current_cost or 0
    update['o'] = o
    spawner = findObjectByName("Armada Spawner")
    if spawner~=nil then
        spawner.call("API_UpdateCard",update)
    end
end
function GetDefinition(name, cost)
    local o = {}
    o['name'] = name
    o['cost'] = cost or 0
    spawner = findObjectByName("Armada Spawner")
    if spawner~=nil then
        return spawner.call("API_GetDefinition",o)
    end
end
function SetCloudCollectionName(name)
    spawner = findObjectByName("Armada Spawner")
    if spawner~=nil then
        return spawner.call("API_SET_GAMEREPORTER_COLLECTION",name)
    end
end
