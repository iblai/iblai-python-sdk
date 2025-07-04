# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.heygen_marketing_video_detail import HeygenMarketingVideoDetail

class TestHeygenMarketingVideoDetail(unittest.TestCase):
    """HeygenMarketingVideoDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HeygenMarketingVideoDetail:
        """Test HeygenMarketingVideoDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HeygenMarketingVideoDetail`
        """
        model = HeygenMarketingVideoDetail()
        if include_optional:
            return HeygenMarketingVideoDetail(
                name = '',
                data = None,
                script = '',
                pk = 56,
                video_file = '',
                generation_status = ''
            )
        else:
            return HeygenMarketingVideoDetail(
                pk = 56,
                video_file = '',
                generation_status = '',
        )
        """

    def testHeygenMarketingVideoDetail(self):
        """Test HeygenMarketingVideoDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
