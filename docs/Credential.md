# Credential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 
**name** | **str** |  | 
**name_override** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**criteria_url** | **str** |  | 
**criteria_narrative** | **str** |  | 
**created_at** | **datetime** |  | 
**icon_image** | **str** |  | 
**background_image** | **str** |  | 
**thumbnail_image** | **str** |  | 
**catalog_items** | **List[str]** |  | [readonly] 
**courses** | **List[Dict[str, str]]** |  | [readonly] 
**programs** | **List[Dict[str, str]]** |  | [readonly] 
**issuer_details** | **Dict[str, str]** |  | [readonly] 
**html_template** | **str** |  | [optional] 
**css_template** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**credential_type** | **str** |  | 
**expires** | **Dict[str, int]** |  | [readonly] 
**tags** | **object** |  | [optional] 
**signatories** | **List[Dict[str, str]]** |  | [readonly] 

## Example

```python
from iblai.models.credential import Credential

# TODO update the JSON string below
json = "{}"
# create an instance of Credential from a JSON string
credential_instance = Credential.from_json(json)
# print the JSON string representation of the object
print(Credential.to_json())

# convert the object into a dict
credential_dict = credential_instance.to_dict()
# create an instance of Credential from a dict
credential_from_dict = Credential.from_dict(credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


