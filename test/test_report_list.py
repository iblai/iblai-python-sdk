# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.report_list import ReportList

class TestReportList(unittest.TestCase):
    """ReportList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportList:
        """Test ReportList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportList`
        """
        model = ReportList()
        if include_optional:
            return ReportList(
                data = [
                    iblai.models.report_data.ReportData(
                        display_name = '', 
                        description = '', 
                        report_name = '', 
                        icon = '', 
                        extra_query_params = [
                            null
                            ], 
                        result_columns = [
                            null
                            ], 
                        status = null, )
                    ]
            )
        else:
            return ReportList(
                data = [
                    iblai.models.report_data.ReportData(
                        display_name = '', 
                        description = '', 
                        report_name = '', 
                        icon = '', 
                        extra_query_params = [
                            null
                            ], 
                        result_columns = [
                            null
                            ], 
                        status = null, )
                    ],
        )
        """

    def testReportList(self):
        """Test ReportList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
