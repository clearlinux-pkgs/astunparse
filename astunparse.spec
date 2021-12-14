#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : astunparse
Version  : 1.6.3
Release  : 40
URL      : https://files.pythonhosted.org/packages/f3/af/4182184d3c338792894f34a62672919db7ca008c89abee9b564dd34d8029/astunparse-1.6.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/f3/af/4182184d3c338792894f34a62672919db7ca008c89abee9b564dd34d8029/astunparse-1.6.3.tar.gz
Summary  : An AST unparser for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: astunparse-license = %{version}-%{release}
Requires: astunparse-python = %{version}-%{release}
Requires: astunparse-python3 = %{version}-%{release}
Requires: six
Requires: wheel
BuildRequires : buildreq-distutils3
BuildRequires : py
BuildRequires : pytest
BuildRequires : six
BuildRequires : testtools
BuildRequires : wheel

%description
AST Unparser
        ============

%package license
Summary: license components for the astunparse package.
Group: Default

%description license
license components for the astunparse package.


%package python
Summary: python components for the astunparse package.
Group: Default
Requires: astunparse-python3 = %{version}-%{release}

%description python
python components for the astunparse package.


%package python3
Summary: python3 components for the astunparse package.
Group: Default
Requires: python3-core
Provides: pypi(astunparse)
Requires: pypi(six)
Requires: pypi(wheel)

%description python3
python3 components for the astunparse package.


%prep
%setup -q -n astunparse-1.6.3
cd %{_builddir}/astunparse-1.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635704269
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/astunparse
cp %{_builddir}/astunparse-1.6.3/LICENSE %{buildroot}/usr/share/package-licenses/astunparse/b291a42f7b452849ae06ea2f18af4afde57cce2e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/astunparse/b291a42f7b452849ae06ea2f18af4afde57cce2e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
