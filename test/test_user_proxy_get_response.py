# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.user_proxy_get_response import UserProxyGetResponse

class TestUserProxyGetResponse(unittest.TestCase):
    """UserProxyGetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserProxyGetResponse:
        """Test UserProxyGetResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserProxyGetResponse`
        """
        model = UserProxyGetResponse()
        if include_optional:
            return UserProxyGetResponse(
                user_id = 56,
                username = '',
                email = '',
                active = True,
                edx_data = None,
                data = None
            )
        else:
            return UserProxyGetResponse(
                user_id = 56,
                username = '',
                email = '',
                active = True,
                edx_data = None,
                data = None,
        )
        """

    def testUserProxyGetResponse(self):
        """Test UserProxyGetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
