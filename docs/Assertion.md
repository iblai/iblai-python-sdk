# Assertion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 
**issued_on** | **str** |  | 
**credential_details** | **Dict[str, str]** |  | [readonly] 
**recipient** | **Dict[str, str]** |  | [readonly] 
**metadata** | **object** |  | [optional] 
**course** | **Dict[str, str]** |  | [readonly] 
**program** | **Dict[str, str]** |  | [readonly] 
**narrative** | **str** |  | [optional] 
**revoked** | **bool** |  | [optional] 
**revocation_reason** | **str** |  | 
**acceptance** | [**AcceptanceEnum**](AcceptanceEnum.md) |  | [optional] 
**expires** | **str** |  | 

## Example

```python
from iblai.models.assertion import Assertion

# TODO update the JSON string below
json = "{}"
# create an instance of Assertion from a JSON string
assertion_instance = Assertion.from_json(json)
# print the JSON string representation of the object
print(Assertion.to_json())

# convert the object into a dict
assertion_dict = assertion_instance.to_dict()
# create an instance of Assertion from a dict
assertion_from_dict = Assertion.from_dict(assertion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


