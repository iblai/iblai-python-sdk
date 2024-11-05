# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from iblai.models.net_revenue_over_time import NetRevenueOverTime
from iblai.models.order import Order
from iblai.models.product import Product
from iblai.models.revenue_by_product import RevenueByProduct

from iblai.api_client import ApiClient, RequestSerialized
from iblai.api_response import ApiResponse
from iblai.rest import RESTResponseType


class FinanceApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def finance_orgs_products_orders_retrieve(
        self,
        item_id: StrictStr,
        org: StrictStr,
        end_date: Annotated[Optional[StrictStr], Field(description="End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """finance_orgs_products_orders_retrieve

        Return list of WooCommerce orders for product item_id over optional date range

        :param item_id: (required)
        :type item_id: str
        :param org: (required)
        :type org: str
        :param end_date: End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.
        :type end_date: str
        :param start_date: Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.
        :type start_date: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._finance_orgs_products_orders_retrieve_serialize(
            item_id=item_id,
            org=org,
            end_date=end_date,
            start_date=start_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Order",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _finance_orgs_products_orders_retrieve_serialize(
        self,
        item_id,
        org,
        end_date,
        start_date,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if item_id is not None:
            _path_params['item_id'] = item_id
        if org is not None:
            _path_params['org'] = org
        # process the query parameters
        if end_date is not None:
            
            _query_params.append(('end_date', end_date))
            
        if start_date is not None:
            
            _query_params.append(('start_date', start_date))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'PlatformApiKeyAuthentication'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/finance/orgs/{org}/products/{item_id}/orders',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def finance_orgs_products_retrieve(
        self,
        org: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """finance_orgs_products_retrieve

        Returns table listing products and product info for all or specific org

        :param org: (required)
        :type org: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._finance_orgs_products_retrieve_serialize(
            org=org,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Product",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _finance_orgs_products_retrieve_serialize(
        self,
        org,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if org is not None:
            _path_params['org'] = org
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'PlatformApiKeyAuthentication'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/finance/orgs/{org}/products',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def finance_orgs_products_sales_over_time_retrieve(
        self,
        item_id: StrictStr,
        org: StrictStr,
        end_date: Annotated[Optional[StrictStr], Field(description="End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """finance_orgs_products_sales_over_time_retrieve

        Returns Net Revenue over time for org and slug

        :param item_id: (required)
        :type item_id: str
        :param org: (required)
        :type org: str
        :param end_date: End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.
        :type end_date: str
        :param start_date: Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.
        :type start_date: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._finance_orgs_products_sales_over_time_retrieve_serialize(
            item_id=item_id,
            org=org,
            end_date=end_date,
            start_date=start_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NetRevenueOverTime",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _finance_orgs_products_sales_over_time_retrieve_serialize(
        self,
        item_id,
        org,
        end_date,
        start_date,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if item_id is not None:
            _path_params['item_id'] = item_id
        if org is not None:
            _path_params['org'] = org
        # process the query parameters
        if end_date is not None:
            
            _query_params.append(('end_date', end_date))
            
        if start_date is not None:
            
            _query_params.append(('start_date', start_date))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'PlatformApiKeyAuthentication'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/finance/orgs/{org}/products/{item_id}/sales-over-time',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def finance_orgs_revenue_net_over_time_retrieve(
        self,
        org: StrictStr,
        end_date: Annotated[Optional[StrictStr], Field(description="End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """finance_orgs_revenue_net_over_time_retrieve

        Returns Net Revenue over time for org and slug

        :param org: (required)
        :type org: str
        :param end_date: End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.
        :type end_date: str
        :param start_date: Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.
        :type start_date: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._finance_orgs_revenue_net_over_time_retrieve_serialize(
            org=org,
            end_date=end_date,
            start_date=start_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NetRevenueOverTime",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _finance_orgs_revenue_net_over_time_retrieve_serialize(
        self,
        org,
        end_date,
        start_date,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if org is not None:
            _path_params['org'] = org
        # process the query parameters
        if end_date is not None:
            
            _query_params.append(('end_date', end_date))
            
        if start_date is not None:
            
            _query_params.append(('start_date', start_date))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'PlatformApiKeyAuthentication'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/finance/orgs/{org}/revenue/net-over-time',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def finance_orgs_revenue_products_retrieve(
        self,
        org: StrictStr,
        end_date: Annotated[Optional[StrictStr], Field(description="End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """finance_orgs_revenue_products_retrieve

        Returns Revenue by Product + summary for specific org

        :param org: (required)
        :type org: str
        :param end_date: End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.
        :type end_date: str
        :param start_date: Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time.
        :type start_date: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._finance_orgs_revenue_products_retrieve_serialize(
            org=org,
            end_date=end_date,
            start_date=start_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RevenueByProduct",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _finance_orgs_revenue_products_retrieve_serialize(
        self,
        org,
        end_date,
        start_date,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if org is not None:
            _path_params['org'] = org
        # process the query parameters
        if end_date is not None:
            
            _query_params.append(('end_date', end_date))
            
        if start_date is not None:
            
            _query_params.append(('start_date', start_date))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'PlatformApiKeyAuthentication'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/finance/orgs/{org}/revenue/products',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


