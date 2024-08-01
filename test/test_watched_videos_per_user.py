# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.watched_videos_per_user import WatchedVideosPerUser

class TestWatchedVideosPerUser(unittest.TestCase):
    """WatchedVideosPerUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WatchedVideosPerUser:
        """Test WatchedVideosPerUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WatchedVideosPerUser`
        """
        model = WatchedVideosPerUser()
        if include_optional:
            return WatchedVideosPerUser(
                data = [
                    iblai.models.watched_videos_per_user_data.WatchedVideosPerUserData(
                        username = '', 
                        full_name = '', 
                        count = 56, 
                        percentage = 1.337, )
                    ],
                total = 56
            )
        else:
            return WatchedVideosPerUser(
        )
        """

    def testWatchedVideosPerUser(self):
        """Test WatchedVideosPerUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
