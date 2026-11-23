# Claude Code

Point Claude Code at Opaq and it runs on your sealed balance.

```bash
export ANTHROPIC_BASE_URL=https://opaq.computer
export ANTHROPIC_API_KEY=$OPAQ_API_KEY
claude --model claude-sonnet-5.5
```

To make it permanent for one project, add to `.claude/settings.json`:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://opaq.computer"
  }
}
```

and keep the key in your shell (`ANTHROPIC_API_KEY`), never in the repository.

Any model of the catalog can be used, by bare id (`claude-sonnet-5.5`) or full id (`anthropic/claude-sonnet-5.5`).
