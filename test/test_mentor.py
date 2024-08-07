# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.mentor import Mentor

class TestMentor(unittest.TestCase):
    """Mentor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Mentor:
        """Test Mentor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Mentor`
        """
        model = Mentor()
        if include_optional:
            return Mentor(
                name = '',
                unique_id = '',
                flow = None,
                slug = 'z',
                platform = '',
                allow_anonymous = True,
                metadata = None,
                enable_moderation = True,
                is_proactive = True,
                proactive_prompt = '',
                moderation_system_prompt = '',
                moderation_response = '',
                proactive_message = '',
                created_by = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Mentor(
                name = '',
                flow = None,
                slug = 'z',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testMentor(self):
        """Test Mentor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
