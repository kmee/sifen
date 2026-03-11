from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


class TcUniMed(Enum):
    """
    :cvar VALUE_87: Metros - m
    :cvar VALUE_2366: Costo Por Mil - CPM
    :cvar VALUE_2329: Unidad Internacional - UI
    :cvar VALUE_110: Metros cúbicos - M3
    :cvar VALUE_77: Unidad - UNI
    :cvar VALUE_86: Gramos - g
    :cvar VALUE_89: Litros - LT
    :cvar VALUE_90: Miligramos - MG
    :cvar VALUE_91: Centimetros - CM
    :cvar VALUE_92: Centimetros cuadrados - CM2
    :cvar VALUE_93: Centimetros cubicos - CM3
    :cvar VALUE_94: Pulgadas - PUL
    :cvar VALUE_96: Milímetros cuadrados - MM2
    :cvar VALUE_79: Kilogramos s/ metro cuadrado - kg/m2
    :cvar VALUE_97: Año - AA
    :cvar VALUE_98: Mes - ME
    :cvar VALUE_99: Tonelada - TN
    :cvar VALUE_100: Hora - Hs
    :cvar VALUE_101: Minuto - Mi
    :cvar VALUE_104: Determinación - DET
    :cvar VALUE_103: Yardas - Ya
    :cvar VALUE_108: Metros - MT
    :cvar VALUE_109: Metros cuadrados - M2
    :cvar VALUE_95: Milímetros - MM
    :cvar VALUE_666: Segundo - Se
    :cvar VALUE_102: Día - Di
    :cvar VALUE_83: Kilogramos - kg
    :cvar VALUE_88: Mililitros - ML
    :cvar VALUE_625: Kilómetros - Km
    :cvar VALUE_660: Metro lineal - ml
    :cvar VALUE_885: Unidad Medida Global - GL
    :cvar VALUE_891: Por Milaje - pm
    :cvar VALUE_869: Hectáreas - ha
    :cvar VALUE_569: Ración - ración
    :cvar VALUE_111: Bovinas - 4A
    :cvar VALUE_112: Curie - Ci
    :cvar VALUE_113: Docena - DOC
    :cvar VALUE_114: Galones (US) (3,7843 LT) - GLL
    :cvar VALUE_115: Gruesas - GRO
    :cvar VALUE_116: Kilogramo Bruto - E4
    :cvar VALUE_117: Kits - KT
    :cvar VALUE_118: Microcurie - M5
    :cvar VALUE_119: Milicurie - MCU
    :cvar VALUE_120: Millar - MIL
    :cvar VALUE_121: Par - PAR
    :cvar VALUE_122: Pies - FOT
    :cvar VALUE_123: Pies Cuadradas - FTK
    :cvar VALUE_124: Piezas - PCE
    :cvar VALUE_125: Quilate - KLT
    :cvar VALUE_126: Resmas - RM
    :cvar VALUE_127: Rollos - RO
    :cvar VALUE_128: 1000 Kilowatt Hora - kWh
    :cvar VALUE_129: Mazos - U(JGO)
    :cvar VALUE_130: Tambores - DR
    :cvar VALUE_131: Caja - BX
    :cvar VALUE_132: Juego - SET
    :cvar VALUE_133: Paquete - PK
    :cvar VALUE_134: Bolsa - BG
    :cvar VALUE_135: Docena Par - DPC
    :cvar VALUE_136: Pote - JR
    :cvar VALUE_137: Fardos - BL
    :cvar VALUE_138: Bulto - AB
    :cvar VALUE_139: Cesta - BK
    :cvar VALUE_140: Peso Base - BW
    """

    VALUE_87 = 87
    VALUE_2366 = 2366
    VALUE_2329 = 2329
    VALUE_110 = 110
    VALUE_77 = 77
    VALUE_86 = 86
    VALUE_89 = 89
    VALUE_90 = 90
    VALUE_91 = 91
    VALUE_92 = 92
    VALUE_93 = 93
    VALUE_94 = 94
    VALUE_96 = 96
    VALUE_79 = 79
    VALUE_97 = 97
    VALUE_98 = 98
    VALUE_99 = 99
    VALUE_100 = 100
    VALUE_101 = 101
    VALUE_104 = 104
    VALUE_103 = 103
    VALUE_108 = 108
    VALUE_109 = 109
    VALUE_95 = 95
    VALUE_666 = 666
    VALUE_102 = 102
    VALUE_83 = 83
    VALUE_88 = 88
    VALUE_625 = 625
    VALUE_660 = 660
    VALUE_885 = 885
    VALUE_891 = 891
    VALUE_869 = 869
    VALUE_569 = 569
    VALUE_111 = 111
    VALUE_112 = 112
    VALUE_113 = 113
    VALUE_114 = 114
    VALUE_115 = 115
    VALUE_116 = 116
    VALUE_117 = 117
    VALUE_118 = 118
    VALUE_119 = 119
    VALUE_120 = 120
    VALUE_121 = 121
    VALUE_122 = 122
    VALUE_123 = 123
    VALUE_124 = 124
    VALUE_125 = 125
    VALUE_126 = 126
    VALUE_127 = 127
    VALUE_128 = 128
    VALUE_129 = 129
    VALUE_130 = 130
    VALUE_131 = 131
    VALUE_132 = 132
    VALUE_133 = 133
    VALUE_134 = 134
    VALUE_135 = 135
    VALUE_136 = 136
    VALUE_137 = 137
    VALUE_138 = 138
    VALUE_139 = 139
    VALUE_140 = 140


