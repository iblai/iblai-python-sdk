# UserLicenseDetail

Response serializer for user license details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the license | 
**created** | **datetime** | When the license was created | 
**started** | **datetime** | When the license becomes active | 
**expired** | **datetime** | When the license expires | 
**name** | **str** | The display name of the license | 
**count** | **int** | The number of seats purchased | 
**active** | **bool** | Whether the license is active | 
**metadata** | **Dict[str, object]** | Additional license metadata | 
**source** | **str** | The source identifier for the license | 
**external_id** | **str** | External identifier for the license | 
**platform_key** | **str** | The platform key associated with the license | 
**usage_count** | **int** | Number of assignments using this license | [optional] [default to 0]
**assignments** | **object** | Assignment counts by status (only included in verbose mode) | [optional] 

## Example

```python
from iblai.models.user_license_detail import UserLicenseDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UserLicenseDetail from a JSON string
user_license_detail_instance = UserLicenseDetail.from_json(json)
# print the JSON string representation of the object
print(UserLicenseDetail.to_json())

# convert the object into a dict
user_license_detail_dict = user_license_detail_instance.to_dict()
# create an instance of UserLicenseDetail from a dict
user_license_detail_from_dict = UserLicenseDetail.from_dict(user_license_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


