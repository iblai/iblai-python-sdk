# SubTimeChild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display name | 
**id** | **str** | block id | 
**block_id** | **str** | block id | [optional] 
**total_time** | **int** | Total time spent | [optional] 

## Example

```python
from iblai.models.sub_time_child import SubTimeChild

# TODO update the JSON string below
json = "{}"
# create an instance of SubTimeChild from a JSON string
sub_time_child_instance = SubTimeChild.from_json(json)
# print the JSON string representation of the object
print(SubTimeChild.to_json())

# convert the object into a dict
sub_time_child_dict = sub_time_child_instance.to_dict()
# create an instance of SubTimeChild from a dict
sub_time_child_from_dict = SubTimeChild.from_dict(sub_time_child_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


