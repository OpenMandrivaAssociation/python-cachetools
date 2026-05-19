%define module cachetools
%bcond tests 1

Summary:	Extensible memoizing collections and decorators
Name:		python-cachetools
Version:	7.1.3
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://github.com/tkem/cachetools
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library `@lru_cache`_
function decorator.

%prep -a
# Remove bundled egg-info
rm -rf src/%{module}.egg-info

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
%{__python3} -m unittest
%endif

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
