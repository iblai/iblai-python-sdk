# PlatformSkillPointBulkRequest

Request serializer for PlatformSkillPointBulkManagementView POST endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | Platform key identifier (required for platform admin access) | [optional] 
**skill_point_data** | **List[Dict[str, object]]** | List of skill point data objects to create/update | 

## Example

```python
from iblai.models.platform_skill_point_bulk_request import PlatformSkillPointBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformSkillPointBulkRequest from a JSON string
platform_skill_point_bulk_request_instance = PlatformSkillPointBulkRequest.from_json(json)
# print the JSON string representation of the object
print(PlatformSkillPointBulkRequest.to_json())

# convert the object into a dict
platform_skill_point_bulk_request_dict = platform_skill_point_bulk_request_instance.to_dict()
# create an instance of PlatformSkillPointBulkRequest from a dict
platform_skill_point_bulk_request_from_dict = PlatformSkillPointBulkRequest.from_dict(platform_skill_point_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


