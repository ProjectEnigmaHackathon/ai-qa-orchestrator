#!/usr/bin/env python3

# This is a temporary script to test the syntax error fix
print("Testing syntax fix...")

# Test basic functionality
import streamlit as st

def test_function():
    st.markdown("### Test")
    with st.expander("Test Expander", expanded=False):
        st.info("Test content")
    st.markdown("---")
    
if __name__ == "__main__":
    test_function()
    print("✅ Syntax test passed!")