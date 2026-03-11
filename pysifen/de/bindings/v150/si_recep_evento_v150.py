from __future__ import annotations

from dataclasses import dataclass

from pysifen.de.bindings.v150.evento_v150 import TgGroupGesEve

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class GGroupGesEve(TgGroupGesEve):
    class Meta:
        name = "gGroupGesEve"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"
