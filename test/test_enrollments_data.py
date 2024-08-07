# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.enrollments_data import EnrollmentsData

class TestEnrollmentsData(unittest.TestCase):
    """EnrollmentsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnrollmentsData:
        """Test EnrollmentsData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnrollmentsData`
        """
        model = EnrollmentsData()
        if include_optional:
            return EnrollmentsData(
                course_id = '',
                name = '',
                users = 56,
                percentage = 1.337
            )
        else:
            return EnrollmentsData(
                course_id = '',
                name = '',
                users = 56,
                percentage = 1.337,
        )
        """

    def testEnrollmentsData(self):
        """Test EnrollmentsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
