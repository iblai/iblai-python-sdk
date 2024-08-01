# MentorDetailAnalytics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_mentors** | **int** |  | 
**active_mentors** | **int** |  | 
**total_questions_answered** | **int** |  | 
**total_ratings** | **int** |  | 

## Example

```python
from iblai.models.mentor_detail_analytics import MentorDetailAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of MentorDetailAnalytics from a JSON string
mentor_detail_analytics_instance = MentorDetailAnalytics.from_json(json)
# print the JSON string representation of the object
print(MentorDetailAnalytics.to_json())

# convert the object into a dict
mentor_detail_analytics_dict = mentor_detail_analytics_instance.to_dict()
# create an instance of MentorDetailAnalytics from a dict
mentor_detail_analytics_from_dict = MentorDetailAnalytics.from_dict(mentor_detail_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


