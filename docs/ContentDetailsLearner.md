# ContentDetailsLearner

Serializer for individual learner entries in content details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Learner identifier | 
**username** | **str** | Learner username | 
**email** | **str** | Learner email | 
**name** | **str** | Learner display name | 
**enrollment_date** | **datetime** | Date the learner enrolled in the content | 
**completion_status** | **str** | Completion status for the learner | 
**completion_percentage** | **float** | Learner completion percentage | 
**last_activity** | **datetime** | Last activity timestamp for the learner | 
**rating** | **float** | Learner rating for the content, if available | 
**review** | **str** | Learner review content, if available | 
**details** | **Dict[str, object]** | Additional learner-specific metadata | [optional] 

## Example

```python
from iblai.models.content_details_learner import ContentDetailsLearner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDetailsLearner from a JSON string
content_details_learner_instance = ContentDetailsLearner.from_json(json)
# print the JSON string representation of the object
print(ContentDetailsLearner.to_json())

# convert the object into a dict
content_details_learner_dict = content_details_learner_instance.to_dict()
# create an instance of ContentDetailsLearner from a dict
content_details_learner_from_dict = ContentDetailsLearner.from_dict(content_details_learner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


