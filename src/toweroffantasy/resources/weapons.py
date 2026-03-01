# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import LangsEnum, weapon_list_params, weapon_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.langs_enum import LangsEnum
from ..types.weapon_list_response import WeaponListResponse
from ..types.weapon_retrieve_response import WeaponRetrieveResponse

__all__ = ["WeaponsResource", "AsyncWeaponsResource"]


class WeaponsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WeaponsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/biellSilva/toweroffantasy.sdk#accessing-raw-response-data-eg-headers
        """
        return WeaponsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WeaponsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/biellSilva/toweroffantasy.sdk#with_streaming_response
        """
        return WeaponsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        weapon_id: str,
        *,
        lang: LangsEnum | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WeaponRetrieveResponse:
        """
        Get Weapon

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not weapon_id:
            raise ValueError(f"Expected a non-empty value for `weapon_id` but received {weapon_id!r}")
        return self._get(
            f"/weapons/{weapon_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"lang": lang}, weapon_retrieve_params.WeaponRetrieveParams),
            ),
            cast_to=WeaponRetrieveResponse,
        )

    def list(
        self,
        *,
        charge_tier: Optional[str] | Omit = omit,
        charge_value: Optional[int] | Omit = omit,
        exclude_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_elements: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_qualities: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_rarities: Optional[SequenceNotStr[str]] | Omit = omit,
        include_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        include_elements: Optional[SequenceNotStr[str]] | Omit = omit,
        include_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_qualities: Optional[SequenceNotStr[str]] | Omit = omit,
        include_rarities: Optional[SequenceNotStr[str]] | Omit = omit,
        is_fate: Optional[bool] | Omit = omit,
        is_limited: Optional[bool] | Omit = omit,
        is_warehouse: Optional[bool] | Omit = omit,
        lang: LangsEnum | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        shatter_tier: Optional[str] | Omit = omit,
        shatter_value: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WeaponListResponse:
        """
        Get All Weapons

        Args:
          charge_tier: Charge tier (A, B, C, ...)

          charge_value: Charge value

          exclude_categories: Category ID should exclude one of

          exclude_elements: Element ID should exclude one of

          exclude_ids: ID should not be one of

          exclude_qualities: Quality should exclude one of

          exclude_rarities: Rarity should exclude one of

          include_categories: Category ID should include one of

          include_elements: Element ID should include one of

          include_ids: ID should be one of

          include_qualities: Quality should include one of

          include_rarities: Rarity should include one of

          is_fate: Is fate weapon

          is_limited: Is limited weapon

          is_warehouse: Is warehouse (player's inventory) weapon

          lang: Language code

          limit: Items per page

          name: Name should be part of

          page: Page number

          shatter_tier: Shatter tier (A, B, C, ...)

          shatter_value: Shatter value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/weapons",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "charge_tier": charge_tier,
                        "charge_value": charge_value,
                        "exclude_categories": exclude_categories,
                        "exclude_elements": exclude_elements,
                        "exclude_ids": exclude_ids,
                        "exclude_qualities": exclude_qualities,
                        "exclude_rarities": exclude_rarities,
                        "include_categories": include_categories,
                        "include_elements": include_elements,
                        "include_ids": include_ids,
                        "include_qualities": include_qualities,
                        "include_rarities": include_rarities,
                        "is_fate": is_fate,
                        "is_limited": is_limited,
                        "is_warehouse": is_warehouse,
                        "lang": lang,
                        "limit": limit,
                        "name": name,
                        "page": page,
                        "shatter_tier": shatter_tier,
                        "shatter_value": shatter_value,
                    },
                    weapon_list_params.WeaponListParams,
                ),
            ),
            cast_to=WeaponListResponse,
        )


class AsyncWeaponsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWeaponsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/biellSilva/toweroffantasy.sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWeaponsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWeaponsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/biellSilva/toweroffantasy.sdk#with_streaming_response
        """
        return AsyncWeaponsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        weapon_id: str,
        *,
        lang: LangsEnum | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WeaponRetrieveResponse:
        """
        Get Weapon

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not weapon_id:
            raise ValueError(f"Expected a non-empty value for `weapon_id` but received {weapon_id!r}")
        return await self._get(
            f"/weapons/{weapon_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"lang": lang}, weapon_retrieve_params.WeaponRetrieveParams),
            ),
            cast_to=WeaponRetrieveResponse,
        )

    async def list(
        self,
        *,
        charge_tier: Optional[str] | Omit = omit,
        charge_value: Optional[int] | Omit = omit,
        exclude_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_elements: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_qualities: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_rarities: Optional[SequenceNotStr[str]] | Omit = omit,
        include_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        include_elements: Optional[SequenceNotStr[str]] | Omit = omit,
        include_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_qualities: Optional[SequenceNotStr[str]] | Omit = omit,
        include_rarities: Optional[SequenceNotStr[str]] | Omit = omit,
        is_fate: Optional[bool] | Omit = omit,
        is_limited: Optional[bool] | Omit = omit,
        is_warehouse: Optional[bool] | Omit = omit,
        lang: LangsEnum | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        shatter_tier: Optional[str] | Omit = omit,
        shatter_value: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WeaponListResponse:
        """
        Get All Weapons

        Args:
          charge_tier: Charge tier (A, B, C, ...)

          charge_value: Charge value

          exclude_categories: Category ID should exclude one of

          exclude_elements: Element ID should exclude one of

          exclude_ids: ID should not be one of

          exclude_qualities: Quality should exclude one of

          exclude_rarities: Rarity should exclude one of

          include_categories: Category ID should include one of

          include_elements: Element ID should include one of

          include_ids: ID should be one of

          include_qualities: Quality should include one of

          include_rarities: Rarity should include one of

          is_fate: Is fate weapon

          is_limited: Is limited weapon

          is_warehouse: Is warehouse (player's inventory) weapon

          lang: Language code

          limit: Items per page

          name: Name should be part of

          page: Page number

          shatter_tier: Shatter tier (A, B, C, ...)

          shatter_value: Shatter value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/weapons",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "charge_tier": charge_tier,
                        "charge_value": charge_value,
                        "exclude_categories": exclude_categories,
                        "exclude_elements": exclude_elements,
                        "exclude_ids": exclude_ids,
                        "exclude_qualities": exclude_qualities,
                        "exclude_rarities": exclude_rarities,
                        "include_categories": include_categories,
                        "include_elements": include_elements,
                        "include_ids": include_ids,
                        "include_qualities": include_qualities,
                        "include_rarities": include_rarities,
                        "is_fate": is_fate,
                        "is_limited": is_limited,
                        "is_warehouse": is_warehouse,
                        "lang": lang,
                        "limit": limit,
                        "name": name,
                        "page": page,
                        "shatter_tier": shatter_tier,
                        "shatter_value": shatter_value,
                    },
                    weapon_list_params.WeaponListParams,
                ),
            ),
            cast_to=WeaponListResponse,
        )


class WeaponsResourceWithRawResponse:
    def __init__(self, weapons: WeaponsResource) -> None:
        self._weapons = weapons

        self.retrieve = to_raw_response_wrapper(
            weapons.retrieve,
        )
        self.list = to_raw_response_wrapper(
            weapons.list,
        )


class AsyncWeaponsResourceWithRawResponse:
    def __init__(self, weapons: AsyncWeaponsResource) -> None:
        self._weapons = weapons

        self.retrieve = async_to_raw_response_wrapper(
            weapons.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            weapons.list,
        )


class WeaponsResourceWithStreamingResponse:
    def __init__(self, weapons: WeaponsResource) -> None:
        self._weapons = weapons

        self.retrieve = to_streamed_response_wrapper(
            weapons.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            weapons.list,
        )


class AsyncWeaponsResourceWithStreamingResponse:
    def __init__(self, weapons: AsyncWeaponsResource) -> None:
        self._weapons = weapons

        self.retrieve = async_to_streamed_response_wrapper(
            weapons.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            weapons.list,
        )
