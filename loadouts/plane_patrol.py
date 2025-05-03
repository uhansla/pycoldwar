import dcs.planes as planes

BLUE = [
    'F_14A_135_GR',
    # 'MB-339A'
    # 'F_A_18A',
    # 'A_10A',
    'F_4E_45MC',
    # 'F_5E',
    # 'F_5E_3',
    'F_86F_Sabre',
    # 'AJS37',
    # 'L_39ZA',
    # 'M_2000C',
    'Mirage_F1CE',
    # 'Mirage_F1EE',
    # MODS
    'VSN_F104G',
]

RED = [
    'F_14A_135_GR',
    'Mirage_F1CE',
    # 'Mirage_F1EE',
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
    # MODS
    'Su_15TM',
]

planes_map = {
    'F_86F_Sabre': [
        {
            "type": planes.F_86F_Sabre,
            "id": planes.F_86F_Sabre.id,
            "fuel": planes.F_86F_Sabre.fuel_max,
            "chaff": planes.F_86F_Sabre.chaff,
            "flare": planes.F_86F_Sabre.flare,
            "payload": {
                "pylons": [
                    planes.F_86F_Sabre.Pylon1.Fuel_Tank_200_gallons,
                    None,
                    None,
                    None,
                    planes.F_86F_Sabre.Pylon5.LAU_7_with_AIM_9B_Sidewinder_IR_AAM,
                    planes.F_86F_Sabre.Pylon6.LAU_7_with_AIM_9B_Sidewinder_IR_AAM,
                    None,
                    None,
                    None,
                    planes.F_86F_Sabre.Pylon10.Fuel_Tank_200_gallons
                ]
            }
        }
    ],
    'VSN_F104G': [
        {
            "type": planes.VSN_F104G,
            "id": planes.VSN_F104G.id,
            "fuel": planes.VSN_F104G.fuel_max,
            "chaff": planes.VSN_F104G.chaff,
            "flare": planes.VSN_F104G.flare,
            "payload": {
                "pylons": [
                    None, #1
                    planes.VSN_F104G.Pylon2.VSN_F104G_L_PTB, #2
                    None, #3
                    planes.VSN_F104G.Pylon4.AIM_9P5_Sidewinder_IR_AAM, #4
                    None, #5
                    None, #6
                    planes.VSN_F104G.Pylon7.AIM_9P5_Sidewinder_IR_AAM, #7
                    planes.VSN_F104G.Pylon8.AIM_9P5_Sidewinder_IR_AAM, #8
                    None, #9
                    planes.VSN_F104G.Pylon10.VSN_F104G_R_PTB, #10
                    None #11
                ]
            }
        }
    ],
    'Su_15TM': [
        {
            "type": planes.Su_15TM,
            "id": planes.Su_15TM.id,
            "fuel": planes.Su_15TM.fuel_max,
            "chaff": planes.Su_15TM.chaff,
            "flare": planes.Su_15TM.flare,
            "payload": {
                "pylons": [
                    planes.Su_15TM.Pylon1.R_98MR,
                    planes.Su_15TM.Pylon2.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM,
                    planes.Su_15TM.Pylon3.PTB_600,
                    planes.Su_15TM.Pylon4.PTB_600,
                    planes.Su_15TM.Pylon5.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM,
                    planes.Su_15TM.Pylon6.R_98MT
                ]
            }
        }
    ],
    'F_14A_135_GR': [
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
    'Mirage_F1EE': [
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
    'Mirage_F1CE': [
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
    'F_4E_45MC': [
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
    'MiG_19P': [
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
    'MiG_21Bis': [
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
