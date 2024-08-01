# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.per_learner_course_last_access_data import PerLearnerCourseLastAccessData

class TestPerLearnerCourseLastAccessData(unittest.TestCase):
    """PerLearnerCourseLastAccessData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PerLearnerCourseLastAccessData:
        """Test PerLearnerCourseLastAccessData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PerLearnerCourseLastAccessData`
        """
        model = PerLearnerCourseLastAccessData()
        if include_optional:
            return PerLearnerCourseLastAccessData(
                course_id = '',
                course_name = '',
                block_id = '',
                block_display_name = '',
                course_grade = 1.337,
                course_progress = 1.337,
                last_accessed = ''
            )
        else:
            return PerLearnerCourseLastAccessData(
        )
        """

    def testPerLearnerCourseLastAccessData(self):
        """Test PerLearnerCourseLastAccessData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()