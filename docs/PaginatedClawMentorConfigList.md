# PaginatedClawMentorConfigList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ClawMentorConfig]**](ClawMentorConfig.md) |  | 

## Example

```python
from iblai.models.paginated_claw_mentor_config_list import PaginatedClawMentorConfigList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClawMentorConfigList from a JSON string
paginated_claw_mentor_config_list_instance = PaginatedClawMentorConfigList.from_json(json)
# print the JSON string representation of the object
print(PaginatedClawMentorConfigList.to_json())

# convert the object into a dict
paginated_claw_mentor_config_list_dict = paginated_claw_mentor_config_list_instance.to_dict()
# create an instance of PaginatedClawMentorConfigList from a dict
paginated_claw_mentor_config_list_from_dict = PaginatedClawMentorConfigList.from_dict(paginated_claw_mentor_config_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


