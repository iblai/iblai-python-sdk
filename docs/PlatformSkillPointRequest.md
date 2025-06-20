# PlatformSkillPointRequest

Request serializer for PlatformSkillPointManagementView POST endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username to update skill points for | 
**platform_key** | **str** | Platform key identifier | 
**point_data** | **Dict[str, int]** | Dictionary mapping skill names to point values. Example: {&#39;skill_name&#39;: 5} | 
**overwrite** | **bool** | If True, removes all skills not in point_data. If False, only updates specified skills. | [optional] [default to True]

## Example

```python
from iblai.models.platform_skill_point_request import PlatformSkillPointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformSkillPointRequest from a JSON string
platform_skill_point_request_instance = PlatformSkillPointRequest.from_json(json)
# print the JSON string representation of the object
print(PlatformSkillPointRequest.to_json())

# convert the object into a dict
platform_skill_point_request_dict = platform_skill_point_request_instance.to_dict()
# create an instance of PlatformSkillPointRequest from a dict
platform_skill_point_request_from_dict = PlatformSkillPointRequest.from_dict(platform_skill_point_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


