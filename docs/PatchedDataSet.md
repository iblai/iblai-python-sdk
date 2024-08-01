# PatchedDataSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**platform** | [**Dict[str, DataSetPlatformValue]**](DataSetPlatformValue.md) |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**prompt** | **str** | (if any) Special instructions for generating the dataset. This could be requirements on tone, language, style, etc. | [optional] 
**source_url** | **str** |  | [optional] 
**source_file** | **str** |  | [optional] 
**status** | [**DataSetStatusEnum**](DataSetStatusEnum.md) |  | [optional] 
**num_data_points** | **int** |  | [optional] 
**train_split** | **float** |  | [optional] 
**train_file** | **str** |  | [optional] 
**test_file** | **str** |  | [optional] 
**retry_attempts** | **int** |  | [optional] 
**error_log** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] [readonly] 
**last_modified** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_data_set import PatchedDataSet

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDataSet from a JSON string
patched_data_set_instance = PatchedDataSet.from_json(json)
# print the JSON string representation of the object
print(PatchedDataSet.to_json())

# convert the object into a dict
patched_data_set_dict = patched_data_set_instance.to_dict()
# create an instance of PatchedDataSet from a dict
patched_data_set_from_dict = PatchedDataSet.from_dict(patched_data_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


