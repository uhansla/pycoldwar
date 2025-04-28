import dcs.planes as planes

planes_map = {
    'F-4E-45MC': [
        {
            'type': planes.F_4E_45MC,
            'id': planes.F_4E_45MC.id,
            'fuel': planes.F_4E_45MC.fuel_max,
            'chaff': planes.F_4E_45MC.chaff,
            'flare': planes.F_4E_45MC.flare,
            'payload': {
                'pylons': [
                    planes.F_4E_45MC.Pylon1._6x_Mk_82___500lb_GP_Bomb_LD__MER_,
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
                    planes.F_4E_45MC.Pylon13._6x_Mk_82___500lb_GP_Bomb_LD__MER_,
                    planes.F_4E_45MC.Pylon14.ALE_40_Dispensers__30_Flares__60_Chaff_,
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
                    planes.Mirage_F1CE.Pylon2.SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1CE.Pylon3.SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1CE.Pylon4.CLB_4___4_x_SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1CE.Pylon5.SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1CE.Pylon6.SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1CE.Pylon7.R550_Magic_1_IR_AAM,
                ]
            }
        },
    ],
    'F-5E-3': [
        {
            'type': planes.F_5E_3,
            'id': planes.F_5E_3.id,
            'fuel': planes.F_5E_3.fuel_max,
            'chaff': planes.F_5E_3.chaff,
            'flare': planes.F_5E_3.flare,
            'payload': {
                'pylons': [
                    planes.F_5E_3.Pylon1.AIM_9P_Sidewinder_IR_AAM,
                    planes.F_5E_3.Pylon2.Mk_82___500lb_GP_Bomb_LD,
                    planes.F_5E_3.Pylon3.F_5_275Gal_Fuel_tank,
                    planes.F_5E_3.Pylon4._5_x_Mk_82___500lb_GP_Bombs_LD,
                    planes.F_5E_3.Pylon5.F_5_275Gal_Fuel_tank,
                    planes.F_5E_3.Pylon6.Mk_82___500lb_GP_Bomb_LD,
                    planes.F_5E_3.Pylon7.AIM_9P_Sidewinder_IR_AAM,
                ]
            }
        },
        {
            'type': planes.F_5E_3,
            'id': planes.F_5E_3.id,
            'fuel': planes.F_5E_3.fuel_max,
            'chaff': planes.F_5E_3.chaff,
            'flare': planes.F_5E_3.flare,
            'payload': {
                'pylons': [
                    planes.F_5E_3.Pylon1.AIM_9P_Sidewinder_IR_AAM,
                    planes.F_5E_3.Pylon2.Mk_82___500lb_GP_Bomb_LD,
                    planes.F_5E_3.Pylon3.Mk_82___500lb_GP_Bomb_LD,
                    planes.F_5E_3.Pylon4._5_x_Mk_82___500lb_GP_Bombs_LD,
                    planes.F_5E_3.Pylon5.Mk_82___500lb_GP_Bomb_LD,
                    planes.F_5E_3.Pylon6.Mk_82___500lb_GP_Bomb_LD,
                    planes.F_5E_3.Pylon7.AIM_9P_Sidewinder_IR_AAM,
                ]
            }
        },
        {
            'type': planes.F_5E_3,
            'id': planes.F_5E_3.id,
            'fuel': planes.F_5E_3.fuel_max,
            'chaff': planes.F_5E_3.chaff,
            'flare': planes.F_5E_3.flare,
            'payload': {
                'pylons': [
                    planes.F_5E_3.Pylon1.AIM_9P_Sidewinder_IR_AAM,
                    None,
                    planes.F_5E_3.Pylon3.Mk_83___1000lb_GP_Bomb_LD,
                    planes.F_5E_3.Pylon4.Mk_83___1000lb_GP_Bomb_LD,
                    planes.F_5E_3.Pylon5.Mk_83___1000lb_GP_Bomb_LD,
                    None,
                    planes.F_5E_3.Pylon7.AIM_9P_Sidewinder_IR_AAM,
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
                    planes.AJS37.Pylon2._4x_SB_M_71_120kg_GP_Bomb_Low_drag,
                    planes.AJS37.Pylon3._4x_SB_M_71_120kg_GP_Bomb_Low_drag,
                    planes.AJS37.Pylon4.AJS_External_tank_1013kg_fuel,
                    planes.AJS37.Pylon5._4x_SB_M_71_120kg_GP_Bomb_Low_drag,
                    planes.AJS37.Pylon6._4x_SB_M_71_120kg_GP_Bomb_Low_drag,
                    planes.AJS37.Pylon7.LAU_7_with_RB_24__AIM_9B__Sidewinder_IR_AAM,
                ]
            }
        },
    ],
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
                    planes.F_14A_135_GR.Pylon4.MAK79_4_Mk_82,
                    planes.F_14A_135_GR.Pylon5.MAK79_3_Mk_82,
                    planes.F_14A_135_GR.Pylon6.MAK79_3_Mk_82_,
                    planes.F_14A_135_GR.Pylon7.MAK79_4_Mk_82,
                    planes.F_14A_135_GR.Pylon8.Fuel_tank_300_gal_,
                    planes.F_14A_135_GR.Pylon9.AIM_7F_,
                    planes.F_14A_135_GR.Pylon10.LAU_138_AIM_9L,
                ]
            }
        },
    ],
    'Mirage-F1CT': [
        {
            'type': planes.Mirage_F1CT,
            'id': planes.Mirage_F1CT.id,
            'fuel': planes.Mirage_F1CT.fuel_max,
            'chaff': planes.Mirage_F1CT.chaff,
            'flare': planes.Mirage_F1CT.flare,
            'payload': {
                'pylons': [
                    planes.Mirage_F1CT.Pylon1.R550_Magic_1_IR_AAM,
                    planes.Mirage_F1CT.Pylon2.SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1CT.Pylon3.SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1CT.Pylon4.CLB_4___4_x_SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1CT.Pylon5.SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1CT.Pylon6.SAMP_400___400_kg_GP_Bomb_LD,
                    planes.Mirage_F1CT.Pylon7.R550_Magic_1_IR_AAM,
                ]
            }
        },
    ],
    'Su-25': [
        {
            'type': planes.Su_25,
            'id': planes.Su_25.id,
            'fuel': planes.Su_25.fuel_max,
            'chaff': planes.Su_25.chaff,
            'flare': planes.Su_25.flare,
            'payload': {
                'pylons': [
                    planes.Su_25.Pylon1.R_60M__AA_8_Aphid_B____IR_AAM,
                    planes.Su_25.Pylon2.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_25.Pylon3.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_25.Pylon4.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_25.Pylon5.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_25.Pylon6.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_25.Pylon7.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_25.Pylon8.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_25.Pylon9.FAB_500_M_62___500kg_GP_Bomb_LD,
                    planes.Su_25.Pylon10.R_60M__AA_8_Aphid_B____IR_AAM,
                ]
            }
        },
    ],
    'F-5E': [
        {
            'type': planes.F_5E,
            'id': planes.F_5E.id,
            'fuel': planes.F_5E.fuel_max,
            'chaff': planes.F_5E.chaff,
            'flare': planes.F_5E.flare,
            'payload': {
                'pylons': [
                    planes.F_5E.Pylon1.AIM_9P_Sidewinder_IR_AAM,
                    planes.F_5E.Pylon2.Mk_82___500lb_GP_Bomb_LD,
                    planes.F_5E.Pylon3.Mk_82___500lb_GP_Bomb_LD,
                    planes.F_5E.Pylon4._5_x_Mk_82___500lb_GP_Bombs_LD,
                    planes.F_5E.Pylon5.Mk_82___500lb_GP_Bomb_LD,
                    planes.F_5E.Pylon6.Mk_82___500lb_GP_Bomb_LD,
                    planes.F_5E.Pylon7.AIM_9P_Sidewinder_IR_AAM,
                ]
            }
        },
    ],
}
