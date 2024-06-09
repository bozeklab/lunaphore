import os
import re


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])



def get_base_dir():
    """
    hardcoded list of where the files could be. This will become obsolete as we dive deeper into cookiecutter
    """
    if os.path.exists('/projects/ag-bozek/lunaphore/'):
        base_dir = '/projects/ag-bozek/lunaphore/'
    else:
        raise FileNotFoundError('The script is not running in one of the usual systems! Check base_dir')
    return base_dir


def list_subdir_filter(source_folder, check_subfolders: bool = False, search_pattern: str = ''):
    """
    Simple wrapper for os.walk() or os.listdir() according to whether one wants to scan subfolders.
    It includes a basic re.search() for filtering purposes.
    :param source_folder: the folder to scan for content
    :param check_subfolders: bool, whether subfolders of source_folder should be checked for files (recursively!)
    :param search_pattern: str,
    :return:
    """
    if check_subfolders:
        all_items = []
        for path, subdirs, files in os.walk(source_folder):
            for filename in files:
                if re.search(search_pattern, filename):
                    all_items.append(os.path.join(path, filename))
    else:
        all_items = [
            os.path.join(source_folder, filename)
            for filename in os.listdir(source_folder)
            if re.search(search_pattern, filename)
        ]
    return sorted(all_items)


def slide_cycle_dot(filename, coords=False):
    slide = int(re.sub('.*slide([0-9]+).*', '\\1', filename))
    cycle = (re.sub('.*cycle([0-9]+).*', '\\1', filename))
    dot = int(re.sub('.*(dot|XY)([0-9]+).*', '\\2', filename))
              
    if coords:
        x, y = re.sub('.*(dot|XY)[0-9]+_([0-9]+)_([0-9]+).*', '\\2,\\3', filename).split(',')
        return slide, cycle, dot, x, y

    return slide, cycle, dot