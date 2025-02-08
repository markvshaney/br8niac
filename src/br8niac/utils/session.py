import streamlit as st
from typing import Any, Dict

def init_session_state() -> None:
    """Initialize session state with default values."""
    defaults: Dict[str, Any] = {
        'search_history': [],
        'current_query': '',
        'saved_results': [],
        'settings': {
            'theme': 'light',
            'max_results': 5,
            'sort_by': 'relevance'
        }
    }
    
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

def update_search_history(query: str) -> None:
    """
    Update search history with new query.
    
    Args:
        query: Search query to add to history
    """
    if query not in st.session_state.search_history:
        st.session_state.search_history.insert(0, query)
        # Keep only last 5 searches
        st.session_state.search_history = st.session_state.search_history[:5]

def save_result(result: Dict[str, Any]) -> None:
    """
    Save a search result for later reference.
    
    Args:
        result: Result dictionary to save
    """
    if result not in st.session_state.saved_results:
        st.session_state.saved_results.append(result)

def get_settings() -> Dict[str, Any]:
    """
    Get current user settings.
    
    Returns:
        Dictionary of user settings
    """
    return st.session_state.settings

def update_settings(new_settings: Dict[str, Any]) -> None:
    """
    Update user settings.
    
    Args:
        new_settings: Dictionary of settings to update
    """
    st.session_state.settings.update(new_settings)