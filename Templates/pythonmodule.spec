%define modulename foo

Name: python-module-%modulename
Version: 1.0
Release: alt1

%setup_python_module %modulename

Summary: ...
License: GPL
Group: Development/Python

Url: http://...
Packager:
BuildArch: noarch

Source: %name-%version.tar

#BuildPreReq: %py_dependencies setuptools

%description
...

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info
