# AI Quality Assurance Orchestrator

## 🤖 Comprehensive AI-Powered Test Generation System

A revolutionary AI-powered system that automatically generates comprehensive test suites across all quality domains using specialized CrewAI agents.

### 🌟 Key Features

- **🎯 Multi-Agent Architecture**: 11 specialized AI agents with dual modes (Story Analysis + Application Discovery)
- **📊 Comprehensive Testing**: Unit, Integration, Security, Performance, AI Validation, Edge Cases
- **🔍 Risk-Based Analysis**: Intelligent risk assessment and test prioritization
- **⚡ Real-Time Generation**: Complete test suites in under 60 seconds
- **📈 Quality Scoring**: Advanced quality metrics and production readiness assessment
- **🔄 CI/CD Integration**: Seamless pipeline integration with quality gates
- **📱 Interactive Dashboard**: Rich visualizations and detailed reporting

### 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Streamlit Dashboard                       │
├─────────────────────────────────────────────────────────────┤
│                QA Orchestration Engine                      │
├─────────────────────────────────────────────────────────────┤
│  🎯 QA         📋 Story      ⚠️  Risk        ✅ Quality    │
│  Orchestrator  Analyst       Assessor       Reviewer       │
│                                                             │
│  🧪 Unit       🔗 Integration 🔒 Security    ⚡ Performance │ 
│  Test Agent    Test Agent     Test Agent     Test Agent     │
│                                                             │
│  🤖 AI         🎪 Edge Case   🚀 Test        ✅ Quality    │
│  Validation    Test Agent     Executor      Reviewer       │
│  Agent                        Agent         Agent          │
├─────────────────────────────────────────────────────────────┤
│          Test Generators | Risk Analyzer | Quality Scorer  │
├─────────────────────────────────────────────────────────────┤
│                     Tools & Utilities                      │
└─────────────────────────────────────────────────────────────┘
```

## 🔄 Dual Testing Modes

### 📋 **Demo Mode** (Story-based Testing)
- **Story Analyst Agent** analyzes user stories and requirements
- Perfect for prototypes, demos, and concept validation
- Uses traditional story-driven test generation
- Run: `streamlit run app.py`

### 🔍 **Real Application Mode** (Discovery-based Testing)  
- **Application Discovery Agent** automatically explores live applications
- AI agents browse your app to discover features, UI elements, and workflows
- Generates tests based on actual application structure
- Run: `streamlit run real_app_demo.py`

### 🚀 Quick Start

#### Prerequisites

- Python 3.11+
- Anthropic API Key (for AI agents)
- Git

#### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Hackathon-2025
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Edit the .env file and add your Anthropic API key:
   # ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

4. **Run the application**
   
   **Option A: Interactive Launcher**
   ```bash
   python launch.py
   ```
   
   **Option B: Direct Launch**
   
   **Demo Mode (Mock Testing):**
   ```bash
   python run_demo.py
   # or
   streamlit run app.py --server.port 8502
   ```
   
   **Real Application Testing:**
   ```bash
   python run_real_app.py  
   # or
   streamlit run real_app_demo.py --server.port 8501
   ```

5. **Open in browser**
   - **Real Application Testing**: `http://localhost:8501`
   - **Demo Mode**: `http://localhost:8502`
   
   💡 **Run both simultaneously** to showcase side-by-side!

### 📖 Usage

#### 🎯 Demo Mode (Mock Testing)
1. **Select a Demo Scenario** or enter your own user story
2. **Configure Settings** in the sidebar (test domains, quality thresholds)
3. **Generate Tests** by clicking the main button
4. **Watch AI Agents Collaborate** in real-time
5. **Review Results** across comprehensive dashboard tabs
6. **Export** test suites and quality reports
7. **Integrate** with your CI/CD pipeline

#### 🚀 Real Application Testing
1. **Configure Your Application**
   - Create `config/app_config.yml` with your app details
   - Set URLs, API endpoints, and testing preferences
   - Configure quality gates and CI/CD integration

2. **Ensure Application is Running**
   - Your application should be accessible on configured URLs
   - API endpoints should be responding
   - Database connections should be active

3. **Run Real Application Testing**
   ```bash
   streamlit run real_app_demo.py
   ```

4. **Execute Comprehensive Testing**
   - The system will test your actual application
   - Real tests will be executed against your APIs and UI
   - Actual code coverage and performance metrics will be collected
   - Quality gates will be validated against real results

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

- **Backend**: Python 3.11, FastAPI, CrewAI, LangChain
- **Frontend**: Streamlit, Plotly, Pandas
- **AI Models**: Anthropic Claude 3.5 Sonnet, specialized domain models
- **Testing Frameworks**: Jest, PyTest, K6, OWASP ZAP
- **Quality Tools**: SonarQube integration, custom scoring algorithms

### 🎓 For QA Professionals

This system is designed by QA architects for QA professionals:

- **Deep Domain Expertise**: Built-in knowledge of testing best practices
- **Risk-First Approach**: Prioritizes testing based on business and technical risks
- **Production-Ready Output**: Generates enterprise-grade test suites
- **Continuous Improvement**: Learn from feedback and improve over time
- **Industry Standards**: Follows OWASP, ISO, and other quality standards

### 🔮 Future Enhancements

- **Custom Agent Training**: Train agents on your specific domain
- **Integration Extensions**: Support for more CI/CD platforms and tools
- **Advanced AI Models**: Integration with latest language models
- **Real-Time Monitoring**: Live quality metrics and alerting
- **Team Collaboration**: Multi-user workflows and review processes

### 🤝 Contributing

This project was developed for the AI x SDLC Hackathon. Contributions and improvements are welcome!

### 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

### 🏅 Hackathon Achievement

Built in 24 hours for the AI x SDLC Hackathon, demonstrating the power of AI-driven quality assurance and the potential for revolutionary improvements in software testing practices.

---

**Ready to revolutionize your quality assurance process? Get started with the AI Quality Assurance Orchestrator today!**