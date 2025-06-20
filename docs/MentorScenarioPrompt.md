# MentorScenarioPrompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** |  | 
**content** | **str** |  | 
**icon** | **str** |  | [optional] 

## Example

```python
from iblai.models.mentor_scenario_prompt import MentorScenarioPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of MentorScenarioPrompt from a JSON string
mentor_scenario_prompt_instance = MentorScenarioPrompt.from_json(json)
# print the JSON string representation of the object
print(MentorScenarioPrompt.to_json())

# convert the object into a dict
mentor_scenario_prompt_dict = mentor_scenario_prompt_instance.to_dict()
# create an instance of MentorScenarioPrompt from a dict
mentor_scenario_prompt_from_dict = MentorScenarioPrompt.from_dict(mentor_scenario_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


