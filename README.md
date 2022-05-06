# gitignore CLI

Fast gitignore CLI tool with cached templates

[Templates source](https://github.com/toptal/gitignore)

- [gitignore CLI](#gitignore-cli)
	- [Features](#features)
	- [Installation](#installation)
		- [pipx](#pipx)
		- [pip](#pip)
	- [Usage](#usage)
	- [Develop](#develop)
## Features
- Extremely fast - no network calls made if the cache has been retrieved with `gi --refresh`.

## Installation

First make sure the `git` executable is installed and in your `$PATH`, 
as it is required to retrieve the gitignore templates.

### pipx

This is the recommended installation method.

```
$ pipx install gitignore-cli-tddschn
```

### [pip](https://pypi.org/project/gitignore-cli-tddschn/)
```
$ pip install gitignore-cli-tddschn
```


## Usage

You can either invoke this tool with `gitignore-cli-tddschn` or `gitignore`,
`--help` is unsupported when using the latter.

```
$ gitignore -h
usage: gitignore [-h] [-o FILE] [-r] [-l] [TEMPLATES ...]

gitignore CLI

positional arguments:
  TEMPLATES            A positional argument (default: None)

options:
  -h, --help           show this help message and exit
  -o FILE, --out FILE  Output to file, append if exists (default: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)
  -r, --refresh        Refresh gitignore cache (default: False)
  -l, --list           Lists available gitignore templates (default: False)
```

## Develop
```
$ git clone https://github.com/tddschn/gitignore-cli-tddschn.git
$ cd gitignore-cli-tddschn
$ poetry install
```