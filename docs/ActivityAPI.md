# ActivityAPI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ActivityData]**](ActivityData.md) |  | [optional] 
**total** | **int** | Total rows | 

## Example

```python
from iblai.models.activity_api import ActivityAPI

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityAPI from a JSON string
activity_api_instance = ActivityAPI.from_json(json)
# print the JSON string representation of the object
print(ActivityAPI.to_json())

# convert the object into a dict
activity_api_dict = activity_api_instance.to_dict()
# create an instance of ActivityAPI from a dict
activity_api_from_dict = ActivityAPI.from_dict(activity_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


