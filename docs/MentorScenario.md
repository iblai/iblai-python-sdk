# MentorScenario


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** |  | [optional] 
**name** | **str** |  | 
**prompts** | [**List[MentorScenarioPrompt]**](MentorScenarioPrompt.md) |  | 

## Example

```python
from iblai.models.mentor_scenario import MentorScenario

# TODO update the JSON string below
json = "{}"
# create an instance of MentorScenario from a JSON string
mentor_scenario_instance = MentorScenario.from_json(json)
# print the JSON string representation of the object
print(MentorScenario.to_json())

# convert the object into a dict
mentor_scenario_dict = mentor_scenario_instance.to_dict()
# create an instance of MentorScenario from a dict
mentor_scenario_from_dict = MentorScenario.from_dict(mentor_scenario_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


