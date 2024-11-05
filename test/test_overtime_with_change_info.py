# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.overtime_with_change_info import OvertimeWithChangeInfo

class TestOvertimeWithChangeInfo(unittest.TestCase):
    """OvertimeWithChangeInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OvertimeWithChangeInfo:
        """Test OvertimeWithChangeInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OvertimeWithChangeInfo`
        """
        model = OvertimeWithChangeInfo()
        if include_optional:
            return OvertimeWithChangeInfo(
                data = {
                    'key' : null
                    },
                total = 56,
                meta = iblai.models.overtime_meta.OvertimeMeta(
                    total = 56, 
                    change_range = 56, 
                    change_last_seven_days = 56, 
                    change_last_thirty_days = 56, 
                    change_last_seven_days_percent = 1.337, 
                    change_last_thirty_days_percent = 1.337, 
                    change_range_percent = 1.337, )
            )
        else:
            return OvertimeWithChangeInfo(
                meta = iblai.models.overtime_meta.OvertimeMeta(
                    total = 56, 
                    change_range = 56, 
                    change_last_seven_days = 56, 
                    change_last_thirty_days = 56, 
                    change_last_seven_days_percent = 1.337, 
                    change_last_thirty_days_percent = 1.337, 
                    change_range_percent = 1.337, ),
        )
        """

    def testOvertimeWithChangeInfo(self):
        """Test OvertimeWithChangeInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
