from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


class PaisType(Enum):
    """
    :cvar MKD: Macedonia del Norte
    :cvar TWN: Taiwán (Provincia de China)
    :cvar DZA: Argelia
    :cvar EGY: Egipto
    :cvar LBY: Libia
    :cvar MAR: Marruecos
    :cvar SDN: Sudán
    :cvar TUN: Túnez
    :cvar ESH: Sáhara Occidental
    :cvar IOT: Territorio Británico del Océano Índico
    :cvar BDI: Burundi
    :cvar COM: Comoras
    :cvar DJI: Djibouti
    :cvar ERI: Eritrea
    :cvar ETH: Etiopía
    :cvar ATF: Territorio de las Tierras Australes Francesas
    :cvar KEN: Kenya
    :cvar MDG: Madagascar
    :cvar MWI: Malawi
    :cvar MUS: Mauricio
    :cvar MYT: Mayotte
    :cvar MOZ: Mozambique
    :cvar REU: Reunión
    :cvar RWA: Rwanda
    :cvar SYC: Seychelles
    :cvar SOM: Somalia
    :cvar SSD: Sudán del Sur
    :cvar UGA: Uganda
    :cvar TZA: República Unida de Tanzanía
    :cvar ZMB: Zambia
    :cvar ZWE: Zimbabwe
    :cvar AGO: Angola
    :cvar CMR: Camerún
    :cvar CAF: República Centroafricana
    :cvar TCD: Chad
    :cvar COG: Congo
    :cvar COD: República Democrática del Congo
    :cvar GNQ: Guinea Ecuatorial
    :cvar GAB: Gabón
    :cvar STP: Santo Tomé y Príncipe
    :cvar BWA: Botswana
    :cvar LSO: Lesotho
    :cvar NAM: Namibia
    :cvar ZAF: Sudáfrica
    :cvar SWZ: Swazilandia
    :cvar BEN: Benin
    :cvar BFA: Burkina Faso
    :cvar CPV: Cabo Verde
    :cvar CIV: Côte d'Ivoire
    :cvar GMB: Gambia
    :cvar GHA: Ghana
    :cvar GIN: Guinea
    :cvar GNB: Guinea-Bissau
    :cvar LBR: Liberia
    :cvar MLI: Malí
    :cvar MRT: Mauritania
    :cvar NER: Níger
    :cvar NGA: Nigeria
    :cvar SHN: Santa Elena
    :cvar SEN: Senegal
    :cvar SLE: Sierra Leona
    :cvar TGO: Togo
    :cvar AIA: Anguila
    :cvar ATG: Antigua y Barbuda
    :cvar ABW: Aruba
    :cvar BHS: Bahamas
    :cvar BRB: Barbados
    :cvar BES: Bonaire, San Eustaquio y Saba
    :cvar VGB: Islas Vírgenes Británicas
    :cvar CYM: Islas Caimán
    :cvar CUB: CUBA
    :cvar CUW: Curaçao
    :cvar DMA: Dominica
    :cvar DOM: República Dominicana
    :cvar GRD: Granada
    :cvar GLP: Guadalupe
    :cvar HTI: Haití
    :cvar JAM: Jamaica
    :cvar MTQ: Martinica
    :cvar MSR: Montserrat
    :cvar PRI: Puerto Rico
    :cvar BLM: San Bartolomé
    :cvar KNA: Saint Kitts y Nevis
    :cvar LCA: Santa Lucía
    :cvar MAF: San Martín (parte francesa)
    :cvar VCT: San Vicente y las Granadinas
    :cvar SXM: San Martín (parte holandés)
    :cvar TTO: Trinidad y Tabago
    :cvar TCA: Islas Turcas y Caicos
    :cvar VIR: Islas Vírgenes de los Estados Unidos
    :cvar BLZ: Belice
    :cvar CRI: Costa Rica
    :cvar SLV: El Salvador
    :cvar GTM: Guatemala
    :cvar HND: Honduras
    :cvar MEX: México
    :cvar NIC: Nicaragua
    :cvar PAN: Panamá
    :cvar ARG: Argentina
    :cvar BOL: Bolivia (Estado Plurinacional de)
    :cvar BRA: Brasil
    :cvar CHL: Chile
    :cvar COL: Colombia
    :cvar ECU: Ecuador
    :cvar FLK: Islas Malvinas (Falkland)
    :cvar GUF: Guayana Francesa
    :cvar GUY: Guyana
    :cvar PRY: Paraguay
    :cvar PER: Perú
    :cvar SGS: Georgia del Sur y las Islas Sandwich del Sur
    :cvar SUR: Suriname
    :cvar URY: Uruguay
    :cvar VEN: Venezuela (República Bolivariana de)
    :cvar BMU: Bermuda
    :cvar CAN: Canadá
    :cvar GRL: Groenlandia
    :cvar SPM: Saint Pierre y Miquelon
    :cvar USA: Estados Unidos de América
    :cvar ATA: Antártida
    :cvar KAZ: Kazajstán
    :cvar KGZ: Kirguistán
    :cvar TJK: Tayikistán
    :cvar TKM: Turkmenistán
    :cvar UZB: Uzbekistán
    :cvar CHN: China
    :cvar HKG: Hong Kong
    :cvar MAC: Macao
    :cvar PRK: República Popular Democrática de Corea
    :cvar JPN: Japón
    :cvar MNG: Mongolia
    :cvar KOR: República de Corea
    :cvar BRN: Brunei Darussalam
    :cvar KHM: Camboya
    :cvar IDN: Indonesia
    :cvar LAO: República Democrática Popular Lao
    :cvar MYS: Malasia
    :cvar MMR: Myanmar
    :cvar PHL: Filipinas
    :cvar SGP: Singapur
    :cvar THA: Tailandia
    :cvar TLS: Timor-Leste
    :cvar VNM: Viet Nam
    :cvar AFG: Afganistán
    :cvar BGD: Bangladesh
    :cvar BTN: Bhután
    :cvar IND: India
    :cvar IRN: Irán (República Islámica del)
    :cvar MDV: Maldivas
    :cvar NPL: Nepal
    :cvar PAK: Pakistán
    :cvar LKA: Sri Lanka
    :cvar ARM: Armenia
    :cvar AZE: Azerbaiyán
    :cvar BHR: Bahrein
    :cvar CYP: Chipre
    :cvar GEO: Georgia
    :cvar IRQ: Iraq
    :cvar ISR: Israel
    :cvar JOR: Jordania
    :cvar KWT: Kuwait
    :cvar LBN: Líbano
    :cvar OMN: Omán
    :cvar QAT: Qatar
    :cvar SAU: Arabia Saudita
    :cvar PSE: Estado de Palestina
    :cvar SYR: República Árabe Siria
    :cvar TUR: Turquía
    :cvar ARE: Emiratos Árabes Unidos
    :cvar YEM: Yemen
    :cvar BLR: Belarús
    :cvar BGR: Bulgaria
    :cvar CZE: Chequia
    :cvar HUN: Hungría
    :cvar POL: Polonia
    :cvar MDA: República de Moldova
    :cvar ROU: Rumania
    :cvar RUS: Federación de Rusia
    :cvar SVK: Eslovaquia
    :cvar UKR: Ucrania
    :cvar ALA: Islas Åland
    :cvar GGY: Guernsey
    :cvar JEY: Jersey
    :cvar DNK: Dinamarca
    :cvar EST: Estonia
    :cvar FRO: Islas Feroe
    :cvar FIN: Finlandia
    :cvar ISL: Islandia
    :cvar IRL: Irlanda
    :cvar IMN: Isla de Man
    :cvar LVA: Letonia
    :cvar LTU: Lituania
    :cvar NOR: Noruega
    :cvar SJM: Islas Svalbard y Jan Mayen
    :cvar SWE: Suecia
    :cvar GBR: Reino Unido de Gran Bretaña e Irlanda del Norte
    :cvar ALB: Albania
    :cvar AND: Andorra
    :cvar BIH: Bosnia y Herzegovina
    :cvar HRV: Croacia
    :cvar GIB: Gibraltar
    :cvar GRC: Grecia
    :cvar VAT: Santa Sede
    :cvar ITA: Italia
    :cvar MLT: Malta
    :cvar MNE: Montenegro
    :cvar PRT: Portugal
    :cvar SMR: San Marino
    :cvar SRB: Serbia
    :cvar SVN: Eslovenia
    :cvar ESP: España
    :cvar AUT: Austria
    :cvar BEL: Bélgica
    :cvar FRA: Francia
    :cvar DEU: Alemania
    :cvar LIE: Liechtenstein
    :cvar LUX: Luxemburgo
    :cvar MCO: Mónaco
    :cvar NLD: Países Bajos
    :cvar CHE: Suiza
    :cvar AUS: Australia
    :cvar CXR: Isla de Navidad
    :cvar CCK: Islas Cocos (Keeling)
    :cvar HMD: Islas Heard y McDonald
    :cvar NZL: Nueva Zelandia
    :cvar NFK: Islas Norfolk
    :cvar FJI: Fiji
    :cvar NCL: Nueva Caledonia
    :cvar PNG: Papua Nueva Guinea
    :cvar SLB: Islas Salomón
    :cvar VUT: Vanuatu
    :cvar GUM: Guam
    :cvar KIR: Kiribati
    :cvar MHL: Islas Marshall
    :cvar FSM: Micronesia (Estados Federados de)
    :cvar NRU: Nauru
    :cvar MNP: Islas Marianas Septentrionales
    :cvar PLW: Palau
    :cvar UMI: Islas menores alejadas de Estados Unidos
    :cvar ASM: Samoa Americana
    :cvar COK: Islas Cook
    :cvar PYF: Polinesia Francesa
    :cvar NIU: Niue
    :cvar PCN: Pitcairn
    :cvar WSM: Samoa
    :cvar TKL: Tokelau
    :cvar TON: Tonga
    :cvar TUV: Tuvalu
    :cvar WLF: Islas Wallis y Futuna
    :cvar NN: NO EXISTE
    """

    MKD = "MKD"
    TWN = "TWN"
    DZA = "DZA"
    EGY = "EGY"
    LBY = "LBY"
    MAR = "MAR"
    SDN = "SDN"
    TUN = "TUN"
    ESH = "ESH"
    IOT = "IOT"
    BDI = "BDI"
    COM = "COM"
    DJI = "DJI"
    ERI = "ERI"
    ETH = "ETH"
    ATF = "ATF"
    KEN = "KEN"
    MDG = "MDG"
    MWI = "MWI"
    MUS = "MUS"
    MYT = "MYT"
    MOZ = "MOZ"
    REU = "REU"
    RWA = "RWA"
    SYC = "SYC"
    SOM = "SOM"
    SSD = "SSD"
    UGA = "UGA"
    TZA = "TZA"
    ZMB = "ZMB"
    ZWE = "ZWE"
    AGO = "AGO"
    CMR = "CMR"
    CAF = "CAF"
    TCD = "TCD"
    COG = "COG"
    COD = "COD"
    GNQ = "GNQ"
    GAB = "GAB"
    STP = "STP"
    BWA = "BWA"
    LSO = "LSO"
    NAM = "NAM"
    ZAF = "ZAF"
    SWZ = "SWZ"
    BEN = "BEN"
    BFA = "BFA"
    CPV = "CPV"
    CIV = "CIV"
    GMB = "GMB"
    GHA = "GHA"
    GIN = "GIN"
    GNB = "GNB"
    LBR = "LBR"
    MLI = "MLI"
    MRT = "MRT"
    NER = "NER"
    NGA = "NGA"
    SHN = "SHN"
    SEN = "SEN"
    SLE = "SLE"
    TGO = "TGO"
    AIA = "AIA"
    ATG = "ATG"
    ABW = "ABW"
    BHS = "BHS"
    BRB = "BRB"
    BES = "BES"
    VGB = "VGB"
    CYM = "CYM"
    CUB = "CUB"
    CUW = "CUW"
    DMA = "DMA"
    DOM = "DOM"
    GRD = "GRD"
    GLP = "GLP"
    HTI = "HTI"
    JAM = "JAM"
    MTQ = "MTQ"
    MSR = "MSR"
    PRI = "PRI"
    BLM = "BLM"
    KNA = "KNA"
    LCA = "LCA"
    MAF = "MAF"
    VCT = "VCT"
    SXM = "SXM"
    TTO = "TTO"
    TCA = "TCA"
    VIR = "VIR"
    BLZ = "BLZ"
    CRI = "CRI"
    SLV = "SLV"
    GTM = "GTM"
    HND = "HND"
    MEX = "MEX"
    NIC = "NIC"
    PAN = "PAN"
    ARG = "ARG"
    BOL = "BOL"
    BRA = "BRA"
    CHL = "CHL"
    COL = "COL"
    ECU = "ECU"
    FLK = "FLK"
    GUF = "GUF"
    GUY = "GUY"
    PRY = "PRY"
    PER = "PER"
    SGS = "SGS"
    SUR = "SUR"
    URY = "URY"
    VEN = "VEN"
    BMU = "BMU"
    CAN = "CAN"
    GRL = "GRL"
    SPM = "SPM"
    USA = "USA"
    ATA = "ATA"
    KAZ = "KAZ"
    KGZ = "KGZ"
    TJK = "TJK"
    TKM = "TKM"
    UZB = "UZB"
    CHN = "CHN"
    HKG = "HKG"
    MAC = "MAC"
    PRK = "PRK"
    JPN = "JPN"
    MNG = "MNG"
    KOR = "KOR"
    BRN = "BRN"
    KHM = "KHM"
    IDN = "IDN"
    LAO = "LAO"
    MYS = "MYS"
    MMR = "MMR"
    PHL = "PHL"
    SGP = "SGP"
    THA = "THA"
    TLS = "TLS"
    VNM = "VNM"
    AFG = "AFG"
    BGD = "BGD"
    BTN = "BTN"
    IND = "IND"
    IRN = "IRN"
    MDV = "MDV"
    NPL = "NPL"
    PAK = "PAK"
    LKA = "LKA"
    ARM = "ARM"
    AZE = "AZE"
    BHR = "BHR"
    CYP = "CYP"
    GEO = "GEO"
    IRQ = "IRQ"
    ISR = "ISR"
    JOR = "JOR"
    KWT = "KWT"
    LBN = "LBN"
    OMN = "OMN"
    QAT = "QAT"
    SAU = "SAU"
    PSE = "PSE"
    SYR = "SYR"
    TUR = "TUR"
    ARE = "ARE"
    YEM = "YEM"
    BLR = "BLR"
    BGR = "BGR"
    CZE = "CZE"
    HUN = "HUN"
    POL = "POL"
    MDA = "MDA"
    ROU = "ROU"
    RUS = "RUS"
    SVK = "SVK"
    UKR = "UKR"
    ALA = "ALA"
    GGY = "GGY"
    JEY = "JEY"
    DNK = "DNK"
    EST = "EST"
    FRO = "FRO"
    FIN = "FIN"
    ISL = "ISL"
    IRL = "IRL"
    IMN = "IMN"
    LVA = "LVA"
    LTU = "LTU"
    NOR = "NOR"
    SJM = "SJM"
    SWE = "SWE"
    GBR = "GBR"
    ALB = "ALB"
    AND = "AND"
    BIH = "BIH"
    HRV = "HRV"
    GIB = "GIB"
    GRC = "GRC"
    VAT = "VAT"
    ITA = "ITA"
    MLT = "MLT"
    MNE = "MNE"
    PRT = "PRT"
    SMR = "SMR"
    SRB = "SRB"
    SVN = "SVN"
    ESP = "ESP"
    AUT = "AUT"
    BEL = "BEL"
    FRA = "FRA"
    DEU = "DEU"
    LIE = "LIE"
    LUX = "LUX"
    MCO = "MCO"
    NLD = "NLD"
    CHE = "CHE"
    AUS = "AUS"
    CXR = "CXR"
    CCK = "CCK"
    HMD = "HMD"
    NZL = "NZL"
    NFK = "NFK"
    FJI = "FJI"
    NCL = "NCL"
    PNG = "PNG"
    SLB = "SLB"
    VUT = "VUT"
    GUM = "GUM"
    KIR = "KIR"
    MHL = "MHL"
    FSM = "FSM"
    NRU = "NRU"
    MNP = "MNP"
    PLW = "PLW"
    UMI = "UMI"
    ASM = "ASM"
    COK = "COK"
    PYF = "PYF"
    NIU = "NIU"
    PCN = "PCN"
    WSM = "WSM"
    TKL = "TKL"
    TON = "TON"
    TUV = "TUV"
    WLF = "WLF"
    NN = "NN"
