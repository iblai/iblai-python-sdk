# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.patched_play_wright_script import PatchedPlayWrightScript

class TestPatchedPlayWrightScript(unittest.TestCase):
    """PatchedPlayWrightScript unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedPlayWrightScript:
        """Test PatchedPlayWrightScript
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedPlayWrightScript`
        """
        model = PatchedPlayWrightScript()
        if include_optional:
            return PatchedPlayWrightScript(
                id = 56,
                platform = 56,
                student = 56,
                title = '',
                description = '',
                script = '',
                is_public = True
            )
        else:
            return PatchedPlayWrightScript(
        )
        """

    def testPatchedPlayWrightScript(self):
        """Test PatchedPlayWrightScript"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
