## Assumptions
- Inputs should be positive integers (0 is not allowed as it does not make sense in terms of dimension/mass)

## Decisions
- Use only stdlib packages, to make it simple
    - e.g., pydantic could be used for data validation, but simple `isinstance` calls were used instead
    - e.g., pytest could be used for testing, but pure functions + `assert` calls were used instead

## Running the program
1. Edit input.json
2. run main.py through `python main.py` or `python3 main.py` (remember to cd into the repository's root directory)

## Running tests
1. run tests.py through `python tests.py` or `python3 tests.py` (remember to cd into the repository's root directory)