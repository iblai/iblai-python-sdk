# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.job_run import JobRun

class TestJobRun(unittest.TestCase):
    """JobRun unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobRun:
        """Test JobRun
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobRun`
        """
        model = JobRun()
        if include_optional:
            return JobRun(
                id = 56,
                title = '',
                description = '',
                session = '',
                active = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                steps = [
                    iblai.models.step.Step(
                        id = 56, 
                        title = '', 
                        description = '', 
                        status = 'completed', 
                        position = 0, 
                        job = 56, )
                    ]
            )
        else:
            return JobRun(
                id = 56,
                title = '',
                session = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                steps = [
                    iblai.models.step.Step(
                        id = 56, 
                        title = '', 
                        description = '', 
                        status = 'completed', 
                        position = 0, 
                        job = 56, )
                    ],
        )
        """

    def testJobRun(self):
        """Test JobRun"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
