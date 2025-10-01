# SetStudentLLMAccess

Serializer for setting student LLM access permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform key where the LLM access should be set | 
**llm_resources** | **List[str]** | List of LLM resource paths. Format: [&#39;llms/openai/models/gpt-4&#39;, &#39;llms/openai/&#39;, &#39;llms/&#39;]. Shorter paths grant access to all sub-resources. | 

## Example

```python
from iblai.models.set_student_llm_access import SetStudentLLMAccess

# TODO update the JSON string below
json = "{}"
# create an instance of SetStudentLLMAccess from a JSON string
set_student_llm_access_instance = SetStudentLLMAccess.from_json(json)
# print the JSON string representation of the object
print(SetStudentLLMAccess.to_json())

# convert the object into a dict
set_student_llm_access_dict = set_student_llm_access_instance.to_dict()
# create an instance of SetStudentLLMAccess from a dict
set_student_llm_access_from_dict = SetStudentLLMAccess.from_dict(set_student_llm_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


