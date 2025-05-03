import dcs.planes as planes

types = [
 'F_A_18A',      # entered ~1983 ✅
 'F_4E',         # Vietnam War, 1960s-70s ✅
 'B_52H',        # early 1960s ✅
 'MiG_27K',      # 1970s ✅
 'MiG_23MLD',    # late 1970s ✅
 'Su_25',        # 1981 ✅
 'Su_17M4',      # 1970s ✅
 'Su_24M',       # 1974 ✅
 'MiG_29A',      # 1983 ✅
 'F_16A',        # 1978 ✅
 'A_10A',        # 1977 ✅
 'AJS37',        # 1971 ✅
 'C_101CC',      # early 1970s Spanish trainer ✅
 'F_5E',         # Vietnam War fighter, 1970s ✅
 'F_5E_3',       # same airframe, minor variant ✅
 'F_86F_Sabre',  # Korean War jet, 1950s ✅
 'F_14A_135_GR', # F-14A, original Tomcat 1970s ✅
 'Hawk',         # BAE Hawk, 1976 ✅
 'L_39C',        # Aero L-39, 1970s ✅
 'L_39ZA',       # L-39 armed trainer, 70s-80s ✅
 'M_2000C',      # Mirage 2000C entered ~1984 ✅
 'MiG_15bis',    # 1950s Korean War classic ✅
 'MiG_19P',      # 1950s first Soviet supersonic jet ✅
 'MiG_21Bis',    # 1960s Cold War jet ✅
 # All Mirage F1 family (entered late 1970s–early 1980s):
 'Mirage_F1C', 'Mirage_F1CE', 'Mirage_F1EE', 'Mirage_F1M_EE', 'Mirage_F1M_CE',
 'Mirage_F1C_200', 'Mirage_F1EH', 'Mirage_F1CH', 'Mirage_F1JA', 'Mirage_F1CG',
 'Mirage_F1CZ', 'Mirage_F1CJ', 'Mirage_F1CK', 'Mirage_F1EQ', 'Mirage_F1ED',
 'Mirage_F1EDA', 'Mirage_F1CR', 'Mirage_F1CT', 'Mirage_F1B', 'Mirage_F1BE',
 'Mirage_F1BQ', 'Mirage_F1BD', 'Mirage_F1DDA'
]

BLUE = [
    'MB_339A',
    # 'F_A_18A',
    'A_10A',
    'F_4E_45MC',
    'F_5E',
    # 'F_5E_3',
    'F_86F_Sabre',
    'AJS37',
    'L_39ZA',
    'M_2000C',
    'Mirage_F1CE',
    # 'Mirage_F1EE',
    # MODS
    'A_4E_C',
    'VSN_F100',
]

RED = [
    'Mirage_F1CE',
    'F_4E_45MC',
    'Su_17M4',
    'Su_24M',
    'MiG_23MLD',
    'MiG_27K',
    'MiG_21Bis',
    'MiG_19P',
    'MiG_15bis',
    'Su_25',
    'F_5E',
    # 'F_5E_3',
]

