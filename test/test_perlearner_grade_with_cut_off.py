# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.perlearner_grade_with_cut_off import PerlearnerGradeWithCutOff

class TestPerlearnerGradeWithCutOff(unittest.TestCase):
    """PerlearnerGradeWithCutOff unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PerlearnerGradeWithCutOff:
        """Test PerlearnerGradeWithCutOff
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PerlearnerGradeWithCutOff`
        """
        model = PerlearnerGradeWithCutOff()
        if include_optional:
            return PerlearnerGradeWithCutOff(
                data = iblai.models.perlearner_grade_with_cut_off_data.PerlearnerGradeWithCutOffData(
                    grade_cutoffs = {
                        'key' : null
                        }, 
                    grade = 1.337, )
            )
        else:
            return PerlearnerGradeWithCutOff(
        )
        """

    def testPerlearnerGradeWithCutOff(self):
        """Test PerlearnerGradeWithCutOff"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()