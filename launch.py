#!/usr/bin/env python3
"""
AI QA Orchestrator Launcher
Choose between demo mode and real application testing
"""

import os
import sys
import subprocess
from pathlib import Path
from config import config


def print_banner():
    """Print the application banner"""
    print("""
🤖 AI Quality Assurance Orchestrator
====================================

Comprehensive AI-powered test generation across all quality domains
""")


def check_environment():
    """Check if the environment is properly set up"""
    issues = []
    
    # Check Python version
    if sys.version_info < (3, 11):
        issues.append("Python 3.11+ is required")
    
    # Check if .env file exists
    if not Path('.env').exists():
        issues.append(".env file not found - create from .env.example")
    
    # Check if Anthropic API key is set properly
    if not config.validate_keys():
        issues.append("ANTHROPIC_API_KEY not properly configured in .env file")
    
    # Check if required files exist
    required_files = ['app.py', 'real_app_demo.py', 'requirements.txt', 'config.py']
    for file in required_files:
        if not Path(file).exists():
            issues.append(f"Required file {file} is missing")
    
    return issues


def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True, capture_output=True, text=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False


def launch_demo_mode():
    """Launch demo mode with mock testing"""
    print("🎯 Launching Demo Mode...")
    print("   • Mock test generation and execution")
    print("   • Interactive dashboard with sample scenarios")
    print("   • No real application required")
    print(f"   • Running on port {config.DEMO_APP_PORT}")
    print(f"   • Access at: http://localhost:{config.DEMO_APP_PORT}")
    print("")
    
    try:
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'app.py', '--server.port', str(config.DEMO_APP_PORT)])
    except KeyboardInterrupt:
        print("\n👋 Demo mode stopped by user")
    except Exception as e:
        print(f"❌ Failed to launch demo mode: {e}")


def launch_real_app_mode():
    """Launch real application testing mode"""
    print("🚀 Launching Real Application Testing Mode...")
    print("   • Test your actual application")
    print("   • Real API and UI testing")
    print("   • Actual code coverage and performance metrics")
    print(f"   • Running on port {config.REAL_APP_PORT}")
    print(f"   • Access at: http://localhost:{config.REAL_APP_PORT}")
    print("")
    
    # Check if configuration exists
    config_path = Path("config/app_config.yml")
    if not config_path.exists():
        print("⚙️  Configuration file not found.")
        print("   The application will guide you through the setup process.")
        print("")
    
    try:
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'real_app_demo.py', '--server.port', str(config.REAL_APP_PORT)])
    except KeyboardInterrupt:
        print("\n👋 Real application testing stopped by user")
    except Exception as e:
        print(f"❌ Failed to launch real application testing: {e}")


def show_configuration_help():
    """Show configuration help"""
    print("""
⚙️  Configuration Help
====================

For real application testing, you need to configure your application details:

1. **Create Configuration File**
   Create config/app_config.yml with your application details

2. **Basic Configuration Example:**
   ```yaml
   application:
     name: "My Application"
     type: "web"  # web, api, mobile, desktop
     language: "javascript"  # javascript, python, java, etc.
     framework: "react"  # react, django, flask, etc.

   urls:
     base_url: "http://localhost:3000"
     api_base_url: "http://localhost:3001/api"

   quality_gates:
     unit_test_coverage: 80
     api_test_pass_rate: 100
     security_critical_issues: 0
   ```

3. **Ensure Your Application is Running**
   - Your application should be accessible on the configured URLs
   - API endpoints should be responding
   - Database connections should be active

4. **Required Testing Tools (Optional)**
   ```bash
   # For JavaScript applications
   npm install -g jest newman

   # For Python applications
   pip install pytest requests

   # For browser testing
   npm install -g playwright
   playwright install
   ```

For more details, see the README.md file or visit the configuration tab in the application.
""")


def main():
    """Main launcher function"""
    print_banner()
    
    # Check environment
    issues = check_environment()
    if issues:
        print("❌ Environment Issues Detected:")
        for issue in issues:
            print(f"   • {issue}")
        print("")
        
        if "ANTHROPIC_API_KEY" in str(issues) or ".env file" in str(issues):
            print("💡 To set up your environment:")
            print("   1. Copy: cp env.example .env")
            print("   2. Edit .env file and add your Anthropic API key")
            print("   3. Get your key from: https://console.anthropic.com/")
            print("")
        
        if any("Python" in issue for issue in issues):
            print("💡 Please upgrade to Python 3.11+")
            return
        
        # Ask if user wants to continue anyway
        response = input("Continue anyway? (y/N): ").strip().lower()
        if response != 'y':
            return
    
    # Check if dependencies are installed
    try:
        import streamlit
        import crewai
        import anthropic
    except ImportError:
        print("📦 Some dependencies are missing. Installing...")
        if not install_dependencies():
            return
    
    # Show menu
    print("Choose your testing mode:")
    print("")
    print("1. 🎯 Demo Mode (Mock Testing)")
    print("   • Interactive demonstration with sample scenarios")
    print("   • Mock test generation and execution")
    print("   • No real application required")
    print("")
    print("2. 🚀 Real Application Testing")
    print("   • Test your actual AI application")
    print("   • Real API and UI testing")
    print("   • Actual metrics and coverage reports")
    print("")
    print("3. ⚙️  Configuration Help")
    print("   • Guide for setting up real application testing")
    print("")
    print("4. ❌ Exit")
    print("")
    
    while True:
        try:
            choice = input("Select option (1-4): ").strip()
            
            if choice == '1':
                launch_demo_mode()
                break
            elif choice == '2':
                launch_real_app_mode()
                break
            elif choice == '3':
                show_configuration_help()
                input("\nPress Enter to continue...")
                continue
            elif choice == '4':
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please select 1, 2, 3, or 4.")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except EOFError:
            print("\n👋 Goodbye!")
            break


if __name__ == "__main__":
    main()