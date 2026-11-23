# Private models (TEE)

Lists the models served inside a hardware enclave, with no fallback to a regular provider, then calls one.

```bash
pip install openai
python main.py
```

Transit through the Opaq gateway is TLS, not end-to-end encryption. Details: [opaq.computer/security](https://opaq.computer/security).
