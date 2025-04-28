import dcs.planes as planes

BLUE = [
    'F-14A-135-GR',
    # 'MB-339A'
    # 'F_A_18A',
    # 'A_10A',
    'F_4E_45MC',
    # 'F_5E',
    # 'F_5E_3',
    # 'F_86F_Sabre',
    # 'AJS37',
    # 'L_39ZA',
    # 'M_2000C',
    'Mirage_F1CE',
    'Mirage_F1EE',
]

RED = [
    'F-14A-135-GR',
    'Mirage_F1CE',
    'Mirage_F1EE',
    'F_4E_45MC',
    # 'Su_17M4',
    # 'Su_24M',
    # 'MiG_23MLD',
    # 'MiG_27K',
    'MiG_21Bis',
    'MiG_19P',
    # 'MiG_15bis',
    # 'Su_25',
    # 'F_5E',
    # 'F_5E_3',
]

planes_map = {
    'F-14A-135-GR': [
        {
            'type': planes.F_14A_135_GR,
            'id': planes.F_14A_135_GR.id,
            'fuel': planes.F_14A_135_GR.fuel_max,
            'chaff': planes.F_14A_135_GR.chaff,
            'flare': planes.F_14A_135_GR.flare,
            'payload': {
                'pylons': [
                    planes.F_14A_135_GR.Pylon1.LAU_138_AIM_9L,
                    planes.F_14A_135_GR.Pylon2.AIM_7F_,
                    planes.F_14A_135_GR.Pylon3.Fuel_tank_300_gal_,
                    planes.F_14A_135_GR.Pylon4.AIM_54A_Mk47,
                    planes.F_14A_135_GR.Pylon5.AIM_54A_Mk47,
                    planes.F_14A_135_GR.Pylon6.AIM_54A_Mk47,
                    planes.F_14A_135_GR.Pylon7.AIM_54A_Mk47,
                    planes.F_14A_135_GR.Pylon8.Fuel_tank_300_gal_,
                    planes.F_14A_135_GR.Pylon9.AIM_7F_,
                    planes.F_14A_135_GR.Pylon10.LAU_138_AIM_9L,
                ]
            }
        },
    ],
    'Mirage-F1EE': [
        {
            'type': planes.Mirage_F1EE,
            'id': planes.Mirage_F1EE.id,
            'fuel': planes.Mirage_F1EE.fuel_max,
            'chaff': planes.Mirage_F1EE.chaff,
            'flare': planes.Mirage_F1EE.flare,
            'payload': {
                'pylons': [
                    planes.Mirage_F1EE.Pylon1.R550_Magic_1_IR_AAM,
                    None,
                    planes.Mirage_F1EE.Pylon3.R530F_EM,
                    planes.Mirage_F1EE.Pylon4.PTB_1200_F1,
                    planes.Mirage_F1EE.Pylon5.R530F_EM,
                    None,
                    planes.Mirage_F1EE.Pylon7.R550_Magic_1_IR_AAM,
                ]
            }
        },
    ],
    'Mirage-F1CE': [
        {
            'type': planes.Mirage_F1CE,
            'id': planes.Mirage_F1CE.id,
            'fuel': planes.Mirage_F1CE.fuel_max,
            'chaff': planes.Mirage_F1CE.chaff,
            'flare': planes.Mirage_F1CE.flare,
            'payload': {
                'pylons': [
                    planes.Mirage_F1CE.Pylon1.R550_Magic_1_IR_AAM,
                    None,
                    planes.Mirage_F1CE.Pylon3.R530F_EM,
                    planes.Mirage_F1CE.Pylon4.PTB_1200_F1,
                    planes.Mirage_F1CE.Pylon5.R530F_EM,
                    None,
                    planes.Mirage_F1CE.Pylon7.R550_Magic_1_IR_AAM,
                ]
            }
        },
    ],
    'F-4E-45MC': [
        {
            'type': planes.F_4E_45MC,
            'id': planes.F_4E_45MC.id,
            'fuel': planes.F_4E_45MC.fuel_max,
            'chaff': planes.F_4E_45MC.chaff,
            'flare': planes.F_4E_45MC.flare,
            'payload': {
                'pylons': [
                    planes.F_4E_45MC.Pylon1.Sargent_Fletcher_Fuel_Tank_370_gallons,
                    planes.F_4E_45MC.Pylon2.AIM_9P5_Sidewinder_IR_AAM,
                    None,
                    planes.F_4E_45MC.Pylon4.AIM_9P5_Sidewinder_IR_AAM,
                    planes.F_4E_45MC.Pylon5.AIM_7M,
                    planes.F_4E_45MC.Pylon6.AIM_7M,
                    None,
                    planes.F_4E_45MC.Pylon8.AIM_7M,
                    planes.F_4E_45MC.Pylon9.AIM_7M,
                    planes.F_4E_45MC.Pylon10.AIM_9P5_Sidewinder_IR_AAM,
                    None,
                    planes.F_4E_45MC.Pylon12.AIM_9P5_Sidewinder_IR_AAM,
                    planes.F_4E_45MC.Pylon13.Sargent_Fletcher_Fuel_Tank_370_gallons_,
                    planes.F_4E_45MC.Pylon14.ALE_40_Dispensers__30_Flares__60_Chaff_,
                ]
            }
        },
    ],
    'MiG-19P': [
        {
            'type': planes.MiG_19P,
            'id': planes.MiG_19P.id,
            'fuel': planes.MiG_19P.fuel_max,
            'chaff': planes.MiG_19P.chaff,
            'flare': planes.MiG_19P.flare,
            'payload': {
                'pylons': [
                    planes.MiG_19P.Pylon1.K_13A,
                    planes.MiG_19P.Pylon2.PTB760_MIG19,
                    None,
                    None,
                    planes.MiG_19P.Pylon5.PTB760_MIG19,
                    planes.MiG_19P.Pylon6.K_13A,
                ]
            }
        },
    ],
    'MiG-21Bis': [
        {
            'type': planes.MiG_21Bis,
            'id': planes.MiG_21Bis.id,
            'fuel': planes.MiG_21Bis.fuel_max,
            'chaff': planes.MiG_21Bis.chaff,
            'flare': planes.MiG_21Bis.flare,
            'payload': {
                'pylons': [
                    planes.MiG_21Bis.Pylon1.APU_13U_2_with_R_3R__AA_2_Atoll_C____Semi_Active_AAM,
                    planes.MiG_21Bis.Pylon2.APU_60_2M_with_2_x_R_60__AA_8_Aphid____IR_AAM,
                    planes.MiG_21Bis.Pylon3.Fuel_Tank_800_L__21_,
                    planes.MiG_21Bis.Pylon4.APU_60_2M_with_2_x_R_60__AA_8_Aphid____IR_AAM_,
                    planes.MiG_21Bis.Pylon5.APU_13U_2_with_R_3R__AA_2_Atoll_C____Semi_Active_AAM,
                    planes.MiG_21Bis.Pylon6.ASO_2___countermeasures_pod,
                ]
            }
        },
    ],
}
