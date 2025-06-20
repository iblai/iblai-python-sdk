# PlatformSkillPointGroupRequest

Request serializer for PlatformSkillPointGroupManagementView POST endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | Platform key identifier | 
**group_id** | **int** | ID of the user group to update | 
**point_data** | **Dict[str, int]** | Dictionary mapping skill names to point values to apply to group | 
**overwrite** | **bool** | If True, removes all skills not in point_data. If False, only updates specified skills. | [optional] [default to True]

## Example

```python
from iblai.models.platform_skill_point_group_request import PlatformSkillPointGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformSkillPointGroupRequest from a JSON string
platform_skill_point_group_request_instance = PlatformSkillPointGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PlatformSkillPointGroupRequest.to_json())

# convert the object into a dict
platform_skill_point_group_request_dict = platform_skill_point_group_request_instance.to_dict()
# create an instance of PlatformSkillPointGroupRequest from a dict
platform_skill_point_group_request_from_dict = PlatformSkillPointGroupRequest.from_dict(platform_skill_point_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


