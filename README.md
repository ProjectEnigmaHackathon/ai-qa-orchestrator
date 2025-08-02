# AI Quality Assurance Orchestrator

## 🤖 Comprehensive AI-Powered Test Generation System

A revolutionary AI-powered system that automatically generates comprehensive test suites across all quality domains using specialized CrewAI agents.

> **🆕 Latest Update**: Now featuring **12 AI Agents** with **Test Code Generator**, **Dynamic Metrics**, **Source Code Analysis**, **Complete Project Export**, and **Dual Port Architecture** for simultaneous demo and real application testing!

### 🌟 Key Features

- **🎯 Multi-Agent Architecture**: 12 specialized AI agents with dual modes (Story Analysis + Application Discovery)
- **📊 Comprehensive Testing**: Unit, Integration, Security, Performance, AI Validation, Edge Cases + Test Code Generation
- **🔍 Risk-Based Analysis**: Intelligent risk assessment and test prioritization
- **⚡ Real-Time Generation**: Complete test suites with executable scripts in under 60 seconds
- **📈 Quality Scoring**: Advanced quality metrics and production readiness assessment
- **🔄 CI/CD Integration**: Seamless pipeline integration with quality gates
- **📱 Interactive Dashboard**: Rich visualizations and detailed reporting
- **🛠️ Test Code Export**: Download complete pytest automation projects with CI/CD configs
- **🔐 Secure Configuration**: Environment-based API key management with .env files
- **🚀 Simultaneous Showcase**: Run demo and real application testing on different ports

### 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│          Streamlit Dashboard (Dual Port Setup)             │
│      Real App Testing (8501) | Demo Mode (8502)            │
├─────────────────────────────────────────────────────────────┤
│                QA Orchestration Engine                      │
├─────────────────────────────────────────────────────────────┤
│  🎯 QA         📋 Story      🔍 Application  ⚠️  Risk      │
│  Orchestrator  Analyst       Discovery      Assessor      │
│                              Agent                         │
├─────────────────────────────────────────────────────────────┤
│  🧪 Unit       🔗 Integration 🔒 Security    ⚡ Performance │ 
│  Test Agent    Test Agent     Test Agent     Test Agent     │
├─────────────────────────────────────────────────────────────┤
│  🤖 AI         🎪 Edge Case   📝 Test Code   🚀 Test       │
│  Validation    Test Agent     Generator      Executor      │
│  Agent                        Agent          Agent         │
├─────────────────────────────────────────────────────────────┤
│              ✅ Quality Reviewer Agent                     │
├─────────────────────────────────────────────────────────────┤
│    Test Generators | Risk Analyzer | Quality Scorer        │
│         AI Validation Metrics | Code Export Tools          │
├─────────────────────────────────────────────────────────────┤
│     Anthropic Claude 3.5 | LangChain | CrewAI | Streamlit  │
└─────────────────────────────────────────────────────────────┘
```

## 🔄 Dual Testing Modes

### 📋 **Demo Mode** (Story-based Testing) - Port 8502
- **Story Analyst Agent** analyzes user stories and requirements
- Perfect for prototypes, demos, and concept validation  
- Uses traditional story-driven test generation
- Mock data and sample scenarios for showcase purposes
- Run: `python run_demo.py` or `streamlit run app.py --server.port 8502`

### 🔍 **Real Application Mode** (Discovery-based Testing) - Port 8501
- **Application Discovery Agent** automatically explores live applications
- AI agents browse your app to discover features, UI elements, and workflows
- Generates tests based on actual application structure and source code
- **Test Code Generator Agent** creates executable pytest automation scripts
- Integration with real APIs, databases, and external services
- Run: `python run_real_app.py` or `streamlit run real_app_demo.py --server.port 8501`

### 🎯 **12 Specialized AI Agents**

| Agent | Demo Mode | Real App Mode | Function |
|-------|-----------|---------------|----------|
| 🎯 QA Orchestrator | ✅ | ✅ | Coordinates all testing activities |
| 📋 Story Analyst | ✅ | ❌ | Analyzes user stories and requirements |
| 🔍 Application Discovery | ❌ | ✅ | Explores live applications automatically |
| ⚠️ Risk Assessor | ✅ | ✅ | Identifies security, performance, and business risks |
| 🧪 Unit Test Agent | ✅ | ✅ | Generates comprehensive unit tests |
| 🔗 Integration Agent | ✅ | ✅ | Creates end-to-end integration tests |
| 🔒 Security Agent | ✅ | ✅ | Builds security and vulnerability tests |
| ⚡ Performance Agent | ✅ | ✅ | Generates performance and load tests |
| 🤖 AI Validation Agent | ✅ | ✅ | Tests AI models with RAGAS, DeepEval, LangSmith |
| 🎪 Edge Case Agent | ✅ | ✅ | Creates boundary and edge case tests |
| 📝 Test Code Generator | ✅ | ✅ | Generates executable pytest automation scripts |
| 🚀 Test Executor | ✅ | ✅ | Executes tests and analyzes results |
| ✅ Quality Reviewer | ✅ | ✅ | Reviews quality and provides recommendations |

### 🚀 Quick Start

#### Prerequisites

- **Python 3.11+**: Required for modern language features
- **Anthropic API Key**: Get from [Anthropic Console](https://console.anthropic.com/)
- **Git**: For repository cloning
- **4GB+ RAM**: Recommended for optimal AI agent performance

#### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-qa-orchestrator
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment configuration**
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Edit .env file with your API key:
   nano .env  # or use your preferred editor
   ```
   
   Add your Anthropic API key to `.env`:
   ```env
   # Required: Get from https://console.anthropic.com/
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   
   # Optional: Port configuration (defaults shown)
   REAL_APP_PORT=8501
   DEMO_APP_PORT=8502
   
   # Optional: Debug settings
   DEBUG=false
   ENVIRONMENT=development
   ```

