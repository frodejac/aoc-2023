#!/usr/bin/env bash
black --check
isort --check
pyright --warnings
fixit lint