# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .langs_enum import LangsEnum

__all__ = ["WeaponListParams"]


class WeaponListParams(TypedDict, total=False):
    charge_tier: Optional[str]
    """Charge tier (A, B, C, ...)"""

    charge_value: Optional[int]
    """Charge value"""

    exclude_categories: Optional[SequenceNotStr[str]]
    """Category ID should exclude one of"""

    exclude_elements: Optional[SequenceNotStr[str]]
    """Element ID should exclude one of"""

    exclude_ids: Optional[SequenceNotStr[str]]
    """ID should not be one of"""

    exclude_qualities: Optional[SequenceNotStr[str]]
    """Quality should exclude one of"""

    exclude_rarities: Optional[SequenceNotStr[str]]
    """Rarity should exclude one of"""

    include_categories: Optional[SequenceNotStr[str]]
    """Category ID should include one of"""

    include_elements: Optional[SequenceNotStr[str]]
    """Element ID should include one of"""

    include_ids: Optional[SequenceNotStr[str]]
    """ID should be one of"""

    include_qualities: Optional[SequenceNotStr[str]]
    """Quality should include one of"""

    include_rarities: Optional[SequenceNotStr[str]]
    """Rarity should include one of"""

    is_fate: Optional[bool]
    """Is fate weapon"""

    is_limited: Optional[bool]
    """Is limited weapon"""

    is_warehouse: Optional[bool]
    """Is warehouse (player's inventory) weapon"""

    lang: LangsEnum
    """Language code"""

    limit: int
    """Items per page"""

    name: Optional[str]
    """Name should be part of"""

    page: int
    """Page number"""

    shatter_tier: Optional[str]
    """Shatter tier (A, B, C, ...)"""

    shatter_value: Optional[int]
    """Shatter value"""
