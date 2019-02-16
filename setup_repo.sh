#!/bin/bash
set -e
git config --local --replace-all include.path ../.project_config
cd .git/hooks/
ln -s ../../hooks/committed_file_limiter.py pre-commit
