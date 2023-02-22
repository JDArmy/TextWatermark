# Begin

## Init project environment

```bash
$ git init
$ git config
# install poetry
$ poetry install

# creating isolated virtual python environments
$ virtualenv venv
$ . venv/bin/activate

# install textwatermark in editable mode
$ pip install --editable .

```

## Develop

- code
- git commit
- tox

## Delivery

### Run tox

Run tox to format code style and check test.

- tox

### Git tag

Modify package version value, then commit.

Add tag

- git tag -a v0.1.0

### Build

Build this tag distribution package.

- poetry build

### Upload index server

Upload to PyPI server, or pass `--repository https://pypi.org/simple` to specify index server.

- poetry publish
