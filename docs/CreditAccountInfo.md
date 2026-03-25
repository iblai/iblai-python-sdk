# CreditAccountInfo

Credit account information API response (GET).  Display balance (has_credits, account_id, available_credits) and auto-recharge preferences.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_credits** | **bool** | True if the account has any credits (or infinite credits). | [readonly] 
**account_id** | **str** | The unique identifier of the credit account. | [readonly] 
**available_credits** | **decimal.Decimal** | The current available credit balance in USD. | [readonly] 
**auto_recharge_threshold_usd** | **decimal.Decimal** | The balance threshold below which auto-recharge is triggered. | [readonly] 
**auto_recharge_amount_usd** | **decimal.Decimal** | The amount in USD to recharge when the threshold is reached. | [readonly] 
**auto_recharge_enabled** | **bool** | True if auto-recharge is currently enabled for this account. | [readonly] 
**auto_recharge_last_triggered_at** | **datetime** | The timestamp when auto-recharge was last successfully triggered. | [readonly] 
**platform_key** | **str** | The platform key associated with this account (if applicable). | [readonly] 
**pricing_table** | **object** | Stripe pricing table details for topping up credits. | [readonly] 
**free_trial** | **bool** | True if the account is on the free trial plan (no paid plan purchased yet). | [readonly] 
**current_plan** | **str** | Current plan identifier, e.g. &#39;free_trial&#39; or Stripe product SKU. | [readonly] 
**previous_plan** | **str** | Previous plan before the last purchase. | [readonly] 
**can_use_auto_recharge** | **bool** | True if the current plan is not free_trial (paid plans can use auto-recharge). | [readonly] 
**has_payment_method** | **bool** | True if the user has a payment method on file (can use manual top-up and auto-recharge). | [readonly] 
**message** | **str** | Message explaining why credits are insufficient (only present when has_credits is False). | [readonly] 

## Example

```python
from iblai.models.credit_account_info import CreditAccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreditAccountInfo from a JSON string
credit_account_info_instance = CreditAccountInfo.from_json(json)
# print the JSON string representation of the object
print(CreditAccountInfo.to_json())

# convert the object into a dict
credit_account_info_dict = credit_account_info_instance.to_dict()
# create an instance of CreditAccountInfo from a dict
credit_account_info_from_dict = CreditAccountInfo.from_dict(credit_account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


