# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.reuest_data_variable_list import ReuestDataVariableList

class TestReuestDataVariableList(unittest.TestCase):
    """ReuestDataVariableList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReuestDataVariableList:
        """Test ReuestDataVariableList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReuestDataVariableList`
        """
        model = ReuestDataVariableList()
        if include_optional:
            return ReuestDataVariableList(
                data_variables = [
                    iblai.models.request_data_variable.RequestDataVariable(
                        variable_name = '', 
                        data_set = null, 
                        number_of_data_points = 56, )
                    ]
            )
        else:
            return ReuestDataVariableList(
                data_variables = [
                    iblai.models.request_data_variable.RequestDataVariable(
                        variable_name = '', 
                        data_set = null, 
                        number_of_data_points = 56, )
                    ],
        )
        """

    def testReuestDataVariableList(self):
        """Test ReuestDataVariableList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()