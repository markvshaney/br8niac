import streamlit as st
from typing import Dict, Union, List
import textwrap

def render_result_card(result: Dict[str, str]) -> None:
    """
    Render a single result card with enhanced styling.
    
    Args:
        result: Dictionary containing result information
    """
    with st.container():
        # Title with link
        st.markdown(f"### [{result['title']}]({result['url']})")
        
        # Preview content with expandable text
        content = result['content']
        if len(content) > 300:
            with st.expander("Show full content"):
                st.markdown(content)
            # Show truncated content
            st.markdown(textwrap.shorten(content, width=300, placeholder="..."))
        else:
            st.markdown(content)
        
        # Metadata and actions
        col1, col2 = st.columns([4, 1])
        with col1:
            st.caption(f"Source: {result['url']}")
        with col2:
            st.button("Save", key=f"save_{result['title'][:20]}")
        
        st.divider()

def render_results(results: Dict[str, Union[List[Dict], str]]) -> None:
    """
    Render search results with enhanced UI and error handling.
    
    Args:
        results: Dictionary containing either results list or error message
    """
    if "error" in results:
        st.error(f"Search failed: {results['error']}")
        st.info("Please try another search query or check if the model is running")
        return
    
    if not results.get("results"):
        st.info("No results found. Try refining your search query.")
        return
    
    # Results summary
    st.success(f"Found {len(results['results'])} results")
    
    # Render filters/sorting options
    col1, col2 = st.columns(2)
    with col1:
        sort_by = st.selectbox(
            "Sort by",
            ["Relevance", "Date", "Title"],
            key="sort_results"
        )
    with col2:
        filter_by = st.multiselect(
            "Filter by",
            ["Articles", "News", "Research", "Other"],
            key="filter_results"
        )
    
    # Results list
    for result in results["results"]:
        render_result_card(result)
    
    # Pagination placeholder
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("1 2 3 ... Next →")