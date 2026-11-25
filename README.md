Before contributing to this repo, please make sure that the following git precommit hook is created at `.git/hooks/pre-commit` to keep the style consistent.

```bash
#!/bin/sh
uv run ruff check --fix .
```