# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.paginated_play_wright_script_list import PaginatedPlayWrightScriptList

class TestPaginatedPlayWrightScriptList(unittest.TestCase):
    """PaginatedPlayWrightScriptList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPlayWrightScriptList:
        """Test PaginatedPlayWrightScriptList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPlayWrightScriptList`
        """
        model = PaginatedPlayWrightScriptList()
        if include_optional:
            return PaginatedPlayWrightScriptList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    iblai.models.play_wright_script.PlayWrightScript(
                        id = 56, 
                        platform = 56, 
                        student = 56, 
                        title = '', 
                        description = '', 
                        script = '', 
                        is_public = True, )
                    ]
            )
        else:
            return PaginatedPlayWrightScriptList(
        )
        """

    def testPaginatedPlayWrightScriptList(self):
        """Test PaginatedPlayWrightScriptList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
