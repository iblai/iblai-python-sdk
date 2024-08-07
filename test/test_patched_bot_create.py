# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.patched_bot_create import PatchedBotCreate

class TestPatchedBotCreate(unittest.TestCase):
    """PatchedBotCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedBotCreate:
        """Test PatchedBotCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedBotCreate`
        """
        model = PatchedBotCreate()
        if include_optional:
            return PatchedBotCreate(
                id = 56,
                name = '',
                client_id = '',
                client_secret = '',
                app_token = '',
                verification_token = '',
                provider = 'webex',
                config = None,
                webhook_url = ''
            )
        else:
            return PatchedBotCreate(
        )
        """

    def testPatchedBotCreate(self):
        """Test PatchedBotCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
