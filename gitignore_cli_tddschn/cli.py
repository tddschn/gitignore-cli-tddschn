#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-05-05
Purpose: gitignore CLI
"""

import argparse
import sys

from . import __version__, __app_name_slug__, logger, __app_name__
import io, json, time
from pathlib import Path
import typer

app = typer.Typer(name='jwc-news')

jwc_url = 'http://www.jwc.fudan.edu.cn'
jwc_news_url = 'http://www.jwc.fudan.edu.cn/9397/list.htm'
cache_dir = Path.home() / '.cache' / __app_name_slug__
gitignore_url = 'https://github.com/toptal/gitignore'
gitignore_dir = cache_dir / 'gitignore'
gitignore_template_dir = gitignore_dir / 'templates'

# cache_file = cache_dir / 'data.json'


# clone https://github.com/toptal/gitignore to cache_dir with subprocess
def update_gitginore_cache():
    """Clone / pull gitignore to cache_dir"""
    cache_dir.mkdir(parents=True, exist_ok=True)
    import subprocess
    if not gitignore_dir.exists():
        subprocess.run(['git', 'clone', gitignore_url, str(gitignore_dir)])
    else:
        # run git -C gitignore_dir pull origin master
        subprocess.run(
            ['git', '-C',
             str(gitignore_dir), 'pull', 'origin', 'master'])


def read_gitignore_from_cache(template: str) -> str:
    """Read gitignore from cache"""
    template_file = gitignore_template_dir / f'{template}.gitignore'
    if template_file.exists():
        return template_file.read_text()
    else:
        # logger.warning(f'{template} not found in cache')
        return f'#!! ERROR: {template} is undefined. Use list command to see defined gitignore types !!#'


def list_templates() -> list[str]:
    """List gitignore templates"""
    # update_gitginore_cache()
    templates = [f.stem for f in gitignore_template_dir.glob('*.gitignore')]
    return templates


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='gitignore CLI',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('templates',
                        metavar='TEMPLATES',
                        nargs='+',
                        help='A positional argument')

    # parser.add_argument('-a',
    #                     '--arg',
    #                     help='A named string argument',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    # parser.add_argument('-i',
    #                     '--int',
    #                     help='A named integer argument',
    #                     metavar='int',
    #                     type=int,
    #                     default=0)

    parser.add_argument('-o',
                        '--out',
                        help='Output to file, append if exists',
                        metavar='FILE',
                        type=argparse.FileType('at'),
                        default=sys.stdout)

    parser.add_argument('-r',
                        '--refresh',
                        help='Refresh gitignore cache',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    templates = args.templates
    out = args.out
    refresh = args.refresh
    if refresh:
        update_gitginore_cache()
        logger.info('gitignore cache is updated')
        # return
    for template in templates:
        out.write(read_gitignore_from_cache(template))
        out.write('\n')
        out.flush()


if __name__ == '__main__':
    main()
