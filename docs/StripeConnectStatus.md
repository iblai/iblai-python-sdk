# StripeConnectStatus

Serializer for Connect account status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_account** | **bool** |  | 
**account_id** | **str** |  | [optional] 
**onboarding_complete** | **bool** |  | 
**charges_enabled** | **bool** |  | [optional] 
**payouts_enabled** | **bool** |  | [optional] 
**details_submitted** | **bool** |  | [optional] 
**commission_percent** | [**ItemTypeCommission**](ItemTypeCommission.md) |  | [optional] 
**is_ready_for_payments** | **bool** |  | [optional] 

## Example

```python
from iblai.models.stripe_connect_status import StripeConnectStatus

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectStatus from a JSON string
stripe_connect_status_instance = StripeConnectStatus.from_json(json)
# print the JSON string representation of the object
print(StripeConnectStatus.to_json())

# convert the object into a dict
stripe_connect_status_dict = stripe_connect_status_instance.to_dict()
# create an instance of StripeConnectStatus from a dict
stripe_connect_status_from_dict = StripeConnectStatus.from_dict(stripe_connect_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


