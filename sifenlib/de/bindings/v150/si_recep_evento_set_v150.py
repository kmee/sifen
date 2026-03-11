from __future__ import annotations

from dataclasses import dataclass

from sifenlib.de.bindings.v150.evento_v150 import TrGesEveSet

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class RGesEve(TrGesEveSet):
    class Meta:
        name = "rGesEve"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"
