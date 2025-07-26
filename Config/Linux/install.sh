#!/bin/sh

# ==============================================================================
# Hackesoup - Installation Script for Linux (POSIX Compliant)
# ==============================================================================
# This script is written to be compliant with POSIX sh, making it highly
# compatible across different Linux systems (like those using dash as /bin/sh).
# ==============================================================================

# --- Script Settings ---
set -eu

# --- Color Definitions ---
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# --- Helper Functions ---
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
    exit 1
}

# --- Script Main Body ---

# 1. Determine Project Root Directory
# Using a POSIX-compliant way to get the script's directory.
SCRIPT_DIR=$(cd -- "$(dirname -- "$0")" &> /dev/null && pwd)
PROJECT_ROOT=$(cd -- "$SCRIPT_DIR/../../" &> /dev/null && pwd)

log_info "Project root directory found: $PROJECT_ROOT"
cd "$PROJECT_ROOT"

# 2. Welcome Message
echo "=========================================="
log_info "Starting Hackesoup installation..."
echo "=========================================="
sleep 1

# 3. Check System Dependencies
log_info "Checking system dependencies..."
DEPS="python3 pip git"
for dep in $DEPS; do
    if ! command -v "$dep" > /dev/null 2>&1; then
        log_error "Dependency '$dep' not found. Please install it first."
        echo "On Debian/Ubuntu, you can try running: sudo apt-get install python3 python3-pip git"
        echo "On RHEL/CentOS/Fedora, you can try running: sudo dnf install python3 python3-pip git"
        exit 1
    fi
done
# Check for venv module
if ! python3 -c "import venv" > /dev/null 2>&1; then
    log_error "Python3 'venv' module not found."
    echo "On Debian/Ubuntu, you can try running: sudo apt-get install python3-venv"
    exit 1
fi
log_info "All system dependencies are met."
sleep 1

# 4. Create Python Virtual Environment
VENV_DIR=".venv"
if [ -d "$VENV_DIR" ]; then
    log_warn "Virtual environment directory '$VENV_DIR' already exists. Skipping creation."
else
    log_info "Creating Python virtual environment in '$VENV_DIR'..."
    python3 -m venv "$VENV_DIR"
fi
log_info "Activating the virtual environment (for this script's session)..."
# MODIFICATION: Changed 'source' to '.' for POSIX compatibility.
# This is the fix for the "source: not found" error.
. "$VENV_DIR/bin/activate"
log_info "Current Python version: $(python --version)"
sleep 1

# 5. Install Python Dependencies
REQUIREMENTS_FILE="requirements.txt"
if [ -f "$REQUIREMENTS_FILE" ]; then
    log_info "Installing Python dependencies from '$REQUIREMENTS_FILE'..."
    pip install -r "$REQUIREMENTS_FILE"
    log_info "All Python dependencies have been installed successfully."
else
    log_warn "'$REQUIREMENTS_FILE' not found. Skipping Python dependency installation."
fi
sleep 1

# 6. Set File Permissions
log_info "Setting executable permissions for main scripts..."
find "Interfaces" -name "*.py" -exec chmod +x {} \;
find "Soup/Tools" -name "*.py" -exec chmod +x {} \;
log_info "File permissions set."
sleep 1

# 7. Installation Complete
echo
echo "=========================================="
log_info "Hackesoup has been installed successfully!"
echo "=========================================="
echo
echo "How to Run:"
echo "1. First, activate the virtual environment:"
echo -e "   ${YELLOW}. ${PROJECT_ROOT}/${VENV_DIR}/bin/activate${NC}" # Also changed here for consistency
echo
echo "2. Then, run the main application from the project root (e.g., the CLI):"
echo -e "   ${YELLOW}python3 Interfaces/hscli.py${NC}"
echo
echo "When you are done, you can exit the virtual environment by typing 'deactivate'."
echo