# Spa

Serializer for SPA (Single Page Application)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | SPA identifier (e.g. skills, mentor, admin) | 
**description** | **str** | Human-friendly description of the SPA | [optional] 

## Example

```python
from iblai.models.spa import Spa

# TODO update the JSON string below
json = "{}"
# create an instance of Spa from a JSON string
spa_instance = Spa.from_json(json)
# print the JSON string representation of the object
print(Spa.to_json())

# convert the object into a dict
spa_dict = spa_instance.to_dict()
# create an instance of Spa from a dict
spa_from_dict = Spa.from_dict(spa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