5. **Verify setup**
   ```bash
   python test_setup.py
   ```

#### 🚀 Running the Application

#### **Option A: Interactive Launcher** (Recommended)
```bash
python launch.py
```
Choose your mode from the interactive menu with environment validation.

#### **Option B: Direct Launch**

**Real Application Testing** (Production Testing):
```bash
python run_real_app.py
# Opens at: http://localhost:8501
```

**Demo Mode** (Showcase & Presentation):
```bash
python run_demo.py  
# Opens at: http://localhost:8502
```

**Simultaneous Showcase** (Both modes):
```bash
# Terminal 1: Real Application Testing
python run_real_app.py

# Terminal 2: Demo Mode  
python run_demo.py

# Access both:
# - Real App Testing: http://localhost:8501
# - Demo Mode: http://localhost:8502
```

#### **Option C: Traditional Streamlit** (Advanced)
```bash
# Real Application Testing
streamlit run real_app_demo.py --server.port 8501

# Demo Mode
streamlit run app.py --server.port 8502
```

### 📖 Usage

#### 🎯 Demo Mode (Mock Testing) - Port 8502
1. **Select a Demo Scenario** from pre-configured options
2. **Configure Settings** in the sidebar (test domains, quality thresholds)
3. **Generate Tests** by clicking the main button
4. **Watch 12 AI Agents Collaborate** in real-time with progress indicators
5. **Review Results** across comprehensive dashboard tabs:
   - 📊 **Test Generation**: View all generated tests by category
   - 🤖 **AI Validation**: See RAGAS, DeepEval, and LangSmith metrics
   - 📝 **Generated Test Scripts**: Executable pytest automation code
   - ✅ **Quality Analysis**: Final quality scores and recommendations
6. **Export Test Automation Project** as a complete ZIP file
7. **Integrate** with your CI/CD pipeline using generated configs

