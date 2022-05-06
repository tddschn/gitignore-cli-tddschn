#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-05-05
Purpose: gitignore CLI
"""

import argparse
import sys

from . import __version__, __app_name_slug__, logger, __app_name__
from pathlib import Path
from utils_tddschn.git_utils import git_root_dir

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


def read_gitignore_from_cache(template: str) -> tuple[int, str]:
    """Read gitignore from cache"""
    if not gitignore_template_dir.exists():
        update_gitginore_cache()
        logger.info('gitignore cache is updated')
    template_file = gitignore_template_dir / f'{template}.gitignore'
    if template_file.exists():
        return 0, template_file.read_text()
    else:
        # logger.warning(f'{template} not found in cache')
        return 1, f'#!! ERROR: {template} is undefined. Use list command to see defined gitignore types !!#'


def list_gitignore_templates() -> list[str]:
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
                        nargs='*',
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

    parser.add_argument(
        '-o',
        '--out',
        help='Output to file, append if exists, if -a or -w is not specified',
        metavar='FILE',
        type=argparse.FileType('at'),
        default=sys.stdout)

    parser.add_argument('-r',
                        '--refresh',
                        help='Refresh gitignore cache',
                        action='store_true')

    parser.add_argument('-l',
                        '--list',
                        help='Lists available gitignore templates',
                        action='store_true')

    parser.add_argument(
        '-a',
        '--append',
        help='Append to the .gitignore of current git repository',
        action='store_true')

    parser.add_argument(
        '-w',
        '--write',
        help='Write to the .gitignore of current git repository (overwrite)',
        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    WARN_NOT_GIT_REPO = False
    args = get_args()
    templates = args.templates
    try:
        if args.append:
            out = open(Path(git_root_dir()) / '.gitignore', 'at')
        elif args.write:
            out = open(Path(git_root_dir()) / '.gitignore', 'wt')
        else:
            out = args.out
    except:
        WARN_NOT_GIT_REPO = True
        logger.info('Writing to stdout')
        out = args.out
    if not args.append and not args.write:
        out = args.out

    refresh = args.refresh
    list_templates = args.list
    if refresh:
        update_gitginore_cache()
        logger.info('gitignore cache is updated')
        # return
    if list_templates:
        print('\n'.join(list_gitignore_templates()))
        return
    if not templates:
        print('No templates specified', file=sys.stderr)
        return
    for template in templates:
        out.write(read_gitignore_from_cache(template)[1])
        out.write('\n')
        out.flush()

    if WARN_NOT_GIT_REPO:
        print(
            f'{Path().absolute()} is not a git repository, outputted to stdout instead.',
            file=sys.stderr)


if __name__ == '__main__':
    main()
