# LtiLaunchGate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_keys** | **List[str]** |  | [optional] 
**allowed_courses** | **List[str]** |  | [optional] 
**allow_all_within_org** | **bool** | If True, a target_link_uri will work with any content within this org | [optional] [default to False]

## Example

```python
from iblai.models.lti_launch_gate import LtiLaunchGate

# TODO update the JSON string below
json = "{}"
# create an instance of LtiLaunchGate from a JSON string
lti_launch_gate_instance = LtiLaunchGate.from_json(json)
# print the JSON string representation of the object
print(LtiLaunchGate.to_json())

# convert the object into a dict
lti_launch_gate_dict = lti_launch_gate_instance.to_dict()
# create an instance of LtiLaunchGate from a dict
lti_launch_gate_from_dict = LtiLaunchGate.from_dict(lti_launch_gate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


