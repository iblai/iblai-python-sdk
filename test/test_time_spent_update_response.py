# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.time_spent_update_response import TimeSpentUpdateResponse

class TestTimeSpentUpdateResponse(unittest.TestCase):
    """TimeSpentUpdateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeSpentUpdateResponse:
        """Test TimeSpentUpdateResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeSpentUpdateResponse`
        """
        model = TimeSpentUpdateResponse()
        if include_optional:
            return TimeSpentUpdateResponse(
                success = True,
                message = None
            )
        else:
            return TimeSpentUpdateResponse(
        )
        """

    def testTimeSpentUpdateResponse(self):
        """Test TimeSpentUpdateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
