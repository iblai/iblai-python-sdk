# StripeConnectDashboardLink

Serializer for Express Dashboard link response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_url** | **str** |  | 

## Example

```python
from iblai.models.stripe_connect_dashboard_link import StripeConnectDashboardLink

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectDashboardLink from a JSON string
stripe_connect_dashboard_link_instance = StripeConnectDashboardLink.from_json(json)
# print the JSON string representation of the object
print(StripeConnectDashboardLink.to_json())

# convert the object into a dict
stripe_connect_dashboard_link_dict = stripe_connect_dashboard_link_instance.to_dict()
# create an instance of StripeConnectDashboardLink from a dict
stripe_connect_dashboard_link_from_dict = StripeConnectDashboardLink.from_dict(stripe_connect_dashboard_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


