# MentorSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **float** |  | 
**summary** | **str** |  | 
**tags** | **List[str]** |  | 

## Example

```python
from iblai.models.mentor_summary import MentorSummary

# TODO update the JSON string below
json = "{}"
# create an instance of MentorSummary from a JSON string
mentor_summary_instance = MentorSummary.from_json(json)
# print the JSON string representation of the object
print(MentorSummary.to_json())

# convert the object into a dict
mentor_summary_dict = mentor_summary_instance.to_dict()
# create an instance of MentorSummary from a dict
mentor_summary_from_dict = MentorSummary.from_dict(mentor_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


