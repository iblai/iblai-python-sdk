# AssociateAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**message** | **object** |  | 
**data** | **object** |  | 

## Example

```python
from iblai.models.associate_account_response import AssociateAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssociateAccountResponse from a JSON string
associate_account_response_instance = AssociateAccountResponse.from_json(json)
# print the JSON string representation of the object
print(AssociateAccountResponse.to_json())

# convert the object into a dict
associate_account_response_dict = associate_account_response_instance.to_dict()
# create an instance of AssociateAccountResponse from a dict
associate_account_response_from_dict = AssociateAccountResponse.from_dict(associate_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


