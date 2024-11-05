# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.llm_scores_view import LLMScoresView

class TestLLMScoresView(unittest.TestCase):
    """LLMScoresView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LLMScoresView:
        """Test LLMScoresView
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LLMScoresView`
        """
        model = LLMScoresView()
        if include_optional:
            return LLMScoresView(
                total_scores_tracked = 56,
                scores_summary = [
                    iblai.models.score_summary.ScoreSummary(
                        name = '', 
                        count = 56, 
                        zero_count = 56, 
                        one_count = 56, 
                        average = 1.337, )
                    ],
                scores = [
                    iblai.models.score.Score(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        value = 1.337, 
                        comment = '', 
                        trace_id = '', 
                        observation_id = '', 
                        trace = null, )
                    ]
            )
        else:
            return LLMScoresView(
                total_scores_tracked = 56,
                scores_summary = [
                    iblai.models.score_summary.ScoreSummary(
                        name = '', 
                        count = 56, 
                        zero_count = 56, 
                        one_count = 56, 
                        average = 1.337, )
                    ],
                scores = [
                    iblai.models.score.Score(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        value = 1.337, 
                        comment = '', 
                        trace_id = '', 
                        observation_id = '', 
                        trace = null, )
                    ],
        )
        """

    def testLLMScoresView(self):
        """Test LLMScoresView"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
