# StudentLLMAccessResponse

Serializer for student LLM access responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform key | 
**llm_resources** | **List[str]** | List of LLM resource paths that students can access. Format: [&#39;llms/openai/models/gpt-4&#39;, &#39;llms/openai/&#39;, &#39;llms/&#39;] | 

## Example

```python
from iblai.models.student_llm_access_response import StudentLLMAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StudentLLMAccessResponse from a JSON string
student_llm_access_response_instance = StudentLLMAccessResponse.from_json(json)
# print the JSON string representation of the object
print(StudentLLMAccessResponse.to_json())

# convert the object into a dict
student_llm_access_response_dict = student_llm_access_response_instance.to_dict()
# create an instance of StudentLLMAccessResponse from a dict
student_llm_access_response_from_dict = StudentLLMAccessResponse.from_dict(student_llm_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


