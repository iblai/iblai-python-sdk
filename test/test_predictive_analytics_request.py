# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.predictive_analytics_request import PredictiveAnalyticsRequest

class TestPredictiveAnalyticsRequest(unittest.TestCase):
    """PredictiveAnalyticsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PredictiveAnalyticsRequest:
        """Test PredictiveAnalyticsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PredictiveAnalyticsRequest`
        """
        model = PredictiveAnalyticsRequest()
        if include_optional:
            return PredictiveAnalyticsRequest(
                prompt = iblai.models.reuest_data_variable_list.ReuestDataVariableList(
                    data_variables = [
                        iblai.models.request_data_variable.RequestDataVariable(
                            variable_name = '', 
                            data_set = null, 
                            number_of_data_points = 56, )
                        ], )
            )
        else:
            return PredictiveAnalyticsRequest(
                prompt = iblai.models.reuest_data_variable_list.ReuestDataVariableList(
                    data_variables = [
                        iblai.models.request_data_variable.RequestDataVariable(
                            variable_name = '', 
                            data_set = null, 
                            number_of_data_points = 56, )
                        ], ),
        )
        """

    def testPredictiveAnalyticsRequest(self):
        """Test PredictiveAnalyticsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
