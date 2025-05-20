#!/bin/bash

# Run all tests for the Psycho-Color Analysis System
# This script executes all test suites and reports results

echo "Running Psycho-Color Analysis System Tests"
echo "=========================================="
echo

# Set up Python path to include parent directory
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Run color analysis tests
echo "Running Color Analysis Tests..."
python3 -m unittest tests/test_color_analysis.py
if [ $? -eq 0 ]; then
    echo "✅ Color Analysis Tests: PASSED"
else
    echo "❌ Color Analysis Tests: FAILED"
fi
echo

# Run LLM integration tests
echo "Running LLM Integration Tests..."
python3 -m unittest tests/test_llm_integration.py
if [ $? -eq 0 ]; then
    echo "✅ LLM Integration Tests: PASSED"
else
    echo "❌ LLM Integration Tests: FAILED"
fi
echo

# Run profile and API tests
echo "Running Profile and API Tests..."
python3 -m unittest tests/test_profile_and_api.py
if [ $? -eq 0 ]; then
    echo "✅ Profile and API Tests: PASSED"
else
    echo "❌ Profile and API Tests: FAILED"
fi
echo

# Run UI validation tests
echo "Validating UI Files..."
if [ -f "code/ui/index.html" ] && [ -f "code/ui/styles.css" ] && [ -f "code/ui/app.js" ]; then
    echo "✅ UI Files Validation: PASSED"
else
    echo "❌ UI Files Validation: FAILED"
fi
echo

echo "Test Summary"
echo "============"
echo "All test suites have been executed."
echo "Please review any failures and fix issues before deployment."
