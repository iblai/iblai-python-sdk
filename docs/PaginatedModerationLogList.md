# PaginatedModerationLogList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ModerationLog]**](ModerationLog.md) |  | 

## Example

```python
from iblai.models.paginated_moderation_log_list import PaginatedModerationLogList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedModerationLogList from a JSON string
paginated_moderation_log_list_instance = PaginatedModerationLogList.from_json(json)
# print the JSON string representation of the object
print(PaginatedModerationLogList.to_json())

# convert the object into a dict
paginated_moderation_log_list_dict = paginated_moderation_log_list_instance.to_dict()
# create an instance of PaginatedModerationLogList from a dict
paginated_moderation_log_list_from_dict = PaginatedModerationLogList.from_dict(paginated_moderation_log_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


