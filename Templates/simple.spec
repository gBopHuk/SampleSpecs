Name: <имя-пакета>
Version: <версия-пакета>
Release: alt<релиз-пакета>

Summary: <однострочное описание>
License: <лицензия>
Group: <группа>

Url: <URL>
Source: %name-%version.tar
Patch:
Packager: <ваше имя> <$login@altlinux.org>

PreReq:
Requires:
Provides:
Conflicts:

BuildPreReq:
BuildRequires:
BuildArch:

%description
<многострочное
описание>

%prep
%setup
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS NEWS README

%changelog
* <дата> <ваше имя> <$login@altlinux.org> <версия-пакета>-<релиз пакета>
- initial build for ALT Linux Sisyphus
