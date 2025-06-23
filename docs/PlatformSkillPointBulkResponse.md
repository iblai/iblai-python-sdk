# PlatformSkillPointBulkResponse

Response serializer for PlatformSkillPointBulkManagementView POST endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | **int** | Number of successful updates | 
**total** | **int** | Total number of updates attempted | 

## Example

```python
from iblai.models.platform_skill_point_bulk_response import PlatformSkillPointBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformSkillPointBulkResponse from a JSON string
platform_skill_point_bulk_response_instance = PlatformSkillPointBulkResponse.from_json(json)
# print the JSON string representation of the object
print(PlatformSkillPointBulkResponse.to_json())

# convert the object into a dict
platform_skill_point_bulk_response_dict = platform_skill_point_bulk_response_instance.to_dict()
# create an instance of PlatformSkillPointBulkResponse from a dict
platform_skill_point_bulk_response_from_dict = PlatformSkillPointBulkResponse.from_dict(platform_skill_point_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


