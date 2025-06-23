# PlatformSkillPointResponse

Response serializer for PlatformSkillPointManagementView GET endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[Dict[str, object]]** | List of platform skill point entries | 
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 

## Example

```python
from iblai.models.platform_skill_point_response import PlatformSkillPointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformSkillPointResponse from a JSON string
platform_skill_point_response_instance = PlatformSkillPointResponse.from_json(json)
# print the JSON string representation of the object
print(PlatformSkillPointResponse.to_json())

# convert the object into a dict
platform_skill_point_response_dict = platform_skill_point_response_instance.to_dict()
# create an instance of PlatformSkillPointResponse from a dict
platform_skill_point_response_from_dict = PlatformSkillPointResponse.from_dict(platform_skill_point_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


