# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.retrieve_task import RetrieveTask

class TestRetrieveTask(unittest.TestCase):
    """RetrieveTask unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveTask:
        """Test RetrieveTask
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveTask`
        """
        model = RetrieveTask()
        if include_optional:
            return RetrieveTask(
                task = ''
            )
        else:
            return RetrieveTask(
                task = '',
        )
        """

    def testRetrieveTask(self):
        """Test RetrieveTask"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