planes_map = {

    'VSN_F100': [
        {
            'type': planes.VSN_F100,
            'id': planes.VSN_F100.id,
            'fuel': planes.VSN_F100.fuel_max,
            'chaff': planes.VSN_F100.chaff,
            'flare': planes.VSN_F100.flare,
            'payload': {
                'pylons': [
                    None,
                    None,
                    planes.VSN_F100.Pylon3.LAU_3___19_x_UnGd_Rkts__70_mm_Mk_4_FFAR_Mk_1_HE,
                    planes.VSN_F100.Pylon4.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
                    planes.VSN_F100.Pylon5.Fuel_tank_500_Liter,
                    None,
                    planes.VSN_F100.Pylon7.Fuel_tank_500_Liter,
                    planes.VSN_F100.Pylon8.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
                    planes.VSN_F100.Pylon9.LAU_3___19_x_UnGd_Rkts__70_mm_Mk_4_FFAR_Mk_1_HE,
                ]
            }
        },
    ],
    
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
                    planes.A_4E_C.Pylon4._5_x_Mk_81_Snakeye___250lb_GP_Bomb_HD__MER_,
                    planes.A_4E_C.Pylon5.LAU_10___4_x_UnGd_Rkts__127_mm_Zuni_Mk__24_Mod__1_HE,
                ]
            }
        },
    ],
    'F_A_18A': [
        {
            "type": planes.F_A_18A,
            "id": planes.F_A_18A.id,
            "fuel": planes.F_A_18A.fuel_max,
            "chaff": planes.F_A_18A.chaff,
            "flare": planes.F_A_18A.flare,
            "payload": {
                "pylons": [
                    planes.F_A_18A.Pylon1.AIM_9P_Sidewinder_IR_AAM,
                    planes.F_A_18A.Pylon2.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
                    planes.F_A_18A.Pylon3.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
                    planes.F_A_18A.Pylon4.AIM_7M_Sparrow_Semi_Active_Radar,
                    planes.F_A_18A.Pylon5.Fuel_tank_330_gal,
                    planes.F_A_18A.Pylon6.AIM_7M_Sparrow_Semi_Active_Radar,
                    planes.F_A_18A.Pylon7.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
                    planes.F_A_18A.Pylon8.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
                    planes.F_A_18A.Pylon9.AIM_9P_Sidewinder_IR_AAM
                ]
            }
        }
    ],

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
                    None, #planes.F_86F_Sabre.Pylon2._2_x_HVAR__UnGd_Rkts,
                    planes.F_86F_Sabre.Pylon3._2_x_HVAR__UnGd_Rkts,
                    planes.F_86F_Sabre.Pylon4.AN_M64___500lb_GP_Bomb_LD_,
                    planes.F_86F_Sabre.Pylon5.LAU_7_with_AIM_9B_Sidewinder_IR_AAM,
                    planes.F_86F_Sabre.Pylon6.LAU_7_with_AIM_9B_Sidewinder_IR_AAM,
                    planes.F_86F_Sabre.Pylon7.AN_M64___500lb_GP_Bomb_LD_,
                    planes.F_86F_Sabre.Pylon8._2_x_HVAR__UnGd_Rkts,
                    None, #planes.F_86F_Sabre.Pylon9._2_x_HVAR__UnGd_Rkts,
                    planes.F_86F_Sabre.Pylon10.Fuel_Tank_200_gallons
                ]
            }
        }
    ],

    'F_4E_45MC': [
        {
            "type": planes.F_4E_45MC,
            "id": planes.F_4E_45MC.id,
            "fuel": planes.F_4E_45MC.fuel_max,
            "chaff": planes.F_4E_45MC.chaff,
            "flare": planes.F_4E_45MC.flare,
            "payload": {
                "pylons": [
                    planes.F_4E_45MC.Pylon1.Sargent_Fletcher_Fuel_Tank_370_gallons,
                    planes.F_4E_45MC.Pylon2.AIM_9M,
                    planes.F_4E_45MC.Pylon3._Special_Weapons_Adapter__AGM_65D___Maverick_D__IIR_ASM___LAU_117__Special_Weapons_Adapter__,
                    planes.F_4E_45MC.Pylon4.AIM_9M,
                    planes.F_4E_45MC.Pylon5.AIM_7M,
                    planes.F_4E_45MC.Pylon6.AIM_7M,
                    planes.F_4E_45MC.Pylon7._6x_Mk_82___500lb_GP_Bomb_LD__MER_,
                    planes.F_4E_45MC.Pylon8.AIM_7M,
                    planes.F_4E_45MC.Pylon9.AIM_7M,
                    planes.F_4E_45MC.Pylon10.AIM_9M,
                    planes.F_4E_45MC.Pylon11._Special_Weapons_Adapter__AGM_65D___Maverick_D__IIR_ASM___LAU_117__Special_Weapons_Adapter__,
                    planes.F_4E_45MC.Pylon12.AIM_9M,
                    planes.F_4E_45MC.Pylon13.Sargent_Fletcher_Fuel_Tank_370_gallons_,
                    planes.F_4E_45MC.Pylon14.ALE_40_Dispensers__30_Flares__60_Chaff_
                ]
            }
        }
    ],

    'MB_339A': [
        {
            'type': planes.MB_339A,
            'id': planes.MB_339A.id,
            'fuel': planes.MB_339A.fuel_max,
            'chaff': planes.MB_339A.chaff,
            'flare': planes.MB_339A.flare,
            'payload': {
                'pylons': [
                    None,
                    planes.MB_339A.Pylon2.Mk_82___500lb_GP_Bomb_LD,
                    planes.MB_339A.Pylon3.LR_25___25_x_UnGd_Rkts__50_mm_ARF_8_M3_API,
                    planes.MB_339A.Pylon4.DEFA553_Gunpod_Left,
                    None,
                    None,
                    planes.MB_339A.Pylon7.DEFA553_Gunpod_Right,
                    planes.MB_339A.Pylon8.LR_25___25_x_UnGd_Rkts__50_mm_ARF_8_M3_API,
                    planes.MB_339A.Pylon9.Mk_82___500lb_GP_Bomb_LD,
                ]
            }
        },
    ],

    'F_5E': [
        {
            "type": planes.F_5E,
            "id": planes.F_5E.id,
            "fuel": planes.F_5E.fuel_max,
            "chaff": planes.F_5E.chaff,
            "flare": planes.F_5E.flare,
            "payload": {
                "pylons": [
                    planes.F_5E.Pylon1.AIM_9P_Sidewinder_IR_AAM,
                    planes.F_5E.Pylon2.M117___750lb_GP_Bomb_LD,
                    planes.F_5E.Pylon3.F_5_275Gal_Fuel_tank,
                    planes.F_5E.Pylon4.M117___750lb_GP_Bomb_LD,
                    planes.F_5E.Pylon5.F_5_275Gal_Fuel_tank,
                    planes.F_5E.Pylon6.M117___750lb_GP_Bomb_LD,
                    planes.F_5E.Pylon7.AIM_9P_Sidewinder_IR_AAM,
                ]
            }
        }
    ],

    'F_5E_3': [
        {
            "type": planes.F_5E_3,
            "id": planes.F_5E_3.id,
            "fuel": planes.F_5E_3.fuel_max,
            "chaff": planes.F_5E_3.chaff,
            "flare": planes.F_5E_3.flare,
            "payload": {
                "pylons": [
                    planes.F_5E_3.Pylon1.AIM_9P_Sidewinder_IR_AAM,
                    planes.F_5E_3.Pylon2.M117___750lb_GP_Bomb_LD,
                    planes.F_5E_3.Pylon3.F_5_275Gal_Fuel_tank,
                    planes.F_5E_3.Pylon4.M117___750lb_GP_Bomb_LD,
                    planes.F_5E_3.Pylon5.F_5_275Gal_Fuel_tank,
                    planes.F_5E_3.Pylon6.M117___750lb_GP_Bomb_LD,
                    planes.F_5E_3.Pylon7.AIM_9P_Sidewinder_IR_AAM,
                ]
            }
        }
    ],

    'A_10A': [
        {
            'type': planes.A_10A,
            'id': planes.A_10A.id,
            'fuel': planes.A_10A.fuel_max,
            'chaff': planes.A_10A.chaff,
            'flare': planes.A_10A.flare,
            'payload': {
                'pylons': [
                    planes.A_10A.Pylon1.LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM,
                    planes.A_10A.Pylon2.LAU_131___7_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE,
                    planes.A_10A.Pylon3.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_,
                    None,
                    None,
                    None,
                    None,
                    None,
                    planes.A_10A.Pylon9.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__,
                    planes.A_10A.Pylon10.LAU_131___7_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE,
                    planes.A_10A.Pylon11.LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM,
                ]
            }
        },
        {
            'type': planes.A_10A,
            'id': planes.A_10A.id,
            'fuel': planes.A_10A.fuel_max,
            'chaff': planes.A_10A.chaff,
            'flare': planes.A_10A.flare,
            'payload': {
                'pylons': [
                    planes.A_10A.Pylon1.LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM,
                    planes.A_10A.Pylon2.LAU_131___7_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE,
                    planes.A_10A.Pylon3.LAU_88_AGM_65H_2_L,
                    None,
                    None,
                    None,
                    None,
                    None,
                    planes.A_10A.Pylon9.LAU_88_AGM_65H_2_R,
                    planes.A_10A.Pylon10.LAU_131___7_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE,
                    planes.A_10A.Pylon11.LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM,
                ]
            }
        },
        {
            "type": planes.A_10A,
            "id": planes.A_10A.id,
            "fuel": planes.A_10A.fuel_max,
            "chaff": planes.A_10A.chaff,
            "flare": planes.A_10A.flare,
            "payload": {
                "pylons": [
                    planes.A_10A.Pylon1.ALQ_131___ECM_Pod,
                    planes.A_10A.Pylon2.LAU_68___7_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE,
                    planes.A_10A.Pylon3.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_,
                    planes.A_10A.Pylon4.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
                    planes.A_10A.Pylon5.Mk_82___500lb_GP_Bomb_LD,
                    planes.A_10A.Pylon6.Mk_82___500lb_GP_Bomb_LD,
                    planes.A_10A.Pylon7.Mk_82___500lb_GP_Bomb_LD,
                    planes.A_10A.Pylon8.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
                    planes.A_10A.Pylon9.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_,
                    planes.A_10A.Pylon10.LAU_68___7_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE,
                    planes.A_10A.Pylon11.LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM
                ]
            }
        }
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
                    planes.AJS37.Pylon2.Rb_75A__AGM_65A_Maverick___TV_ASM_,
                    planes.AJS37.Pylon3.Rb_75A__AGM_65A_Maverick___TV_ASM_,
                    planes.AJS37.Pylon4.AJS_External_tank_1013kg_fuel,
                    planes.AJS37.Pylon5.Rb_75A__AGM_65A_Maverick___TV_ASM_,
                    planes.AJS37.Pylon6.Rb_75A__AGM_65A_Maverick___TV_ASM_,
                    planes.AJS37.Pylon7.LAU_7_with_RB_24__AIM_9B__Sidewinder_IR_AAM,
                ]
            }
        },
        {
            "type": planes.AJS37,
            "id": planes.AJS37.id,
            "fuel": planes.AJS37.fuel_max,
            "chaff": planes.AJS37.chaff,
            "flare": planes.AJS37.flare,
            "payload": {
                "pylons": [
                    planes.AJS37.Pylon1.LAU_7_with_RB_24J__AIM_9P3__Sidewinder_IR_AAM,
                    planes.AJS37.Pylon2.Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_,
                    None,
                    planes.AJS37.Pylon4.AJS_External_tank_1013kg_fuel,
                    None,
                    planes.AJS37.Pylon6.Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_,
                    planes.AJS37.Pylon7.LAU_7_with_RB_24J__AIM_9P3__Sidewinder_IR_AAM
                ]
            }
        }
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
                    planes.Mirage_F1EE.Pylon2.SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1EE.Pylon3.PTB_1200_F1,
                    planes.Mirage_F1EE.Pylon4.CLB_4___4_x_SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1EE.Pylon5.PTB_1200_F1,
                    planes.Mirage_F1EE.Pylon6.SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1EE.Pylon7.R550_Magic_1_IR_AAM,
                ]
            }
        },
    ],

    'MiG_21Bis': [
        {
            "type": planes.MiG_21Bis,
            "id": planes.MiG_21Bis.id,
            "fuel": planes.MiG_21Bis.fuel_max,
            "chaff": planes.MiG_21Bis.chaff,
            "flare": planes.MiG_21Bis.flare,
            "payload": {
                "pylons": [
                    planes.MiG_21Bis.Pylon1.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM,
                    planes.MiG_21Bis.Pylon2.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.MiG_21Bis.Pylon3.Fuel_Tank_800_L__21_,
                    planes.MiG_21Bis.Pylon4.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.MiG_21Bis.Pylon5.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM,
                    planes.MiG_21Bis.Pylon6.ASO_2___countermeasures_pod
                ]
            }
        }
    ],

    'L_39ZA': [
        {
            "type": planes.L_39ZA,
            "id": planes.L_39ZA.id,
            "fuel": planes.L_39ZA.fuel_max,
            "chaff": planes.L_39ZA.chaff,
            "flare": planes.L_39ZA.flare,
            "payload": {
                "pylons": [
                    planes.L_39ZA.Pylon1.UB_16_57UMP___16_x_UnGd_Rkts__57_mm_S_5KO_HEAT_Frag,
                    planes.L_39ZA.Pylon2.UB_16_57UMP___16_x_UnGd_Rkts__57_mm_S_5KO_HEAT_Frag,
                    None,
                    planes.L_39ZA.Pylon4.UB_16_57UMP___16_x_UnGd_Rkts__57_mm_S_5KO_HEAT_Frag,
                    planes.L_39ZA.Pylon5.UB_16_57UMP___16_x_UnGd_Rkts__57_mm_S_5KO_HEAT_Frag,
                ]
            }
        },
        {
            'type': planes.L_39ZA,
            'id': planes.L_39ZA.id,
            'fuel': planes.L_39ZA.fuel_max,
            'chaff': planes.L_39ZA.chaff,
            'flare': planes.L_39ZA.flare,
            'payload': {
                'pylons': [
                    planes.L_39ZA.Pylon1.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.L_39ZA.Pylon2.FAB_250_M62___250_kg_GP_Bomb_LD,
                    None,
                    planes.L_39ZA.Pylon4.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.L_39ZA.Pylon5.FAB_250_M62___250_kg_GP_Bomb_LD,
                ]
            }
        },
    ],

    'MiG_15bis': [
        {
            "type": planes.MiG_15bis,
            "id": planes.MiG_15bis.id,
            "fuel": planes.MiG_15bis.fuel_max,
            "chaff": planes.MiG_15bis.chaff,
            "flare": planes.MiG_15bis.flare,
            "payload": {
                "pylons": [
                    planes.MiG_15bis.Pylon1.FAB_100M,
                    planes.MiG_15bis.Pylon2.FAB_100M
                ]
            }
        }
    ],

    'MiG_27K': [
        {
            "type": planes.MiG_27K,
            "id": planes.MiG_27K.id,
            "fuel": planes.MiG_27K.fuel_max,
            "chaff": planes.MiG_27K.chaff,
            "flare": planes.MiG_27K.flare,
            "payload": {
                "pylons": [
                    None,
                    planes.MiG_27K.Pylon2.B_8M1___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag,
                    planes.MiG_27K.Pylon3.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                    planes.MiG_27K.Pylon4.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.MiG_27K.Pylon5.Fuel_tank_800L,
                    planes.MiG_27K.Pylon6.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.MiG_27K.Pylon7.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                    planes.MiG_27K.Pylon8.B_8M1___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag,
                    None,
                ]
            }
        }
    ],

    'MiG_23MLD': [
        {
            "type": planes.MiG_23MLD,
            "id": planes.MiG_23MLD.id,
            "fuel": planes.MiG_23MLD.fuel_max,
            "chaff": planes.MiG_23MLD.chaff,
            "flare": planes.MiG_23MLD.flare,
            "payload": {
                "pylons": [
                    None,
                    planes.MiG_23MLD.Pylon2.R_24T__AA_7_Apex_IR____Infra_Red,
                    planes.MiG_23MLD.Pylon3.APU_68___S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk_,
                    planes.MiG_23MLD.Pylon4.Fuel_tank_800L,
                    planes.MiG_23MLD.Pylon5.APU_68___S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk_,
                    planes.MiG_23MLD.Pylon6.R_24T__AA_7_Apex_IR____Infra_Red,
                    None
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
                    planes.Su_17M4.Pylon1.MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD,
                    planes.Su_17M4.Pylon2.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                    planes.Su_17M4.Pylon3.UB_32A___32_x_UnGd_Rkts__57_mm_S_5KO_HEAT_Frag,
                    planes.Su_17M4.Pylon4.Fuel_tank_800L,
                    planes.Su_17M4.Pylon5.Fuel_tank_800L,
                    planes.Su_17M4.Pylon6.UB_32A___32_x_UnGd_Rkts__57_mm_S_5KO_HEAT_Frag,
                    planes.Su_17M4.Pylon7.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                    planes.Su_17M4.Pylon8.MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD,
                ]
            }
        },
        {
            "type": planes.Su_17M4,
            "id": planes.Su_17M4.id,
            "fuel": planes.Su_17M4.fuel_max,
            "chaff": planes.Su_17M4.chaff,
            "flare": planes.Su_17M4.flare,
            "payload": {
                "pylons": [
                    planes.Su_17M4.Pylon1.APU_68___S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk_,
                    planes.Su_17M4.Pylon2.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                    planes.Su_17M4.Pylon3.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_17M4.Pylon4.Fuel_tank_800L,
                    planes.Su_17M4.Pylon5.Fuel_tank_800L,
                    planes.Su_17M4.Pylon6.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_17M4.Pylon7.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                    planes.Su_17M4.Pylon8.APU_68___S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk_

                ]
            }
        },
    ],

    'Su_25': [
        {
            'type': planes.Su_25,
            'id': planes.Su_25.id,
            'fuel': planes.Su_25.fuel_max,
            'chaff': planes.Su_25.chaff,
            'flare': planes.Su_25.flare,
            'payload': {
                'pylons': [
                    planes.Su_25.Pylon1.R_60M__AA_8_Aphid_B____IR_AAM,
                    planes.Su_25.Pylon2.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.Su_25.Pylon3.B_8M1___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag,
                    planes.Su_25.Pylon4.B_8M1___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag,
                    planes.Su_25.Pylon5.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod,
                    planes.Su_25.Pylon6.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod,
                    planes.Su_25.Pylon7.B_8M1___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag,
                    planes.Su_25.Pylon8.B_8M1___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag,
                    planes.Su_25.Pylon9.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.Su_25.Pylon10.R_60M__AA_8_Aphid_B____IR_AAM,
                ]
            }
        },
        {
            "type": planes.Su_25,
            "id": planes.Su_25.id,
            "fuel": planes.Su_25.fuel_max,
            "chaff": planes.Su_25.chaff,
            "flare": planes.Su_25.flare,
            "payload": {
                "pylons": [
                    planes.Su_25.Pylon1.R_60M__AA_8_Aphid_B____IR_AAM,
                    planes.Su_25.Pylon2.APU_68___S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk_,
                    planes.Su_25.Pylon3.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.Su_25.Pylon4.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.Su_25.Pylon5.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.Su_25.Pylon6.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.Su_25.Pylon7.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.Su_25.Pylon8.FAB_250_M62___250_kg_GP_Bomb_LD,
                    planes.Su_25.Pylon9.APU_68___S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk_,
                    planes.Su_25.Pylon10.R_60M__AA_8_Aphid_B____IR_AAM,
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
                    planes.Su_24M.Pylon2.O_25___1_x_UnGd_Rkts__340_mm_S_25_OFM_Hardened_Target_Penetrator,
                    planes.Su_24M.Pylon3.FAB_500_M_62___500kg_GP_Bomb_LD,
                    None,
                    planes.Su_24M.Pylon5.Fuel_tank_2000L,
                    planes.Su_24M.Pylon6.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_24M.Pylon7.O_25___1_x_UnGd_Rkts__340_mm_S_25_OFM_Hardened_Target_Penetrator,
                    planes.Su_24M.Pylon8.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                ]
            }
        },
        {
            "type": planes.Su_24M,
            "id": planes.Su_24M.id,
            "fuel": planes.Su_24M.fuel_max,
            "chaff": planes.Su_24M.chaff,
            "flare": planes.Su_24M.flare,
            "payload": {
                "pylons": [
                    planes.Su_24M.Pylon1.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_,
                    planes.Su_24M.Pylon2.APU_68___S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk_,
                    planes.Su_24M.Pylon3.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_24M.Pylon4.KAB_1500Kr___1500kg_TV_Guided_Bomb,
                    planes.Su_24M.Pylon5.Fuel_tank_2000L,
                    planes.Su_24M.Pylon6.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_24M.Pylon7.APU_68___S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk_,
                    planes.Su_24M.Pylon8.APU_60_1M_with_R_60M__AA_8_Aphid_B____IR_AAM_

                ]
            }
        },
    ],

    'MiG_19P': [
        {
            "type": planes.MiG_19P,
            "id": planes.MiG_19P.id,
            "fuel": planes.MiG_19P.fuel_max,
            "chaff": planes.MiG_19P.chaff,
            "flare": planes.MiG_19P.flare,
            "payload": {
                "pylons": [
                    planes.MiG_19P.Pylon1.K_13A,
                    planes.MiG_19P.Pylon2.PTB760_MIG19,
                    planes.MiG_19P.Pylon3.ORO_57K___S_5M_x_8,
                    planes.MiG_19P.Pylon4.ORO_57K___S_5M_x_8,
                    planes.MiG_19P.Pylon5.PTB760_MIG19,
                    planes.MiG_19P.Pylon6.K_13A,
                ]
            }
        },
    ],

    'M_2000C': [
        {
            "type": planes.M_2000C,
            "id": planes.M_2000C.id,
            "fuel": planes.M_2000C.fuel_max,
            "chaff": planes.M_2000C.chaff,
            "flare": planes.M_2000C.flare,
            "payload": {
                "pylons": [
                    planes.M_2000C.Pylon1.Matra_Magic_II,
                    planes.M_2000C.Pylon2.AUF2_SAMP_250_HD_x_2,
                    planes.M_2000C.Pylon3.BLG_66_AC_Belouga,
                    planes.M_2000C.Pylon5.RPL_522_1300_liters_Fuel_Tank,
                    planes.M_2000C.Pylon6.BLG_66_AC_Belouga,
                    planes.M_2000C.Pylon8.AUF2_SAMP_250_HD_x_2,
                    planes.M_2000C.Pylon9.Matra_Magic_II,
                    planes.M_2000C.Pylon10.Eclair_M_4_2__32_flares_36_chaffs,
                    None,
                ]
            }
        },
    ],

    'Mirage_F1CE': [
        {
            "type": planes.Mirage_F1CE,
            "id": planes.Mirage_F1CE.id,
            "fuel": planes.Mirage_F1CE.fuel_max,
            "chaff": planes.Mirage_F1CE.chaff,
            "flare": planes.Mirage_F1CE.flare,
            "livery_id": "114th combat wing tanagra ab (fictional c version)",
            "payload": {
                "pylons": [
                    planes.Mirage_F1CE.Pylon1.R550_Magic_2_IR_AAM,
                    planes.Mirage_F1CE.Pylon2.MATRA_F1___36_x_UnGd_Rkts__68_mm_SNEB_Type_257_F1B_HE_Frag_Lg_Whd,
                    planes.Mirage_F1CE.Pylon3.BR_500,
                    planes.Mirage_F1CE.Pylon4.PTB_1200_F1,
                    planes.Mirage_F1CE.Pylon5.BR_500,
                    planes.Mirage_F1CE.Pylon6.MATRA_F1___36_x_UnGd_Rkts__68_mm_SNEB_Type_257_F1B_HE_Frag_Lg_Whd,
                    planes.Mirage_F1CE.Pylon7.R550_Magic_2_IR_AAM,
                ]
            }
        },
    ],
}

