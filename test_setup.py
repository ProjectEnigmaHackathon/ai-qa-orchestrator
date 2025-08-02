#!/usr/bin/env python3
"""
Test the setup and configuration
"""

import sys
from pathlib import Path

def test_setup():
    """Test if everything is set up correctly"""
    print("🧪 Testing AI QA Orchestrator Setup...")
    print("=" * 50)
    
    errors = []
    
    # Test config import
    try:
        from config import config
        print("✅ Config module imported successfully")
        
        # Test API key loading
        api_key = config.get_anthropic_key()
        if api_key and api_key != 'demo-key-for-development':
            print("✅ Anthropic API key loaded from .env")
        else:
            print("⚠️  Using demo API key (.env file setup needed)")
            
        # Test port configuration
        print(f"✅ Real App Port: {config.REAL_APP_PORT}")
        print(f"✅ Demo App Port: {config.DEMO_APP_PORT}")
        
    except ImportError as e:
        errors.append(f"Config import failed: {e}")
    
    # Test required files
    required_files = [
        'app.py',
        'real_app_demo.py', 
        'config.py',
        'launch.py',
        'run_demo.py',
        'run_real_app.py',
        'env.example',
        'requirements.txt'
    ]
    
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file} exists")
        else:
            errors.append(f"Missing file: {file}")
    
    # Test imports
    test_imports = [
        'streamlit',
        'crewai', 
        'anthropic',
        'langchain_anthropic',
        'dotenv'
    ]
    
    for module in test_imports:
        try:
            __import__(module)
            print(f"✅ {module} import successful")
        except ImportError:
            errors.append(f"Module not installed: {module}")
    
    print("=" * 50)
    
    if errors:
        print("❌ Setup Issues Found:")
        for error in errors:
            print(f"   • {error}")
        print("\n💡 Run: pip install -r requirements.txt")
        print("💡 Create .env file from env.example")
        return False
    else:
        print("🎉 Setup Complete! Ready to run AI QA Orchestrator")
        print(f"\n🚀 Start Real App Testing: python run_real_app.py")
        print(f"🎯 Start Demo Mode: python run_demo.py")
        print(f"📋 Interactive Launcher: python launch.py")
        return True

if __name__ == "__main__":
    success = test_setup()
    sys.exit(0 if success else 1)