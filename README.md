# CSV processor

Independent variant for the academic experiment. The application and tests contain no hostname collection. The only experimental difference is the verification comment beside the `xfail` test.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Expected result: `1 passed, 1 xfailed`.
