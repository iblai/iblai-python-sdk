# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.model_cost import ModelCost

class TestModelCost(unittest.TestCase):
    """ModelCost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelCost:
        """Test ModelCost
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelCost`
        """
        model = ModelCost()
        if include_optional:
            return ModelCost(
                model = '',
                total_tokens = 56,
                total_cost = 1.337
            )
        else:
            return ModelCost(
                model = '',
                total_tokens = 56,
                total_cost = 1.337,
        )
        """

    def testModelCost(self):
        """Test ModelCost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
