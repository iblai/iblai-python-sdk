# Spa

Serializer for SPA

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Unique identifier for the SPA (e.g., &#39;skills&#39;, &#39;mentor&#39;, &#39;admin&#39;, &#39;mobile&#39;) | 
**description** | **str** | Human-friendly description of this SPA | [optional] 

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


