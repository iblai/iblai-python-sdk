# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.avg_course_grade_with_cutoff import AvgCourseGradeWithCutoff

class TestAvgCourseGradeWithCutoff(unittest.TestCase):
    """AvgCourseGradeWithCutoff unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AvgCourseGradeWithCutoff:
        """Test AvgCourseGradeWithCutoff
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AvgCourseGradeWithCutoff`
        """
        model = AvgCourseGradeWithCutoff()
        if include_optional:
            return AvgCourseGradeWithCutoff(
                data = iblai.models.avg_course_grade_with_cutoff_data.AvgCourseGradeWithCutoffData(
                    grade_cutoffs = {
                        'key' : null
                        }, 
                    average_grade = 1.337, )
            )
        else:
            return AvgCourseGradeWithCutoff(
        )
        """

    def testAvgCourseGradeWithCutoff(self):
        """Test AvgCourseGradeWithCutoff"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()