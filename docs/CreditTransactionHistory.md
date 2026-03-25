# CreditTransactionHistory

Serializer for user-facing transaction history. NEVER exposes internal USD amounts (amount_usd, usd_balance_*).  - payment_amount_usd: only shown for ``add`` transactions (real user payment). - description: user-friendly label derived from service_name/transaction_type. - service_name is excluded from the response (internal detail).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**transaction_type** | [**TransactionTypeEnum**](TransactionTypeEnum.md) |  | 
**status** | [**CreditTransactionHistoryStatusEnum**](CreditTransactionHistoryStatusEnum.md) |  | [optional] 
**payment_amount_usd** | **str** |  | [readonly] 
**credits_amount** | **str** |  | [readonly] 
**credits_balance_after** | **str** |  | [readonly] 
**description** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.credit_transaction_history import CreditTransactionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of CreditTransactionHistory from a JSON string
credit_transaction_history_instance = CreditTransactionHistory.from_json(json)
# print the JSON string representation of the object
print(CreditTransactionHistory.to_json())

# convert the object into a dict
credit_transaction_history_dict = credit_transaction_history_instance.to_dict()
# create an instance of CreditTransactionHistory from a dict
credit_transaction_history_from_dict = CreditTransactionHistory.from_dict(credit_transaction_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


