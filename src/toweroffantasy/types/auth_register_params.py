# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthRegisterParams"]


class AuthRegisterParams(TypedDict, total=False):
    email: Required[str]

    password: Required[str]

    username: Required[str]