#### 🚀 Real Application Testing - Port 8501
1. **Configure Your Application** (UI-based, no files needed):
   - Choose from pre-configured apps (Hugging Face Chat, Perplexity AI, etc.)
   - Or configure custom application (Web, API, or Hybrid)
   - Set base URLs, API endpoints, and testing preferences
   - Select test types (UI, API, Security, Performance, AI Validation)

2. **Advanced Integration** (Optional):
   - **Project Enigma Integration**: Point to `http://localhost:8000/` for LangChain workflow testing
   - **Source Code Analysis**: Place source in `project-enigma-source/` for fine-tuned tests
   - **Swagger Integration**: Automatic API endpoint discovery and testing

3. **Execute Comprehensive Testing**:
   - **Application Discovery Agent** explores your live application
   - **Test Code Generator Agent** creates executable pytest scripts
   - All 12 agents collaborate to generate real, contextual tests
   - Dynamic test counts based on actual application structure
   - Real execution metrics and performance data

4. **Review and Export**:
   - View detailed technical methodology explanations
   - See actual generated test code (API, AI validation, performance, edge cases)
   - Export complete test automation project with CI/CD configurations
   - Download and run tests independently with proper setup instructions

#### 🌟 **New Features**

- **📝 Test Code Generator Agent**: Creates executable pytest automation scripts
- **🛠️ Source Code Analysis**: Analyzes LangChain workflows for precise AI validation
- **📦 Complete Project Export**: Download full test automation projects
- **🔄 Dynamic Test Metrics**: Real numbers based on actual application analysis
- **🚀 Dual Port Setup**: Run both modes simultaneously for comparisons
- **🔐 Secure Configuration**: Environment-based API key management

### 🎯 Demo Scenarios

The system includes several pre-built scenarios:

- 🔐 **User Authentication System** - Multi-factor authentication with security focus
- 💰 **Banking Transaction System** - Financial transactions with compliance requirements  
- 🤖 **AI-Powered Recommendation Engine** - ML system with bias detection
- 📱 **Mobile Healthcare Application** - HIPAA-compliant patient management
- 🚚 **Supply Chain Management System** - Real-time inventory and logistics
- 🎓 **Online Learning Platform** - Educational content delivery system

### 🏆 Quality Metrics

The system provides comprehensive quality assessment:

- **Overall Quality Score**: Weighted average across all domains
- **Domain-Specific Scores**: Individual quality metrics per testing area
- **Coverage Analysis**: Statement, branch, function, and line coverage
- **Risk Assessment**: Security, performance, and business risk evaluation
- **Production Readiness**: Deployment readiness with actionable recommendations

### 🚀 Real Application Testing

The AI QA Orchestrator can test your actual applications with UI and APIs! Here's what it supports:

#### 🏗️ Supported Application Types
- **Web Applications** (React, Vue, Angular, HTML/CSS/JS)
- **API Services** (REST, GraphQL, microservices)
- **Full-Stack Applications** (MEAN, MERN, Django, Flask, FastAPI)
- **AI-Powered Applications** (Chat apps, recommendation engines, ML services)
- **Mobile Web Apps** (responsive web applications)

#### 🔧 Real Testing Capabilities
- **Live API Testing** - Tests your actual API endpoints with real requests
- **Browser Automation** - Uses Selenium/Playwright for real UI testing
- **Database Integration** - Tests actual database operations and data integrity
- **Performance Monitoring** - Real load testing with K6 or similar tools
- **Security Scanning** - Uses OWASP ZAP and other security tools
- **Code Coverage** - Generates actual coverage reports from your test runs

#### ⚙️ Easy Configuration
1. **Simple YAML Configuration** - Configure your app in `config/app_config.yml`
2. **Auto-Discovery** - System detects your application type and suggests optimal settings
3. **Quality Gates** - Set custom thresholds for coverage, performance, and security
4. **CI/CD Integration** - Ready-to-use pipeline configurations

