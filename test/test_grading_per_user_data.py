# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.grading_per_user_data import GradingPerUserData

class TestGradingPerUserData(unittest.TestCase):
    """GradingPerUserData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GradingPerUserData:
        """Test GradingPerUserData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GradingPerUserData`
        """
        model = GradingPerUserData()
        if include_optional:
            return GradingPerUserData(
                username = '',
                full_name = '',
                start_date = '',
                submissions = 56,
                last_active = '',
                percent = 1.337
            )
        else:
            return GradingPerUserData(
                username = '',
                full_name = '',
                start_date = '',
                submissions = 56,
                last_active = '',
                percent = 1.337,
        )
        """

    def testGradingPerUserData(self):
        """Test GradingPerUserData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
