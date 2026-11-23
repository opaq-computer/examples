import os

import anthropic

client = anthropic.Anthropic(base_url="https://opaq.computer", api_key=os.environ["OPAQ_API_KEY"])

msg = client.messages.create(
    model="claude-sonnet-5.5",
    max_tokens=512,
    messages=[{"role": "user", "content": "Hello from the Messages API."}],
)
print(msg.content[0].text)
