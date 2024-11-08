# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.time_child_data import TimeChildData

class TestTimeChildData(unittest.TestCase):
    """TimeChildData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeChildData:
        """Test TimeChildData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeChildData`
        """
        model = TimeChildData()
        if include_optional:
            return TimeChildData(
                display_name = '',
                id = '',
                block_id = '',
                total_time = 56,
                children = [
                    iblai.models.sub_time_child.SubTimeChild(
                        display_name = '', 
                        id = '', 
                        block_id = '', 
                        total_time = 56, )
                    ]
            )
        else:
            return TimeChildData(
                display_name = '',
                id = '',
                children = [
                    iblai.models.sub_time_child.SubTimeChild(
                        display_name = '', 
                        id = '', 
                        block_id = '', 
                        total_time = 56, )
                    ],
        )
        """

    def testTimeChildData(self):
        """Test TimeChildData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
