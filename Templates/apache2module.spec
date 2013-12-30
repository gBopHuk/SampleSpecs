%define modname sample

Name: apache2-mod_%modname
Version: 0.0.1
Release: alt1
Epoch: ...

Summary: ...
License: ...
Group: System/Servers

Url: ...
Packager: ...
BuildArch: ...

Source: mod_%modname-%version.tar
Source1: %modname.load
Source2: %modname.start
Source3: %modname.conf
Patch: ...

PreReq: ...
Requires: %apache2_name-base > 2.2.22-alt15
Requires: %apache2_name-mmn = %apache2_mmn
Requires: %apache2_libaprutil_name >= %apache2_libaprutil_evr
Requires: %apache2_libapr_name >= %apache2_libapr_evr
Provides: ...
Conflicts: ...

BuildRequires(pre): apache2-devel > 2.2.22-alt15
BuildPreReq: ...
BuildRequires: ...

%description
...

%prep
%setup -n mod_%modname-%version
%patch0 -p1

%build
%apache2_apxs ... -c -Wc,-std=gnu99 mod_%modname.c

%install
install -pDm0644 .libs/mod_%modname.so %buildroot%apache2_moduledir/mod_%modname.so
install -pDm0644 %SOURCE1 %buildroot%apache2_mods_available/%modname.load
install -pDm0644 %SOURCE3 %buildroot%apache2_mods_available/%modname.conf
install -pDm0644 %SOURCE2 %buildroot%apache2_mods_start/100-%modname.conf

# for %%ghost
mkdir -p %buildroot%apache2_mods_enabled/
touch %buildroot%apache2_mods_enabled/%modname.load
touch %buildroot%apache2_mods_enabled/%modname.conf

%files
%doc ...
%config(noreplace) %apache2_mods_available/*.load
%config(noreplace) %apache2_mods_available/*.conf
%config(noreplace) %apache2_mods_start/*.conf
%ghost %apache2_mods_enabled/*.load
%ghost %apache2_mods_enabled/*.conf
%apache2_moduledir/*

%changelog
