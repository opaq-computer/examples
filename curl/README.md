# curl

```bash
curl https://opaq.computer/v1/chat/completions \
  -H "Authorization: Bearer $OPAQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"anthropic/claude-sonnet-5.5","messages":[{"role":"user","content":"Hello"}]}'
```

Streaming (server-sent events):

```bash
curl -N https://opaq.computer/v1/chat/completions \
  -H "Authorization: Bearer $OPAQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek/deepseek-v4.1-flash","stream":true,"messages":[{"role":"user","content":"Count to five."}]}'
```

The catalog, no key needed:

```bash
curl -s https://opaq.computer/v1/models | jq '.data[] | {id, prompt: .pricing.prompt_per_mtok, completion: .pricing.completion_per_mtok}'
```
