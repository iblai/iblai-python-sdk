# PortalUrlResponse

Response containing a Stripe customer portal URL for subscription management.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portal_url** | **str** | Stripe customer portal URL. | 

## Example

```python
from iblai.models.portal_url_response import PortalUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PortalUrlResponse from a JSON string
portal_url_response_instance = PortalUrlResponse.from_json(json)
# print the JSON string representation of the object
print(PortalUrlResponse.to_json())

# convert the object into a dict
portal_url_response_dict = portal_url_response_instance.to_dict()
# create an instance of PortalUrlResponse from a dict
portal_url_response_from_dict = PortalUrlResponse.from_dict(portal_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


