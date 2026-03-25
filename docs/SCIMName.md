# SCIMName

SCIM name object serializer. Fields allow_blank=True so response validation succeeds for users with no name set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formatted** | **str** | Full formatted name | [optional] 
**family_name** | **str** | Family/last name | [optional] 
**given_name** | **str** | Given/first name | [optional] 

## Example

```python
from iblai.models.scim_name import SCIMName

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMName from a JSON string
scim_name_instance = SCIMName.from_json(json)
# print the JSON string representation of the object
print(SCIMName.to_json())

# convert the object into a dict
scim_name_dict = scim_name_instance.to_dict()
# create an instance of SCIMName from a dict
scim_name_from_dict = SCIMName.from_dict(scim_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


