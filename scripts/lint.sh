#!/bin/bash
set -e

pip install pylint
pylint /Users/bobbynewsome/Desktop/python-bazel-ci/tests /Users/bobbynewsome/Desktop/python-bazel-ci/src/*.py --fail-under=8.0