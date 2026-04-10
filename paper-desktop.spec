Name:           paper-desktop
Version:        1.1
Release:        1%{?dist}
Summary:        Official Paper Environment Desktop
License:        GPL
URL:            https://github.com/Superchavo/paper-desktop
BuildArch:      noarch

Requires:       jwm, pcmanfm, xterm, adwaita-icon-theme, lxappearance

%description
Official lightweight desktop environment with full icon support.

%install
# Creamos las carpetas en el sistema
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/etc/skel
mkdir -p %{buildroot}/usr/share/paper-desktop/papericon

# Copiamos los archivos desde tu repo al RPM
cp -r %{_sourcedir}/usr/local/bin/* %{buildroot}/usr/local/bin/
cp %{_sourcedir}/etc/skel/.jwmrc %{buildroot}/etc/skel/.jwmrc
cp %{_sourcedir}/papericon/icon.png %{buildroot}/usr/share/paper-desktop/papericon/icon.png

%files
/usr/local/bin/*
/etc/skel/.jwmrc
/usr/share/paper-desktop/
/usr/share/paper-desktop/papericon/icon.png

%changelog
* Thu Apr 09 2026 Superchavo <superchavoofficialscratchyt@gmail.com> - 1.1-1
- Restored papericon structure to ensure system stability.

