# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.time_detail_data import TimeDetailData

class TestTimeDetailData(unittest.TestCase):
    """TimeDetailData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeDetailData:
        """Test TimeDetailData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeDetailData`
        """
        model = TimeDetailData()
        if include_optional:
            return TimeDetailData(
                average_time = 1.337,
                display_name = '',
                id = '',
                children = [
                    iblai.models.time_detail_child.TimeDetailChild(
                        average_time = 1.337, 
                        display_name = '', 
                        id = '', 
                        block_id = '', 
                        total_time = 56, 
                        total_users = 56, )
                    ],
                total_time = 56,
                total_users = 56
            )
        else:
            return TimeDetailData(
                average_time = 1.337,
                display_name = '',
                id = '',
        )
        """

    def testTimeDetailData(self):
        """Test TimeDetailData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
