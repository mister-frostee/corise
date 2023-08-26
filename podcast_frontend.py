import streamlit as st
import modal
import openai
import json
import os

def process_podcast(url):
    f = modal.Function.lookup("corise-podcast-project-v3", "process_podcast")
    output = f.call(url, '/content/podcast/')
    return output

def main():
    st.title("Podcast Summarizer")
    
    # Create a layout with columns
    col1, col2 = st.columns([1, 3])  # Width ratio of 1:3
    
    with col1:
        st.header("Input")
        podcast_url = st.text_input("Enter the podcast URL:")
        if st.button("Summarize"):
            if podcast_url and not podcast_url.endswith('/'):
                    podcast_url += '/'
            # Add a loading state while the process_podcast function is running
            with st.spinner("Processing, please wait..."):
                # Call the process_podcast function to get podcast information
                podcast_info = process_podcast(podcast_url, podcast_path)

    with col2:
        if podcast_info is not None:
            st.header("Podcast Details")
            st.write("Title:", podcast_info['podcast_details']['title'])
            st.image(podcast_info['episode_image'])
            
            st.header("Episode Title")
            st.write(podcast_info['episode_title'])
            
            st.header("Podcast Summary")
            st.write(podcast_info['podcast_summary'])
            
            st.header("Podcast Guest")
            st.write("Name:", podcast_info['podcast_guest']['guest_name'])
            st.write("Summary:", podcast_info['podcast_guest']['guest_summary'])
            st.write("Organization:", podcast_info['podcast_guest']['guest_organization'])
            
            st.header("Podcast Highlights")
            st.write(podcast_info['podcast_highlights'])
        
        else:
            st.write("Error: Unable to retrieve podcast information. Please check the URL.")
            
if __name__ == "__main__":
    main()
