#!/bin/bash
# Paper ENVIRONMENT - Universal Installer
# Developer: Superchavo

echo "--------------------------------------------------"
echo "   🚀 Installing Paper ENVIRONMENT (Bunker v1)   "
echo "--------------------------------------------------"

# 1. DEPENDENCIES
echo "[1/4] Installing system dependencies..."
# This works on both Proot and Real Fedora PC
if [ -x "$(command -v sudo)" ]; then
    sudo dnf install jwm pcmanfm yad xterm xdotool hicolor-icon-theme adwaita-icon-theme -y
else
    su -c 'dnf install jwm pcmanfm yad xterm xdotool hicolor-icon-theme adwaita-icon-theme -y'
fi

# 2. BINARIES AND SCRIPTS
echo "[2/4] Deploying Paper-Utils to /usr/local/bin..."
CURRENT_DIR=$(pwd)

# Function to copy with correct permissions
install_script() {
    if [ -x "$(command -v sudo)" ]; then
        sudo cp "$1" /usr/local/bin/
        sudo chmod +x /usr/local/bin/$(basename "$1")
    else
        su -c "cp $1 /usr/local/bin/ && chmod +x /usr/local/bin/$(basename $1)"
    fi
}

# Copying scripts from the repo folders
install_script "$CURRENT_DIR/usr/local/bin/paper-session"
install_script "$CURRENT_DIR/usr/local/bin/paper-about"
install_script "$CURRENT_DIR/usr/local/bin/paper-menu-gen"
install_script "$CURRENT_DIR/usr/local/bin/paperpopup"

# 3. APPEARANCE SETTINGS (.Xresources)
echo "[3/4] Optimizing UI rendering and Fonts..."
cat <<XRES > ~/.Xresources
Xft.antialias: 1
Xft.hinting: 1
Xft.rgba: rgb
Xft.autohint: 0
Xft.hintstyle: hintslight
Xft.lcdfilter: lcddefault

PaperTerminal*background: #1c1c1c
PaperTerminal*foreground: #ffffff
PaperTerminal*faceName: Monospace:size=10
XRES

# Apply Xresources if display is active
if [ -n "$DISPLAY" ]; then
    xrdb -merge ~/.Xresources
fi

# 4. DESKTOP CONFIGURATION
echo "[4/4] Applying custom JWM and Desktop settings..."
# Deploy .jwmrc from repo to home
if [ -f "$CURRENT_DIR/etc/skel/.jwmrc" ]; then
    cp "$CURRENT_DIR/etc/skel/.jwmrc" ~/.jwmrc
fi

# Setup PCManFM blue background
mkdir -p ~/.config/pcmanfm/default
cat <<PCMAN > ~/.config/pcmanfm/default/desktop-items-0.conf
[*]
desktop_bg_0=#004687
desktop_fg_0=#ffffff
desktop_shadow_0=#000000
show_wm_menu=0
wallpaper_mode=color
PCMAN

echo "--------------------------------------------------"
echo "   ✅ INSTALLATION SUCCESSFUL!                  "
echo "   Developer: Superchavo                        "
echo "   Command: 'paper-session' to start the bunker "
echo "--------------------------------------------------"
