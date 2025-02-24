# Define Python Library for math utils
py_library(
  name = "math_utils"
  srcs = ["src/math_utils.py"],
  visibility = ["//visibility:public"]
)

# Define Python Library for string utils
py_library(
  name = "string_utils"
  srcs = ["src/string_utils.py"],
  visibility = ["//visibility:public"]
)

# Define unit tests for math utils
py_test(
  name = "test_math_utils",
  srcs = ["tests/test_math_utils.py"],
  deps = [
    ":math_utils",
  ],
)

# Define unit tests for string utils
py_test(
  name = "test_string_utils",
  srcs = ["tests/test_string_utils.py"],
  deps = [
    ":string_utils",
  ],
)

# Linting with pylint
sh_test(
  name = "lint",
  srcs = ["scripts/lint.sh"],
)

#Checks the formatting of the codebase
sh_test(
  name = "format",
  srcs = ["scripts/format.sh"],
)