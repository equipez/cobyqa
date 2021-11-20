import importlib
import os
import platform
import sys

from cobyqa.utils._min_dependencies import dependent_pkgs


def _get_sys_info():
    """
    Get system-related information.

    Returns
    -------
    dict
        Python version, path to the Python executable, and system information.
    """
    return {
        'python': sys.version.replace(os.linesep, ' '),
        'executable': sys.executable,
        'machine': platform.platform(),
    }


def _get_deps_info():
    """
    Get information on the package and its dependencies.

    Returns
    -------
    dict:
        Versions of the package and its dependencies.
    """
    deps = ['pip', 'setuptools', 'cobyqa']
    for pkg, (_, extras) in dependent_pkgs.items():
        if {'build', 'install'}.intersection(extras.split(', ')):
            deps.append(pkg)
    deps_info = {}
    for module in deps:
        try:
            if module in sys.modules:
                mod = sys.modules[module]
            else:
                mod = importlib.import_module(module)
            deps_info[module] = mod.__version__  # noqa
        except ImportError:
            deps_info[module] = None
    return deps_info


def show_versions():
    """
    Print debugging information.
    """
    sys_info = _get_sys_info()
    deps_info = _get_deps_info()

    print()
    print('System settings')
    print('---------------')
    sys_width = max(map(len, sys_info.keys())) + 1
    for k, stat in sys_info.items():
        print(f'{k:>{sys_width}}: {stat}')

    print()
    print('Python dependencies')
    print('-------------------')
    deps_width = max(map(len, deps_info.keys())) + 1
    for k, stat in deps_info.items():
        print(f'{k:>{deps_width}}: {stat}')
    print()
