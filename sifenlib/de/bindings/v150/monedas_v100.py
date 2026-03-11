from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from sifenlib.CommonMixin import CommonMixin

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


class CMondT(Enum):
    """
    :cvar AED: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Dirham</ns1:CodeName>
    :cvar AFN: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Afghani</ns1:CodeName>
    :cvar ALL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Lek</ns1:CodeName>
    :cvar AMD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Dram</ns1:CodeName>
    :cvar ANG: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Netherlands
        Antillian Guilder</ns1:CodeName>
    :cvar AOA: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Kwanza</ns1:CodeName>
    :cvar ARS: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Argentine
        Peso</ns1:CodeName>
    :cvar AUD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Australian
        Dollar</ns1:CodeName>
    :cvar AWG: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Aruban
        Guilder</ns1:CodeName>
    :cvar AZM: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Azerbaijanian
        Manat</ns1:CodeName>
    :cvar BAM: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Convertible
        Mark</ns1:CodeName>
    :cvar BBD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Barbados
        Dollar</ns1:CodeName>
    :cvar BDT: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Taka</ns1:CodeName>
    :cvar BGN: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Bulgarian
        Lev</ns1:CodeName>
    :cvar BHD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Bahraini
        Dinar</ns1:CodeName>
    :cvar BIF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Burundi
        Franc</ns1:CodeName>
    :cvar BMD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Bermudian Dollar
        (customarily: Bermuda Dollar)</ns1:CodeName>
    :cvar BND: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Brunei
        Dollar</ns1:CodeName>
    :cvar BOB: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Boliviano</ns1:CodeName>
    :cvar BRL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Brazilian
        Real</ns1:CodeName>
    :cvar BSD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Bahamian
        Dollar</ns1:CodeName>
    :cvar BTN: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Ngultrum</ns1:CodeName>
    :cvar BWP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Pula</ns1:CodeName>
    :cvar BYR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Belarussian
        Ruble</ns1:CodeName>
    :cvar BZD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Belize
        Dollar</ns1:CodeName>
    :cvar CAD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Canadian
        Dollar</ns1:CodeName>
    :cvar CDF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Franc
        Congolais</ns1:CodeName>
    :cvar CHF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Swiss
        Franc</ns1:CodeName>
    :cvar CLP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Chilean
        Peso</ns1:CodeName>
    :cvar CNY: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Yuan
        Renminbi</ns1:CodeName>
    :cvar COP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Colombian
        Peso</ns1:CodeName>
    :cvar CRC: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Costa Rican
        Colon</ns1:CodeName>
    :cvar CUP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Cuban
        Peso</ns1:CodeName>
    :cvar CVE: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Cape Verde
        Escudo</ns1:CodeName>
    :cvar CYP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Cyprus
        Pound</ns1:CodeName>
    :cvar CZK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Czech
        Koruna</ns1:CodeName>
    :cvar DJF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Djibouti
        Franc</ns1:CodeName>
    :cvar DKK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Danish
        Krone</ns1:CodeName>
    :cvar DOP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Dominican
        Peso</ns1:CodeName>
    :cvar DZD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Algerian
        Dinar</ns1:CodeName>
    :cvar EEK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Kroon</ns1:CodeName>
    :cvar EGP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Egyptian
        Pound</ns1:CodeName>
    :cvar ERN: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Nakfa</ns1:CodeName>
    :cvar ETB: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Ethopian
        Birr</ns1:CodeName>
    :cvar EUR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Euro</ns1:CodeName>
    :cvar FJD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Fiji
        Dollar</ns1:CodeName>
    :cvar FKP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Falkland Islands
        Pound</ns1:CodeName>
    :cvar GBP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Pound
        Sterling</ns1:CodeName>
    :cvar GEL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Lari</ns1:CodeName>
    :cvar GHC: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Cedi</ns1:CodeName>
    :cvar GIP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Gibraltar
        Pound</ns1:CodeName>
    :cvar GMD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Dalasi</ns1:CodeName>
    :cvar GNF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Guinea
        Franc</ns1:CodeName>
    :cvar GTQ: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Quetzal</ns1:CodeName>
    :cvar GYD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Guyana
        Dollar</ns1:CodeName>
    :cvar HKD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Honk Kong
        Dollar</ns1:CodeName>
    :cvar HNL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Lempira</ns1:CodeName>
    :cvar HRK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Kuna</ns1:CodeName>
    :cvar HTG: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Gourde</ns1:CodeName>
    :cvar HUF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Forint</ns1:CodeName>
    :cvar IDR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Rupiah</ns1:CodeName>
    :cvar ILS: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">New Israeli
        Sheqel</ns1:CodeName>
    :cvar INR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Indian
        Rupee</ns1:CodeName>
    :cvar IQD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Iraqi
        Dinar</ns1:CodeName>
    :cvar IRR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Iranian
        Rial</ns1:CodeName>
    :cvar ISK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Iceland
        Krona</ns1:CodeName>
    :cvar JMD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Jamaican
        Dollar</ns1:CodeName>
    :cvar JOD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Jordanian
        Dinar</ns1:CodeName>
    :cvar JPY: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Yen</ns1:CodeName>
    :cvar KES: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Kenyan
        Shilling</ns1:CodeName>
    :cvar KGS: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Som</ns1:CodeName>
    :cvar KHR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Riel</ns1:CodeName>
    :cvar KMF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Comoro
        Franc</ns1:CodeName>
    :cvar KPW: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">North Korean
        Won</ns1:CodeName>
    :cvar KRW: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Won</ns1:CodeName>
    :cvar KWD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Kuwaiti
        Dinar</ns1:CodeName>
    :cvar KYD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Cayman Islands
        Dollar</ns1:CodeName>
    :cvar KZT: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Tenge</ns1:CodeName>
    :cvar LAK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Kip</ns1:CodeName>
    :cvar LBP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Lebanese
        Pound</ns1:CodeName>
    :cvar LKR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Sri Lanka
        Rupee</ns1:CodeName>
    :cvar LRD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Liberian
        Dollar</ns1:CodeName>
    :cvar LSL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Loti</ns1:CodeName>
    :cvar LTL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Lithuanian
        Litas</ns1:CodeName>
    :cvar LVL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Latvian
        Lats</ns1:CodeName>
    :cvar LYD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Libyan
        Dinar</ns1:CodeName>
    :cvar MAD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Morrocan
        Dirham</ns1:CodeName>
    :cvar MDL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Moldovan
        Leu</ns1:CodeName>
    :cvar MGF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Malagasy
        Franc</ns1:CodeName>
    :cvar MKD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Denar</ns1:CodeName>
    :cvar MMK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Kyat</ns1:CodeName>
    :cvar MNT: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Tugrik</ns1:CodeName>
    :cvar MOP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Pataca</ns1:CodeName>
    :cvar MRO: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Ouguiya</ns1:CodeName>
    :cvar MTL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Maltese
        Lira</ns1:CodeName>
    :cvar MUR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Mauritius
        Rupee</ns1:CodeName>
    :cvar MVR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Rufiyaa</ns1:CodeName>
    :cvar MWK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Kwacha</ns1:CodeName>
    :cvar MXN: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Mexican
        Peso</ns1:CodeName>
    :cvar MYR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Malaysian
        Ringgit</ns1:CodeName>
    :cvar MZM: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Metical</ns1:CodeName>
    :cvar NAD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Namibia
        Dollar</ns1:CodeName>
    :cvar NGN: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Naira</ns1:CodeName>
    :cvar NIO: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Cordoba
        Oro</ns1:CodeName>
    :cvar NOK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Norwegian
        Krone</ns1:CodeName>
    :cvar NPR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Nepalese
        Rupee</ns1:CodeName>
    :cvar NZD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">New Zealand
        Dollar</ns1:CodeName>
    :cvar OMR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Rial
        Omani</ns1:CodeName>
    :cvar PAB: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Balboa</ns1:CodeName>
    :cvar PEN: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Nuevo
        Sol</ns1:CodeName>
    :cvar PGK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Kina</ns1:CodeName>
    :cvar PHP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Philippine
        Peso</ns1:CodeName>
    :cvar PKR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Pakistan
        Rupee</ns1:CodeName>
    :cvar PLN: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Zloty</ns1:CodeName>
    :cvar PYG: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Guarani</ns1:CodeName>
    :cvar QAR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Qatari
        Rial</ns1:CodeName>
    :cvar ROL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Leu</ns1:CodeName>
    :cvar RUB: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Russian
        Ruble</ns1:CodeName>
    :cvar RWF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Rwanda
        Franc</ns1:CodeName>
    :cvar SAR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Saudi
        Riyal</ns1:CodeName>
    :cvar SBD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Solomon Islands
        Dollar</ns1:CodeName>
    :cvar SCR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Seychelles
        Rupee</ns1:CodeName>
    :cvar SDD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Sudanese
        Dinar</ns1:CodeName>
    :cvar SEK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Swedish
        Krona</ns1:CodeName>
    :cvar SGD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Singapore
        Dollar</ns1:CodeName>
    :cvar SHP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">St. Helena
        Pound</ns1:CodeName>
    :cvar SIT: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Tolar</ns1:CodeName>
    :cvar SKK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Slovak
        Koruna</ns1:CodeName>
    :cvar SLL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Leone</ns1:CodeName>
    :cvar SOS: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Somali
        Shilling</ns1:CodeName>
    :cvar SRG: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Suriname
        Guilder</ns1:CodeName>
    :cvar STD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Dobra</ns1:CodeName>
    :cvar SVC: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">El Salvador
        Colon</ns1:CodeName>
    :cvar SYP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Syrian
        Pound</ns1:CodeName>
    :cvar SZL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Lilangeni</ns1:CodeName>
    :cvar THB: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Baht</ns1:CodeName>
    :cvar TJS: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Somoni</ns1:CodeName>
    :cvar TMM: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Manat</ns1:CodeName>
    :cvar TND: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Tunisian
        Dinar</ns1:CodeName>
    :cvar TOP: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Pa'anga</ns1:CodeName>
    :cvar TRL: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Turkish
        Lira</ns1:CodeName>
    :cvar TTD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Trinidad and
        Tobago Dollar</ns1:CodeName>
    :cvar TWD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">New Taiwan
        Dollar</ns1:CodeName>
    :cvar TZS: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Tanzanian
        Shilling</ns1:CodeName>
    :cvar UAH: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Hryvnia</ns1:CodeName>
    :cvar UGX: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Uganda
        Shilling</ns1:CodeName>
    :cvar USD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">US
        Dollar</ns1:CodeName>
    :cvar UYU: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Peso
        Uruguayo</ns1:CodeName>
    :cvar UZS: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Uzbekistan
        Sum</ns1:CodeName>
    :cvar VEB: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Bolivar</ns1:CodeName>
    :cvar VND: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Dong</ns1:CodeName>
    :cvar VUV: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Vatu</ns1:CodeName>
    :cvar WST: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Tala</ns1:CodeName>
    :cvar XAF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">CFA
        Franc</ns1:CodeName>
    :cvar XAG: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Silver</ns1:CodeName>
    :cvar XAU: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Gold</ns1:CodeName>
    :cvar XCD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">East Carribean
        Dollar</ns1:CodeName>
    :cvar XDR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">SDR</ns1:CodeName>
    :cvar XOF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">CFA
        Franc</ns1:CodeName>
    :cvar XPD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Palladium</ns1:CodeName>
    :cvar XPF: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">CFP
        Franc</ns1:CodeName>
    :cvar XPT: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Platinum</ns1:CodeName>
    :cvar YER: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Yemeni
        Rial</ns1:CodeName>
    :cvar YUM: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">New
        Dinar</ns1:CodeName>
    :cvar ZAR: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Rand</ns1:CodeName>
    :cvar ZMK: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Kwacha</ns1:CodeName>
    :cvar ZWD: <ns1:CodeName
        xmlns:ns1="http://ekuatia.set.gov.py/sifen/xsd">Zimbabwe
        Dollar</ns1:CodeName>
    """

    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZM = "AZM"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYR = "BYR"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHF = "CHF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    CRC = "CRC"
    CUP = "CUP"
    CVE = "CVE"
    CYP = "CYP"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EEK = "EEK"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHC = "GHC"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LTL = "LTL"
    LVL = "LVL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGF = "MGF"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MTL = "MTL"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MYR = "MYR"
    MZM = "MZM"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    ROL = "ROL"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDD = "SDD"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SIT = "SIT"
    SKK = "SKK"
    SLL = "SLL"
    SOS = "SOS"
    SRG = "SRG"
    STD = "STD"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMM = "TMM"
    TND = "TND"
    TOP = "TOP"
    TRL = "TRL"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    UYU = "UYU"
    UZS = "UZS"
    VEB = "VEB"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XAG = "XAG"
    XAU = "XAU"
    XCD = "XCD"
    XDR = "XDR"
    XOF = "XOF"
    XPD = "XPD"
    XPF = "XPF"
    XPT = "XPT"
    YER = "YER"
    YUM = "YUM"
    ZAR = "ZAR"
    ZMK = "ZMK"
    ZWD = "ZWD"


@dataclass(kw_only=True)
class CurrencyCodeType(CommonMixin):
    """
    ISO 4217 Alpha.
    """

    value: CMondT = field()
    codeListID: str = field(
        init=False,
        default="ISO 4217 Alpha",
        metadata={
            "type": "Attribute",
        },
    )
