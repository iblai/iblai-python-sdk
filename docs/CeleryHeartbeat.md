# CeleryHeartbeat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**CeleryHeartbeatStatusEnum**](CeleryHeartbeatStatusEnum.md) |  | 
**message** | **str** |  | 

## Example

```python
from iblai.models.celery_heartbeat import CeleryHeartbeat

# TODO update the JSON string below
json = "{}"
# create an instance of CeleryHeartbeat from a JSON string
celery_heartbeat_instance = CeleryHeartbeat.from_json(json)
# print the JSON string representation of the object
print(CeleryHeartbeat.to_json())

# convert the object into a dict
celery_heartbeat_dict = celery_heartbeat_instance.to_dict()
# create an instance of CeleryHeartbeat from a dict
celery_heartbeat_from_dict = CeleryHeartbeat.from_dict(celery_heartbeat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


