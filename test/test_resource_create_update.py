# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.resource_create_update import ResourceCreateUpdate

class TestResourceCreateUpdate(unittest.TestCase):
    """ResourceCreateUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceCreateUpdate:
        """Test ResourceCreateUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceCreateUpdate`
        """
        model = ResourceCreateUpdate()
        if include_optional:
            return ResourceCreateUpdate(
                id = 56,
                user_id = 56,
                username = '',
                resource_type = '',
                url = '',
                name = '',
                description = '',
                skills = [
                    ''
                    ],
                image = '',
                data = None
            )
        else:
            return ResourceCreateUpdate(
                resource_type = '',
                url = '',
                name = '',
        )
        """

    def testResourceCreateUpdate(self):
        """Test ResourceCreateUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
