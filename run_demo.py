#!/usr/bin/env python3
"""
Run Demo Mode - AI QA Orchestrator
Mock testing with sample scenarios
"""

import subprocess
import sys
from config import config

def main():
    """Run the demo application on configured port"""
    print("🎯 Starting AI QA Orchestrator - Demo Mode")
    print(f"   Running on: http://localhost:{config.DEMO_APP_PORT}")
    print("   Press Ctrl+C to stop")
    print("")
    
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'app.py',
            '--server.port', str(config.DEMO_APP_PORT),
            '--server.headless', 'true',
            '--browser.serverAddress', 'localhost'
        ])
    except KeyboardInterrupt:
        print("\n👋 Demo mode stopped")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()