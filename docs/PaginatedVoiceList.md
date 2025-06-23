# PaginatedVoiceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Voice]**](Voice.md) |  | 

## Example

```python
from iblai.models.paginated_voice_list import PaginatedVoiceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedVoiceList from a JSON string
paginated_voice_list_instance = PaginatedVoiceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedVoiceList.to_json())

# convert the object into a dict
paginated_voice_list_dict = paginated_voice_list_instance.to_dict()
# create an instance of PaginatedVoiceList from a dict
paginated_voice_list_from_dict = PaginatedVoiceList.from_dict(paginated_voice_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