class TdDesUniMed(Enum):
    """
    :cvar M: Metros
    :cvar CPM: Costo Por Mil
    :cvar UI: Unidad Internacional
    :cvar M3: Metros cúbicos
    :cvar UNI: Unidad
    :cvar G: Gramos
    :cvar LT: Litros
    :cvar MG: Miligramos
    :cvar CM: Centimetros
    :cvar CM2: Centimetros cuadrados
    :cvar CM3: Centimetros cubicos
    :cvar PUL: Pulgadas
    :cvar MM2: Milímetros cuadrados
    :cvar KG_M2: Kilogramos s/ metro cuadrado
    :cvar AA: Año
    :cvar ME: Mes
    :cvar TN: Tonelada
    :cvar HS: Hora
    :cvar MI: Minuto
    :cvar DET: Determinación
    :cvar YA: Yardas
    :cvar MT: Metros
    :cvar M2: Metros cuadrados
    :cvar MM: Milímetros
    :cvar SE: Segundo
    :cvar DI: Día
    :cvar KG: Kilogramos
    :cvar ML: Mililitros
    :cvar KM: Kilómetros
    :cvar ML_1: Metro lineal
    :cvar GL: Unidad Medida Global
    :cvar PM: Por Milaje
    :cvar HA: Hectáreas
    :cvar RACI_N: Ración
    :cvar VALUE_4_A: Bovinas
    :cvar CI: Curie
    :cvar DOC: Docena
    :cvar GLL: Galones (US) (3,7843 LT)
    :cvar GRO: Gruesas
    :cvar E4: Kilogramo Bruto
    :cvar KT: Kits
    :cvar M5: Microcurie
    :cvar MCU: Milicurie
    :cvar MIL: Millar
    :cvar PAR: Par
    :cvar FOT: Pies
    :cvar FTK: Pies Cuadradas
    :cvar PCE: Piezas
    :cvar KLT: Quilate
    :cvar RM: Resmas
    :cvar RO: Rollos
    :cvar K_WH: 1000 Kilowatt Hora
    :cvar U_JGO: Mazos
    :cvar DR: Tambores
    :cvar BX: Caja
    :cvar SET: Juego
    :cvar PK: Paquete
    :cvar BG: Bolsa
    :cvar DPC: Docena Par
    :cvar JR: Pote
    :cvar BL: Fardos
    :cvar AB: Bulto
    :cvar BK: Cesta
    :cvar BW: Peso Base
    """

    M = "m"
    CPM = "CPM"
    UI = "UI"
    M3 = "M3"
    UNI = "UNI"
    G = "g"
    LT = "LT"
    MG = "MG"
    CM = "CM"
    CM2 = "CM2"
    CM3 = "CM3"
    PUL = "PUL"
    MM2 = "MM2"
    KG_M2 = "kg/m2"
    AA = "AA"
    ME = "ME"
    TN = "TN"
    HS = "Hs"
    MI = "Mi"
    DET = "DET"
    YA = "Ya"
    MT = "MT"
    M2 = "M2"
    MM = "MM"
    SE = "Se"
    DI = "Di"
    KG = "kg"
    ML = "ML"
    KM = "Km"
    ML_1 = "ml"
    GL = "GL"
    PM = "pm"
    HA = "ha"
    RACI_N = "ración"
    VALUE_4_A = "4A"
    CI = "Ci"
    DOC = "DOC"
    GLL = "GLL"
    GRO = "GRO"
    E4 = "E4"
    KT = "KT"
    M5 = "M5"
    MCU = "MCU"
    MIL = "MIL"
    PAR = "PAR"
    FOT = "FOT"
    FTK = "FTK"
    PCE = "PCE"
    KLT = "KLT"
    RM = "RM"
    RO = "RO"
    K_WH = "kWh"
    U_JGO = "U(JGO)"
    DR = "DR"
    BX = "BX"
    SET = "SET"
    PK = "PK"
    BG = "BG"
    DPC = "DPC"
    JR = "JR"
    BL = "BL"
    AB = "AB"
    BK = "BK"
    BW = "BW"
