# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from iblai.models.average import Average
from iblai.models.course_completion_summary_overtime import CourseCompletionSummaryOvertime
from iblai.models.overtime_with_change_info import OvertimeWithChangeInfo
from iblai.models.perlearner_user_list import PerlearnerUserList
from iblai.models.time_spent_per_course import TimeSpentPerCourse

from iblai.api_client import ApiClient, RequestSerialized
from iblai.api_response import ApiResponse
from iblai.rest import RESTResponseType


class OverviewApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def overview_orgs_active_users_retrieve(
        self,
        org: StrictStr,
        end_date: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="end date. ISO 8601")] = None,
        format: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="Format  * `json` - json")] = None,
        include_main_platform: Annotated[Optional[StrictBool], Field(description="Include main platform data")] = None,
        start_date: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="start date. ISO 8601")] = None,
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
        """overview_orgs_active_users_retrieve

        Count of users with known activity within the past 30 days on a per day basis  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive) Returns ``` {     \"data\": {         \"2022-04-26\": 0,         \"2022-04-27\": 0,         \"2022-04-28\": 0,         \"2022-04-29\": 60,         ...         \"2022-05-05\": 0     },     \"total\": 60,     \"meta\": {         \"change_last_seven_days\": 0,         \"change_last_seven_days_percent\": 0.0,         \"change_last_thirty_days\": 0,         \"change_last_thirty_days_percent\": 0.0,         \"change_range\": 0,         \"change_range_percent\": 0.0,         \"total\": 0,     } }

        :param org: (required)
        :type org: str
        :param end_date: end date. ISO 8601
        :type end_date: str
        :param format: Format  * `json` - json
        :type format: str
        :param include_main_platform: Include main platform data
        :type include_main_platform: bool
        :param start_date: start date. ISO 8601
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

        _param = self._overview_orgs_active_users_retrieve_serialize(
            org=org,
            end_date=end_date,
            format=format,
            include_main_platform=include_main_platform,
            start_date=start_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "OvertimeWithChangeInfo",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _overview_orgs_active_users_retrieve_serialize(
        self,
        org,
        end_date,
        format,
        include_main_platform,
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
            
        if format is not None:
            
            _query_params.append(('format', format))
            
        if include_main_platform is not None:
            
            _query_params.append(('include_main_platform', include_main_platform))
            
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
            resource_path='/api/overview/orgs/{org}/active-users',
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
    def overview_orgs_average_grade_retrieve(
        self,
        org: StrictStr,
        format: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="Format  * `json` - json")] = None,
        include_main_platform: Annotated[Optional[StrictBool], Field(description="Include main platform data")] = None,
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
        """overview_orgs_average_grade_retrieve

        Average grade value for platform, course, or user.  Query Params course_id <optional>  e.g course-v1:Org+Course4+Run learner_id <optional> e.g std123 , student@email.com

        :param org: (required)
        :type org: str
        :param format: Format  * `json` - json
        :type format: str
        :param include_main_platform: Include main platform data
        :type include_main_platform: bool
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

        _param = self._overview_orgs_average_grade_retrieve_serialize(
            org=org,
            format=format,
            include_main_platform=include_main_platform,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Average",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _overview_orgs_average_grade_retrieve_serialize(
        self,
        org,
        format,
        include_main_platform,
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
        if format is not None:
            
            _query_params.append(('format', format))
            
        if include_main_platform is not None:
            
            _query_params.append(('include_main_platform', include_main_platform))
            
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
            resource_path='/api/overview/orgs/{org}/average-grade',
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
    def overview_orgs_courses_completions_retrieve(
        self,
        org: StrictStr,
        end_date: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="end date. ISO 8601")] = None,
        format: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="Format  * `json` - json")] = None,
        include_main_platform: Annotated[Optional[StrictBool], Field(description="Include main platform data")] = None,
        start_date: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="start date. ISO 8601")] = None,
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
        """overview_orgs_courses_completions_retrieve

        Course Completion Across the Platform Ovetime with unique User count Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive)

        :param org: (required)
        :type org: str
        :param end_date: end date. ISO 8601
        :type end_date: str
        :param format: Format  * `json` - json
        :type format: str
        :param include_main_platform: Include main platform data
        :type include_main_platform: bool
        :param start_date: start date. ISO 8601
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

        _param = self._overview_orgs_courses_completions_retrieve_serialize(
            org=org,
            end_date=end_date,
            format=format,
            include_main_platform=include_main_platform,
            start_date=start_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CourseCompletionSummaryOvertime",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _overview_orgs_courses_completions_retrieve_serialize(
        self,
        org,
        end_date,
        format,
        include_main_platform,
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
            
        if format is not None:
            
            _query_params.append(('format', format))
            
        if include_main_platform is not None:
            
            _query_params.append(('include_main_platform', include_main_platform))
            
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
            resource_path='/api/overview/orgs/{org}/courses/completions',
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
    def overview_orgs_learners_retrieve(
        self,
        org: StrictStr,
        format: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="Format  * `json` - json")] = None,
        include_main_platform: Annotated[Optional[StrictBool], Field(description="Include main platform data")] = None,
        length: Annotated[Optional[StrictInt], Field(description="Size of data to return")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page offset")] = None,
        search: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="Search string for learner")] = None,
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
        """overview_orgs_learners_retrieve

        List of entire learners on the platform with aggregated enrollments, completions and time spent

        :param org: (required)
        :type org: str
        :param format: Format  * `json` - json
        :type format: str
        :param include_main_platform: Include main platform data
        :type include_main_platform: bool
        :param length: Size of data to return
        :type length: int
        :param page: Page offset
        :type page: int
        :param search: Search string for learner
        :type search: str
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

        _param = self._overview_orgs_learners_retrieve_serialize(
            org=org,
            format=format,
            include_main_platform=include_main_platform,
            length=length,
            page=page,
            search=search,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PerlearnerUserList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _overview_orgs_learners_retrieve_serialize(
        self,
        org,
        format,
        include_main_platform,
        length,
        page,
        search,
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
        if format is not None:
            
            _query_params.append(('format', format))
            
        if include_main_platform is not None:
            
            _query_params.append(('include_main_platform', include_main_platform))
            
        if length is not None:
            
            _query_params.append(('length', length))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
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
            resource_path='/api/overview/orgs/{org}/learners',
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
    def overview_orgs_most_active_courses_retrieve(
        self,
        org: StrictStr,
        end_date: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="end date. ISO 8601")] = None,
        format: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="Format  * `json` - json")] = None,
        include_main_platform: Annotated[Optional[StrictBool], Field(description="Include main platform data")] = None,
        length: Annotated[Optional[StrictInt], Field(description="Size of data to return")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page offset")] = None,
        start_date: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="start date. ISO 8601")] = None,
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
        """overview_orgs_most_active_courses_retrieve

        Aggregated time spent value on a per course basis

        :param org: (required)
        :type org: str
        :param end_date: end date. ISO 8601
        :type end_date: str
        :param format: Format  * `json` - json
        :type format: str
        :param include_main_platform: Include main platform data
        :type include_main_platform: bool
        :param length: Size of data to return
        :type length: int
        :param page: Page offset
        :type page: int
        :param start_date: start date. ISO 8601
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

        _param = self._overview_orgs_most_active_courses_retrieve_serialize(
            org=org,
            end_date=end_date,
            format=format,
            include_main_platform=include_main_platform,
            length=length,
            page=page,
            start_date=start_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TimeSpentPerCourse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _overview_orgs_most_active_courses_retrieve_serialize(
        self,
        org,
        end_date,
        format,
        include_main_platform,
        length,
        page,
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
            
        if format is not None:
            
            _query_params.append(('format', format))
            
        if include_main_platform is not None:
            
            _query_params.append(('include_main_platform', include_main_platform))
            
        if length is not None:
            
            _query_params.append(('length', length))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
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
            resource_path='/api/overview/orgs/{org}/most-active-courses',
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
    def overview_orgs_registered_users_retrieve(
        self,
        org: StrictStr,
        end_date: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="end date. ISO 8601")] = None,
        format: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="Format  * `json` - json")] = None,
        include_main_platform: Annotated[Optional[StrictBool], Field(description="Include main platform data")] = None,
        start_date: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="start date. ISO 8601")] = None,
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
        """overview_orgs_registered_users_retrieve

        Registered users count on a per day basis  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive)

        :param org: (required)
        :type org: str
        :param end_date: end date. ISO 8601
        :type end_date: str
        :param format: Format  * `json` - json
        :type format: str
        :param include_main_platform: Include main platform data
        :type include_main_platform: bool
        :param start_date: start date. ISO 8601
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

        _param = self._overview_orgs_registered_users_retrieve_serialize(
            org=org,
            end_date=end_date,
            format=format,
            include_main_platform=include_main_platform,
            start_date=start_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "OvertimeWithChangeInfo",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _overview_orgs_registered_users_retrieve_serialize(
        self,
        org,
        end_date,
        format,
        include_main_platform,
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
            
        if format is not None:
            
            _query_params.append(('format', format))
            
        if include_main_platform is not None:
            
            _query_params.append(('include_main_platform', include_main_platform))
            
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
            resource_path='/api/overview/orgs/{org}/registered-users',
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


