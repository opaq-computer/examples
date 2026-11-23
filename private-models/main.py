# Only models served inside a hardware enclave (TEE). Their ids start with "private/".
import json
import os
import urllib.request

from openai import OpenAI

with urllib.request.urlopen("https://opaq.computer/v1/models") as r:
    enclave = [m for m in json.load(r)["data"] if m.get("private")]

for m in enclave:
    print(f'{m["id"]:<48} ${m["pricing"]["prompt_per_mtok"]:.4f} / ${m["pricing"]["completion_per_mtok"]:.4f} per 1M tokens')

client = OpenAI(base_url="https://opaq.computer/v1", api_key=os.environ["OPAQ_API_KEY"])
r = client.chat.completions.create(model=enclave[0]["id"], messages=[{"role": "user", "content": "Hello from inside the enclave."}])
print(r.choices[0].message.content)
