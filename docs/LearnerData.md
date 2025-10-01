# LearnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courses** | [**List[CourseDetail]**](CourseDetail.md) |  | [optional] 
**programs** | [**List[ProgramDetail]**](ProgramDetail.md) |  | [optional] 
**pathways** | [**List[PathwayDetail]**](PathwayDetail.md) |  | [optional] 
**mentors** | [**List[MentorDetail]**](MentorDetail.md) |  | [optional] 
**skills** | [**SkillsDetail**](SkillsDetail.md) |  | [optional] 
**credentials** | [**List[Credential]**](Credential.md) |  | [optional] 
**time_spent** | [**TimeSpentDetail**](TimeSpentDetail.md) |  | [optional] 

## Example

```python
from iblai.models.learner_data import LearnerData

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerData from a JSON string
learner_data_instance = LearnerData.from_json(json)
# print the JSON string representation of the object
print(LearnerData.to_json())

# convert the object into a dict
learner_data_dict = learner_data_instance.to_dict()
# create an instance of LearnerData from a dict
learner_data_from_dict = LearnerData.from_dict(learner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


