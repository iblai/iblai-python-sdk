# CreditAccountAutoRechargeUpdate

Partial update for CreditAccount auto-recharge fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_recharge_threshold_usd** | **decimal.Decimal** | Set the balance threshold for auto-recharge (must be non-negative). | [optional] 
**auto_recharge_amount_usd** | **decimal.Decimal** | Set the amount to recharge (min $0.50). | [optional] 
**auto_recharge_enabled** | **bool** | Enable or disable auto-recharge. | [optional] 
**auto_recharge_spending_limit_usd** | **decimal.Decimal** | Cap on auto-recharge + manual top-up per 30-day period (user USD). 0 &#x3D; unlimited. When &gt; 0, backend sets recharge amount to 20% of limit (min $0.50). | [optional] 
**platform_key** | **str** | The platform key to update settings for (read-only in update context). | [readonly] 

## Example

```python
from iblai.models.credit_account_auto_recharge_update import CreditAccountAutoRechargeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CreditAccountAutoRechargeUpdate from a JSON string
credit_account_auto_recharge_update_instance = CreditAccountAutoRechargeUpdate.from_json(json)
# print the JSON string representation of the object
print(CreditAccountAutoRechargeUpdate.to_json())

# convert the object into a dict
credit_account_auto_recharge_update_dict = credit_account_auto_recharge_update_instance.to_dict()
# create an instance of CreditAccountAutoRechargeUpdate from a dict
credit_account_auto_recharge_update_from_dict = CreditAccountAutoRechargeUpdate.from_dict(credit_account_auto_recharge_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


