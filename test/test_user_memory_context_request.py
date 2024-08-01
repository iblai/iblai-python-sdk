# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.user_memory_context_request import UserMemoryContextRequest

class TestUserMemoryContextRequest(unittest.TestCase):
    """UserMemoryContextRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserMemoryContextRequest:
        """Test UserMemoryContextRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserMemoryContextRequest`
        """
        model = UserMemoryContextRequest()
        if include_optional:
            return UserMemoryContextRequest(
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
            return UserMemoryContextRequest(
        )
        """

    def testUserMemoryContextRequest(self):
        """Test UserMemoryContextRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()