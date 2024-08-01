# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.llm_scores_view_response import LLMScoresViewResponse

class TestLLMScoresViewResponse(unittest.TestCase):
    """LLMScoresViewResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LLMScoresViewResponse:
        """Test LLMScoresViewResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LLMScoresViewResponse`
        """
        model = LLMScoresViewResponse()
        if include_optional:
            return LLMScoresViewResponse(
                id = '',
                trace_id = '',
                name = '',
                value = 1.337,
                observation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                comment = ''
            )
        else:
            return LLMScoresViewResponse(
                id = '',
                trace_id = '',
                name = '',
                value = 1.337,
                observation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                comment = '',
        )
        """

    def testLLMScoresViewResponse(self):
        """Test LLMScoresViewResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
