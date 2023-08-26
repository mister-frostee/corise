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

    podcast_info = None
        
    st.title("Podcast Summarizer")
    
    st.sidebar.header("Input")
    podcast_url = st.sidebar.text_input("Enter the podcast URL:")
    
    if st.sidebar.button("Summarize"):
        if podcast_url and not podcast_url.endswith('/'):
            podcast_url += '/'
        with st.spinner("Processing..."):
            # Call the process_podcast function to get podcast information
            podcast_info = process_podcast(podcast_url)

    if podcast_info is not None:
        output_container = st.container()
        with output_container:
                st.subheader("Raw Podcast Output:")
                st.text(podcast_info)
                st.header("Podcast Details")
                st.write("Title:", podcast_info['podcast_details']['podcast_title'])
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
        st.write("Nothing to see here...")
            
if __name__ == "__main__":
    main()
