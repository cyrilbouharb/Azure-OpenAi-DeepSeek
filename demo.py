# azure ai inference api

import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

client = ChatCompletionsClient(
    endpoint="https://DeepSeek-R1-obuij.eastus2.models.ai.azure.com",
    credential=AzureKeyCredential(os.environ["AZUREAI_ENDPOINT_KEY"]),
)
print(client.get_model_info())

model_info = client.get_model_info()
print("Model Name:", model_info.model_name)
print("Model Type:", model_info.model_type)
print("Model Provider Name:", model_info.model_provider_name)

payload = {
    "messages": [
        {
            "role": "user",
            "content": "Talk about Kuwait 2035 AI vision?"
        },
        {
            "role": "assistant",
            "content": "Kuwait has a long-term development strategy called \"New Kuwait 2035\" (Kuwait Vision 2035). This vision aims to transform Kuwait into a leading financial and commercial hub while reducing its dependence on oil revenues and enhancing its global competitiveness.\n\nKey Pillars of Kuwait Vision 2035 (New Kuwait)\n\nThe vision is built around seven strategic pillars:\n\n- Effective Government – Improve governance, transparency, and efficiency in public administration.\n- Diverse & Sustainable Economy – Reduce reliance on oil and boost private sector participation.\n-"
        },
        {
            "role": "user",
            "content": "That's good to know. What else?"
        }
    ],
    "max_tokens": 2048
}
response = client.complete(payload)
print("Response: ",response.choices[0].message.content)
print("Model:", response.model)
print("Usage:")
print("Prompt tokens:", response.usage.prompt_tokens)
print("Total tokens:", response.usage.total_tokens)
print("Completion tokens:", response.usage.completion_tokens)