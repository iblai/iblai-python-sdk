# TimeChildData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display name | 
**id** | **str** | block id | 
**block_id** | **str** | block id | [optional] 
**total_time** | **int** | Total time spent | [optional] 
**children** | [**List[SubTimeChild]**](SubTimeChild.md) |  | 

## Example

```python
from iblai.models.time_child_data import TimeChildData

# TODO update the JSON string below
json = "{}"
# create an instance of TimeChildData from a JSON string
time_child_data_instance = TimeChildData.from_json(json)
# print the JSON string representation of the object
print(TimeChildData.to_json())

# convert the object into a dict
time_child_data_dict = time_child_data_instance.to_dict()
# create an instance of TimeChildData from a dict
time_child_data_from_dict = TimeChildData.from_dict(time_child_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


