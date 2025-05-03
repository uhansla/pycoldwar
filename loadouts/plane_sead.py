import dcs.planes as planes

BLUE = [
    # 'MB-339A'
    # 'F_A_18A',
    # 'A_10A',
    'F_4E_45MC',
    # 'F_5E',
    # 'F_5E_3',
    # 'F_86F_Sabre',
    'AJS37',
    # 'L_39ZA',
    # 'M_2000C',
    # 'Mirage_F1CE',
    # 'Mirage_F1EE',
    # MODS
    'A_4E_C',
]

RED = [
    # 'Mirage_F1CE',
    'F_4E_45MC',
    'Su_17M4',
    'Su_24M',
    # 'MiG_23MLD',
    'MiG_27K',
    # 'MiG_21Bis',
    # 'MiG_19P',
    # 'MiG_15bis',
    # 'Su_25',
    # 'F_5E',
    # 'F_5E_3',
]

planes_map = {
    'A_4E_C': [
        {
            'type': planes.A_4E_C,
            'id': planes.A_4E_C.id,
            'fuel': planes.A_4E_C.fuel_max,
            'chaff': planes.A_4E_C.chaff,
            'flare': planes.A_4E_C.flare,
            'payload': {
                'pylons': [
                    planes.A_4E_C.Pylon1.LAU_10___4_x_UnGd_Rkts__127_mm_Zuni_Mk__24_Mod__1_HE,
                    planes.A_4E_C.Pylon2._5_x_Mk_81_Snakeye___250lb_GP_Bomb_HD__MER_,
                    planes.A_4E_C.Pylon3.Fuel_Tank_300_gallons,
                    planes.A_4E_C.Pylon4._5_x_Mk_81_Snakeye___250lb_GP_Bomb_HD__MER__,
                    planes.A_4E_C.Pylon5.LAU_10___4_x_UnGd_Rkts__127_mm_Zuni_Mk__24_Mod__1_HE,
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
                    planes.F_4E_45MC.Pylon1.AGM_45A_Shrike_ARM__LAU_34_,
                    None,
                    planes.F_4E_45MC.Pylon3._2x_AGM_65B___Maverick_B__TV_Guided___LAU_88__,
                    None,
                    planes.F_4E_45MC.Pylon5.AIM_7M,
                    planes.F_4E_45MC.Pylon6.AIM_7M,
                    None,
                    planes.F_4E_45MC.Pylon8.AIM_7M,
                    planes.F_4E_45MC.Pylon9.AIM_7M,
                    None,
                    planes.F_4E_45MC.Pylon11._2x_AGM_65B___Maverick_B__TV_Guided___LAU_88_,
                    None,
                    planes.F_4E_45MC.Pylon13.AGM_45A_Shrike_ARM__LAU_34_,
                    planes.F_4E_45MC.Pylon14.ALE_40_Dispensers__30_Flares__60_Chaff_,
                ]
            }
        },
    ],
    'AJS37': [
        {
            'type': planes.AJS37,
            'id': planes.AJS37.id,
            'fuel': planes.AJS37.fuel_max,
            'chaff': planes.AJS37.chaff,
            'flare': planes.AJS37.flare,
            'payload': {
                'pylons': [
                    planes.AJS37.Pylon1.LAU_7_with_RB_24__AIM_9B__Sidewinder_IR_AAM,
                    planes.AJS37.Pylon2.KB_Flare_Chaff_dispenser_pod,
                    planes.AJS37.Pylon3.Rb_75B__AGM_65B_Maverick___TV_ASM_,
                    None,
                    planes.AJS37.Pylon5.Rb_75B__AGM_65B_Maverick___TV_ASM_,
                    planes.AJS37.Pylon6.U_22_Jammer_pod,
                    planes.AJS37.Pylon7.LAU_7_with_RB_24__AIM_9B__Sidewinder_IR_AAM,
                ]
            }
        },
        {
            'type': planes.AJS37,
            'id': planes.AJS37.id,
            'fuel': planes.AJS37.fuel_max,
            'chaff': planes.AJS37.chaff,
            'flare': planes.AJS37.flare,
            'payload': {
                'pylons': [
                    planes.AJS37.Pylon1.LAU_7_with_RB_24__AIM_9B__Sidewinder_IR_AAM,
                    planes.AJS37.Pylon2.KB_Flare_Chaff_dispenser_pod,
                    planes.AJS37.Pylon3.Rb_75B__AGM_65B_Maverick___TV_ASM_,
                    planes.AJS37.Pylon4.AJS_External_tank_1013kg_fuel,
                    planes.AJS37.Pylon5.Rb_75B__AGM_65B_Maverick___TV_ASM_,
                    planes.AJS37.Pylon6.U_22_Jammer_pod,
                    planes.AJS37.Pylon7.LAU_7_with_RB_24__AIM_9B__Sidewinder_IR_AAM,
                ]
            }
        },
    ],
    'Su_17M4': [
        {
            'type': planes.Su_17M4,
            'id': planes.Su_17M4.id,
            'fuel': planes.Su_17M4.fuel_max,
            'chaff': planes.Su_17M4.chaff,
            'flare': planes.Su_17M4.flare,
            'payload': {
                'pylons': [
                    planes.Su_17M4.Pylon1.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr,
                    planes.Su_17M4.Pylon2.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                    planes.Su_17M4.Pylon3.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr,
                    planes.Su_17M4.Pylon4.Fuel_tank_800L,
                    planes.Su_17M4.Pylon5.Fuel_tank_800L,
                    planes.Su_17M4.Pylon6.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr,
                    planes.Su_17M4.Pylon7.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                    planes.Su_17M4.Pylon8.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr,
                ]
            }
        },
    ],
    'MiG_27K': [
        {
            'type': planes.MiG_27K,
            'id': planes.MiG_27K.id,
            'fuel': planes.MiG_27K.fuel_max,
            'chaff': planes.MiG_27K.chaff,
            'flare': planes.MiG_27K.flare,
            'payload': {
                'pylons': [
                    None,
                    planes.MiG_27K.Pylon2.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr,
                    planes.MiG_27K.Pylon3.APU_60_2M_with_2_x_R_60M__AA_8_Aphid_B____IR_AAM__,
                    planes.MiG_27K.Pylon4.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP,
                    None,
                    planes.MiG_27K.Pylon6.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP,
                    planes.MiG_27K.Pylon7.APU_60_2M_with_2_x_R_60M__AA_8_Aphid_B____IR_AAM___,
                    planes.MiG_27K.Pylon8.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr,
                ]
            }
        },
    ],
    'Su_24M': [
        {
            'type': planes.Su_24M,
            'id': planes.Su_24M.id,
            'fuel': planes.Su_24M.fuel_max,
            'chaff': planes.Su_24M.chaff,
            'flare': planes.Su_24M.flare,
            'payload': {
                'pylons': [
                    planes.Su_24M.Pylon1.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                    planes.Su_24M.Pylon2.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr,
                    None,
                    None,
                    planes.Su_24M.Pylon5.Fuel_tank_2000L,
                    None,
                    planes.Su_24M.Pylon7.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr,
                    planes.Su_24M.Pylon8.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                ]
            }
        },
    ],
}
