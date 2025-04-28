import dcs.helicopters as helicopters

BLUE = [
    'AH-1W'
]

RED = [
    'Mi-24V'
]

helicopters_map = {
    'AH-1W': [
        {
            'type': helicopters.AH_1W,
            'id': helicopters.AH_1W.id,
            'fuel': helicopters.AH_1W.fuel_max,
            'chaff': helicopters.AH_1W.chaff,
            'flare': helicopters.AH_1W.flare,
            'payload': {
                'pylons': [
                    helicopters.AH_1W.Pylon1._4_x_BGM_71D_TOW_ATGM,
                    helicopters.AH_1W.Pylon2.M260_HYDRA,
                    helicopters.AH_1W.Pylon3.M260_HYDRA,
                    helicopters.AH_1W.Pylon4._4_x_BGM_71D_TOW_ATGM,
                ]
            }
        },
    ],
    'Mi-24V': [
        {
            'type': helicopters.Mi_24V,
            'id': helicopters.Mi_24V.id,
            'fuel': helicopters.Mi_24V.fuel_max,
            'chaff': helicopters.Mi_24V.chaff,
            'flare': helicopters.Mi_24V.flare,
            'payload': {
                'pylons': [
                    helicopters.Mi_24V.Pylon1._2_x_9M114_Shturm__AT_6_Spiral____ATGM__SACLOS__HEAT,
                    helicopters.Mi_24V.Pylon2._2_x_9M114_Shturm__AT_6_Spiral____ATGM__SACLOS__HEAT,
                    helicopters.Mi_24V.Pylon3.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag,
                    helicopters.Mi_24V.Pylon4.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag,
                    helicopters.Mi_24V.Pylon5._2_x_9M114_Shturm__AT_6_Spiral____ATGM__SACLOS__HEAT,
                    helicopters.Mi_24V.Pylon6._2_x_9M114_Shturm__AT_6_Spiral____ATGM__SACLOS__HEAT,
                ]
            }
        },
    ],
}
