# UserSentimentCountView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | 
**sentiment_count** | **int** |  | 

## Example

```python
from iblai.models.user_sentiment_count_view import UserSentimentCountView

# TODO update the JSON string below
json = "{}"
# create an instance of UserSentimentCountView from a JSON string
user_sentiment_count_view_instance = UserSentimentCountView.from_json(json)
# print the JSON string representation of the object
print(UserSentimentCountView.to_json())

# convert the object into a dict
user_sentiment_count_view_dict = user_sentiment_count_view_instance.to_dict()
# create an instance of UserSentimentCountView from a dict
user_sentiment_count_view_from_dict = UserSentimentCountView.from_dict(user_sentiment_count_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


