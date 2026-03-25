# ItemSubscriptionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** |  | [readonly] 
**user_id** | **int** |  | [readonly] 
**username** | **str** |  | [readonly] 
**email** | **str** |  | [readonly] 
**item_type** | [**ItemType40fEnum**](ItemType40fEnum.md) | Type of item being subscribed to  * &#x60;mentor&#x60; - Mentor * &#x60;course&#x60; - Course * &#x60;program&#x60; - Program * &#x60;pathway&#x60; - Pathway | 
**item_id** | **str** | Identifier for the item | 
**item_name** | **str** |  | [readonly] 
**status** | [**Status0e3Enum**](Status0e3Enum.md) | Current subscription status  * &#x60;active&#x60; - Active * &#x60;free&#x60; - Free Tier * &#x60;grandfathered&#x60; - Grandfathered * &#x60;trialing&#x60; - Trialing * &#x60;past_due&#x60; - Past Due * &#x60;canceled&#x60; - Canceled * &#x60;incomplete&#x60; - Incomplete | [optional] 
**price** | [**ItemPrice**](ItemPrice.md) |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.item_subscription_list import ItemSubscriptionList

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSubscriptionList from a JSON string
item_subscription_list_instance = ItemSubscriptionList.from_json(json)
# print the JSON string representation of the object
print(ItemSubscriptionList.to_json())

# convert the object into a dict
item_subscription_list_dict = item_subscription_list_instance.to_dict()
# create an instance of ItemSubscriptionList from a dict
item_subscription_list_from_dict = ItemSubscriptionList.from_dict(item_subscription_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


