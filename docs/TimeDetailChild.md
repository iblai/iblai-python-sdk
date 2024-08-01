# TimeDetailChild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_time** | **float** | Average time spent | 
**display_name** | **str** | Subsection Display name | 
**id** | **str** | Subsection HTML id | 
**block_id** | **str** | Subsection block id | 
**total_time** | **int** | Total time spent | [optional] 
**total_users** | **int** | Total users who accessed the subsection | [optional] 

## Example

```python
from iblai.models.time_detail_child import TimeDetailChild

# TODO update the JSON string below
json = "{}"
# create an instance of TimeDetailChild from a JSON string
time_detail_child_instance = TimeDetailChild.from_json(json)
# print the JSON string representation of the object
print(TimeDetailChild.to_json())

# convert the object into a dict
time_detail_child_dict = time_detail_child_instance.to_dict()
# create an instance of TimeDetailChild from a dict
time_detail_child_from_dict = TimeDetailChild.from_dict(time_detail_child_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


