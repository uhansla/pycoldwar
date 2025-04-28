import dcs.helicopters as helicopters

BLUE = [
    'UH-1H'
]

RED = [
    'Mi-8MT'
]

helicopters_map = {
    'UH-1H': [
        {
            'type': helicopters.UH_1H,
            'id': helicopters.UH_1H.id,
            'fuel': helicopters.UH_1H.fuel_max,
            'chaff': helicopters.UH_1H.chaff,
            'flare': helicopters.UH_1H.flare,
            'payload': {
                'pylons': [
                    None,
                    None,
                    helicopters.UH_1H.Pylon3.M60_SIDE_L,
                    helicopters.UH_1H.Pylon4.M60_SIDE_R,
                ]
            }
        },
    ],
    'Mi-8MT': [
        {
            'type': helicopters.Mi_8MT,
            'id': helicopters.Mi_8MT.id,
            'fuel': helicopters.Mi_8MT.fuel_max,
            'chaff': helicopters.Mi_8MT.chaff,
            'flare': helicopters.Mi_8MT.flare,
            'payload': {
                'pylons': [
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    helicopters.Mi_8MT.Pylon7.KORD_12_7,
                    helicopters.Mi_8MT.Pylon8.PKT_7_62,
                ]
            }
        },
    ],
}
