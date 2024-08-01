# PaginatedPlayWrightScriptList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PlayWrightScript]**](PlayWrightScript.md) |  | [optional] 

## Example

```python
from iblai.models.paginated_play_wright_script_list import PaginatedPlayWrightScriptList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPlayWrightScriptList from a JSON string
paginated_play_wright_script_list_instance = PaginatedPlayWrightScriptList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPlayWrightScriptList.to_json())

# convert the object into a dict
paginated_play_wright_script_list_dict = paginated_play_wright_script_list_instance.to_dict()
# create an instance of PaginatedPlayWrightScriptList from a dict
paginated_play_wright_script_list_from_dict = PaginatedPlayWrightScriptList.from_dict(paginated_play_wright_script_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


