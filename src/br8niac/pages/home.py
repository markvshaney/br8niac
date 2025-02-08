import streamlit as st
from pathlib import Path
import json
from typing import Optional

from br8niac.services.ai_service import AIService, ModelStatus
from br8niac.components.search_box import render_search_box
from br8niac.components.results_display import render_results
from br8niac.utils.session import init_session_state

def load_config() -> dict:
    """Load configuration from config.json."""
    config_path = Path(__file__).parent.parent / "config.json"
    with open(config_path) as f:
        return json.load(f)

def initialize_page():
    """Initialize page configuration and styling."""
    st.set_page_config(
        page_title="Local AI Search",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Apply custom CSS
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .search-container {
            margin: 2rem 0;
        }
        .stButton>button {
            width: 100%;
        }
        .model-status {
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

def render_sidebar(ai_service: AIService):
    """Render sidebar with model status and settings."""
    with st.sidebar:
        st.title("🔧 Settings")
        
        # Model Status
        status = ai_service.check_model_status()
        if status == ModelStatus.READY:
            st.success("Model Status: Ready")
        elif status == ModelStatus.ERROR:
            st.error("Model Status: Error")
            st.info("Please check if Ollama is running")
        else:
            st.warning("Model Status: Not Available")
            
        # Search History
        if st.session_state.search_history:
            st.subheader("Recent Searches")
            for query in st.session_state.search_history:
                if st.button(f"🔄 {query}", key=f"history_{query}"):
                    st.session_state.current_query = query
                    st.experimental_rerun()

def main():
    """Main application entry point."""
    # Initialize
    config = load_config()
    initialize_page()
    init_session_state()
    
    # Create services
    ai_service = AIService(config)
    
    # Render sidebar
    render_sidebar(ai_service)
    
    # Main content
    st.title("🔍 Local AI Search")
    st.markdown("""
        Search the web using your local AI model. Your data stays private!
    """)
    
    # Search interface
    query = render_search_box()
    
    if query:
        # Update search history
        if query not in st.session_state.search_history:
            st.session_state.search_history.insert(0, query)
            st.session_state.search_history = st.session_state.search_history[:5]
        
        # Perform search with error handling
        try:
            with st.spinner("🔍 Searching..."):
                results = ai_service.perform_search(query)
            render_results(results)
        except Exception as e:
            st.error(f"Search failed: {str(e)}")
            st.info("Please check if the AI model is running and try again")

if __name__ == "__main__":
    main()