# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .langs_enum import LangsEnum

__all__ = ["SimulacraListParams"]


class SimulacraListParams(TypedDict, total=False):
    exclude_ids: Optional[SequenceNotStr[str]]
    """Id should not be one of"""

    exclude_rarities: Optional[SequenceNotStr[str]]
    """Rarity should exclude one of"""

    exclude_sex: Optional[SequenceNotStr[str]]
    """Sex should exclude one of"""

    include_ids: Optional[SequenceNotStr[str]]
    """Id should be one of"""

    include_rarities: Optional[SequenceNotStr[str]]
    """Rarity should include one of"""

    include_sex: Optional[SequenceNotStr[str]]
    """Sex should include one of"""

    is_limited: Optional[bool]
    """Is limited weapon (Red Nucleous)"""

    lang: LangsEnum
    """Language code"""

    limit: int
    """Items per page"""

    name: Optional[str]
    """Name should be part of"""

    no_weapon: Optional[bool]
    """No weapon (Polymorph)"""

    page: int
    """Page number"""
