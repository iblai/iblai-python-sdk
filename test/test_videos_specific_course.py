# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.videos_specific_course import VideosSpecificCourse

class TestVideosSpecificCourse(unittest.TestCase):
    """VideosSpecificCourse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideosSpecificCourse:
        """Test VideosSpecificCourse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VideosSpecificCourse`
        """
        model = VideosSpecificCourse()
        if include_optional:
            return VideosSpecificCourse(
                data = [
                    iblai.models.videos_specific_course_data.VideosSpecificCourseData(
                        display_name = '', 
                        id = '', 
                        duration = 56, 
                        total_time = 56, 
                        total_users = 56, 
                        average_time = 1.337, )
                    ]
            )
        else:
            return VideosSpecificCourse(
        )
        """

    def testVideosSpecificCourse(self):
        """Test VideosSpecificCourse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
