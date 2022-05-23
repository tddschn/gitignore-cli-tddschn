# gitignore CLI

Fast gitignore CLI tool with cached templates


- [gitignore CLI](#gitignore-cli)
  - [Features](#features)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)
  - [Usage](#usage)
  - [Develop](#develop)
## Features
- Extremely fast - no network calls made if the cache has been retrieved with `gi --refresh`.
- [Templates source](https://github.com/toptal/gitignore), you can also set additional custom templates dir with `-c` or via `$GITIGNORE_CLI_TEMPLATE_DIR`.

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

You can either invoke gitignore CLI with `gi` or `gitignore`.

```
$ gi -h

usage: gi [-h] [-c CUSTOM_TEMPLATES_DIR] [-o FILE] [-r] [-l] [-a] [-w] [TEMPLATES ...]

gitignore CLI

positional arguments:
  TEMPLATES             A positional argument (default: None)

options:
  -h, --help            show this help message and exit
  -c CUSTOM_TEMPLATES_DIR, --custom-templates-dir CUSTOM_TEMPLATES_DIR
                        Custom templates dir, gitignore CLI will look for templates named *.gitignore in this dir first. Defaults to the value of
                        $GITIGNORE_CLI_TEMPLATE_DIR env var (default: /Users/tscp/.cache/gitignore-cli/gitignore-tddschn/templates)
  -o FILE, --out FILE   Output to file, append if exists, if -a or -w is not specified (default: <_io.TextIOWrapper name='<stdout>' mode='w'
                        encoding='utf-8'>)
  -r, --refresh         Refresh gitignore cache (default: False)
  -l, --list            Lists available gitignore templates (default: False)
  -a, --append          Append to the .gitignore of current git repository (default: False)
  -w, --write           Write to the .gitignore of current git repository (overwrite) (default: False)
```

## Develop
```
$ git clone https://github.com/tddschn/gitignore-cli-tddschn.git
$ cd gitignore-cli-tddschn
$ poetry install
```