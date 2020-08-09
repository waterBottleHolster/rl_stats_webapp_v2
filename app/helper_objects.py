# the first item in the tuple is the string as it'll appear in the db
# the second item in the tuple is how it'll appear to users
rl_vehicle_list = [
    ("batmobile16", "'16 Batmobile"),
    ("dodge_charger", "'70 Dodge Charger R/T"),
    ("batmobile89", "'89 Batmobile"),
    ("skyline99", "'99 Nissan Skyline"),
    ("aftershock", "Aftershock"),
    ("animus_gp", "Animus FP"),
    ("artemis", "Artemis"),
    ("backfire", "Backfire"),
    ("bone_shaker", "Bone Shaker"),
    ("breakout", "Breakout"),
    ("breakout_s", "Breakout Type S"),
    ("centio", "Centio V17"),
    ("chikara", "Chikara"),
    ("cyclone", "Cyclone"),
    ("delorean", "Delorean"),
    ("diestro", "Diestro"),
    ("dominus", "Dominus"),
    ("dominus_gt", "Dominus GT"),
    ("ecto_1", "Ecto-1"),
    ("endo", "Endo"),
    ("esper", "Esper"),
    ("fast_4wd", "Fast 4WD"),
    ("fennec", "Fennec"),
    ("gazella", "Gazella GT"),
    ("gizmo", "Gizmo"),
    ("grog", "Grog"),
    ("guardian", "Guardian"),
    ("hotshot", "Hotshot"),
    ("ice_charger", "Ice Charger"),
    ("imperator", "Imperator"),
    ("jager_619", "Jager 619 RS"),
    ("jurassic_jeep_wrangler", "Jurassic Jeep Wrangler"),
    ("kitt", "K.I.T.T"),
    ("komodo", "Komodo"),
    ("mantis", "Mantis"),
    ("marauder", "Marauder"),
    ("masamune", "Masamune"),
    ("maverick", "Maverick"),
    ("mclaren", "McLaren 570S"),
    ("merc", "Merc"),
    ("mr11", "MR11"),
    ("mudcat", "Mudcat"),
    ("nemesis", "Nemesis"),
    ("nimbus", "Nimbus"),
    ("octane", "Octane"),
    ("octane_zsr", "Octane ZSR"),
    ("paladin", "Paladin"),
    ("proteus", "Proteus"),
    ("ripper", "Ripper"),
    ("road_hog", "Road Hog"),
    ("road_hog_xl", "Road Hog xL"),
    ("ronin", "Ronin"),
    ("samurai", "Samurai"),
    ("scarab", "Scarab"),
    ("sentinel", "Sentinel"),
    ("takumi", "Takumi"),
    ("takumi_rxt", "Takumi RX-T"),
    ("tdkr_tumbler", "T.D.K.R Tumbler"),
    ("triton", "Triton"),
    ("twin_mill", "Twin Mill III"),
    ("twinzer", "Twinzer"),
    ("venom", "Venom"),
    ("vulcan", "Vulcan"),
    ("werewolf", "Werewolf"),
    ("xdevil", "X-Devil"),
    ("xdevil_mk2", "X-Devil Mk2"),
    ("zippy", "Zippy")
]

rl_vehicle_list_v2 = [
    "'16 Batmobile",
    "'70 Dodge Charger R/T",
    "'89 Batmobile",
    "'99 Nissan Skyline",
    "Aftershock",
    "Animus FP",
    "Artemis",
    "Backfire",
    "Bone Shaker",
    "Breakout",
    "Breakout Type S",
    "Centio V17",
    "Chikara",
    "Cyclone",
    "Delorean",
    "Diestro",
    "Dominus",
    "Dominus GT",
    "Ecto-1",
    "Endo",
    "Esper",
    "Fast 4WD",
    "Fennec",
    "Gazella GT",
    "Gizmo",
    "Grog",
    "Guardian",
    "Hotshot",
    "Ice Charger",
    "Imperator",
    "Jager 619 RS",
    "Jurassic Jeep Wrangler",
    "K.I.T.T",
    "Komodo",
    "Mantis",
    "Marauder",
    "Masamune",
    "Maverick",
    "McLaren 570S",
    "Merc",
    "MR11",
    "Mudcat",
    "Nemesis",
    "Nimbus",
    "Octane",
    "Octane ZSR",
    "Paladin",
    "Proteus",
    "Ripper",
    "Road Hog",
    "Road Hog xL",
    "Ronin",
    "Samurai",
    "Scarab",
    "Sentinel",
    "Takumi",
    "Takumi RX-T",
    "T.D.K.R Tumbler",
    "Triton",
    "Twin Mill III",
    "Twinzer",
    "Venom",
    "Vulcan",
    "Werewolf",
    "X-Devil",
    "X-Devil Mk2",
    "Zippy"
]

#first item is how it'll go into the database
#second item is how it'll appear on the rendered page
rl_gamemode_list = [
    ('three_v_three', '3v3'),
    ('two_v_two', '2v2'),
    ('one_v_one', '1v1'),
    ('four_v_four', '4v4'),
    ('standard', 'STANDARD'),
    ('DOUBLES', 'DOUBLES'),
    ('DUEL', "DUEL"),
    ('SOLO STANDARD', 'SOLO STANDARD'),
    ('RUMBLE', 'RUMBLE'),
    ('DROPSHOT', 'DROPSHOT'),
    ('HOOPS', 'HOOPS'),
    ('SNOW DAY', "SNOW DAY"),
    ('BEACH BALL', 'BEACH BALL'),
    ('BOOMER BALL', 'BOOMER BALL'),
    ('DROPSHOT RUMBLE', "DROPSHOT RUMBLE"),
    ('HEATSEEKER', 'HEATSEEKER')
]

rl_gamemode_list_v2 = [
    "3v3",
    "2v2",
    "1v1",
    "4v4",
    "Standard",
    "Doubles",
    "Duel",
    "Solo Standard",
    "Rumble",
    "Dropshot",
    "Hoops",
    "Snow Day",
    "Beach Ball",
    "Boomer Ball",
    "Dropshot Rumble",
    "Heatseeker"
]

def boolean_to_binary(input):
    if input == True:
        output = 1
    else:
        output = 0
    return output

def binary_to_boolean(input):
    if input == 1:
        output = True
    else:
        output = False
    return output

def pretty_translate(input):
    if input == "win":
        output = "Win"
    elif input == "loss":
        output = "Loss"
    elif input == "forfeit_win":
        output = "Forfeit (W)"
    elif input == "forfeit_loss":
        output = "Forfeit (L)"
    elif input == "disconnect":
        output = "Disconnect"
    elif input == 1:
        output = True
    elif input == 0:
        output = False
