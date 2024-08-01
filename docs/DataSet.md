# DataSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**platform** | [**Dict[str, DataSetPlatformValue]**](DataSetPlatformValue.md) |  | [readonly] 
**name** | **str** |  | 
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
**date_created** | **datetime** |  | [readonly] 
**last_modified** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.data_set import DataSet

# TODO update the JSON string below
json = "{}"
# create an instance of DataSet from a JSON string
data_set_instance = DataSet.from_json(json)
# print the JSON string representation of the object
print(DataSet.to_json())

# convert the object into a dict
data_set_dict = data_set_instance.to_dict()
# create an instance of DataSet from a dict
data_set_from_dict = DataSet.from_dict(data_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


