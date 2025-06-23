# VectorResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'document']
**title** | **str** |  | [optional] [default to '']
**snippet** | **str** |  | 
**source** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**confidence_level** | **float** |  | [optional] 

## Example

```python
from iblai.models.vector_result import VectorResult

# TODO update the JSON string below
json = "{}"
# create an instance of VectorResult from a JSON string
vector_result_instance = VectorResult.from_json(json)
# print the JSON string representation of the object
print(VectorResult.to_json())

# convert the object into a dict
vector_result_dict = vector_result_instance.to_dict()
# create an instance of VectorResult from a dict
vector_result_from_dict = VectorResult.from_dict(vector_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


