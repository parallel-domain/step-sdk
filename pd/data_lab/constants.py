# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

TIME_OF_DAY_MAP = {
    "DAWN": [
        "dawn_clear_01",
        "dawn_partlyCloudy_01",
        "dawn_mostlyCloudy_03",
    ],
    "DUSK": [
        "dusk_mostlyCloudy_01",
        "dusk_partlyCloudy_02",
    ],
    "EVENING": [
        "day_overcast_06",
        "day_partlyCloudy_04",
    ],
    "NIGHT": [
        "night_clear_06",
        "dawn_clear_02",
        "dusk_clear_01",
        "dawn_overcast_01",
    ],
    "DAY": [
        "day_partlyCloudy_03",
        "day_clear_06",
        "day_overcast_07",
        "day_clear_07",
        "day_clear_04",
        "day_clear_05",
        "day_overcast_03",
        "day_overcast_04",
        "day_overcast_05",
        "day_partlyCloudy_01",
        "day_partlyCloudy_02",
    ],
}


MAP_LOCATIONS = {
    "SUBURBAN": [
        "A2_BurnsPark",
        "A2_Kerrytown",
        "SC_GranadaAndFloravista_large",
        "SC_MathildaAndSunnyvaleSaratoga_large",
        "SC_MathildaAndSunnyvaleSaratoga",
    ],
    "URBAN": [
        "SF_6thAndMission_medium",
        "SF_GrantAndCalifornia",
        "SF_JacksonAndKearny",
        "SF_VanNessAveAndTurkSt",
    ],
    "HIGHWAY": [
        "SJ_237AndGreatAmerica",
        "SJ_237AndNorth1st",
        "SJ_680MissionPass",
        "SJ_237AndZanker",
        "MV_280AndPageMill",
        "EB_580_Dublin",
        "FICT_Highway_TestTrack_01",
    ],
    "RESIDENTIAL": [
        "SC_Highlands",
        "SC_KennewickDrive",
        "SC_W8thAndOrchard",
        "SJ_EssexAndBradford",
        "SJ_KettmanAndOrinda_aus",
    ],
}

LOCATION_TO_CATEGORY = {loc: cat for cat, loclist in MAP_LOCATIONS.items() for loc in loclist}
