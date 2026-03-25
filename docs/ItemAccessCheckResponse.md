# ItemAccessCheckResponse

Response for the generic item access check endpoint.  Mirrors :class:`PaymentCheckResult` but only exposes the fields relevant to API consumers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_access** | **bool** | True if the user can access the item. | 
**item_type** | [**ItemType3e2Enum**](ItemType3e2Enum.md) | Item type that was checked (e.g. &#39;mentor&#39;).  * &#x60;mentor&#x60; - mentor * &#x60;course&#x60; - course * &#x60;program&#x60; - program * &#x60;pathway&#x60; - pathway | 
**item_id** | **str** | ID of the item that was checked. | 
**reason** | **str** | Machine-readable reason for the access decision (e.g. &#39;active&#39;, &#39;no_paywall&#39;, &#39;no_subscription&#39;). | 
**requires_payment** | **bool** | True if the user must pay to gain access. | 
**pricing_available** | **bool** | True if pricing tiers are available for purchase. | 
**pricing** | **object** | Pricing details when access is denied (item name, tiers, amounts). | [optional] 
**subscription** | [**ItemSubscription**](ItemSubscription.md) | Active subscription details when the user has access via subscription. | [optional] 

## Example

```python
from iblai.models.item_access_check_response import ItemAccessCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAccessCheckResponse from a JSON string
item_access_check_response_instance = ItemAccessCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ItemAccessCheckResponse.to_json())

# convert the object into a dict
item_access_check_response_dict = item_access_check_response_instance.to_dict()
# create an instance of ItemAccessCheckResponse from a dict
item_access_check_response_from_dict = ItemAccessCheckResponse.from_dict(item_access_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


