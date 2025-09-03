# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .langs_enum import LangsEnum

__all__ = ["MountListParams"]


class MountListParams(TypedDict, total=False):
    exclude_ids: Optional[SequenceNotStr[str]]
    """Id should not be one of"""

    exclude_mount_type: Optional[SequenceNotStr[str]]
    """Mount type should exclude one of"""

    exclude_quality: Optional[SequenceNotStr[str]]
    """Quality should exclude one of"""

    include_ids: Optional[SequenceNotStr[str]]
    """Id should be one of"""

    include_mount_type: Optional[SequenceNotStr[str]]
    """Mount type should include one of"""

    include_quality: Optional[SequenceNotStr[str]]
    """Quality should include one of"""

    lang: LangsEnum
    """Language code"""

    limit: int
    """Items per page"""

    name: Optional[str]
    """Name should be part of"""

    page: int
    """Page number"""
