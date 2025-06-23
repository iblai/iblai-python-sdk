# Pathway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**pathway_id** | **str** | A unique pathway ID. | 
**pathway_uuid** | **str** |  | [optional] 
**path** | **str** |  | [readonly] 
**name** | **str** | The verbose name of the pathway. | [optional] 
**visible** | **bool** | Pathway visibility | [optional] 
**slug** | **str** | An additional unique slug field. (Optional) | [optional] 
**user_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**platform_key** | **str** |  | [optional] 
**data** | **object** | Metadata | [optional] 

## Example

```python
from iblai.models.pathway import Pathway

# TODO update the JSON string below
json = "{}"
# create an instance of Pathway from a JSON string
pathway_instance = Pathway.from_json(json)
# print the JSON string representation of the object
print(Pathway.to_json())

# convert the object into a dict
pathway_dict = pathway_instance.to_dict()
# create an instance of Pathway from a dict
pathway_from_dict = Pathway.from_dict(pathway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


