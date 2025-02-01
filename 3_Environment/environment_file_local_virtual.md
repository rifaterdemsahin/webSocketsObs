The Roadmap and Use Cases - A roadmap with learning modules and real-world use cases to apply new skills. Create it
The environment is python


.
├── enviroment_structure.md
├── path
│   └── to
│       └── venv
│           ├── bin
│           │   ├── Activate.ps1
│           │   ├── activate
│           │   ├── activate.csh
│           │   ├── activate.fish
│           │   ├── pip
│           │   ├── pip3
│           │   ├── pip3.13
│           │   ├── python -> python3.13
│           │   ├── python3 -> python3.13
│           │   ├── python3.13 -> /opt/homebrew/opt/python@3.13/bin/python3.13
│           │   └── wsdump
│           ├── include
│           │   └── python3.13
│           ├── lib
│           │   └── python3.13
│           │       └── site-packages
│           │           ├── obs_websocket_py-1.0.dist-info
│           │           │   ├── INSTALLER
│           │           │   ├── LICENSE
│           │           │   ├── METADATA
│           │           │   ├── RECORD
│           │           │   ├── REQUESTED
│           │           │   ├── WHEEL
│           │           │   └── top_level.txt
│           │           ├── obswebsocket
│           │           │   ├── __init__.py
│           │           │   ├── __pycache__
│           │           │   │   ├── __init__.cpython-313.pyc
│           │           │   │   ├── base_classes.cpython-313.pyc
│           │           │   │   ├── core.cpython-313.pyc
│           │           │   │   └── exceptions.cpython-313.pyc
│           │           │   ├── base_classes.py
│           │           │   ├── core.py
│           │           │   └── exceptions.py
│           │           ├── pip
│           │           │   ├── __init__.py
│           │           │   ├── __main__.py
│           │           │   ├── __pip-runner__.py
│           │           │   ├── __pycache__
│           │           │   │   ├── __init__.cpython-313.pyc
│           │           │   │   ├── __main__.cpython-313.pyc
│           │           │   │   └── __pip-runner__.cpython-313.pyc
│           │           │   ├── _internal
│           │           │   │   ├── __init__.py
│           │           │   │   ├── __pycache__
│           │           │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   ├── build_env.cpython-313.pyc
│           │           │   │   │   ├── cache.cpython-313.pyc
│           │           │   │   │   ├── configuration.cpython-313.pyc
│           │           │   │   │   ├── exceptions.cpython-313.pyc
│           │           │   │   │   ├── main.cpython-313.pyc
│           │           │   │   │   ├── pyproject.cpython-313.pyc
│           │           │   │   │   ├── self_outdated_check.cpython-313.pyc
│           │           │   │   │   └── wheel_builder.cpython-313.pyc
│           │           │   │   ├── build_env.py
│           │           │   │   ├── cache.py
│           │           │   │   ├── cli
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── autocompletion.cpython-313.pyc
│           │           │   │   │   │   ├── base_command.cpython-313.pyc
│           │           │   │   │   │   ├── cmdoptions.cpython-313.pyc
│           │           │   │   │   │   ├── command_context.cpython-313.pyc
│           │           │   │   │   │   ├── index_command.cpython-313.pyc
│           │           │   │   │   │   ├── main.cpython-313.pyc
│           │           │   │   │   │   ├── main_parser.cpython-313.pyc
│           │           │   │   │   │   ├── parser.cpython-313.pyc
│           │           │   │   │   │   ├── progress_bars.cpython-313.pyc
│           │           │   │   │   │   ├── req_command.cpython-313.pyc
│           │           │   │   │   │   ├── spinners.cpython-313.pyc
│           │           │   │   │   │   └── status_codes.cpython-313.pyc
│           │           │   │   │   ├── autocompletion.py
│           │           │   │   │   ├── base_command.py
│           │           │   │   │   ├── cmdoptions.py
│           │           │   │   │   ├── command_context.py
│           │           │   │   │   ├── index_command.py
│           │           │   │   │   ├── main.py
│           │           │   │   │   ├── main_parser.py
│           │           │   │   │   ├── parser.py
│           │           │   │   │   ├── progress_bars.py
│           │           │   │   │   ├── req_command.py
│           │           │   │   │   ├── spinners.py
│           │           │   │   │   └── status_codes.py
│           │           │   │   ├── commands
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── cache.cpython-313.pyc
│           │           │   │   │   │   ├── check.cpython-313.pyc
│           │           │   │   │   │   ├── completion.cpython-313.pyc
│           │           │   │   │   │   ├── configuration.cpython-313.pyc
│           │           │   │   │   │   ├── debug.cpython-313.pyc
│           │           │   │   │   │   ├── download.cpython-313.pyc
│           │           │   │   │   │   ├── freeze.cpython-313.pyc
│           │           │   │   │   │   ├── hash.cpython-313.pyc
│           │           │   │   │   │   ├── help.cpython-313.pyc
│           │           │   │   │   │   ├── index.cpython-313.pyc
│           │           │   │   │   │   ├── inspect.cpython-313.pyc
│           │           │   │   │   │   ├── install.cpython-313.pyc
│           │           │   │   │   │   ├── list.cpython-313.pyc
│           │           │   │   │   │   ├── search.cpython-313.pyc
│           │           │   │   │   │   ├── show.cpython-313.pyc
│           │           │   │   │   │   ├── uninstall.cpython-313.pyc
│           │           │   │   │   │   └── wheel.cpython-313.pyc
│           │           │   │   │   ├── cache.py
│           │           │   │   │   ├── check.py
│           │           │   │   │   ├── completion.py
│           │           │   │   │   ├── configuration.py
│           │           │   │   │   ├── debug.py
│           │           │   │   │   ├── download.py
│           │           │   │   │   ├── freeze.py
│           │           │   │   │   ├── hash.py
│           │           │   │   │   ├── help.py
│           │           │   │   │   ├── index.py
│           │           │   │   │   ├── inspect.py
│           │           │   │   │   ├── install.py
│           │           │   │   │   ├── list.py
│           │           │   │   │   ├── search.py
│           │           │   │   │   ├── show.py
│           │           │   │   │   ├── uninstall.py
│           │           │   │   │   └── wheel.py
│           │           │   │   ├── configuration.py
│           │           │   │   ├── distributions
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── base.cpython-313.pyc
│           │           │   │   │   │   ├── installed.cpython-313.pyc
│           │           │   │   │   │   ├── sdist.cpython-313.pyc
│           │           │   │   │   │   └── wheel.cpython-313.pyc
│           │           │   │   │   ├── base.py
│           │           │   │   │   ├── installed.py
│           │           │   │   │   ├── sdist.py
│           │           │   │   │   └── wheel.py
│           │           │   │   ├── exceptions.py
│           │           │   │   ├── index
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── collector.cpython-313.pyc
│           │           │   │   │   │   ├── package_finder.cpython-313.pyc
│           │           │   │   │   │   └── sources.cpython-313.pyc
│           │           │   │   │   ├── collector.py
│           │           │   │   │   ├── package_finder.py
│           │           │   │   │   └── sources.py
│           │           │   │   ├── locations
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── _distutils.cpython-313.pyc
│           │           │   │   │   │   ├── _sysconfig.cpython-313.pyc
│           │           │   │   │   │   └── base.cpython-313.pyc
│           │           │   │   │   ├── _distutils.py
│           │           │   │   │   ├── _sysconfig.py
│           │           │   │   │   └── base.py
│           │           │   │   ├── main.py
│           │           │   │   ├── metadata
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── _json.cpython-313.pyc
│           │           │   │   │   │   ├── base.cpython-313.pyc
│           │           │   │   │   │   └── pkg_resources.cpython-313.pyc
│           │           │   │   │   ├── _json.py
│           │           │   │   │   ├── base.py
│           │           │   │   │   ├── importlib
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   ├── _compat.cpython-313.pyc
│           │           │   │   │   │   │   ├── _dists.cpython-313.pyc
│           │           │   │   │   │   │   └── _envs.cpython-313.pyc
│           │           │   │   │   │   ├── _compat.py
│           │           │   │   │   │   ├── _dists.py
│           │           │   │   │   │   └── _envs.py
│           │           │   │   │   └── pkg_resources.py
│           │           │   │   ├── models
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── candidate.cpython-313.pyc
│           │           │   │   │   │   ├── direct_url.cpython-313.pyc
│           │           │   │   │   │   ├── format_control.cpython-313.pyc
│           │           │   │   │   │   ├── index.cpython-313.pyc
│           │           │   │   │   │   ├── installation_report.cpython-313.pyc
│           │           │   │   │   │   ├── link.cpython-313.pyc
│           │           │   │   │   │   ├── scheme.cpython-313.pyc
│           │           │   │   │   │   ├── search_scope.cpython-313.pyc
│           │           │   │   │   │   ├── selection_prefs.cpython-313.pyc
│           │           │   │   │   │   ├── target_python.cpython-313.pyc
│           │           │   │   │   │   └── wheel.cpython-313.pyc
│           │           │   │   │   ├── candidate.py
│           │           │   │   │   ├── direct_url.py
│           │           │   │   │   ├── format_control.py
│           │           │   │   │   ├── index.py
│           │           │   │   │   ├── installation_report.py
│           │           │   │   │   ├── link.py
│           │           │   │   │   ├── scheme.py
│           │           │   │   │   ├── search_scope.py
│           │           │   │   │   ├── selection_prefs.py
│           │           │   │   │   ├── target_python.py
│           │           │   │   │   └── wheel.py
│           │           │   │   ├── network
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── auth.cpython-313.pyc
│           │           │   │   │   │   ├── cache.cpython-313.pyc
│           │           │   │   │   │   ├── download.cpython-313.pyc
│           │           │   │   │   │   ├── lazy_wheel.cpython-313.pyc
│           │           │   │   │   │   ├── session.cpython-313.pyc
│           │           │   │   │   │   ├── utils.cpython-313.pyc
│           │           │   │   │   │   └── xmlrpc.cpython-313.pyc
│           │           │   │   │   ├── auth.py
│           │           │   │   │   ├── cache.py
│           │           │   │   │   ├── download.py
│           │           │   │   │   ├── lazy_wheel.py
│           │           │   │   │   ├── session.py
│           │           │   │   │   ├── utils.py
│           │           │   │   │   └── xmlrpc.py
│           │           │   │   ├── operations
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── check.cpython-313.pyc
│           │           │   │   │   │   ├── freeze.cpython-313.pyc
│           │           │   │   │   │   └── prepare.cpython-313.pyc
│           │           │   │   │   ├── build
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   ├── build_tracker.cpython-313.pyc
│           │           │   │   │   │   │   ├── metadata.cpython-313.pyc
│           │           │   │   │   │   │   ├── metadata_editable.cpython-313.pyc
│           │           │   │   │   │   │   ├── metadata_legacy.cpython-313.pyc
│           │           │   │   │   │   │   ├── wheel.cpython-313.pyc
│           │           │   │   │   │   │   ├── wheel_editable.cpython-313.pyc
│           │           │   │   │   │   │   └── wheel_legacy.cpython-313.pyc
│           │           │   │   │   │   ├── build_tracker.py
│           │           │   │   │   │   ├── metadata.py
│           │           │   │   │   │   ├── metadata_editable.py
│           │           │   │   │   │   ├── metadata_legacy.py
│           │           │   │   │   │   ├── wheel.py
│           │           │   │   │   │   ├── wheel_editable.py
│           │           │   │   │   │   └── wheel_legacy.py
│           │           │   │   │   ├── check.py
│           │           │   │   │   ├── freeze.py
│           │           │   │   │   ├── install
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   ├── editable_legacy.cpython-313.pyc
│           │           │   │   │   │   │   └── wheel.cpython-313.pyc
│           │           │   │   │   │   ├── editable_legacy.py
│           │           │   │   │   │   └── wheel.py
│           │           │   │   │   └── prepare.py
│           │           │   │   ├── pyproject.py
│           │           │   │   ├── req
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── constructors.cpython-313.pyc
│           │           │   │   │   │   ├── req_file.cpython-313.pyc
│           │           │   │   │   │   ├── req_install.cpython-313.pyc
│           │           │   │   │   │   ├── req_set.cpython-313.pyc
│           │           │   │   │   │   └── req_uninstall.cpython-313.pyc
│           │           │   │   │   ├── constructors.py
│           │           │   │   │   ├── req_file.py
│           │           │   │   │   ├── req_install.py
│           │           │   │   │   ├── req_set.py
│           │           │   │   │   └── req_uninstall.py
│           │           │   │   ├── resolution
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   └── base.cpython-313.pyc
│           │           │   │   │   ├── base.py
│           │           │   │   │   ├── legacy
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   └── resolver.cpython-313.pyc
│           │           │   │   │   │   └── resolver.py
│           │           │   │   │   └── resolvelib
│           │           │   │   │       ├── __init__.py
│           │           │   │   │       ├── __pycache__
│           │           │   │   │       │   ├── __init__.cpython-313.pyc
│           │           │   │   │       │   ├── base.cpython-313.pyc
│           │           │   │   │       │   ├── candidates.cpython-313.pyc
│           │           │   │   │       │   ├── factory.cpython-313.pyc
│           │           │   │   │       │   ├── found_candidates.cpython-313.pyc
│           │           │   │   │       │   ├── provider.cpython-313.pyc
│           │           │   │   │       │   ├── reporter.cpython-313.pyc
│           │           │   │   │       │   ├── requirements.cpython-313.pyc
│           │           │   │   │       │   └── resolver.cpython-313.pyc
│           │           │   │   │       ├── base.py
│           │           │   │   │       ├── candidates.py
│           │           │   │   │       ├── factory.py
│           │           │   │   │       ├── found_candidates.py
│           │           │   │   │       ├── provider.py
│           │           │   │   │       ├── reporter.py
│           │           │   │   │       ├── requirements.py
│           │           │   │   │       └── resolver.py
│           │           │   │   ├── self_outdated_check.py
│           │           │   │   ├── utils
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── _jaraco_text.cpython-313.pyc
│           │           │   │   │   │   ├── _log.cpython-313.pyc
│           │           │   │   │   │   ├── appdirs.cpython-313.pyc
│           │           │   │   │   │   ├── compat.cpython-313.pyc
│           │           │   │   │   │   ├── compatibility_tags.cpython-313.pyc
│           │           │   │   │   │   ├── datetime.cpython-313.pyc
│           │           │   │   │   │   ├── deprecation.cpython-313.pyc
│           │           │   │   │   │   ├── direct_url_helpers.cpython-313.pyc
│           │           │   │   │   │   ├── egg_link.cpython-313.pyc
│           │           │   │   │   │   ├── entrypoints.cpython-313.pyc
│           │           │   │   │   │   ├── filesystem.cpython-313.pyc
│           │           │   │   │   │   ├── filetypes.cpython-313.pyc
│           │           │   │   │   │   ├── glibc.cpython-313.pyc
│           │           │   │   │   │   ├── hashes.cpython-313.pyc
│           │           │   │   │   │   ├── logging.cpython-313.pyc
│           │           │   │   │   │   ├── misc.cpython-313.pyc
│           │           │   │   │   │   ├── packaging.cpython-313.pyc
│           │           │   │   │   │   ├── retry.cpython-313.pyc
│           │           │   │   │   │   ├── setuptools_build.cpython-313.pyc
│           │           │   │   │   │   ├── subprocess.cpython-313.pyc
│           │           │   │   │   │   ├── temp_dir.cpython-313.pyc
│           │           │   │   │   │   ├── unpacking.cpython-313.pyc
│           │           │   │   │   │   ├── urls.cpython-313.pyc
│           │           │   │   │   │   ├── virtualenv.cpython-313.pyc
│           │           │   │   │   │   └── wheel.cpython-313.pyc
│           │           │   │   │   ├── _jaraco_text.py
│           │           │   │   │   ├── _log.py
│           │           │   │   │   ├── appdirs.py
│           │           │   │   │   ├── compat.py
│           │           │   │   │   ├── compatibility_tags.py
│           │           │   │   │   ├── datetime.py
│           │           │   │   │   ├── deprecation.py
│           │           │   │   │   ├── direct_url_helpers.py
│           │           │   │   │   ├── egg_link.py
│           │           │   │   │   ├── entrypoints.py
│           │           │   │   │   ├── filesystem.py
│           │           │   │   │   ├── filetypes.py
│           │           │   │   │   ├── glibc.py
│           │           │   │   │   ├── hashes.py
│           │           │   │   │   ├── logging.py
│           │           │   │   │   ├── misc.py
│           │           │   │   │   ├── packaging.py
│           │           │   │   │   ├── retry.py
│           │           │   │   │   ├── setuptools_build.py
│           │           │   │   │   ├── subprocess.py
│           │           │   │   │   ├── temp_dir.py
│           │           │   │   │   ├── unpacking.py
│           │           │   │   │   ├── urls.py
│           │           │   │   │   ├── virtualenv.py
│           │           │   │   │   └── wheel.py
│           │           │   │   ├── vcs
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── bazaar.cpython-313.pyc
│           │           │   │   │   │   ├── git.cpython-313.pyc
│           │           │   │   │   │   ├── mercurial.cpython-313.pyc
│           │           │   │   │   │   ├── subversion.cpython-313.pyc
│           │           │   │   │   │   └── versioncontrol.cpython-313.pyc
│           │           │   │   │   ├── bazaar.py
│           │           │   │   │   ├── git.py
│           │           │   │   │   ├── mercurial.py
│           │           │   │   │   ├── subversion.py
│           │           │   │   │   └── versioncontrol.py
│           │           │   │   └── wheel_builder.py
│           │           │   ├── _vendor
│           │           │   │   ├── __init__.py
│           │           │   │   ├── __pycache__
│           │           │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   └── typing_extensions.cpython-313.pyc
│           │           │   │   ├── cachecontrol
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── _cmd.cpython-313.pyc
│           │           │   │   │   │   ├── adapter.cpython-313.pyc
│           │           │   │   │   │   ├── cache.cpython-313.pyc
│           │           │   │   │   │   ├── controller.cpython-313.pyc
│           │           │   │   │   │   ├── filewrapper.cpython-313.pyc
│           │           │   │   │   │   ├── heuristics.cpython-313.pyc
│           │           │   │   │   │   ├── serialize.cpython-313.pyc
│           │           │   │   │   │   └── wrapper.cpython-313.pyc
│           │           │   │   │   ├── _cmd.py
│           │           │   │   │   ├── adapter.py
│           │           │   │   │   ├── cache.py
│           │           │   │   │   ├── caches
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   ├── file_cache.cpython-313.pyc
│           │           │   │   │   │   │   └── redis_cache.cpython-313.pyc
│           │           │   │   │   │   ├── file_cache.py
│           │           │   │   │   │   └── redis_cache.py
│           │           │   │   │   ├── controller.py
│           │           │   │   │   ├── filewrapper.py
│           │           │   │   │   ├── heuristics.py
│           │           │   │   │   ├── py.typed
│           │           │   │   │   ├── serialize.py
│           │           │   │   │   └── wrapper.py
│           │           │   │   ├── certifi
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __main__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── __main__.cpython-313.pyc
│           │           │   │   │   │   └── core.cpython-313.pyc
│           │           │   │   │   ├── cacert.pem
│           │           │   │   │   ├── core.py
│           │           │   │   │   └── py.typed
│           │           │   │   ├── distlib
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── compat.cpython-313.pyc
│           │           │   │   │   │   ├── database.cpython-313.pyc
│           │           │   │   │   │   ├── index.cpython-313.pyc
│           │           │   │   │   │   ├── locators.cpython-313.pyc
│           │           │   │   │   │   ├── manifest.cpython-313.pyc
│           │           │   │   │   │   ├── markers.cpython-313.pyc
│           │           │   │   │   │   ├── metadata.cpython-313.pyc
│           │           │   │   │   │   ├── resources.cpython-313.pyc
│           │           │   │   │   │   ├── scripts.cpython-313.pyc
│           │           │   │   │   │   ├── util.cpython-313.pyc
│           │           │   │   │   │   ├── version.cpython-313.pyc
│           │           │   │   │   │   └── wheel.cpython-313.pyc
│           │           │   │   │   ├── compat.py
│           │           │   │   │   ├── database.py
│           │           │   │   │   ├── index.py
│           │           │   │   │   ├── locators.py
│           │           │   │   │   ├── manifest.py
│           │           │   │   │   ├── markers.py
│           │           │   │   │   ├── metadata.py
│           │           │   │   │   ├── resources.py
│           │           │   │   │   ├── scripts.py
│           │           │   │   │   ├── t32.exe
│           │           │   │   │   ├── t64-arm.exe
│           │           │   │   │   ├── t64.exe
│           │           │   │   │   ├── util.py
│           │           │   │   │   ├── version.py
│           │           │   │   │   ├── w32.exe
│           │           │   │   │   ├── w64-arm.exe
│           │           │   │   │   ├── w64.exe
│           │           │   │   │   └── wheel.py
│           │           │   │   ├── distro
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __main__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── __main__.cpython-313.pyc
│           │           │   │   │   │   └── distro.cpython-313.pyc
│           │           │   │   │   ├── distro.py
│           │           │   │   │   └── py.typed
│           │           │   │   ├── idna
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── codec.cpython-313.pyc
│           │           │   │   │   │   ├── compat.cpython-313.pyc
│           │           │   │   │   │   ├── core.cpython-313.pyc
│           │           │   │   │   │   ├── idnadata.cpython-313.pyc
│           │           │   │   │   │   ├── intranges.cpython-313.pyc
│           │           │   │   │   │   ├── package_data.cpython-313.pyc
│           │           │   │   │   │   └── uts46data.cpython-313.pyc
│           │           │   │   │   ├── codec.py
│           │           │   │   │   ├── compat.py
│           │           │   │   │   ├── core.py
│           │           │   │   │   ├── idnadata.py
│           │           │   │   │   ├── intranges.py
│           │           │   │   │   ├── package_data.py
│           │           │   │   │   ├── py.typed
│           │           │   │   │   └── uts46data.py
│           │           │   │   ├── msgpack
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── exceptions.cpython-313.pyc
│           │           │   │   │   │   ├── ext.cpython-313.pyc
│           │           │   │   │   │   └── fallback.cpython-313.pyc
│           │           │   │   │   ├── exceptions.py
│           │           │   │   │   ├── ext.py
│           │           │   │   │   └── fallback.py
│           │           │   │   ├── packaging
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── _elffile.cpython-313.pyc
│           │           │   │   │   │   ├── _manylinux.cpython-313.pyc
│           │           │   │   │   │   ├── _musllinux.cpython-313.pyc
│           │           │   │   │   │   ├── _parser.cpython-313.pyc
│           │           │   │   │   │   ├── _structures.cpython-313.pyc
│           │           │   │   │   │   ├── _tokenizer.cpython-313.pyc
│           │           │   │   │   │   ├── markers.cpython-313.pyc
│           │           │   │   │   │   ├── metadata.cpython-313.pyc
│           │           │   │   │   │   ├── requirements.cpython-313.pyc
│           │           │   │   │   │   ├── specifiers.cpython-313.pyc
│           │           │   │   │   │   ├── tags.cpython-313.pyc
│           │           │   │   │   │   ├── utils.cpython-313.pyc
│           │           │   │   │   │   └── version.cpython-313.pyc
│           │           │   │   │   ├── _elffile.py
│           │           │   │   │   ├── _manylinux.py
│           │           │   │   │   ├── _musllinux.py
│           │           │   │   │   ├── _parser.py
│           │           │   │   │   ├── _structures.py
│           │           │   │   │   ├── _tokenizer.py
│           │           │   │   │   ├── licenses
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   └── _spdx.cpython-313.pyc
│           │           │   │   │   │   └── _spdx.py
│           │           │   │   │   ├── markers.py
│           │           │   │   │   ├── metadata.py
│           │           │   │   │   ├── py.typed
│           │           │   │   │   ├── requirements.py
│           │           │   │   │   ├── specifiers.py
│           │           │   │   │   ├── tags.py
│           │           │   │   │   ├── utils.py
│           │           │   │   │   └── version.py
│           │           │   │   ├── pkg_resources
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   └── __pycache__
│           │           │   │   │       └── __init__.cpython-313.pyc
│           │           │   │   ├── platformdirs
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __main__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── __main__.cpython-313.pyc
│           │           │   │   │   │   ├── android.cpython-313.pyc
│           │           │   │   │   │   ├── api.cpython-313.pyc
│           │           │   │   │   │   ├── macos.cpython-313.pyc
│           │           │   │   │   │   ├── unix.cpython-313.pyc
│           │           │   │   │   │   ├── version.cpython-313.pyc
│           │           │   │   │   │   └── windows.cpython-313.pyc
│           │           │   │   │   ├── android.py
│           │           │   │   │   ├── api.py
│           │           │   │   │   ├── macos.py
│           │           │   │   │   ├── py.typed
│           │           │   │   │   ├── unix.py
│           │           │   │   │   ├── version.py
│           │           │   │   │   └── windows.py
│           │           │   │   ├── pygments
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __main__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── __main__.cpython-313.pyc
│           │           │   │   │   │   ├── cmdline.cpython-313.pyc
│           │           │   │   │   │   ├── console.cpython-313.pyc
│           │           │   │   │   │   ├── filter.cpython-313.pyc
│           │           │   │   │   │   ├── formatter.cpython-313.pyc
│           │           │   │   │   │   ├── lexer.cpython-313.pyc
│           │           │   │   │   │   ├── modeline.cpython-313.pyc
│           │           │   │   │   │   ├── plugin.cpython-313.pyc
│           │           │   │   │   │   ├── regexopt.cpython-313.pyc
│           │           │   │   │   │   ├── scanner.cpython-313.pyc
│           │           │   │   │   │   ├── sphinxext.cpython-313.pyc
│           │           │   │   │   │   ├── style.cpython-313.pyc
│           │           │   │   │   │   ├── token.cpython-313.pyc
│           │           │   │   │   │   ├── unistring.cpython-313.pyc
│           │           │   │   │   │   └── util.cpython-313.pyc
│           │           │   │   │   ├── cmdline.py
│           │           │   │   │   ├── console.py
│           │           │   │   │   ├── filter.py
│           │           │   │   │   ├── filters
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   └── __pycache__
│           │           │   │   │   │       └── __init__.cpython-313.pyc
│           │           │   │   │   ├── formatter.py
│           │           │   │   │   ├── formatters
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   ├── _mapping.cpython-313.pyc
│           │           │   │   │   │   │   ├── bbcode.cpython-313.pyc
│           │           │   │   │   │   │   ├── groff.cpython-313.pyc
│           │           │   │   │   │   │   ├── html.cpython-313.pyc
│           │           │   │   │   │   │   ├── img.cpython-313.pyc
│           │           │   │   │   │   │   ├── irc.cpython-313.pyc
│           │           │   │   │   │   │   ├── latex.cpython-313.pyc
│           │           │   │   │   │   │   ├── other.cpython-313.pyc
│           │           │   │   │   │   │   ├── pangomarkup.cpython-313.pyc
│           │           │   │   │   │   │   ├── rtf.cpython-313.pyc
│           │           │   │   │   │   │   ├── svg.cpython-313.pyc
│           │           │   │   │   │   │   ├── terminal.cpython-313.pyc
│           │           │   │   │   │   │   └── terminal256.cpython-313.pyc
│           │           │   │   │   │   ├── _mapping.py
│           │           │   │   │   │   ├── bbcode.py
│           │           │   │   │   │   ├── groff.py
│           │           │   │   │   │   ├── html.py
│           │           │   │   │   │   ├── img.py
│           │           │   │   │   │   ├── irc.py
│           │           │   │   │   │   ├── latex.py
│           │           │   │   │   │   ├── other.py
│           │           │   │   │   │   ├── pangomarkup.py
│           │           │   │   │   │   ├── rtf.py
│           │           │   │   │   │   ├── svg.py
│           │           │   │   │   │   ├── terminal.py
│           │           │   │   │   │   └── terminal256.py
│           │           │   │   │   ├── lexer.py
│           │           │   │   │   ├── lexers
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   ├── _mapping.cpython-313.pyc
│           │           │   │   │   │   │   └── python.cpython-313.pyc
│           │           │   │   │   │   ├── _mapping.py
│           │           │   │   │   │   └── python.py
│           │           │   │   │   ├── modeline.py
│           │           │   │   │   ├── plugin.py
│           │           │   │   │   ├── regexopt.py
│           │           │   │   │   ├── scanner.py
│           │           │   │   │   ├── sphinxext.py
│           │           │   │   │   ├── style.py
│           │           │   │   │   ├── styles
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   └── _mapping.cpython-313.pyc
│           │           │   │   │   │   └── _mapping.py
│           │           │   │   │   ├── token.py
│           │           │   │   │   ├── unistring.py
│           │           │   │   │   └── util.py
│           │           │   │   ├── pyproject_hooks
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   └── _impl.cpython-313.pyc
│           │           │   │   │   ├── _impl.py
│           │           │   │   │   ├── _in_process
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   └── _in_process.cpython-313.pyc
│           │           │   │   │   │   └── _in_process.py
│           │           │   │   │   └── py.typed
│           │           │   │   ├── requests
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── __version__.cpython-313.pyc
│           │           │   │   │   │   ├── _internal_utils.cpython-313.pyc
│           │           │   │   │   │   ├── adapters.cpython-313.pyc
│           │           │   │   │   │   ├── api.cpython-313.pyc
│           │           │   │   │   │   ├── auth.cpython-313.pyc
│           │           │   │   │   │   ├── certs.cpython-313.pyc
│           │           │   │   │   │   ├── compat.cpython-313.pyc
│           │           │   │   │   │   ├── cookies.cpython-313.pyc
│           │           │   │   │   │   ├── exceptions.cpython-313.pyc
│           │           │   │   │   │   ├── help.cpython-313.pyc
│           │           │   │   │   │   ├── hooks.cpython-313.pyc
│           │           │   │   │   │   ├── models.cpython-313.pyc
│           │           │   │   │   │   ├── packages.cpython-313.pyc
│           │           │   │   │   │   ├── sessions.cpython-313.pyc
│           │           │   │   │   │   ├── status_codes.cpython-313.pyc
│           │           │   │   │   │   ├── structures.cpython-313.pyc
│           │           │   │   │   │   └── utils.cpython-313.pyc
│           │           │   │   │   ├── __version__.py
│           │           │   │   │   ├── _internal_utils.py
│           │           │   │   │   ├── adapters.py
│           │           │   │   │   ├── api.py
│           │           │   │   │   ├── auth.py
│           │           │   │   │   ├── certs.py
│           │           │   │   │   ├── compat.py
│           │           │   │   │   ├── cookies.py
│           │           │   │   │   ├── exceptions.py
│           │           │   │   │   ├── help.py
│           │           │   │   │   ├── hooks.py
│           │           │   │   │   ├── models.py
│           │           │   │   │   ├── packages.py
│           │           │   │   │   ├── sessions.py
│           │           │   │   │   ├── status_codes.py
│           │           │   │   │   ├── structures.py
│           │           │   │   │   └── utils.py
│           │           │   │   ├── resolvelib
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── providers.cpython-313.pyc
│           │           │   │   │   │   ├── reporters.cpython-313.pyc
│           │           │   │   │   │   ├── resolvers.cpython-313.pyc
│           │           │   │   │   │   └── structs.cpython-313.pyc
│           │           │   │   │   ├── compat
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   └── collections_abc.cpython-313.pyc
│           │           │   │   │   │   └── collections_abc.py
│           │           │   │   │   ├── providers.py
│           │           │   │   │   ├── py.typed
│           │           │   │   │   ├── reporters.py
│           │           │   │   │   ├── resolvers.py
│           │           │   │   │   └── structs.py
│           │           │   │   ├── rich
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __main__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── __main__.cpython-313.pyc
│           │           │   │   │   │   ├── _cell_widths.cpython-313.pyc
│           │           │   │   │   │   ├── _emoji_codes.cpython-313.pyc
│           │           │   │   │   │   ├── _emoji_replace.cpython-313.pyc
│           │           │   │   │   │   ├── _export_format.cpython-313.pyc
│           │           │   │   │   │   ├── _extension.cpython-313.pyc
│           │           │   │   │   │   ├── _fileno.cpython-313.pyc
│           │           │   │   │   │   ├── _inspect.cpython-313.pyc
│           │           │   │   │   │   ├── _log_render.cpython-313.pyc
│           │           │   │   │   │   ├── _loop.cpython-313.pyc
│           │           │   │   │   │   ├── _null_file.cpython-313.pyc
│           │           │   │   │   │   ├── _palettes.cpython-313.pyc
│           │           │   │   │   │   ├── _pick.cpython-313.pyc
│           │           │   │   │   │   ├── _ratio.cpython-313.pyc
│           │           │   │   │   │   ├── _spinners.cpython-313.pyc
│           │           │   │   │   │   ├── _stack.cpython-313.pyc
│           │           │   │   │   │   ├── _timer.cpython-313.pyc
│           │           │   │   │   │   ├── _win32_console.cpython-313.pyc
│           │           │   │   │   │   ├── _windows.cpython-313.pyc
│           │           │   │   │   │   ├── _windows_renderer.cpython-313.pyc
│           │           │   │   │   │   ├── _wrap.cpython-313.pyc
│           │           │   │   │   │   ├── abc.cpython-313.pyc
│           │           │   │   │   │   ├── align.cpython-313.pyc
│           │           │   │   │   │   ├── ansi.cpython-313.pyc
│           │           │   │   │   │   ├── bar.cpython-313.pyc
│           │           │   │   │   │   ├── box.cpython-313.pyc
│           │           │   │   │   │   ├── cells.cpython-313.pyc
│           │           │   │   │   │   ├── color.cpython-313.pyc
│           │           │   │   │   │   ├── color_triplet.cpython-313.pyc
│           │           │   │   │   │   ├── columns.cpython-313.pyc
│           │           │   │   │   │   ├── console.cpython-313.pyc
│           │           │   │   │   │   ├── constrain.cpython-313.pyc
│           │           │   │   │   │   ├── containers.cpython-313.pyc
│           │           │   │   │   │   ├── control.cpython-313.pyc
│           │           │   │   │   │   ├── default_styles.cpython-313.pyc
│           │           │   │   │   │   ├── diagnose.cpython-313.pyc
│           │           │   │   │   │   ├── emoji.cpython-313.pyc
│           │           │   │   │   │   ├── errors.cpython-313.pyc
│           │           │   │   │   │   ├── file_proxy.cpython-313.pyc
│           │           │   │   │   │   ├── filesize.cpython-313.pyc
│           │           │   │   │   │   ├── highlighter.cpython-313.pyc
│           │           │   │   │   │   ├── json.cpython-313.pyc
│           │           │   │   │   │   ├── jupyter.cpython-313.pyc
│           │           │   │   │   │   ├── layout.cpython-313.pyc
│           │           │   │   │   │   ├── live.cpython-313.pyc
│           │           │   │   │   │   ├── live_render.cpython-313.pyc
│           │           │   │   │   │   ├── logging.cpython-313.pyc
│           │           │   │   │   │   ├── markup.cpython-313.pyc
│           │           │   │   │   │   ├── measure.cpython-313.pyc
│           │           │   │   │   │   ├── padding.cpython-313.pyc
│           │           │   │   │   │   ├── pager.cpython-313.pyc
│           │           │   │   │   │   ├── palette.cpython-313.pyc
│           │           │   │   │   │   ├── panel.cpython-313.pyc
│           │           │   │   │   │   ├── pretty.cpython-313.pyc
│           │           │   │   │   │   ├── progress.cpython-313.pyc
│           │           │   │   │   │   ├── progress_bar.cpython-313.pyc
│           │           │   │   │   │   ├── prompt.cpython-313.pyc
│           │           │   │   │   │   ├── protocol.cpython-313.pyc
│           │           │   │   │   │   ├── region.cpython-313.pyc
│           │           │   │   │   │   ├── repr.cpython-313.pyc
│           │           │   │   │   │   ├── rule.cpython-313.pyc
│           │           │   │   │   │   ├── scope.cpython-313.pyc
│           │           │   │   │   │   ├── screen.cpython-313.pyc
│           │           │   │   │   │   ├── segment.cpython-313.pyc
│           │           │   │   │   │   ├── spinner.cpython-313.pyc
│           │           │   │   │   │   ├── status.cpython-313.pyc
│           │           │   │   │   │   ├── style.cpython-313.pyc
│           │           │   │   │   │   ├── styled.cpython-313.pyc
│           │           │   │   │   │   ├── syntax.cpython-313.pyc
│           │           │   │   │   │   ├── table.cpython-313.pyc
│           │           │   │   │   │   ├── terminal_theme.cpython-313.pyc
│           │           │   │   │   │   ├── text.cpython-313.pyc
│           │           │   │   │   │   ├── theme.cpython-313.pyc
│           │           │   │   │   │   ├── themes.cpython-313.pyc
│           │           │   │   │   │   ├── traceback.cpython-313.pyc
│           │           │   │   │   │   └── tree.cpython-313.pyc
│           │           │   │   │   ├── _cell_widths.py
│           │           │   │   │   ├── _emoji_codes.py
│           │           │   │   │   ├── _emoji_replace.py
│           │           │   │   │   ├── _export_format.py
│           │           │   │   │   ├── _extension.py
│           │           │   │   │   ├── _fileno.py
│           │           │   │   │   ├── _inspect.py
│           │           │   │   │   ├── _log_render.py
│           │           │   │   │   ├── _loop.py
│           │           │   │   │   ├── _null_file.py
│           │           │   │   │   ├── _palettes.py
│           │           │   │   │   ├── _pick.py
│           │           │   │   │   ├── _ratio.py
│           │           │   │   │   ├── _spinners.py
│           │           │   │   │   ├── _stack.py
│           │           │   │   │   ├── _timer.py
│           │           │   │   │   ├── _win32_console.py
│           │           │   │   │   ├── _windows.py
│           │           │   │   │   ├── _windows_renderer.py
│           │           │   │   │   ├── _wrap.py
│           │           │   │   │   ├── abc.py
│           │           │   │   │   ├── align.py
│           │           │   │   │   ├── ansi.py
│           │           │   │   │   ├── bar.py
│           │           │   │   │   ├── box.py
│           │           │   │   │   ├── cells.py
│           │           │   │   │   ├── color.py
│           │           │   │   │   ├── color_triplet.py
│           │           │   │   │   ├── columns.py
│           │           │   │   │   ├── console.py
│           │           │   │   │   ├── constrain.py
│           │           │   │   │   ├── containers.py
│           │           │   │   │   ├── control.py
│           │           │   │   │   ├── default_styles.py
│           │           │   │   │   ├── diagnose.py
│           │           │   │   │   ├── emoji.py
│           │           │   │   │   ├── errors.py
│           │           │   │   │   ├── file_proxy.py
│           │           │   │   │   ├── filesize.py
│           │           │   │   │   ├── highlighter.py
│           │           │   │   │   ├── json.py
│           │           │   │   │   ├── jupyter.py
│           │           │   │   │   ├── layout.py
│           │           │   │   │   ├── live.py
│           │           │   │   │   ├── live_render.py
│           │           │   │   │   ├── logging.py
│           │           │   │   │   ├── markup.py
│           │           │   │   │   ├── measure.py
│           │           │   │   │   ├── padding.py
│           │           │   │   │   ├── pager.py
│           │           │   │   │   ├── palette.py
│           │           │   │   │   ├── panel.py
│           │           │   │   │   ├── pretty.py
│           │           │   │   │   ├── progress.py
│           │           │   │   │   ├── progress_bar.py
│           │           │   │   │   ├── prompt.py
│           │           │   │   │   ├── protocol.py
│           │           │   │   │   ├── py.typed
│           │           │   │   │   ├── region.py
│           │           │   │   │   ├── repr.py
│           │           │   │   │   ├── rule.py
│           │           │   │   │   ├── scope.py
│           │           │   │   │   ├── screen.py
│           │           │   │   │   ├── segment.py
│           │           │   │   │   ├── spinner.py
│           │           │   │   │   ├── status.py
│           │           │   │   │   ├── style.py
│           │           │   │   │   ├── styled.py
│           │           │   │   │   ├── syntax.py
│           │           │   │   │   ├── table.py
│           │           │   │   │   ├── terminal_theme.py
│           │           │   │   │   ├── text.py
│           │           │   │   │   ├── theme.py
│           │           │   │   │   ├── themes.py
│           │           │   │   │   ├── traceback.py
│           │           │   │   │   └── tree.py
│           │           │   │   ├── tomli
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── _parser.cpython-313.pyc
│           │           │   │   │   │   ├── _re.cpython-313.pyc
│           │           │   │   │   │   └── _types.cpython-313.pyc
│           │           │   │   │   ├── _parser.py
│           │           │   │   │   ├── _re.py
│           │           │   │   │   ├── _types.py
│           │           │   │   │   └── py.typed
│           │           │   │   ├── truststore
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── _api.cpython-313.pyc
│           │           │   │   │   │   ├── _macos.cpython-313.pyc
│           │           │   │   │   │   ├── _openssl.cpython-313.pyc
│           │           │   │   │   │   ├── _ssl_constants.cpython-313.pyc
│           │           │   │   │   │   └── _windows.cpython-313.pyc
│           │           │   │   │   ├── _api.py
│           │           │   │   │   ├── _macos.py
│           │           │   │   │   ├── _openssl.py
│           │           │   │   │   ├── _ssl_constants.py
│           │           │   │   │   ├── _windows.py
│           │           │   │   │   └── py.typed
│           │           │   │   ├── typing_extensions.py
│           │           │   │   ├── urllib3
│           │           │   │   │   ├── __init__.py
│           │           │   │   │   ├── __pycache__
│           │           │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   ├── _collections.cpython-313.pyc
│           │           │   │   │   │   ├── _version.cpython-313.pyc
│           │           │   │   │   │   ├── connection.cpython-313.pyc
│           │           │   │   │   │   ├── connectionpool.cpython-313.pyc
│           │           │   │   │   │   ├── exceptions.cpython-313.pyc
│           │           │   │   │   │   ├── fields.cpython-313.pyc
│           │           │   │   │   │   ├── filepost.cpython-313.pyc
│           │           │   │   │   │   ├── poolmanager.cpython-313.pyc
│           │           │   │   │   │   ├── request.cpython-313.pyc
│           │           │   │   │   │   └── response.cpython-313.pyc
│           │           │   │   │   ├── _collections.py
│           │           │   │   │   ├── _version.py
│           │           │   │   │   ├── connection.py
│           │           │   │   │   ├── connectionpool.py
│           │           │   │   │   ├── contrib
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   ├── _appengine_environ.cpython-313.pyc
│           │           │   │   │   │   │   ├── appengine.cpython-313.pyc
│           │           │   │   │   │   │   ├── ntlmpool.cpython-313.pyc
│           │           │   │   │   │   │   ├── pyopenssl.cpython-313.pyc
│           │           │   │   │   │   │   ├── securetransport.cpython-313.pyc
│           │           │   │   │   │   │   └── socks.cpython-313.pyc
│           │           │   │   │   │   ├── _appengine_environ.py
│           │           │   │   │   │   ├── _securetransport
│           │           │   │   │   │   │   ├── __init__.py
│           │           │   │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   │   ├── bindings.cpython-313.pyc
│           │           │   │   │   │   │   │   └── low_level.cpython-313.pyc
│           │           │   │   │   │   │   ├── bindings.py
│           │           │   │   │   │   │   └── low_level.py
│           │           │   │   │   │   ├── appengine.py
│           │           │   │   │   │   ├── ntlmpool.py
│           │           │   │   │   │   ├── pyopenssl.py
│           │           │   │   │   │   ├── securetransport.py
│           │           │   │   │   │   └── socks.py
│           │           │   │   │   ├── exceptions.py
│           │           │   │   │   ├── fields.py
│           │           │   │   │   ├── filepost.py
│           │           │   │   │   ├── packages
│           │           │   │   │   │   ├── __init__.py
│           │           │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   └── six.cpython-313.pyc
│           │           │   │   │   │   ├── backports
│           │           │   │   │   │   │   ├── __init__.py
│           │           │   │   │   │   │   ├── __pycache__
│           │           │   │   │   │   │   │   ├── __init__.cpython-313.pyc
│           │           │   │   │   │   │   │   ├── makefile.cpython-313.pyc
│           │           │   │   │   │   │   │   └── weakref_finalize.cpython-313.pyc
│           │           │   │   │   │   │   ├── makefile.py
│           │           │   │   │   │   │   └── weakref_finalize.py
│           │           │   │   │   │   └── six.py
│           │           │   │   │   ├── poolmanager.py
│           │           │   │   │   ├── request.py
│           │           │   │   │   ├── response.py
│           │           │   │   │   └── util
│           │           │   │   │       ├── __init__.py
│           │           │   │   │       ├── __pycache__
│           │           │   │   │       │   ├── __init__.cpython-313.pyc
│           │           │   │   │       │   ├── connection.cpython-313.pyc
│           │           │   │   │       │   ├── proxy.cpython-313.pyc
│           │           │   │   │       │   ├── queue.cpython-313.pyc
│           │           │   │   │       │   ├── request.cpython-313.pyc
│           │           │   │   │       │   ├── response.cpython-313.pyc
│           │           │   │   │       │   ├── retry.cpython-313.pyc
│           │           │   │   │       │   ├── ssl_.cpython-313.pyc
│           │           │   │   │       │   ├── ssl_match_hostname.cpython-313.pyc
│           │           │   │   │       │   ├── ssltransport.cpython-313.pyc
│           │           │   │   │       │   ├── timeout.cpython-313.pyc
│           │           │   │   │       │   ├── url.cpython-313.pyc
│           │           │   │   │       │   └── wait.cpython-313.pyc
│           │           │   │   │       ├── connection.py
│           │           │   │   │       ├── proxy.py
│           │           │   │   │       ├── queue.py
│           │           │   │   │       ├── request.py
│           │           │   │   │       ├── response.py
│           │           │   │   │       ├── retry.py
│           │           │   │   │       ├── ssl_.py
│           │           │   │   │       ├── ssl_match_hostname.py
│           │           │   │   │       ├── ssltransport.py
│           │           │   │   │       ├── timeout.py
│           │           │   │   │       ├── url.py
│           │           │   │   │       └── wait.py
│           │           │   │   └── vendor.txt
│           │           │   └── py.typed
│           │           ├── pip-25.0.dist-info
│           │           │   ├── AUTHORS.txt
│           │           │   ├── INSTALLER
│           │           │   ├── LICENSE.txt
│           │           │   ├── METADATA
│           │           │   ├── RECORD
│           │           │   ├── REQUESTED
│           │           │   ├── WHEEL
│           │           │   ├── entry_points.txt
│           │           │   └── top_level.txt
│           │           ├── websocket
│           │           │   ├── __init__.py
│           │           │   ├── __pycache__
│           │           │   │   ├── __init__.cpython-313.pyc
│           │           │   │   ├── _abnf.cpython-313.pyc
│           │           │   │   ├── _app.cpython-313.pyc
│           │           │   │   ├── _cookiejar.cpython-313.pyc
│           │           │   │   ├── _core.cpython-313.pyc
│           │           │   │   ├── _exceptions.cpython-313.pyc
│           │           │   │   ├── _handshake.cpython-313.pyc
│           │           │   │   ├── _http.cpython-313.pyc
│           │           │   │   ├── _logging.cpython-313.pyc
│           │           │   │   ├── _socket.cpython-313.pyc
│           │           │   │   ├── _ssl_compat.cpython-313.pyc
│           │           │   │   ├── _url.cpython-313.pyc
│           │           │   │   ├── _utils.cpython-313.pyc
│           │           │   │   └── _wsdump.cpython-313.pyc
│           │           │   ├── _abnf.py
│           │           │   ├── _app.py
│           │           │   ├── _cookiejar.py
│           │           │   ├── _core.py
│           │           │   ├── _exceptions.py
│           │           │   ├── _handshake.py
│           │           │   ├── _http.py
│           │           │   ├── _logging.py
│           │           │   ├── _socket.py
│           │           │   ├── _ssl_compat.py
│           │           │   ├── _url.py
│           │           │   ├── _utils.py
│           │           │   ├── _wsdump.py
│           │           │   ├── py.typed
│           │           │   └── tests
│           │           │       ├── __init__.py
│           │           │       ├── __pycache__
│           │           │       │   ├── __init__.cpython-313.pyc
│           │           │       │   ├── echo-server.cpython-313.pyc
│           │           │       │   ├── test_abnf.cpython-313.pyc
│           │           │       │   ├── test_app.cpython-313.pyc
│           │           │       │   ├── test_cookiejar.cpython-313.pyc
│           │           │       │   ├── test_http.cpython-313.pyc
│           │           │       │   ├── test_url.cpython-313.pyc
│           │           │       │   └── test_websocket.cpython-313.pyc
│           │           │       ├── data
│           │           │       │   ├── header01.txt
│           │           │       │   ├── header02.txt
│           │           │       │   └── header03.txt
│           │           │       ├── echo-server.py
│           │           │       ├── test_abnf.py
│           │           │       ├── test_app.py
│           │           │       ├── test_cookiejar.py
│           │           │       ├── test_http.py
│           │           │       ├── test_url.py
│           │           │       └── test_websocket.py
│           │           └── websocket_client-1.8.0.dist-info
│           │               ├── INSTALLER
│           │               ├── LICENSE
│           │               ├── METADATA
│           │               ├── RECORD
│           │               ├── REQUESTED
│           │               ├── WHEEL
│           │               ├── entry_points.txt
│           │               └── top_level.txt
│           └── pyvenv.cfg
└── run.py

122 directories, 936 files

