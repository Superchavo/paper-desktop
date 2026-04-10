Name:           paper-desktop
Version:        1.2
Release:        1%{?dist}
Summary:        A lightweight desktop environment based on JWM
Group:          User Interface/Desktops
License:        MIT
URL:            https://github.com/Superchavo/paper-desktop
BuildArch:      noarch

# Core Dependencies
Requires:       jwm
Requires:       feh
Requires:       adwaita-icon-theme
Requires:       pcmanfm

# Weak Dependencies
Recommends:     fastfetch

%description
Paper Desktop is a minimal, high-performance desktop environment 
built on top of JWM, designed for efficiency and simplicity. 
It includes PCManFM for file management and the custom paper-info tool.
Developed by Superchavo.

%prep
# No compilation required

%install
# 1. Create directory structure
mkdir -p %{buildroot}/usr/share/paper-desktop/papericon
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/etc/skel/
mkdir -p %{buildroot}/usr/share/xsessions

# 2. Copy files from local repository
cp %{_sourcedir}/papericon/icon.png %{buildroot}/usr/share/paper-desktop/papericon/icon.png
cp %{_sourcedir}/usr/local/bin/paper-session %{buildroot}/usr/local/bin/
cp %{_sourcedir}/usr/local/bin/paper-menu-gen %{buildroot}/usr/local/bin/
cp %{_sourcedir}/usr/local/bin/paper-about %{buildroot}/usr/local/bin/
cp %{_sourcedir}/usr/local/bin/paperpopup %{buildroot}/usr/local/bin/
cp %{_sourcedir}/usr/local/bin/paper-info %{buildroot}/usr/local/bin/

# JWM Config deployment
if [ -f %{_sourcedir}/etc/skel/.jwmrc ]; then
    cp %{_sourcedir}/etc/skel/.jwmrc %{buildroot}/etc/skel/
else
    cp %{_sourcedir}/.jwmrc %{buildroot}/etc/skel/
fi

# 3. Create Session file for Display Managers
cat <<EOF > %{buildroot}/usr/share/xsessions/paper.desktop
[Desktop Entry]
Name=Paper Desktop
Name[es]=Paper Desktop
Comment=Lightweight environment by Superchavo
Exec=/usr/local/bin/paper-session
Type=Application
DesktopNames=Paper
EOF

%post
# Set execution permissions
chmod +x /usr/local/bin/paper-session
chmod +x /usr/local/bin/paper-menu-gen
chmod +x /usr/local/bin/paper-about
chmod +x /usr/local/bin/paperpopup
chmod +x /usr/local/bin/paper-info

%files
/usr/share/paper-desktop/papericon/icon.png
/usr/local/bin/paper-session
/usr/local/bin/paper-menu-gen
/usr/local/bin/paper-about
/usr/local/bin/paperpopup
/usr/local/bin/paper-info
/etc/skel/.jwmrc
/usr/share/xsessions/paper.desktop

%changelog
* Fri Apr 10 2026 Superchavo <superchavoofficialscratchyt@gmail.com> - 1.2-1
- Version 1.2 release
- Added paper-info tool with ASCII art
- Fixed paper-info memory reporting for proot compatibility
- Full English localization of spec metadata

