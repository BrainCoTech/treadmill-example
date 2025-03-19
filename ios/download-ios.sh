#!/bin/bash
set -e # Exit on error

# Check platform compatibility
if [[ "$OSTYPE" == "msys" ]]; then
  echo -e "\033[0;31mError: This script does not support your platform ($OSTYPE)\033[0m"
  exit 1
fi

# Colorful echo functions
echo_y() { echo -e "\033[1;33m$*\033[0m"; } # Yellow
echo_r() { echo -e "\033[0;31m$*\033[0m"; } # Red

# Get the script's directory to handle paths relative to it
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIST_DIR="${SCRIPT_DIR}/dist"
ZIP_NAME="ios.zip"

# Configuration
LIB_VERSION="v0.0.4"
BASE_URL="https://app.brainco.cn/universal/treadmill/libs/${LIB_VERSION}"
LIB_NAME="ios"
DOWNLOAD_URL="${BASE_URL}/${ZIP_NAME}?$(date +%s)" # Use timestamp for uniqueness

# Clean up previous files
echo_y "[treadmill-sdk] Cleaning up previous distribution..."
rm -rf "$DIST_DIR" "${SCRIPT_DIR}/__MACOSX" "${SCRIPT_DIR}/${ZIP_NAME}"

# Create dist directory if it doesn't exist
mkdir -p "$DIST_DIR"

# Download library
echo_y "[treadmill-sdk] Downloading ${LIB_NAME} (${LIB_VERSION})..."
echo_y "[treadmill-sdk] Download URL: ${DOWNLOAD_URL}"
if ! command -v wget >/dev/null 2>&1; then
  echo_r "Error: wget is not installed. Please install it and try again."
  exit 1
fi

wget -q --show-progress "$DOWNLOAD_URL" -O "${SCRIPT_DIR}/${ZIP_NAME}" || {
  echo_r "Error: Failed to download ${ZIP_NAME}"
  exit 1
}

# Extract and clean up
echo_y "[treadmill-sdk] Extracting ${ZIP_NAME}..."
unzip -o -q "${SCRIPT_DIR}/${ZIP_NAME}" -d "$DIST_DIR" || {
  echo_r "Error: Failed to unzip ${ZIP_NAME}"
  exit 1
}
rm -f "${SCRIPT_DIR}/${ZIP_NAME}"
rm -rf "${SCRIPT_DIR}/__MACOSX"
rm -rf "${DIST_DIR}/__MACOSX"

echo_y "[treadmill-${LIB_NAME}-sdk] (${LIB_VERSION}) downloaded successfully to ${DIST_DIR}"
