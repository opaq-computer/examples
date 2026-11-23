import os

from openai import OpenAI

client = OpenAI(base_url="https://opaq.computer/v1", api_key=os.environ["OPAQ_API_KEY"])

r = client.chat.completions.create(
    model="anthropic/claude-sonnet-5.5",
    messages=[{"role": "user", "content": "In one sentence, why does private inference matter?"}],
)
print(r.choices[0].message.content)
print(f"{r.usage.prompt_tokens} in, {r.usage.completion_tokens} out")