#### 🎯 Example Configuration
```yaml
application:
  name: "My AI Chat App"
  type: "web"
  language: "javascript"
  framework: "react"

urls:
  base_url: "http://localhost:3000"
  api_base_url: "http://localhost:3001/api"

api:
  endpoints:
    - path: "/chat"
      methods: ["POST"]
    - path: "/health" 
      methods: ["GET"]

quality_gates:
  unit_test_coverage: 80
  api_test_pass_rate: 100
  security_critical_issues: 0
```

### 🔧 Advanced Features

#### Multi-Domain Test Generation

- **Unit Tests**: Happy path, error handling, edge cases, mocking
- **Integration Tests**: API endpoints, database operations, service integration
- **Security Tests**: OWASP Top 10, authentication, authorization, data protection
- **Performance Tests**: Load, stress, spike, volume testing scenarios
- **AI Validation Tests**: 25+ metrics including Faithfulness, Groundedness, Answer Relevancy, G-Eval scoring, Response time, Token efficiency, Bias detection, Toxicity classification, Hallucination prevention, Model drift monitoring
- **Edge Case Tests**: Boundary conditions, null handling, concurrency

#### Risk-Based Prioritization

- **Business Risk Analysis**: Financial impact, regulatory compliance
- **Technical Risk Assessment**: Complexity, integration challenges
- **Security Risk Evaluation**: Vulnerability assessment, attack vectors
- **Performance Risk Identification**: Bottlenecks, scalability concerns

#### CI/CD Integration

Generated configurations for:
- GitHub Actions
- Jenkins
- GitLab CI
- Azure DevOps

### 📊 Dashboard Features

- **Executive Overview**: Key metrics and achievements
- **Test Results**: Detailed test code and coverage analysis
- **Quality Reports**: Comprehensive quality breakdown and trends
- **Risk Visualization**: Interactive risk matrices and heat maps
- **Performance Monitoring**: Response times, throughput, resource usage
- **AI Validation**: 25+ metrics covering RAGAS framework (Faithfulness, Groundedness, Context Precision), DeepEval capabilities (G-Eval, Answer Correctness), Performance analysis, Safety & Bias detection

### 🛠️ Technical Stack

- **Backend**: Python 3.11+, CrewAI, LangChain, FastAPI
- **Frontend**: Streamlit (Dual Port: 8501/8502), Plotly, Pandas
- **AI Models**: Anthropic Claude 3.5 Sonnet, LangChain integrations
- **Testing Frameworks**: pytest, httpx, Selenium WebDriver, Hypothesis  
- **AI Validation**: RAGAS, DeepEval, LangSmith, Promptfoo
- **Quality Tools**: Custom scoring algorithms, memory profilers, AST analysis
- **Configuration**: python-dotenv, YAML configs, environment management
- **Export Tools**: ZIP generation, CI/CD templates, Docker configurations

### 🔧 Troubleshooting

#### **Environment Setup Issues**

**Problem**: `ANTHROPIC_API_KEY not found`
```bash
# Solution: Check your .env file exists and contains the key
cp env.example .env
nano .env  # Add: ANTHROPIC_API_KEY=your_key_here
python test_setup.py  # Verify setup
```

