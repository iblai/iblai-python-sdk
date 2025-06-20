# StripeBillingPageIdentifierResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publishable_key** | **str** |  | 
**pricing_table_id** | **str** |  | 
**pricing_table_js** | **object** |  | 
**payment_link_id** | **str** |  | 
**payment_link_url** | **str** |  | 
**customer_email** | **str** |  | 
**client_reference_id** | **str** |  | 

## Example

```python
from iblai.models.stripe_billing_page_identifier_response import StripeBillingPageIdentifierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StripeBillingPageIdentifierResponse from a JSON string
stripe_billing_page_identifier_response_instance = StripeBillingPageIdentifierResponse.from_json(json)
# print the JSON string representation of the object
print(StripeBillingPageIdentifierResponse.to_json())

# convert the object into a dict
stripe_billing_page_identifier_response_dict = stripe_billing_page_identifier_response_instance.to_dict()
# create an instance of StripeBillingPageIdentifierResponse from a dict
stripe_billing_page_identifier_response_from_dict = StripeBillingPageIdentifierResponse.from_dict(stripe_billing_page_identifier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


