# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.grading_per_user import GradingPerUser

class TestGradingPerUser(unittest.TestCase):
    """GradingPerUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GradingPerUser:
        """Test GradingPerUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GradingPerUser`
        """
        model = GradingPerUser()
        if include_optional:
            return GradingPerUser(
                data = [
                    iblai.models.grading_per_user_data.GradingPerUserData(
                        username = '', 
                        full_name = '', 
                        start_date = '', 
                        submissions = 56, 
                        last_active = '', 
                        percent = 1.337, )
                    ],
                total = 56
            )
        else:
            return GradingPerUser(
        )
        """

    def testGradingPerUser(self):
        """Test GradingPerUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
