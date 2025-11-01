# color-print

Tiny Python package to format and print colored text using ANSI escape sequences.

Usage

```python
from color_print import color_print, format_text

color_print("Hello", "green")
# or
s = format_text("Hello", "red")
print(s)
```

Install

```bash
pip install .
```

Run tests

```bash
pip install -e .[test]
pytest
```


CI & Publishing
-----------------

This repository includes GitHub Actions workflows to run tests and publish releases.

- CI: `.github/workflows/ci.yml` — runs tests on push and PRs to `main` across multiple Python versions and OSes.
- Publish (tag-based): `.github/workflows/publish.yml` — builds and uploads to PyPI when you push a tag matching `v*.*.*`.
- Release-based: `.github/workflows/release-publish.yml` — builds on GitHub Release published and uploads to PyPI.

Before publishing to PyPI

1. Create a PyPI API token on https://pypi.org/manage/account/#api-tokens. Copy the token immediately.
2. In GitHub, go to your repository → Settings → Secrets and variables → Actions → New repository secret.
	- Name: `PYPI_API_TOKEN`
	- Value: paste the token from PyPI

Publish using a tag (from PowerShell)

```powershell
# create annotated tag at current main HEAD
git checkout main
git pull origin main
git tag -a v0.1.0 -m "release v0.1.0"
git push origin v0.1.0
```

Or publish by creating a GitHub Release (UI): create a release for the version and publish it — the `release-publish.yml` workflow will run.

If a workflow fails to resolve a third-party action (for example `pypa/gh-action-pypi-publish@...`), the repository includes fallbacks that run `twine` directly on the runner. Ensure `PYPI_API_TOKEN` is set and the tag/release points at the commit that contains the updated workflow file.
