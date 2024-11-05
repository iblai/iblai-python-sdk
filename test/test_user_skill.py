# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.user_skill import UserSkill

class TestUserSkill(unittest.TestCase):
    """UserSkill unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSkill:
        """Test UserSkill
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSkill`
        """
        model = UserSkill()
        if include_optional:
            return UserSkill(
                skill = iblai.models.skill.Skill(
                    id = 56, 
                    name = '', ),
                courses = [
                    iblai.models.course_point.CoursePoint(
                        course_id = '', 
                        points = 56, )
                    ],
                resources = [
                    iblai.models.resource_point.ResourcePoint(
                        name = '', 
                        points = 56, )
                    ],
                total_points = 56,
                percentile = 1.337
            )
        else:
            return UserSkill(
                skill = iblai.models.skill.Skill(
                    id = 56, 
                    name = '', ),
                courses = [
                    iblai.models.course_point.CoursePoint(
                        course_id = '', 
                        points = 56, )
                    ],
                resources = [
                    iblai.models.resource_point.ResourcePoint(
                        name = '', 
                        points = 56, )
                    ],
                total_points = 56,
        )
        """

    def testUserSkill(self):
        """Test UserSkill"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
