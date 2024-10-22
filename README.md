# Test setup using `uv` with path dependencies

- The root `pyproject.toml` declares a git submodule (`more-itertools`) and a local package (`package_a`) as editable path dependencies
- The local package (`packages/package_a`) declares a specific version `more-itertools==10.5.0` as its dependency
- However, the root `pyproject.toml` overrides the version of `more-itertools`.

See https://github.com/astral-sh/uv/issues/8407
