#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Oslo Context library
Summary(pl.UTF-8):	Biblioteka Oslo Context
Name:		python3-oslo.context
Version:	6.1.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/oslo-context/
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.context/oslo_context-%{version}.tar.gz
# Source0-md5:	a93f7e92e6bfa231bbc9efc327defdde
URL:		https://pypi.org/project/oslo.context/
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-pbr >= 6.1.1
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-oslotest >= 3.2.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-typing_extensions >= 4.12.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-openstackdocstheme >= 2.2.0
BuildRequires:	python3-reno >= 3.1.0
BuildRequires:	sphinx-pdg-3 >= 2.0.0
%endif
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Oslo context library has helpers to maintain useful information
about a request context. The request context is usually populated in
the WSGI pipeline and used by various modules such as logging.

%description -l pl.UTF-8
Biblioteka Oslo context zawiera funkcje pomocnicze do utrzymywania
przydatnych informacji o kontekście żądania. Kontest ten jest zwykle
wypełniany w potoku WSGI i używany przez różne moduły, np. logowanie.

%package apidocs
Summary:	API documentation for Python oslo.context module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona oslo.context
Group:		Documentation

%description apidocs
API documentation for Python oslo.context module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona oslo.context.

%prep
%setup -q -n oslo_context-%{version}

%build
%py3_build

%if %{with tests}
stestr-3 run
%endif

%if %{with doc}
sphinx-build-3 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/oslo_context/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/oslo_context
%{py3_sitescriptdir}/oslo.context-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,install,reference,user,*.html,*.js}
%endif
