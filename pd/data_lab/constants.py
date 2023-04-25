# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

TIME_OF_DAY_MAP = {
    "DAWN": [
        "LS_sky_dawn_clear_0428_HDS014",
        "LS_sky_dawn_mostlySunny_0514_HDS026",
        "LS_sky_dawn_partlyCloudy_0440_HDS038",
    ],
    "DUSK": [
        "LS_sky_dusk_mostlyCloudy_2000_HDS033",
        "LS_sky_dusk_partlyCloudy_2040_HDS036",
    ],
    "EVENING": [
        "LS_sky_evening_mostlyCloudy_1830_HDS019",
        "LS_sky_evening_partlyCloudy_1950_HDS032",
    ],
    "NIGHT": [
        "LS_sky_night_clear_0530_HDS377",
        "LS_sky_night_clear_0650_HDS363",
        "LS_sky_night_clear_2200_HDS380",
        "LS_sky_night_mostlyCloudy_0600_HDS340",
    ],
    "DAY": [
        "LS_sky_noon_mostlyCloudy_1205_HDS001",
        "LS_sky_noon_mostlySunny_1250_HDS025",
        "LS_sky_noon_overcast_1214_HDS018",
        "LS_sky_noon_partlyCloudy_1113_HDS024",
        "LS_sky_afternoon_mostlySunny_1444_HDS035",
        "LS_sky_afternoon_mostlySunny_1740_HDS030",
        "LS_sky_afternoon_overcast_1314_HDS034",
        "LS_sky_afternoon_overcast_1430_HDS004",
        "LS_sky_afternoon_overcast_1655_HDS028",
        "LS_sky_afternoon_partlyCloudy_1401_HDS039",
        "LS_sky_afternoon_partlyCloudy_1745_HDS016",
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
