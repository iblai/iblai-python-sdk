# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.patched_credential_request import PatchedCredentialRequest

class TestPatchedCredentialRequest(unittest.TestCase):
    """PatchedCredentialRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedCredentialRequest:
        """Test PatchedCredentialRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedCredentialRequest`
        """
        model = PatchedCredentialRequest()
        if include_optional:
            return PatchedCredentialRequest(
                name = '',
                value = None,
                platform = ''
            )
        else:
            return PatchedCredentialRequest(
        )
        """

    def testPatchedCredentialRequest(self):
        """Test PatchedCredentialRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
