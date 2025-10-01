# Disclaimer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**scope** | [**ScopeEnum**](ScopeEnum.md) |  | [optional] 
**platform** | **int** | Platform to which the disclaimer applies.  | [readonly] 
**content** | **str** |  | 
**title** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**has_agreed** | **bool** |  | [readonly] 
**platform_key** | **str** |  | [readonly] 
**mentors** | **List[str]** |  | [optional] 

## Example

```python
from iblai.models.disclaimer import Disclaimer

# TODO update the JSON string below
json = "{}"
# create an instance of Disclaimer from a JSON string
disclaimer_instance = Disclaimer.from_json(json)
# print the JSON string representation of the object
print(Disclaimer.to_json())

# convert the object into a dict
disclaimer_dict = disclaimer_instance.to_dict()
# create an instance of Disclaimer from a dict
disclaimer_from_dict = Disclaimer.from_dict(disclaimer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


