# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.tool_response import ToolResponse

class TestToolResponse(unittest.TestCase):
    """ToolResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ToolResponse:
        """Test ToolResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ToolResponse`
        """
        model = ToolResponse()
        if include_optional:
            return ToolResponse(
                id = 56,
                name = '',
                display_name = '',
                slug = 'z',
                description = '',
                metadata = None,
                allow_retriever_mentors = True
            )
        else:
            return ToolResponse(
                id = 56,
                name = '',
        )
        """

    def testToolResponse(self):
        """Test ToolResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
