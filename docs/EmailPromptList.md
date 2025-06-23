# EmailPromptList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**sender_email** | **str** |  | 
**sender_name** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**content_summary** | **str** |  | [readonly] 
**mentor_name** | **str** |  | [optional] 
**mentor_email** | **str** |  | 
**is_processed** | **bool** |  | [optional] 
**inserted_at** | **str** |  | [readonly] 

## Example

```python
from iblai.models.email_prompt_list import EmailPromptList

# TODO update the JSON string below
json = "{}"
# create an instance of EmailPromptList from a JSON string
email_prompt_list_instance = EmailPromptList.from_json(json)
# print the JSON string representation of the object
print(EmailPromptList.to_json())

# convert the object into a dict
email_prompt_list_dict = email_prompt_list_instance.to_dict()
# create an instance of EmailPromptList from a dict
email_prompt_list_from_dict = EmailPromptList.from_dict(email_prompt_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


