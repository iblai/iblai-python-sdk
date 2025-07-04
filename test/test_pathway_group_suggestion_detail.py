# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.pathway_group_suggestion_detail import PathwayGroupSuggestionDetail

class TestPathwayGroupSuggestionDetail(unittest.TestCase):
    """PathwayGroupSuggestionDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PathwayGroupSuggestionDetail:
        """Test PathwayGroupSuggestionDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PathwayGroupSuggestionDetail`
        """
        model = PathwayGroupSuggestionDetail()
        if include_optional:
            return PathwayGroupSuggestionDetail(
                id = 56,
                group_id = 56,
                group_name = '',
                platform_key = '',
                accepted = True,
                visible = True,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                metadata = {
                    'key' : null
                    },
                pathway_id = '',
                pathway_uuid = '',
                pathway_name = '',
                pathway_platform_key = '',
                user_count = 56
            )
        else:
            return PathwayGroupSuggestionDetail(
                id = 56,
                group_id = 56,
                group_name = '',
                platform_key = '',
                visible = True,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                metadata = {
                    'key' : null
                    },
                pathway_id = '',
                pathway_uuid = '',
                pathway_name = '',
                pathway_platform_key = '',
        )
        """

    def testPathwayGroupSuggestionDetail(self):
        """Test PathwayGroupSuggestionDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
