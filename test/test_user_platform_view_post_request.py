# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.user_platform_view_post_request import UserPlatformViewPostRequest

class TestUserPlatformViewPostRequest(unittest.TestCase):
    """UserPlatformViewPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserPlatformViewPostRequest:
        """Test UserPlatformViewPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserPlatformViewPostRequest`
        """
        model = UserPlatformViewPostRequest()
        if include_optional:
            return UserPlatformViewPostRequest(
                user_id = 56,
                platform_key = '',
                added_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expired_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_admin = True,
                active = True
            )
        else:
            return UserPlatformViewPostRequest(
                user_id = 56,
                platform_key = '',
        )
        """

    def testUserPlatformViewPostRequest(self):
        """Test UserPlatformViewPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
