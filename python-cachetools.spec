Summary:	Extensible memoizing collections and decorators
Name:		python-cachetools
Version:	5.2.1
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/tkem/cachetools
Source0:	https://pypi.io/packages/source/c/cachetools/cachetools-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)

BuildArch:	noarch

%description
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library `@lru_cache`_
function decorator.

%files
%doc README.rst
%license LICENSE
%{py_puresitedir}/cachetools
%{py_puresitedir}/cachetools-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -n cachetools-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%py_build

%install
%py_install

