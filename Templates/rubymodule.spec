# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname <pkgname>

Name: ruby-%pkgname
Version: 0.1
Release: alt1

Summary: FILL ME
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/%pkgname

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Sun Sep 32 3001 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
FILL ME.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%check
%ruby_test_unit -Ilib:test test

%files
%doc README
%ruby_sitelibdir/*
# For arch-specific files
#%%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sun Sep 32 3001 Sample Packager <sample@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus
