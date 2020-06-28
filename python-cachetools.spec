%define pypi_name cachetools

Name:           python-cachetools
Version:        4.1.0
Release:        1
Group:          Development/Python
Summary:        Extensible memoizing collections and decorators

License:        MIT
URL:            https://github.com/tkem/cachetools
Source0:        https://pypi.io/packages/source/c/cachetools/cachetools-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library `@lru_cache`_
function decorator.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
