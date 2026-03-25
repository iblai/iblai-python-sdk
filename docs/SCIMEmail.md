# SCIMEmail

SCIM email object serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Email address | 
**primary** | **bool** | Whether this is the primary email | [optional] [default to True]
**type** | **str** | Email type (work, home, etc.) | [optional] [default to 'work']

## Example

```python
from iblai.models.scim_email import SCIMEmail

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMEmail from a JSON string
scim_email_instance = SCIMEmail.from_json(json)
# print the JSON string representation of the object
print(SCIMEmail.to_json())

# convert the object into a dict
scim_email_dict = scim_email_instance.to_dict()
# create an instance of SCIMEmail from a dict
scim_email_from_dict = SCIMEmail.from_dict(scim_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


