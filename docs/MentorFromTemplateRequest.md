# MentorFromTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** |  | 
**new_mentor_name** | **str** |  | 

## Example

```python
from iblai.models.mentor_from_template_request import MentorFromTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MentorFromTemplateRequest from a JSON string
mentor_from_template_request_instance = MentorFromTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(MentorFromTemplateRequest.to_json())

# convert the object into a dict
mentor_from_template_request_dict = mentor_from_template_request_instance.to_dict()
# create an instance of MentorFromTemplateRequest from a dict
mentor_from_template_request_from_dict = MentorFromTemplateRequest.from_dict(mentor_from_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


