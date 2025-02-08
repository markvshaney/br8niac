"""
Entry point for the Local AI Search application.
This module sets up and launches the Streamlit application.
"""

import os
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv

# Set up environment
load_dotenv()

# Add the src directory to Python path
import sys
src_path = str(Path(__file__).parent / "src")
if src_path not in sys.path:
    sys.path.append(src_path)

# Import local modules
from local_ai_search.pages.home import main
from local_ai_search.utils.session import init_session_state

if __name__ == "__main__":
    try:
        # Initialize session state
        init_session_state()
        
        # Run the main application
        main()
        
    except Exception as e:
        st.error(f"Application Error: {str(e)}")
        st.info("Please check the logs for more details and ensure all dependencies are installed.")
        
        # Add a way to see detailed error in development
        if os.getenv("DEBUG", "False").lower() == "true":
            st.exception(e)