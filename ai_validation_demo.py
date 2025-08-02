#!/usr/bin/env python3
"""
AI Validation Metrics Demo
Showcases comprehensive AI model validation capabilities with RAGAS, DeepEval-inspired metrics
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import sys
import os

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from tools.ai_validation_metrics import AIValidationMetrics, AIValidationTestScenarios

# Page configuration
st.set_page_config(
    page_title="AI Validation Metrics Demo",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }
    .metric-score {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
    }
    .metric-name {
        font-size: 1.2em;
        text-align: center;
        margin-top: 10px;
    }
    .category-header {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        padding: 15px;
        border-radius: 8px;
        color: white;
        font-weight: bold;
        margin: 20px 0 10px 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🤖 AI Model Validation Metrics Suite")
    st.markdown("### Comprehensive AI Testing with RAGAS, DeepEval & Industry Standards")
    
    ai_metrics = AIValidationMetrics()
    test_scenarios = AIValidationTestScenarios()
    
    # Sidebar for navigation
    st.sidebar.title("🧭 Navigation")
    page = st.sidebar.selectbox(
        "Choose a section:",
        ["📊 Metrics Overview", "🎯 Accuracy & Faithfulness", "⚡ Performance Analysis", 
         "🛡️ Safety & Bias Detection", "🧪 Advanced Evaluation", "📈 Dashboard Demo"]
    )
    
    if page == "📊 Metrics Overview":
        show_metrics_overview(ai_metrics)
    elif page == "🎯 Accuracy & Faithfulness":
        show_accuracy_metrics(ai_metrics)
    elif page == "⚡ Performance Analysis":
        show_performance_metrics(ai_metrics)
    elif page == "🛡️ Safety & Bias Detection":
        show_safety_metrics(ai_metrics)
    elif page == "🧪 Advanced Evaluation":
        show_advanced_metrics(ai_metrics)
    elif page == "📈 Dashboard Demo":
        show_dashboard_demo(ai_metrics, test_scenarios)

def show_metrics_overview(ai_metrics):
    st.header("📊 Comprehensive AI Validation Metrics")
    
    st.markdown("""
    Our AI Quality Assurance Orchestrator now includes **25+ industry-standard metrics** 
    inspired by leading frameworks like RAGAS, DeepEval, and research best practices.
    """)
    
    # Metrics by category
    categories = ai_metrics.get_metrics_by_category()
    
    for category, metrics in categories.items():
        st.markdown(f'<div class="category-header">{category}</div>', unsafe_allow_html=True)
        
        cols = st.columns(min(len(metrics), 3))
        for i, metric in enumerate(metrics):
            with cols[i % 3]:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-name">{metric.name}</div>
                    <div style="font-size: 0.9em; margin-top: 10px; opacity: 0.9;">
                        {metric.description[:100]}...
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # Quick stats
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Metrics", "25+", delta="New!")
    with col2:
        st.metric("Framework Coverage", "4", delta="RAGAS, DeepEval, Custom")
    with col3:
        st.metric("Evaluation Domains", "6", delta="Accuracy to Safety")
    with col4:
        st.metric("Test Scenarios", "50+", delta="Automated Generation")

def show_accuracy_metrics(ai_metrics):
    st.header("🎯 Accuracy & Faithfulness Evaluation")
    
    st.markdown("""
    **Faithfulness and Groundedness** are crucial for AI systems, especially RAG applications.
    Our metrics ensure responses are factually accurate and grounded in provided context.
    """)
    
    # Faithfulness Demo
    st.subheader("📋 Faithfulness Evaluation Demo")
    
    with st.expander("🔍 View Faithfulness Test Scenarios", expanded=True):
        scenarios = test_scenarios.generate_test_scenarios()
        faithfulness_tests = scenarios["faithfulness_tests"]
        
        for i, test in enumerate(faithfulness_tests):
            st.markdown(f"**Test {i+1}: {test['description']}**")
            st.code(f"Input: {test['input']}")
            st.code(f"Context: {test['context']}")
            
            # Simulate faithfulness score
            score = 0.92 if test['expected_faithful'] else 0.34
            color = "green" if score > 0.7 else "red"
            st.markdown(f"**Faithfulness Score:** :{color}[{score:.2f}]")
            st.markdown("---")
    
    # Interactive metrics demo
    st.subheader("🧪 Interactive Evaluation")
    
    user_input = st.text_area("Enter your test input:", "What are the benefits of renewable energy?")
    user_context = st.text_area("Enter context:", "Solar and wind power are clean energy sources that reduce carbon emissions.")
    
    if st.button("🚀 Run Faithfulness Analysis"):
        with st.spinner("Analyzing faithfulness..."):
            # Simulate analysis
            st.success("Analysis Complete!")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Faithfulness", "0.89", delta="0.05")
            with col2:
                st.metric("Groundedness", "0.94", delta="0.12")
            with col3:
                st.metric("Factual Accuracy", "0.87", delta="-0.03")

def show_performance_metrics(ai_metrics):
    st.header("⚡ Performance & Efficiency Analysis")
    
    st.markdown("""
    **Response time, token efficiency, and resource usage** are critical for production AI systems.
    Our performance metrics help optimize both speed and cost.
    """)
    
    # Generate mock performance data
    np.random.seed(42)
    input_lengths = [10, 50, 100, 500, 1000, 2000, 5000]
    response_times = [0.2, 0.4, 0.6, 1.2, 2.1, 4.5, 12.3]
    token_costs = [0.001, 0.005, 0.012, 0.045, 0.089, 0.178, 0.445]
    
    # Response time chart
    st.subheader("📈 Response Time Analysis")
    fig_time = px.line(
        x=input_lengths, y=response_times,
        labels={'x': 'Input Length (tokens)', 'y': 'Response Time (seconds)'},
        title="Response Time vs Input Length"
    )
    fig_time.add_hline(y=2.0, line_dash="dash", line_color="red", 
                       annotation_text="SLA Threshold (2s)")
    st.plotly_chart(fig_time, use_container_width=True)
    
    # Token efficiency chart
    st.subheader("💰 Token Efficiency Analysis")
    fig_cost = px.bar(
        x=input_lengths, y=token_costs,
        labels={'x': 'Input Length (tokens)', 'y': 'Cost per Query ($)'},
        title="Cost Efficiency by Input Length"
    )
    st.plotly_chart(fig_cost, use_container_width=True)
    
    # Real-time metrics simulation
    st.subheader("🔄 Real-time Performance Monitoring")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Avg Response Time", "1.2s", delta="-0.3s")
    with col2:
        st.metric("Throughput", "45 req/min", delta="5 req/min")
    with col3:
        st.metric("Token Efficiency", "89%", delta="3%")
    with col4:
        st.metric("Memory Usage", "2.1 GB", delta="-0.2 GB")

def show_safety_metrics(ai_metrics):
    st.header("🛡️ Safety & Bias Detection")
    
    st.markdown("""
    **Safety and fairness** are paramount in AI systems. Our comprehensive bias detection
    covers demographic, cultural, linguistic, and ideological biases.
    """)
    
    # Bias detection categories
    st.subheader("🔍 Bias Detection Categories")
    
    bias_types = {
        "Demographic": ["Gender", "Age", "Race", "Religion", "Nationality"],
        "Cultural": ["Western Bias", "Language Preference", "Cultural Stereotypes"],
        "Professional": ["Occupational Stereotypes", "Industry Bias", "Skill Assumptions"],
        "Linguistic": ["Dialect Discrimination", "Accent Bias", "Language Complexity"]
    }
    
    for category, biases in bias_types.items():
        with st.expander(f"📊 {category} Bias Analysis"):
            # Generate mock bias scores
            scores = np.random.uniform(0.1, 0.9, len(biases))
            
            df = pd.DataFrame({
                'Bias Type': biases,
                'Risk Score': scores,
                'Status': ['High' if s > 0.7 else 'Medium' if s > 0.4 else 'Low' for s in scores]
            })
            
            fig = px.bar(df, x='Bias Type', y='Risk Score', color='Status',
                        color_discrete_map={'Low': 'green', 'Medium': 'orange', 'High': 'red'})
            st.plotly_chart(fig, use_container_width=True)
    
    # Toxicity analysis
    st.subheader("☢️ Toxicity Classification")
    
    toxicity_categories = ["Hate Speech", "Violence", "Self-Harm", "Harassment", "Adult Content"]
    toxicity_scores = np.random.uniform(0.05, 0.25, len(toxicity_categories))
    
    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(values=toxicity_scores, names=toxicity_categories, 
                     title="Toxicity Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("**Safety Status:** ✅ **SAFE**")
        st.markdown("All toxicity scores below threshold (0.3)")
        
        for cat, score in zip(toxicity_categories, toxicity_scores):
            color = "green" if score < 0.3 else "red"
            st.markdown(f"- {cat}: :{color}[{score:.3f}]")

def show_advanced_metrics(ai_metrics):
    st.header("🧪 Advanced Evaluation Capabilities")
    
    st.markdown("""
    **Advanced metrics** including G-Eval scoring, model drift detection,
    and uncertainty quantification for cutting-edge AI evaluation.
    """)
    
    # G-Eval demonstration
    st.subheader("🤔 G-Eval: LLM-as-Judge Evaluation")
    
    with st.expander("📋 G-Eval Scoring Example"):
        st.code("""
        Evaluation Prompt: "Rate the response quality on a scale of 1-5 considering:
        1. Relevance to the question
        2. Factual accuracy  
        3. Completeness of answer
        4. Clarity and coherence"
        
        Human Question: "Explain machine learning in simple terms"
        AI Response: "Machine learning is like teaching computers to learn patterns 
        from data, similar to how humans learn from experience..."
        
        G-Eval Score: 4.2/5.0
        Reasoning: Response is relevant, accurate, and clear but could be more comprehensive.
        """)
    
    # Model drift visualization
    st.subheader("📉 Model Drift Detection")
    
    # Generate drift simulation data
    dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
    accuracy_drift = np.random.normal(0.85, 0.05, 30)
    accuracy_drift[20:] = np.random.normal(0.78, 0.03, 10)  # Simulate drift
    
    df_drift = pd.DataFrame({
        'Date': dates,
        'Accuracy': accuracy_drift,
        'Baseline': [0.85] * 30
    })
    
    fig = px.line(df_drift, x='Date', y=['Accuracy', 'Baseline'], 
                  title="Model Performance Drift Over Time")
    fig.add_vline(x=dates[20], line_dash="dash", line_color="red",
                  annotation_text="Drift Detected")
    st.plotly_chart(fig, use_container_width=True)
    
    # Uncertainty quantification
    st.subheader("🎲 Uncertainty Quantification")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**High Confidence Predictions**")
        high_conf_data = pd.DataFrame({
            'Prediction': ['Classification A', 'Classification B', 'Classification C'],
            'Confidence': [0.95, 0.87, 0.92],
            'Uncertainty': [0.05, 0.13, 0.08]
        })
        st.dataframe(high_conf_data)
    
    with col2:
        st.markdown("**Low Confidence Predictions (Require Review)**")
        low_conf_data = pd.DataFrame({
            'Prediction': ['Classification X', 'Classification Y', 'Classification Z'],
            'Confidence': [0.52, 0.48, 0.61],
            'Uncertainty': [0.48, 0.52, 0.39]
        })
        st.dataframe(low_conf_data)

def show_dashboard_demo(ai_metrics, test_scenarios):
    st.header("📈 Comprehensive AI Validation Dashboard")
    
    st.markdown("""
    **Real-time dashboard** showing all validation metrics in action.
    This simulates what you'd see when testing your AI application.
    """)
    
    # Generate comprehensive mock results
    np.random.seed(42)
    
    # Overall score
    overall_score = 0.847
    st.markdown(f"## Overall AI Quality Score: **{overall_score:.1%}**")
    
    # Progress bar
    st.progress(overall_score)
    
    # Category breakdown
    st.subheader("📊 Score Breakdown by Category")
    
    categories_scores = {
        "Accuracy & Faithfulness": 0.89,
        "Performance & Efficiency": 0.76,
        "Safety & Bias": 0.92,
        "Quality & Consistency": 0.83,
        "Robustness": 0.78,
        "Context & Retrieval": 0.91
    }
    
    col1, col2, col3 = st.columns(3)
    for i, (category, score) in enumerate(categories_scores.items()):
        with [col1, col2, col3][i % 3]:
            delta = np.random.uniform(-0.05, 0.05)
            st.metric(category, f"{score:.1%}", delta=f"{delta:.1%}")
    
    # Detailed metrics heatmap
    st.subheader("🔥 Detailed Metrics Heatmap")
    
    metrics_data = []
    all_metrics = ai_metrics.get_all_metrics()
    
    for metric in all_metrics[:15]:  # Show first 15 for demo
        score = np.random.uniform(0.6, 0.95)
        metrics_data.append({
            'Metric': metric.name.replace('_', ' ').title(),
            'Score': score,
            'Category': np.random.choice(list(categories_scores.keys()))
        })
    
    df_metrics = pd.DataFrame(metrics_data)
    
    # Create pivot table for heatmap
    pivot_df = df_metrics.pivot_table(values='Score', index='Metric', columns='Category', fill_value=0)
    
    fig = px.imshow(pivot_df.values, 
                    x=pivot_df.columns, 
                    y=pivot_df.index,
                    color_continuous_scale='RdYlGn',
                    title="AI Validation Metrics Heatmap")
    st.plotly_chart(fig, use_container_width=True)
    
    # Test execution summary
    st.subheader("🧪 Test Execution Summary")
    
    execution_stats = {
        "Total Tests Run": 247,
        "Passed": 219,
        "Failed": 18,
        "Warnings": 10,
        "Execution Time": "2.4 minutes",
        "Coverage": "94.2%"
    }
    
    col1, col2, col3 = st.columns(3)
    for i, (stat, value) in enumerate(execution_stats.items()):
        with [col1, col2, col3][i % 3]:
            if stat == "Failed":
                delta_color = "inverse"
            else:
                delta_color = "normal"
            st.metric(stat, value, delta="New", delta_color=delta_color)
    
    # Action recommendations
    st.subheader("🎯 Recommended Actions")
    
    recommendations = [
        "🔧 **Performance**: Optimize token usage for inputs >1000 tokens",
        "🛡️ **Safety**: Review edge cases for demographic bias detection",
        "⚡ **Efficiency**: Implement caching for repeated queries",
        "🎯 **Accuracy**: Fine-tune context retrieval for complex queries"
    ]
    
    for rec in recommendations:
        st.markdown(rec)

if __name__ == "__main__":
    main()