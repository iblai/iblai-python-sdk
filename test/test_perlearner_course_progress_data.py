# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.perlearner_course_progress_data import PerlearnerCourseProgressData

class TestPerlearnerCourseProgressData(unittest.TestCase):
    """PerlearnerCourseProgressData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PerlearnerCourseProgressData:
        """Test PerlearnerCourseProgressData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PerlearnerCourseProgressData`
        """
        model = PerlearnerCourseProgressData()
        if include_optional:
            return PerlearnerCourseProgressData(
                progress = 1.337
            )
        else:
            return PerlearnerCourseProgressData(
                progress = 1.337,
        )
        """

    def testPerlearnerCourseProgressData(self):
        """Test PerlearnerCourseProgressData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
