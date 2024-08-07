# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.tenant_mentor_traces import TenantMentorTraces

class TestTenantMentorTraces(unittest.TestCase):
    """TenantMentorTraces unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantMentorTraces:
        """Test TenantMentorTraces
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantMentorTraces`
        """
        model = TenantMentorTraces()
        if include_optional:
            return TenantMentorTraces(
                tenant = '',
                tenant_total_cost = 1.337,
                tenant_average_latency = 1.337,
                total_traces = 56,
                mentor_traces = [
                    iblai.models.mentor_data.MentorData(
                        mentor = '', 
                        total_cost = 1.337, 
                        total_latency = 1.337, 
                        mentor_traces = [
                            iblai.models.mentor_trace.MentorTrace(
                                session_id = '', 
                                cost = 1.337, 
                                latency = 1.337, 
                                username = '', )
                            ], )
                    ]
            )
        else:
            return TenantMentorTraces(
                tenant = '',
                tenant_total_cost = 1.337,
                tenant_average_latency = 1.337,
                total_traces = 56,
                mentor_traces = [
                    iblai.models.mentor_data.MentorData(
                        mentor = '', 
                        total_cost = 1.337, 
                        total_latency = 1.337, 
                        mentor_traces = [
                            iblai.models.mentor_trace.MentorTrace(
                                session_id = '', 
                                cost = 1.337, 
                                latency = 1.337, 
                                username = '', )
                            ], )
                    ],
        )
        """

    def testTenantMentorTraces(self):
        """Test TenantMentorTraces"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
