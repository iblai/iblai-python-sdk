# Issuer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [readonly] 
**org** | **str** |  | [readonly] 
**entity_id** | **str** |  | 
**signatories** | **Dict[str, str]** |  | [readonly] 
**url** | **str** |  | [readonly] 
**icon_image** | **str** |  | 
**allowed_template_tags** | **object** |  | [optional] 

## Example

```python
from iblai.models.issuer import Issuer

# TODO update the JSON string below
json = "{}"
# create an instance of Issuer from a JSON string
issuer_instance = Issuer.from_json(json)
# print the JSON string representation of the object
print(Issuer.to_json())

# convert the object into a dict
issuer_dict = issuer_instance.to_dict()
# create an instance of Issuer from a dict
issuer_from_dict = Issuer.from_dict(issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


