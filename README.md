# iblai

API for [ibl.ai](https://ibl.ai/) — a generative AI backend as a service for educators.


## Requirements

Python 3.7+

## Installation & Usage
### pip install

To install the API client library, simply execute:

```sh
pip install iblai
```

Then import the package:
```python
import iblai
```


## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

### Adding LLM credentials

```python
from iblai.helpers import add_llm_credential

base_url = "https://base.manager.iblai.app/"
api_token = "<MY_ACCESS_TOKEN>"

credential_name = "openai"
credential_value = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
tenant = "new-platform"

add_llm_credential(credential_name, credential_value, tenant, api_token, base_url)
```

### Chatting with a mentor

```python
from iblai.helpers import (
    create_mentor,
    upload_document_to_mentor,
    wait_for_document_training_to_complete,
    create_chat_session,
    chat_with_mentor_async
)

tenant = "new-platform"
username = "my-user"
base_url = "https://base.manager.iblai.app/"
asgi_base_url = "wss://asgi.data.iblai.app"
api_token = "<MY_ACCESS_TOKEN>"

mentor_name = "My New Mentor"
mentor_settings = {
    "new_mentor_name": mentor_name,
    "display_name": mentor_name,
}

mentor_data = await create_mentor(tenant, username, mentor_settings, api_token, base_url)
await upload_document_to_mentor(
    mentor_name=mentor_name,
    file_path="doc.pdf",
    tenant, username, api_token, base_url
)

await wait_for_document_training_to_complete(mentor_name, tenant, username, api_token, base_url)

session_id = await create_chat_session(mentor_name, tenant, username, base_url)
await chat_with_mentor_async(
    prompt, session_id, mentor_name, tenant, username, api_token, asgi_base_url
)
```


### Inviting a user


```python
from iblai.helpers import invite_user_to_platform

base_url = "https://base.manager.iblai.app/"
api_token = "<MY_ACCESS_TOKEN>"

tenant = "new-platform"
email = "new-student@example.com"

invite_user_to_platform(tenant, email, api_token, base_url)
```
