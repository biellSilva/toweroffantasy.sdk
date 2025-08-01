# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthChangePasswordParams"]


class AuthChangePasswordParams(TypedDict, total=False):
    new_password: Required[str]

    old_password: Required[str]
