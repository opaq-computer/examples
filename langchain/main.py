import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="anthropic/claude-sonnet-5.5",
    base_url="https://opaq.computer/v1",
    api_key=os.environ["OPAQ_API_KEY"],
)
print(llm.invoke("Summarize what a sealed balance is, in two sentences.").content)
