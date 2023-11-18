#!/bin/bash

black .
isort .
ruff .

# chmod +x lint_format.sh