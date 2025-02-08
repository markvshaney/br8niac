import streamlit as st
from services.ai_service import perform_search
from components.search_box import render_search_box
from components.results_display import render_results

st.set_page_config(page_title="Search - Local AI Search", layout="wide")

st.title("🔍 Search")

# Initialize session state for search history
if 'search_history' not in st.session_state:
    st.session_state.search_history = []

# Sidebar with search history
with st.sidebar:
    st.header("Search History")
    if st.session_state.search_history:
        for query in st.session_state.search_history:
            if st.button(f"🔄 {query}", key=f"history_{query}"):
                st.session_state.current_query = query
    else:
        st.write("No recent searches")

# Main search interface
query = render_search_box()

if query:
    # Add to search history
    if query not in st.session_state.search_history:
        st.session_state.search_history.insert(0, query)
        # Keep only last 5 searches
        st.session_state.search_history = st.session_state.search_history[:5]
    
    # Perform search with loading indicator
    with st.spinner("Searching..."):
        results = perform_search(query)
    
    # Display results
    render_results(results)