from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


class TcCatIsc(Enum):
    """
    Categoria de ISC.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class TcCondNeg(Enum):
    """
    Condicion de la negociacion.

    :cvar CFR: Costo y flete
    :cvar CIF: Costo, seguro y flete
    :cvar CIP: Transporte y seguros pagados hasta
    :cvar CPT: Transporte pagado hasta
    :cvar DAP: Entregada en el lugar convenido
    :cvar DAT: Entregada en terminal
    :cvar DDP: Entregada derechos pagados
    :cvar EXW: En fabrica
    :cvar FAS: Franco al costado del buque
    :cvar FCA: Franco transportista
    :cvar FOB: Franco a bordo
    """

    CFR = "CFR"
    CIF = "CIF"
    CIP = "CIP"
    CPT = "CPT"
    DAP = "DAP"
    DAT = "DAT"
    DDP = "DDP"
    EXW = "EXW"
    FAS = "FAS"
    FCA = "FCA"
    FOB = "FOB"


class TcTasaIsc(Enum):
    """
    Tasa del ISC.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12


class TdCondTiCam(Enum):
    """
    Condición del tipo de cambio 1(Global), 2(Por ítem).
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TdDcondCred(Enum):
    """
    Descripción de la condición de la operación a crédito.
    """

    PLAZO = "Plazo"
    CUOTA = "Cuota"


class TdDcondOpe(Enum):
    """
    Descripcion de condicion de operacion.
    """

    CONTADO = "Contado"
    CR_DITO = "Crédito"


class TdDmotivTrasValue(Enum):
    TRASLADO_POR_VENTAS = "Traslado por ventas"
    TRASLADO_POR_CONSIGNACI_N = "Traslado por consignación"
    EXPORTACI_N = "Exportación"
    TRASLADO_POR_COMPRA = "Traslado por Compra"
    IMPORTACI_N = "Importación"
    TRASLADO_POR_DEVOLUCI_N = "Traslado por devolución"
    TRASLADO_ENTRE_LOCALES_DE_LA_EMPRESA = (
        "Traslado entre locales de la empresa"
    )
    TRASLADO_DE_BIENES_POR_TRANSFORMACI_N = (
        "Traslado de bienes por transformación"
    )
    TRASLADO_DE_BIENES_PARA_REPARACION = "Traslado de bienes para reparacion"
    TRASLADO_POR_EMISOR_M_VIL = "Traslado por emisor móvil"
    EXHIBICI_N_O_DEMOSTRACI_N = "Exhibición o Demostración"
    PARTICIPACI_N_EN_FERIAS = "Participación en ferias"
    TRASLADO_DE_ENCOMIENDA = "Traslado de encomienda"
    DECOMISO = "Decomiso"


class TdDesAfecIva(Enum):
    """
    Descripcion de la afectacion del IVA.
    """

    GRAVADO_IVA = "Gravado IVA"
    EXONERADO_ART_83_LEY_125_91 = "Exonerado (Art. 83- Ley 125/91)"
    EXENTO = "Exento"
    GRAVADO_PARCIAL_GRAV_EXENTO = "Gravado parcial (Grav- Exento)"


class TdDesCatIsc(Enum):
    """
    Descripcion de categoria de ISC.
    """

    SECCION_I_CIGARRILLOS_TABACOS_ESENCIAS_Y_OTROS_DERIVADOS_DEL_TABACO = (
        "SECCION I-(Cigarrillos,Tabacos,Esencias y Otros derivados del Tabaco)"
    )
    SECCION_II_BEBIDAS_CON_Y_SIN_ALCOHOL = (
        "SECCION II - (Bebidas con y sin alcohol)"
    )
    SECCION_III_ALCOHOLES_Y_DERIVADOS_DEL_ALCOHOL = (
        "SECCION III - (Alcoholes y Derivados del alcohol)"
    )
    SECCION_IV_COMBUSTIBLES = "SECCION IV - (Combustibles)"
    SECCION_V_ART_CULOS_CONSIDERADOS_DE_LUJO = (
        "SECCION V - (Artículos considerados de lujo)"
    )


class TdDesDenTarjValue(Enum):
    VISA = "Visa"
    MASTERCARD = "Mastercard"
    AMERICAN_EXPRESS = "American Express"
    MAESTRO = "Maestro"
    PANAL = "Panal"
    CABAL = "Cabal"


class TdDesIndPresValue(Enum):
    OPERACI_N_PRESENCIAL = "Operación presencial"
    OPERACI_N_ELECTR_NICA = "Operación electrónica"
    OPERACI_N_TELEMARKETING = "Operación telemarketing"
    VENTA_A_DOMICILIO = "Venta a domicilio"
    OPERACI_N_BANCARIA = "Operación bancaria"
    OPERACI_N_C_CLICA = "Operación cíclica"


class TdDesModTrans(Enum):
    """
    Descripcion de la Modalidad de transporte.
    """

    TERRESTRE = "Terrestre"
    FLUVIAL = "Fluvial"
    A_REO = "Aéreo"
    MULTIMODAL = "Multimodal"


class TdDesMotEmi(Enum):
    """
    Descripcion del motivo de la emision de la nota de credito/debito.
    """

    ANULACI_N = "Anulación"
    DEVOLUCI_N = "Devolución"
    DESCUENTO = "Descuento"
    BONIFICACI_N = "Bonificación"
    CR_DITO_INCOBRABLE = "Crédito incobrable"
    RECUPERO_DE_COSTO = "Recupero de costo"
    RECUPERO_DE_GASTO = "Recupero de gasto"
    AJUSTE_DE_PRECIO = "Ajuste de precio"


class TdDesTimp(Enum):
    """
    Descripcion del tipo de impuesto.

    :cvar IVA: Corresponde al codigo 1 del campo dDesTimp
    """

    IVA = "IVA"


class TdDesTipoDoc(Enum):
    """
    Tipos de documentos impresos.
    """

    FACTURA = "Factura"
    NOTA_DE_CR_DITO = "Nota de crédito"
    NOTA_DE_D_BITO = "Nota de débito"
    NOTA_DE_REMISI_N = "Nota de remisión"
    COMPROBANTE_DE_RETENCI_N = "Comprobante de retención"


class TdDesTtrans(Enum):
    """
    Descripcion del tipo de transporte.
    """

    PROPIO = "Propio"
    TERCERO = "Tercero"


class TdDesTiDe(Enum):
    """
    Descripcion del tipo de documento electronico.
    """

    FACTURA_ELECTR_NICA = "Factura electrónica"
    NOTA_DE_CR_DITO_ELECTR_NICA = "Nota de crédito electrónica"
    NOTA_DE_D_BITO_ELECTR_NICA = "Nota de débito electrónica"


class TdDesTiPag(Enum):
    """
    Descripcion del tipo de pago.
    """

    EFECTIVO = "Efectivo"
    CHEQUE = "Cheque"
    TARJETA_DE_CR_DITO = "Tarjeta de crédito"
    TARJETA_DE_D_BITO = "Tarjeta de débito"
    TRANSFERENCIA = "Transferencia"
    GIRO = "Giro"
    BILLETERA_ELECTR_NICA = "Billetera electrónica"
    TARJETA_EMPRESARIAL = "Tarjeta empresarial"
    VALE = "Vale"
    RETENCI_N = "Retención"
    ANTICIPO = "Anticipo"
    VALOR_FISCAL = "Valor fiscal"
    VALOR_COMERCIAL = "Valor comercial"
    COMPENSACI_N = "Compensación"
    PERMUTA = "Permuta"
    PAGO_BANCARIO = "Pago bancario"


class TdDesTiTran(Enum):
    """
    Descripcion del tipo de transaccion.
    """

    VENTA_DE_MERCADER_A = "Venta de mercadería"
    PRESTACI_N_DE_SERVICIOS = "Prestación de servicios"
    MIXTO_VENTA_DE_MERCADER_A_Y_SERVICIOS = (
        "Mixto (Venta de mercadería y servicios)"
    )
    VENTA_DE_ACTIVO_FIJO = "Venta de activo fijo"
    VENTA_DE_DIVISAS = "Venta de divisas"
    COMPRA_DE_DIVISAS = "Compra de divisas"
    PROMOCI_N_O_ENTREGA_DE_MUESTRAS = "Promoción o entrega de muestras"
    DONACI_N = "Donación"
    ANTICIPO = "Anticipo"
    COMPRA_DE_PRODUCTOS = "Compra de productos"
    COMPRA_DE_SERVICIOS = "Compra de servicios"
    VENTA_DE_CR_DITO_FISCAL = "Venta de crédito fiscal"


class TdDesTipComValue(Enum):
    GASOLINA = "Gasolina"
    DI_SEL = "Diésel"
    ETANOL = "Etanol"
    GNV = "GNV"
    FLEX = "Flex"


class TdDesTipDocAso(Enum):
    """
    Descripcion del tipo de documento asociado.
    """

    ELECTR_NICO = "Electrónico"
    IMPRESO = "Impreso"


class TdDesTipEmi(Enum):
    """
    Descripcion del tipo de emision: 1(Normal). 2(Contingencia).
    """

    NORMAL = "Normal"
    CONTINGENCIA = "Contingencia"


class TdDesTipOpVnValue(Enum):
    VENTA_A_REPRESENTANTE = "Venta a representante"
    VENTA_AL_CONSUMIDOR_FINAL = "Venta al Consumidor final"
    VENTA_A_GOBIERNO = "Venta a gobierno"
    VENTA_A_FLOTA_DE_VEH_CULOS = "Venta a flota de vehículos"


class TdDtipDoc(Enum):
    """
    Descripcion del tipo de documento de identidad del vendedor.
    """

    C_DULA_PARAGUAYA = "Cédula paraguaya"
    PASAPORTE = "Pasaporte"
    C_DULA_EXTRANJERA = "Cédula extranjera"
    CARNET_DE_RESIDENCIA = "Carnet de residencia"


class TdDtipDocRec(Enum):
    """
    Descripcion del tipo de documento de identidad del receptor.
    """

    C_DULA_PARAGUAYA = "Cédula paraguaya"
    PASAPORTE = "Pasaporte"
    C_DULA_EXTRANJERA = "Cédula extranjera"
    CARNET_DE_RESIDENCIA = "Carnet de residencia"
    INNOMINADO = "Innominado"


class TdTipCons(Enum):
    """
    Tipo de constancia de autofactura electronica.
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TiAfecIva(Enum):
    """
    Forma de afectacion del IVA 1(Gravado), 2(Exonerado), 3(Exento),
    4(Gravado parcial).
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class TiCondOpe(Enum):
    """
    Condicion de la operacion.

    :cvar VALUE_1: Contado
    :cvar VALUE_2: Crédito
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TiDenTarj(Enum):
    """
    Codigo de tipo de tarjeta.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_9 = 9


class TiForProPa(Enum):
    """
    Forma de procesamiento del pago. 1(POS), 2(Pago Electronico).
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TiIndPres(Enum):
    """
    Indicador de presencia.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_9 = 9


class TiModTrans(Enum):
    """
    Modalidad del transporte.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class TiMotEmi(Enum):
    """
    Motivo de emision de la nota de credito/debito electronica.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9 = "9"


class TiMotivTras(Enum):
    """
    Motivo de emisión.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14


class TiRespEmiNr(Enum):
    """
    Responsable por la emision de la Nota de remision electronica.

    :cvar VALUE_1: Emisor de la factura
    :cvar VALUE_2: Receptor de la factura
    :cvar VALUE_3: Empresa Transportista
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TiRespFlete(Enum):
    """
    Responsable por el costo del flete.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TiTimp(Enum):
    """
    Tipo de impuesto al consumo afectado.
    """

    VALUE_1 = 1


class TiTipoDoc(Enum):
    """
    Tipos de documentos impresos.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class TiTtrans(Enum):
    """
    Tipo de transporte.
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TiTiPago(Enum):
    """
    Codigo de tipo de pago.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16


class TiTipCom(Enum):
    """
    Tipo de combustible.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_9 = 9


class TiTipDocAso(Enum):
    """
    Tipo de documento asociado.
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TiTipOpVn(Enum):
    """
    Tipo de operacion de venta de vehiculos.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class TiTipTra(Enum):
    """
    Tipo de transaccion.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
