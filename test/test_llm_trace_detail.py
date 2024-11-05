# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.llm_trace_detail import LLMTraceDetail

class TestLLMTraceDetail(unittest.TestCase):
    """LLMTraceDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LLMTraceDetail:
        """Test LLMTraceDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LLMTraceDetail`
        """
        model = LLMTraceDetail()
        if include_optional:
            return LLMTraceDetail(
                trace = iblai.models.trace.Trace(
                    id = '', 
                    username = '', 
                    external_id = '', 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    totalprice = 1.337, 
                    user_id = '', 
                    metadata = {
                        'key' : null
                        }, 
                    release = '', 
                    version = '', 
                    project_id = '', 
                    public = True, 
                    bookmarked = True, 
                    tags = [
                        ''
                        ], 
                    input = null, 
                    output = null, 
                    session_id = '', 
                    scores = [
                        {
                            'key' : null
                            }
                        ], 
                    observations = [
                        iblai.models.observation.Observation(
                            id = '', 
                            trace_id = '', 
                            project_id = '', 
                            type = '', 
                            start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '', 
                            metadata = {
                                'key' : null
                                }, 
                            parent_observation_id = '', 
                            level = '', 
                            status_message = '', 
                            version = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            model = '', 
                            model_parameters = {
                                'key' : null
                                }, 
                            input = null, 
                            output = null, 
                            prompt_tokens = 56, 
                            completion_tokens = 56, 
                            total_tokens = 56, 
                            unit = '', 
                            completion_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            prompt_id = '', 
                            usage = {
                                'key' : null
                                }, 
                            price = 1.337, )
                        ], )
            )
        else:
            return LLMTraceDetail(
        )
        """

    def testLLMTraceDetail(self):
        """Test LLMTraceDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
