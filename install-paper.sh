#!/bin/bash
# Paper ENVIRONMENT - Installer
# Developer: Superchavo

echo "--------------------------------------------------"
echo "   🚀 Installing Paper ENVIRONMENT (Bunker v1)   "
echo "--------------------------------------------------"

# 1. INSTALAR DEPENDENCIAS
echo "[1/3] Downloading JWM, PCManFM, YAD and more..."
su -c 'dnf install jwm pcmanfm yad xterm xdotool hicolor-icon-theme -y'

# 2. CONFIGURAR SCRIPTS (Paper-Utils)
echo "[2/3] Setting up Paper-Utils in /usr/local/bin..."
# Usamos el directorio donde está el script para copiar los archivos
CURRENT_DIR=$(pwd)
su -c "cp $CURRENT_DIR/usr/local/bin/paper-* /usr/local/bin/"
su -c "cp $CURRENT_DIR/usr/local/bin/paperpopup /usr/local/bin/"
su -c 'chmod +x /usr/local/bin/paper-* /usr/local/bin/paperpopup'

# 3. CONFIGURAR SETTINGS (JWM y Desktop)
echo "[3/3] Applying Superchavo's custom settings..."
# Copiamos la configuración de JWM al home del usuario
cp $CURRENT_DIR/etc/skel/.jwmrc ~/.jwmrc

# Crear el perfil de escritorio para PCManFM (para que no se vea vacío)
mkdir -p ~/.config/pcmanfm/paper
cat <<CONF > ~/.config/pcmanfm/paper/desktop-items-0.conf
[*]
desktop_bg_0=#004687
desktop_fg_0=#ffffff
desktop_shadow_0=#000000
show_wm_menu=0
CONF

echo "--------------------------------------------------"
echo "   ✅ DONE! Your bunker is ready.               "
echo "   Type 'paper-session' to start.               "
echo "--------------------------------------------------"
