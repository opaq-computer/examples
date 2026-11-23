<p align="center"><img src="https://raw.githubusercontent.com/opaq-computer/brand/main/logo/opaq-logo-512.png" width="96" alt="Opaq" /></p>

<h1 align="center">Opaq examples</h1>

<p align="center">Run your tools on <a href="https://opaq.computer">Opaq</a>: private AI inference on Solana, paid from a sealed balance. Each folder is a working setup you can copy.</p>

| Example | Stack |
|---|---|
| [curl](curl/) | Raw HTTP, streaming |
| [python-openai](python-openai/) | Official OpenAI Python SDK |
| [typescript-openai](typescript-openai/) | Official OpenAI Node SDK |
| [anthropic-sdk](anthropic-sdk/) | Official Anthropic SDK (Messages API) |
| [claude-code](claude-code/) | Claude Code on your Opaq balance |
| [cursor](cursor/) | Cursor with a custom OpenAI base URL |
| [langchain](langchain/) | LangChain `ChatOpenAI` |
| [vercel-ai-sdk](vercel-ai-sdk/) | Vercel AI SDK |
| [private-models](private-models/) | Only models served inside a hardware enclave (TEE) |

## Before you start

1. Open the [console](https://opaq.computer/console) and sign in with your Solana wallet.
2. Seal a top-up: a private transfer through Solana Privacy Rings.
3. Create an API key and export it:

```bash
export OPAQ_API_KEY=opaq_sk_...
```

Model ids come from the live catalog: [opaq.computer/models](https://opaq.computer/models) or `GET https://opaq.computer/v1/models`.

[Website](https://opaq.computer) · [Docs](https://opaq.computer/docs) · [Security](https://opaq.computer/security) · [Changelog](https://opaq.computer/changelog) · [X](https://x.com/OpaqPrivacy)
