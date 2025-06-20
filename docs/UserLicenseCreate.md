# UserLicenseCreate

Request serializer for UserLicenseCreateView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform to create a license for | 
**platform_org** | **str** | The organization identifier for the platform | [optional] 
**name** | **str** | Display name for the license | [optional] 
**count** | **int** | Number of seats purchased | [optional] [default to 0]
**started** | **datetime** | Date when license should begin | [optional] 
**expired** | **datetime** | Date when license should expire | [optional] 
**active** | **bool** | Whether the license is active | [optional] [default to True]
**metadata** | **Dict[str, object]** | Additional license metadata | [optional] 
**enrollment_config** | **Dict[str, object]** | Additional enrollment configuration | [optional] 
**source** | **str** | Source identifier | [optional] 
**external_id** | **str** | External identifier (must be unique) | [optional] 
**transaction_id** | **str** | Transaction identifier for tracking | [optional] 
**change_type** | **str** | Type of change being made | [optional] [default to 'create']

## Example

```python
from iblai.models.user_license_create import UserLicenseCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserLicenseCreate from a JSON string
user_license_create_instance = UserLicenseCreate.from_json(json)
# print the JSON string representation of the object
print(UserLicenseCreate.to_json())

# convert the object into a dict
user_license_create_dict = user_license_create_instance.to_dict()
# create an instance of UserLicenseCreate from a dict
user_license_create_from_dict = UserLicenseCreate.from_dict(user_license_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


