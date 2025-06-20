# EmailPromptSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_emails** | **int** |  | [readonly] 
**replied_emails** | **int** |  | [readonly] 
**pending_emails** | **int** |  | [readonly] 

## Example

```python
from iblai.models.email_prompt_summary import EmailPromptSummary

# TODO update the JSON string below
json = "{}"
# create an instance of EmailPromptSummary from a JSON string
email_prompt_summary_instance = EmailPromptSummary.from_json(json)
# print the JSON string representation of the object
print(EmailPromptSummary.to_json())

# convert the object into a dict
email_prompt_summary_dict = email_prompt_summary_instance.to_dict()
# create an instance of EmailPromptSummary from a dict
email_prompt_summary_from_dict = EmailPromptSummary.from_dict(email_prompt_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


