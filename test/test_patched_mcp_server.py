# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.patched_mcp_server import PatchedMCPServer

class TestPatchedMCPServer(unittest.TestCase):
    """PatchedMCPServer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedMCPServer:
        """Test PatchedMCPServer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedMCPServer`
        """
        model = PatchedMCPServer()
        if include_optional:
            return PatchedMCPServer(
                id = 56,
                platform = 56,
                name = '',
                url = '',
                transport = 'sse',
                headers = None,
                platform_key = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PatchedMCPServer(
        )
        """

    def testPatchedMCPServer(self):
        """Test PatchedMCPServer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
