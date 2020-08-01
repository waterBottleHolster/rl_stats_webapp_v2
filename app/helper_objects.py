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

#first item is how it'll go into the database
#second item is how it'll appear on the rendered page
rl_gamemode_list = [
    ('three_v_three', '3v3'),
    ('two_v_two', '2v2'),
    ('one_v_one', '1v1'),
    ('four_v_four', '4v4'),
    ('standard', 'STANDARD'),
    ('doubles', 'DOUBLES'),
    ('duel', "DUEL"),
    ('solo_standard', 'SOLO STANDARD'),
    ('rumble', 'RUMBLE'),
    ('dropshot', 'DROPSHOT'),
    ('hoops', 'HOOPS'),
    ('snow_day', "SNOW DAY"),
    ('beach_ball', 'BEACH BALL'),
    ('boomer_ball', 'BOOMER BALL'),
    ('dropshot_rumble', "DROPSHOT RUMBLE"),
    ('heatseeker', 'HEATSEEKER')
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
