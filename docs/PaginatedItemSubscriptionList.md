# PaginatedItemSubscriptionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ItemSubscription]**](ItemSubscription.md) |  | 

## Example

```python
from iblai.models.paginated_item_subscription_list import PaginatedItemSubscriptionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedItemSubscriptionList from a JSON string
paginated_item_subscription_list_instance = PaginatedItemSubscriptionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedItemSubscriptionList.to_json())

# convert the object into a dict
paginated_item_subscription_list_dict = paginated_item_subscription_list_instance.to_dict()
# create an instance of PaginatedItemSubscriptionList from a dict
paginated_item_subscription_list_from_dict = PaginatedItemSubscriptionList.from_dict(paginated_item_subscription_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


