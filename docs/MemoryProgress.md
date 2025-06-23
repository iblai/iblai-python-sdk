# MemoryProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_type** | **str** |  | [readonly] 
**all_units** | **int** |  | [readonly] 
**all_unit_names** | **List[str]** |  | [readonly] 
**current_unit** | **int** |  | [readonly] 
**current_unit_name** | **str** |  | [readonly] 
**item_name** | **str** |  | [readonly] 

## Example

```python
from iblai.models.memory_progress import MemoryProgress

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryProgress from a JSON string
memory_progress_instance = MemoryProgress.from_json(json)
# print the JSON string representation of the object
print(MemoryProgress.to_json())

# convert the object into a dict
memory_progress_dict = memory_progress_instance.to_dict()
# create an instance of MemoryProgress from a dict
memory_progress_from_dict = MemoryProgress.from_dict(memory_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


