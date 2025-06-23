# EmailPromptDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**inserted_at** | **str** |  | [readonly] 
**sender_email** | **str** |  | 
**sender_name** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**content** | **str** |  | 
**mentor_name** | **str** |  | [optional] 
**mentor_email** | **str** |  | 
**is_processed** | **bool** |  | [optional] 
**mentor_response** | **str** |  | [optional] 
**send_status** | **str** |  | [optional] 

## Example

```python
from iblai.models.email_prompt_detail import EmailPromptDetail

# TODO update the JSON string below
json = "{}"
# create an instance of EmailPromptDetail from a JSON string
email_prompt_detail_instance = EmailPromptDetail.from_json(json)
# print the JSON string representation of the object
print(EmailPromptDetail.to_json())

# convert the object into a dict
email_prompt_detail_dict = email_prompt_detail_instance.to_dict()
# create an instance of EmailPromptDetail from a dict
email_prompt_detail_from_dict = EmailPromptDetail.from_dict(email_prompt_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


