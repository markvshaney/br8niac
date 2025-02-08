import streamlit as st
from typing import Optional

def render_search_box() -> Optional[str]:
    """
    Render the search input box with enhanced UI.
    
    Returns:
        Optional[str]: The search query if submitted, None otherwise
    """
    search_container = st.container()
    
    with search_container:
        # Create a form for better input handling
        with st.form(key="search_form"):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                query = st.text_input(
                    "Enter your search query",
                    value=st.session_state.get('current_query', ''),
                    placeholder="What would you like to search for?",
                    key="search_input"
                )
            
            with col2:
                submit_button = st.form_submit_button(
                    "🔍 Search",
                    use_container_width=True
                )
        
        # Handle form submission
        if submit_button and query:
            return query.strip()
    
    return None