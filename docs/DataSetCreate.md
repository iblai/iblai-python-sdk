# DataSetCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**name** | **str** |  | 
**source_url** | **str** |  | [optional] 
**source_file** | **str** |  | [optional] 
**num_data_points** | **int** |  | [optional] 
**train_split** | **float** |  | [optional] 
**prompt** | **str** | (if any) Special instructions for generating the dataset. This could be requirements on tone, language, style, etc. | [optional] 

## Example

```python
from iblai.models.data_set_create import DataSetCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DataSetCreate from a JSON string
data_set_create_instance = DataSetCreate.from_json(json)
# print the JSON string representation of the object
print(DataSetCreate.to_json())

# convert the object into a dict
data_set_create_dict = data_set_create_instance.to_dict()
# create an instance of DataSetCreate from a dict
data_set_create_from_dict = DataSetCreate.from_dict(data_set_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


