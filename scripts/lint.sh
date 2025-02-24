#!/bin/bash
set -e

pip install pylint
pylint pylint src/*.py tests/*.py --fail-under=8.0