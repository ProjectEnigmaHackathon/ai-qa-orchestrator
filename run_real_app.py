#!/usr/bin/env python3
"""
Run Real Application Mode - AI QA Orchestrator
Test your actual applications with AI agents
"""

import subprocess
import sys
from config import config

def main():
    """Run the real application testing on configured port"""
    print("🚀 Starting AI QA Orchestrator - Real Application Testing")
    print(f"   Running on: http://localhost:{config.REAL_APP_PORT}")
    print("   Press Ctrl+C to stop")
    print("")
    
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'real_app_demo.py',
            '--server.port', str(config.REAL_APP_PORT),
            '--server.headless', 'true',
            '--browser.serverAddress', 'localhost'
        ])
    except KeyboardInterrupt:
        print("\n👋 Real application testing stopped")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()