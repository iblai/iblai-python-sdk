# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.user_memory_context_response import UserMemoryContextResponse

class TestUserMemoryContextResponse(unittest.TestCase):
    """UserMemoryContextResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserMemoryContextResponse:
        """Test UserMemoryContextResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserMemoryContextResponse`
        """
        model = UserMemoryContextResponse()
        if include_optional:
            return UserMemoryContextResponse(
                username = '',
                platform_key = '',
                extra_data = '',
                use_reported_skills = True,
                use_desired_skills = True,
                use_credentials = True,
                use_enrolled_courses = True,
                use_time_spent = True,
                use_completed_courses = True,
                use_completed_programs = True
            )
        else:
            return UserMemoryContextResponse(
                username = '',
                platform_key = '',
        )
        """

    def testUserMemoryContextResponse(self):
        """Test UserMemoryContextResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
