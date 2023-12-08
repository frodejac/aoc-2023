#!/usr/bin/env bash
set -e
ruff check
pyright --warnings
fixit lint
vulture .