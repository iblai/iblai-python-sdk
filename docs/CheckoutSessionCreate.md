# CheckoutSessionCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_id** | **str** |  | 
**success_url** | **str** |  | [optional] 
**cancel_url** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from iblai.models.checkout_session_create import CheckoutSessionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionCreate from a JSON string
checkout_session_create_instance = CheckoutSessionCreate.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionCreate.to_json())

# convert the object into a dict
checkout_session_create_dict = checkout_session_create_instance.to_dict()
# create an instance of CheckoutSessionCreate from a dict
checkout_session_create_from_dict = CheckoutSessionCreate.from_dict(checkout_session_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


