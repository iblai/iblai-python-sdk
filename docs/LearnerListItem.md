# LearnerListItem

Serializer for individual learner in the list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | 
**username** | **str** | Username | 
**email** | **str** | Email address | 
**name** | **str** | Display name | 
**is_active** | **bool** | Whether user is active | 
**platform_id** | **int** | Platform ID | 
**platform_name** | **str** | Platform name | 
**platform_key** | **str** | Platform key | 
**metrics** | [**LearnerMetrics**](LearnerMetrics.md) | Learner metrics | 
**first_activity** | **datetime** | First activity date | 
**last_activity** | **datetime** | Last activity date | 

## Example

```python
from iblai.models.learner_list_item import LearnerListItem

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerListItem from a JSON string
learner_list_item_instance = LearnerListItem.from_json(json)
# print the JSON string representation of the object
print(LearnerListItem.to_json())

# convert the object into a dict
learner_list_item_dict = learner_list_item_instance.to_dict()
# create an instance of LearnerListItem from a dict
learner_list_item_from_dict = LearnerListItem.from_dict(learner_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


