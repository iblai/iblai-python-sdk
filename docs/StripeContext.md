# StripeContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publishable_key** | **str** |  | 
**pricing_table_id** | **str** |  | 
**pricing_table_js** | **object** |  | 
**payment_link_id** | **str** |  | 
**payment_link_url** | **str** |  | 

## Example

```python
from iblai.models.stripe_context import StripeContext

# TODO update the JSON string below
json = "{}"
# create an instance of StripeContext from a JSON string
stripe_context_instance = StripeContext.from_json(json)
# print the JSON string representation of the object
print(StripeContext.to_json())

# convert the object into a dict
stripe_context_dict = stripe_context_instance.to_dict()
# create an instance of StripeContext from a dict
stripe_context_from_dict = StripeContext.from_dict(stripe_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


