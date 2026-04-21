#!/usr/bin/env bash
set -euo pipefail

# Publish the Forma static site (formares.org) via rsync/scp.
#
# Usage:
#   ./publish.sh [USER@HOST] [DEST_PATH]
#   ./publish.sh [HOST]      [DEST_PATH]
#
# Environment overrides:
#   USER          — remote username (default: root)
#
# Defaults:
#   HOST          gotchoices.org
#   DEST_PATH     /var/www/formares.org

HOST_ARG="${1:-gotchoices.org}"

if [[ "$HOST_ARG" == *"@"* ]]; then
  REMOTE="$HOST_ARG"
else
  # No username supplied; default to root (matches existing GotChoices sites).
  RUSER="${USER:-root}"
  if [[ "$RUSER" == "$(whoami)" ]]; then
    # If USER is just the current login, prefer root for GotChoices hosts.
    RUSER="root"
  fi
  REMOTE="${RUSER}@${HOST_ARG}"
fi

DEST="${2:-/var/www/formares.org}"

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Publishing ${ROOT_DIR} → ${REMOTE}:${DEST}"

ssh "$REMOTE" "mkdir -p '$DEST'"

EXCLUDES=(
  --exclude "server.sh"
  --exclude "publish.sh"
  --exclude "README.md"
  --exclude ".DS_Store"
  --exclude "*.swp"
)

if command -v rsync >/dev/null 2>&1; then
  rsync -avz --delete "${EXCLUDES[@]}" "$ROOT_DIR/" "$REMOTE:$DEST/"
else
  echo "rsync not found; falling back to scp (no --delete, no excludes)."
  scp -r "$ROOT_DIR"/* "$REMOTE:$DEST/"
fi

HOST_ONLY="${REMOTE##*@}"
echo "Publish complete: https://formares.org/"
echo "(via ${HOST_ONLY})"
