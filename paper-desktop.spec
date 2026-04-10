Name:           paper-desktop
Version:        1.1
Release:        1%{?dist}
Summary:        A lightweight and elegant desktop environment based on JWM.
License:        GPL
URL:            https://github.com/Superchavo/paper-desktop
BuildArch:      noarch

# Dependencies for everyone
Requires:       jwm, pcmanfm, xterm, adwaita-icon-theme, lxappearance

%description
Official Paper Environment. Includes all system scripts, custom JWM 
configuration, and tools for a seamless blue-themed experience.

%install
# 1. Create the system structure inside the RPM
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/etc/skel
mkdir -p %{buildroot}/usr/share/paper-desktop

# 2. Guardar los scripts (from your repo to the RPM)
cp -r %{_sourcedir}/usr/local/bin/* %{buildroot}/usr/local/bin/

# 3. Guardar el .jwmrc en skel (para que nuevos usuarios lo tengan)
cp %{_sourcedir}/etc/skel/.jwmrc %{buildroot}/etc/skel/.jwmrc

# 4. Guardar iconos o recursos extra si existen
if [ -d %{_sourcedir}/papericon ]; then
    cp -r %{_sourcedir}/papericon %{buildroot}/usr/share/paper-desktop/
fi

%files
/usr/local/bin/*
/etc/skel/.jwmrc
/usr/share/paper-desktop/

%changelog
* Thu Apr 09 2026 Superchavo <superchavoofficialscratchyt@gmail.com> - 1.1-1
- Full system integration. Scripts, config, and icons included in a single package.


