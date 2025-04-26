import dcs.planes as planes
import random


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

planes = {
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

    'A_10A': [
        {
            "type": planes.A_10A,
            "id": planes.A_10A.id,
            "fuel": planes.A_10A.fuel_max,
            "chaff": planes.A_10A.chaff,
            "flare": planes.A_10A.flare,
            "payload": {
                "pylons": [
                    planes.A_10A.Pylon1.ALQ_131___ECM_Pod,
                    planes.A_10A.Pylon2.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
                    planes.A_10A.Pylon3.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_,
                    planes.A_10A.Pylon4.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
                    planes.A_10A.Pylon5.Mk_82___500lb_GP_Bomb_LD,
                    planes.A_10A.Pylon6.Mk_82___500lb_GP_Bomb_LD,
                    planes.A_10A.Pylon7.Mk_82___500lb_GP_Bomb_LD,
                    planes.A_10A.Pylon8.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
                    planes.A_10A.Pylon9.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_,
                    planes.A_10A.Pylon10.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
                    planes.A_10A.Pylon11.LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM
                ]
            }
        }
    ],

    'AJS37': [
        {
            "type": planes.AJS37,
            "id": planes.AJS37.id,
            "fuel": planes.AJS37.fuel_max,
            "chaff": planes.AJS37.chaff,
            "flare": planes.AJS37.flare,
            "payload": {
                "pylons": [
                    planes.AJS37.Pylon1.Rb_24J__AIM_9P__Sidewinder_IR_AAM,
                    planes.AJS37.Pylon2.Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_,
                    None,
                    planes.AJS37.Pylon4.AJS_External_tank_1013kg_fuel,
                    None,
                    planes.AJS37.Pylon6.Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_,
                    planes.AJS37.Pylon7.Rb_24J__AIM_9P__Sidewinder_IR_AAM
                ]
            }
        }
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


    'MiG_21Bis': [
        {
            "type": planes.MiG_21Bis,
            "id": planes.MiG_21Bis.id,
            "fuel": planes.MiG_21Bis.fuel_max,
            "chaff": planes.MiG_21Bis.chaff,
            "flare": planes.MiG_21Bis.flare,
            "payload": {
                "pylons": [
                    planes.MiG_21Bis.Pylon1.R_60M,
                    planes.MiG_21Bis.Pylon2.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.MiG_21Bis.Pylon3.Fuel_Tank_800_L__21_,
                    planes.MiG_21Bis.Pylon4.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.MiG_21Bis.Pylon5.R_60M,
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
                    planes.L_39ZA.Pylon1.UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag,
                    planes.L_39ZA.Pylon2.UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag,
                    None,
                    planes.L_39ZA.Pylon4.UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag,
                    planes.L_39ZA.Pylon5.UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag,
                ]
            }
        }
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
                    planes.MiG_27K.Pylon2.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red,
                    planes.MiG_27K.Pylon3.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag,
                    planes.MiG_27K.Pylon4.FAB_250_M62___250kg_GP_Bomb_LD,
                    planes.MiG_27K.Pylon5.Fuel_tank_800L,
                    planes.MiG_27K.Pylon6.FAB_250_M62___250kg_GP_Bomb_LD,
                    planes.MiG_27K.Pylon7.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag,
                    planes.MiG_27K.Pylon8.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red,
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
                    planes.MiG_23MLD.Pylon2.R_24T__AA_7_Apex_IR____Infra_Red,
                    planes.MiG_23MLD.Pylon3.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__,
                    planes.MiG_23MLD.Pylon4.Fuel_tank_800L,
                    planes.MiG_23MLD.Pylon5.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__,
                    planes.MiG_23MLD.Pylon6.R_24T__AA_7_Apex_IR____Infra_Red,
                ]
            }
        },
    ],

    'Su_25': [
        {
            "type": planes.Su_25,
            "id": planes.Su_25.id,
            "fuel": planes.Su_25.fuel_max,
            "chaff": planes.Su_25.chaff,
            "flare": planes.Su_25.flare,
            "payload": {
                "pylons": [
                    planes.Su_25.Pylon1.R_60M__AA_8_Aphid____Infra_Red,
                    planes.Su_25.Pylon2.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__,
                    planes.Su_25.Pylon3.FAB_250_M62___250kg_GP_Bomb_LD,
                    planes.Su_25.Pylon4.FAB_250_M62___250kg_GP_Bomb_LD,
                    planes.Su_25.Pylon5.FAB_250_M62___250kg_GP_Bomb_LD,
                    planes.Su_25.Pylon6.FAB_250_M62___250kg_GP_Bomb_LD,
                    planes.Su_25.Pylon7.FAB_250_M62___250kg_GP_Bomb_LD,
                    planes.Su_25.Pylon8.FAB_250_M62___250kg_GP_Bomb_LD,
                    planes.Su_25.Pylon9.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__,
                    planes.Su_25.Pylon10.R_60M__AA_8_Aphid____Infra_Red,
                ]
            }
        },
    ],

    'Su_17M4': [
        {
            "type": planes.Su_17M4,
            "id": planes.Su_17M4.id,
            "fuel": planes.Su_17M4.fuel_max,
            "chaff": planes.Su_17M4.chaff,
            "flare": planes.Su_17M4.flare,
            "payload": {
                "pylons": [
                    planes.Su_17M4.Pylon1.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__,
                    planes.Su_17M4.Pylon2.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red,
                    planes.Su_17M4.Pylon3.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_17M4.Pylon4.Fuel_tank_800L,
                    planes.Su_17M4.Pylon5.Fuel_tank_800L,
                    planes.Su_17M4.Pylon6.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_17M4.Pylon7.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red,
                    planes.Su_17M4.Pylon8.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__

                ]
            }
        },
    ],

    'Su_24M': [
        {
            "type": planes.Su_24M,
            "id": planes.Su_24M.id,
            "fuel": planes.Su_24M.fuel_max,
            "chaff": planes.Su_24M.chaff,
            "flare": planes.Su_24M.flare,
            "payload": {
                "pylons": [
                    planes.Su_24M.Pylon1.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red,
                    planes.Su_24M.Pylon2.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__,
                    planes.Su_24M.Pylon3.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_24M.Pylon4.KAB_1500Kr___1500kg_TV_Guided_Bomb,
                    planes.Su_24M.Pylon5.Fuel_tank_2000L,
                    planes.Su_24M.Pylon6.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_24M.Pylon7.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__,
                    planes.Su_24M.Pylon8.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red

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
}

BLUE = [
    'F_A_18A',
    'A_10A',
    # 'F_4E',
    # 'Mirage_F1C',
    # 'Mirage_F1CE',
    # 'Mirage_F1EE',
    # 'Mirage_F1M_EE',
    'F_5E',
    'F_5E_3',
    # 'F_86F_Sabre',
    'AJS37',
    'L_39ZA',
    # 'M_2000C'
]

RED = [
    'Su_17M4',
    'Su_24M',
    'MiG_23MLD',
    'MiG_27K',
    'MiG_21Bis',
    'MiG_19P',
    'MiG_15bis',
    'Su_25'
]

def get_random_payload(plane_name):
    """
    Returns a random payload dictionary for the given plane name.
    """
    payload_options = planes.get(plane_name)
    if not payload_options:
        raise ValueError(f"Plane {plane_name} not found in planes dictionary.")
    return random.choice(payload_options)