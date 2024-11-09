#!/bin/bash
PORT=${PORT:-8000}
# Determine the directory of the current script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $SCRIPT_DIR/../app
poetry run streamlit run app.py --server.port $PORT --server.address 0.0.0.0
