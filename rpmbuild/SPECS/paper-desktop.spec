Name:           paper-desktop
Version:        1.1
Release:        1%{?dist}
Summary:        Official Paper Environment Desktop
License:        GPL
URL:            https://github.com/Superchavo/paper-env
BuildArch:      noarch

Requires:       jwm, pcmanfm, xterm, adwaita-icon-theme

%description
Official lightweight desktop environment developed by Superchavo.

%install
# Copying files to buildroot
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/etc/skel
cp -r usr/local/bin/* %{buildroot}/usr/local/bin/
cp etc/skel/.jwmrc %{buildroot}/etc/skel/.jwmrc

%files
/usr/local/bin/*
/etc/skel/.jwmrc

%changelog
* Thu Apr 09 2026 Superchavo <superchavoofficialscratchyt@gmail.com> - 1.1-1
- Rebuilt from scratch. Added 📄 icon and fixed menu structure.

