# PaginatedPlatformInvitation

Response serializer for paginated platform invitation list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[PlatformInvitationDetail]**](PlatformInvitationDetail.md) | List of platform invitations | 

## Example

```python
from iblai.models.paginated_platform_invitation import PaginatedPlatformInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPlatformInvitation from a JSON string
paginated_platform_invitation_instance = PaginatedPlatformInvitation.from_json(json)
# print the JSON string representation of the object
print(PaginatedPlatformInvitation.to_json())

# convert the object into a dict
paginated_platform_invitation_dict = paginated_platform_invitation_instance.to_dict()
# create an instance of PaginatedPlatformInvitation from a dict
paginated_platform_invitation_from_dict = PaginatedPlatformInvitation.from_dict(paginated_platform_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


