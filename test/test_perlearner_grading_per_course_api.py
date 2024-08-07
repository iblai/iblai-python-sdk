# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.perlearner_grading_per_course_api import PerlearnerGradingPerCourseAPI

class TestPerlearnerGradingPerCourseAPI(unittest.TestCase):
    """PerlearnerGradingPerCourseAPI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PerlearnerGradingPerCourseAPI:
        """Test PerlearnerGradingPerCourseAPI
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PerlearnerGradingPerCourseAPI`
        """
        model = PerlearnerGradingPerCourseAPI()
        if include_optional:
            return PerlearnerGradingPerCourseAPI(
                data = [
                    iblai.models.perlearner_grading_per_course_api_data.PerlearnerGradingPerCourseAPIData(
                        course_id = '', 
                        name = '', 
                        graded_activities = '', 
                        submissions = 56, 
                        problems_attempted = 56, 
                        assignments_correct = 56, 
                        class_average = 1.337, 
                        grade = 1.337, )
                    ]
            )
        else:
            return PerlearnerGradingPerCourseAPI(
                data = [
                    iblai.models.perlearner_grading_per_course_api_data.PerlearnerGradingPerCourseAPIData(
                        course_id = '', 
                        name = '', 
                        graded_activities = '', 
                        submissions = 56, 
                        problems_attempted = 56, 
                        assignments_correct = 56, 
                        class_average = 1.337, 
                        grade = 1.337, )
                    ],
        )
        """

    def testPerlearnerGradingPerCourseAPI(self):
        """Test PerlearnerGradingPerCourseAPI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
