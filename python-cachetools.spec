%define module cachetools

Summary:	Extensible memoizing collections and decorators
Name:		python-cachetools
Version:	6.2.4
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/tkem/cachetools
Source0:	https://pypi.io/packages/source/c/%{module}/%{module}-%{version}.tar.gz
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

%prep
%autosetup -n %{module}-%{version}

# Remove bundled egg-info
rm -rf src/%{module}.egg-info

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
