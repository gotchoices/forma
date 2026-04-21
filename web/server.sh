#!/usr/bin/env bash
# Simple static server for the Forma site (formares.org).
# Usage: ./server.sh [port]
# Default port: 8080

set -euo pipefail

PORT="${1:-8080}"

cd "$(dirname "$0")"

echo "Serving Forma at http://localhost:${PORT}/index.html#home"
echo "Press Ctrl+C to stop."
python3 -m http.server "${PORT}"
