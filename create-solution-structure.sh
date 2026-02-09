#!/bin/bash

# Script to create directory structure for DSA solutions
# Usage: bash create-solution-structure.sh <student_name> [language1 language2 ...]
# Supported languages: python, js, c, cpp, java, go, rust, dart
# Default languages (if none specified): python, js, c, cpp

if [ -z "$1" ]; then
    echo "Usage: bash create-solution-structure.sh <student_name> [language1 language2 ...]"
    echo ""
    echo "Example with default languages (python, js, c, cpp):"
    echo "  bash create-solution-structure.sh deo-bata"
    echo ""
    echo "Example with specific languages:"
    echo "  bash create-solution-structure.sh deo-bata python js"
    echo ""
    echo "Supported languages: python, js, c, cpp, java, go, rust, dart"
    exit 1
fi

STUDENT_NAME=$1
shift  # Remove first argument, remaining are languages

# Supported languages
SUPPORTED_LANGUAGES=("python" "js" "c" "cpp" "java" "go" "rust" "dart")

# Default languages if none specified
if [ $# -eq 0 ]; then
    LANGUAGES=("python" "js" "c" "cpp")
else
    LANGUAGES=("$@")
fi

# Validate languages
for lang in "${LANGUAGES[@]}"; do
    if [[ ! " ${SUPPORTED_LANGUAGES[@]} " =~ " ${lang} " ]]; then
        echo "❌ Error: '$lang' is not a supported language"
        echo "Supported languages: ${SUPPORTED_LANGUAGES[*]}"
        exit 1
    fi
done

BASE_PATH="solutions/$STUDENT_NAME"
PROBLEM_DIRS=("p-00-general" "p-01-conditions" "p-02-arrays" "p-03-strings" "p-04-loops" "p-05-functions")

# Create directory structure for each specified language
for lang in "${LANGUAGES[@]}"; do
    for problem_dir in "${PROBLEM_DIRS[@]}"; do
        mkdir -p "$BASE_PATH/$lang/$problem_dir"
    done
done

echo "✓ Directory structure created successfully for $STUDENT_NAME!"
echo ""
echo "Languages: ${LANGUAGES[*]}"
echo "Structure created at: $BASE_PATH/"
echo ""
echo "You can now start adding your solution files:"
echo "  - $BASE_PATH/python/p-01-conditions/solution-01.py"
echo "  - $BASE_PATH/js/p-02-arrays/solution-01.js"
echo "  - etc."
