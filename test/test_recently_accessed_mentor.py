# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.recently_accessed_mentor import RecentlyAccessedMentor

class TestRecentlyAccessedMentor(unittest.TestCase):
    """RecentlyAccessedMentor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecentlyAccessedMentor:
        """Test RecentlyAccessedMentor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecentlyAccessedMentor`
        """
        model = RecentlyAccessedMentor()
        if include_optional:
            return RecentlyAccessedMentor(
                slug = '',
                name = '',
                description = '',
                recently_accessed_at = '',
                platform_key = '',
                last_accessed_by = ''
            )
        else:
            return RecentlyAccessedMentor(
                slug = '',
                name = '',
                description = '',
                recently_accessed_at = '',
                platform_key = '',
                last_accessed_by = '',
        )
        """

    def testRecentlyAccessedMentor(self):
        """Test RecentlyAccessedMentor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
