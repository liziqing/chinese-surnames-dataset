# Contributing

Thank you for helping improve the Chinese Surnames Dataset. Contributions are welcome in data quality, historical references, multilingual review, regional romanization, documentation, and validation tooling.

## Before opening a pull request

- Search existing issues and pull requests before starting duplicate work.
- For factual changes, include a reliable source and identify the fields affected.
- When sources disagree, document the competing interpretations instead of presenting one account as universally definitive.
- Do not add private personal information or unsupported claims about living people.
- Keep changes focused and preserve the existing JSON field names unless a schema change is discussed first.

## Data changes

Each surname record must remain valid JSON and conform to `schema/surnames.schema.json`.

Please check the following before submitting a data change:

- `hanzi` and `pinyin` are present and non-empty;
- the `hanzi` value is not already used by another record;
- the `hanzi` and `pinyin` combination is unique;
- multilingual descriptions accurately reflect the source and language;
- regional or diaspora variants identify the relevant language or region where possible;
- traditional Wu Xing classifications are described as cultural classifications, not scientific facts;
- no string contains accidental leading or trailing whitespace.

## Local validation

From the repository root, install the validator dependency and run:

```bash
python -m pip install jsonschema
python scripts/validate_dataset.py
```

The same validation runs automatically for pushes and pull requests through GitHub Actions.

## Pull requests

Use a focused branch and explain what changed, why it changed, and which sources or checks support the change. Keep generated files and unrelated formatting changes out of a data correction pull request.

Pull requests should pass the validation workflow before they are merged. Maintainers may request additional references or ask for uncertain claims to be marked as provisional.

## License

By contributing, you agree that your contribution may be distributed under the license that applies to the changed material: code and tooling under the MIT License, and dataset content under CC BY 4.0 as described in `LICENSE` and `LICENSE-DATA`.
