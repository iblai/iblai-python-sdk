# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.block_skill_point_info_request import BlockSkillPointInfoRequest

class TestBlockSkillPointInfoRequest(unittest.TestCase):
    """BlockSkillPointInfoRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BlockSkillPointInfoRequest:
        """Test BlockSkillPointInfoRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlockSkillPointInfoRequest`
        """
        model = BlockSkillPointInfoRequest()
        if include_optional:
            return BlockSkillPointInfoRequest(
                block_id = '',
                point_data = {
                    'key' : 0
                    },
                overwrite = True
            )
        else:
            return BlockSkillPointInfoRequest(
                block_id = '',
                point_data = {
                    'key' : 0
                    },
        )
        """

    def testBlockSkillPointInfoRequest(self):
        """Test BlockSkillPointInfoRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