**Problem**: `ModuleNotFoundError` or import errors
```bash
# Solution: Reinstall dependencies in virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Problem**: Port already in use
```bash
# Solution: Change ports in .env file or kill existing processes
# Check what's using the port:
lsof -i :8501  # or :8502
# Kill process: kill -9 <PID>
# Or change ports in .env:
REAL_APP_PORT=8503
DEMO_APP_PORT=8504
```

#### **Runtime Issues**

**Problem**: "Demo key" or API authentication errors
```bash
# Solution: Verify your Anthropic API key is correct
python -c "from config import config; print('Key loaded:', bool(config.ANTHROPIC_API_KEY != 'demo-key-for-development'))"
```

**Problem**: Test Executor shows incorrect numbers
```bash
# Solution: Clear browser cache and restart application
# The new version uses dynamic test calculations
python run_real_app.py  # Fresh start
```

**Problem**: UI/API tests not showing properly
```bash
# Solution: Ensure application type is correctly configured
# In Real App mode, select correct app type (Web/API/Hybrid)
# UI tests only show for Web/Hybrid apps
# API tests only show for API/Hybrid apps
```

#### **Application Integration Issues**

**Problem**: Local application not accessible
```bash
# Solution: Verify your application is running and accessible
curl http://localhost:8000/health  # Test API endpoint
# Ensure your application accepts connections from localhost
```

**Problem**: Source code analysis not working
```bash
# Solution: Verify source code placement
ls project-enigma-source/  # Should contain your source code
# Ensure Python source files are readable
```

**Problem**: Export feature not working
```bash
# Solution: Check file permissions and disk space
df -h  # Check disk space
# Ensure write permissions in current directory
```

#### **Performance Issues**

**Problem**: Slow AI agent execution
```bash
# Solution: Check system resources and API rate limits
# Close other applications consuming RAM
# Monitor API usage at https://console.anthropic.com/
```

**Problem**: Browser loading issues
```bash
# Solution: Try different browser or clear cache
# Chrome/Firefox recommended
# Disable browser extensions that might interfere
```

#### **Getting Help**

If issues persist:
1. **Run setup validation**: `python test_setup.py`
2. **Check logs**: Look for error messages in terminal output
3. **Verify environment**: Ensure `.env` file is properly configured
4. **Test API key**: Visit Anthropic Console to verify key is active
5. **System requirements**: Ensure Python 3.11+ and 4GB+ RAM

### 🎓 For QA Professionals

This system is designed by QA architects for QA professionals:

- **Deep Domain Expertise**: Built-in knowledge of testing best practices
- **Risk-First Approach**: Prioritizes testing based on business and technical risks
- **Production-Ready Output**: Generates enterprise-grade test suites
- **Continuous Improvement**: Learn from feedback and improve over time
- **Industry Standards**: Follows OWASP, ISO, and other quality standards

### 🔮 Future Enhancements

#### **Recently Implemented ✅**
- ✅ **Test Code Generator Agent**: Executable pytest automation scripts
- ✅ **Dynamic Test Metrics**: Real numbers from application analysis  
- ✅ **Source Code Integration**: LangChain workflow analysis
- ✅ **Complete Project Export**: ZIP downloads with CI/CD configs
- ✅ **Dual Port Architecture**: Simultaneous demo and real app testing
- ✅ **Environment Configuration**: Secure .env-based API key management

#### **Coming Next 🚧**
- 🚧 **Database Integration Testing**: Direct database test generation
- 🚧 **Container Testing**: Docker and Kubernetes deployment tests
- 🚧 **Multi-Language Support**: JavaScript, Java, C#, Go test generation
- 🚧 **Advanced UI Testing**: Playwright integration with visual regression
- 🚧 **Load Testing Integration**: K6 and Locust automated load tests

#### **Roadmap 🗺️**
- 🗺️ **Custom Agent Training**: Train agents on your specific domain knowledge
- 🗺️ **Team Collaboration**: Multi-user workflows, test review processes
- 🗺️ **Real-Time Monitoring**: Live quality metrics dashboards and alerting
- 🗺️ **Enterprise Integration**: JIRA, Azure DevOps, ServiceNow connectors
- 🗺️ **AI Model Flexibility**: OpenAI, Google Gemini, local model support

### 🤝 Contributing

This project was developed for the AI x SDLC Hackathon. Contributions and improvements are welcome!

### 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.


**Ready to revolutionize your quality assurance process? Get started with the AI Quality Assurance Orchestrator today!**