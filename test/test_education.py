# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.education import Education

class TestEducation(unittest.TestCase):
    """Education unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Education:
        """Test Education
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Education`
        """
        model = Education()
        if include_optional:
            return Education(
                id = 56,
                user = 56,
                user_info = iblai.models.user_info.UserInfo(
                    id = 56, 
                    username = '', 
                    name = '', 
                    email = '', 
                    active = True, 
                    edx_data = null, ),
                institution = iblai.models.institution.Institution(
                    id = 56, 
                    name = '', 
                    institution_type = 'university', 
                    location = '', 
                    website = '', 
                    accreditation = '', 
                    established_year = 56, 
                    data = null, 
                    metadata = null, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                institution_id = 56,
                degree = '',
                field_of_study = '',
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                grade = '-8',
                activities = '',
                description = '',
                data = None,
                metadata = None,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_current = True
            )
        else:
            return Education(
                id = 56,
                user = 56,
                user_info = iblai.models.user_info.UserInfo(
                    id = 56, 
                    username = '', 
                    name = '', 
                    email = '', 
                    active = True, 
                    edx_data = null, ),
                institution = iblai.models.institution.Institution(
                    id = 56, 
                    name = '', 
                    institution_type = 'university', 
                    location = '', 
                    website = '', 
                    accreditation = '', 
                    established_year = 56, 
                    data = null, 
                    metadata = null, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                institution_id = 56,
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testEducation(self):
        """Test Education"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()