%define pypi_name cachetools

Name:           python-cachetools
Version:        4.1.0
Release:        %mkrel 1
Group:          Development/Python
Summary:        Extensible memoizing collections and decorators

License:        MIT
URL:            https://github.com/tkem/cachetools
Source0:        https://pypi.io/packages/source/c/cachetools/cachetools-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)


%description
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library `@lru_cache`_
function decorator.

%package -n     python3-%{pypi_name}
Summary:        Extensible memoizing collections and decorators
Group:          Development/Python
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library `@lru_cache`_
function decorator.


%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
