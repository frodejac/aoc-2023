#!/usr/bin/env bash
set -e
black . --check
isort . --check
pyright --warnings
fixit lint
flake8