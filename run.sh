#!/bin/bash

# AI Quality Assurance Orchestrator - Run Script
# 
# This script sets up and runs the AI Quality Assurance Orchestrator

echo "🤖 AI Quality Assurance Orchestrator"
echo "======================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.11"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "⚠️  Python 3.11+ is required. Current version: $python_version"
    echo "Please upgrade Python and try again."
    exit 1
fi

# Check if ANTHROPIC_API_KEY is set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  ANTHROPIC_API_KEY environment variable is not set."
    echo "Please set your Anthropic API key:"
    echo "export ANTHROPIC_API_KEY='your-api-key-here'"
    echo ""
    echo "You can also create a .env file with:"
    echo "ANTHROPIC_API_KEY=your-api-key-here"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade requirements
echo "📚 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Check if Streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit installation failed. Please check requirements.txt"
    exit 1
fi

echo ""
echo "🚀 Starting AI Quality Assurance Orchestrator..."
echo "   Dashboard will open at: http://localhost:8501"
echo ""
echo "🎯 Demo Features:"
echo "   • 11 Specialized AI Agents"
echo "   • 6 Testing Domains Covered"
echo "   • Real-time Test Generation"
echo "   • Comprehensive Quality Scoring"
echo "   • CI/CD Pipeline Integration"
echo ""
echo "📖 Usage:"
echo "   1. Select a demo scenario or enter your user story"
echo "   2. Configure testing preferences in the sidebar"
echo "   3. Click 'Generate Comprehensive Test Suite'"
echo "   4. Watch AI agents collaborate in real-time"
echo "   5. Review results and export test suites"
echo ""
echo "🛑 To stop the application, press Ctrl+C"
echo ""

# Run Streamlit app
streamlit run app.py

echo "👋 Thank you for using AI Quality Assurance Orchestrator!"