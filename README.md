# iblai

API for [ibl.ai](https://ibl.ai/) — a generative AI backend as a service for educators.


## Requirements

Python 3.9+

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

### Authentication

The SDK requires a **Platform API Key** for authentication. This is different from JWT tokens or user session tokens.

**How to obtain your API token:**
1. Log in to your ibl.ai admin dashboard
2. Navigate to **Settings** → **API Keys**
3. Create or copy an existing Platform API Key

**Important notes:**
- The API key is **tenant-specific** and **user-specific**
- The SDK automatically uses the `Api-Token` authorization header format
- Token format: 64-character hexadecimal string (e.g., `5223a68d...cf29`)

```python
# Platform API Key - obtain from ibl.ai dashboard → Settings → API Keys
# Must be associated with the tenant and username you're using
api_token = "your-64-character-platform-api-key"
```

### Adding LLM credentials

```python
from iblai.helpers import add_llm_credential

base_url = "https://base.manager.iblai.app/"
api_token = "your-platform-api-key"  # Platform API Key from dashboard

credential_name = "openai"
credential_value = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
tenant = "new-platform"

add_llm_credential(credential_name, credential_value, tenant, api_token, base_url)
```

### Chatting with a mentor

```python
import asyncio
from iblai.helpers import (
    create_mentor,
    upload_document_to_mentor,
    wait_for_document_training_to_complete,
    create_chat_session,
    chat_with_mentor_async
)

async def main():
    tenant = "new-platform"
    username = "my-user"
    base_url = "https://base.manager.iblai.app/"
    asgi_base_url = "wss://asgi.data.iblai.app"
    api_token = "your-platform-api-key"  # Platform API Key from dashboard

    mentor_name = "My New Mentor"
    # Available template names: "ai-mentor", "mentorAI"
    # Templates define default settings, prompts, and behaviors for the mentor
    mentor_settings = {
        "template_name": "ai-mentor",  # Required: the template to base the mentor on
        "new_mentor_name": mentor_name,
        "display_name": mentor_name,
    }

    mentor_data = await create_mentor(tenant, username, mentor_settings, api_token, base_url)

    # Extract unique_id - required for document operations and chat
    mentor_unique_id = mentor_data["unique_id"]

    await upload_document_to_mentor(
        mentor_name=mentor_unique_id,  # Must use unique_id, not the display name
        file_path="doc.pdf",
        tenant=tenant,
        username=username,
        api_token=api_token,
        base_url=base_url
    )

    await wait_for_document_training_to_complete(
        mentor_name=mentor_unique_id,
        tenant=tenant,
        username=username,
        api_token=api_token,
        base_url=base_url
    )

    session_id = await create_chat_session(
        mentor_name=mentor_unique_id,
        tenant=tenant,
        username=username,
        base_url=base_url
    )

    prompt = "What is the main topic of the document?"
    async for token in chat_with_mentor_async(
        prompt, session_id, mentor_unique_id, tenant, username, api_token, asgi_base_url
    ):
        print(token, end="")

asyncio.run(main())
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

### Error Handling

Common errors and their solutions:

| HTTP Status | Error Message | Cause | Solution |
|-------------|---------------|-------|----------|
| 401 | `{"detail":"Invalid token."}` | Invalid API token or token doesn't match tenant/username | Verify your Platform API Key is correct and associated with the tenant/user |
| 400 | `{"template_name":["This field is required."]}` | Missing `template_name` in mentor_settings | Add `"template_name": "ai-mentor"` to your settings |
| 400 | `{"error":"Document pathway (name) is not a valid mentor unique id"}` | Using mentor display name instead of unique_id | Use `mentor_data["unique_id"]` for document operations |
| 400 | `{"error":"Template mentor X not found."}` | Invalid template_name value | Use a valid template: `"ai-mentor"` or `"mentorAI"` |

**Example with error handling:**

```python
mentor_data = await create_mentor(
    tenant=tenant,
    username=username,
    settings=mentor_settings,
    api_token=api_token,
    base_url=base_url,
)

if mentor_data is None:
    print("Failed to create mentor - check API token, tenant, username, and template_name")
    return

# Proceed with the unique_id
mentor_unique_id = mentor_data["unique_id"]
print(f"Mentor created successfully: {mentor_unique_id}")
```
