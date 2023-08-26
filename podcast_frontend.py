import streamlit as st
import modal
import json
import os

def process_podcast(url):
    f = modal.Function.lookup("corise-podcast-project-v3", "process_podcast")
    output = f.call(url, '/content/podcast/')
    return output

def main():
    
    # Create a sidebar for inputs
    st.sidebar.header("Input")
    podcast_url = st.sidebar.text_input("Enter the podcast URL:")
    if st.sidebar.button("Summarize"):
        
        with st.spinner("Processing, please wait..."):
            # Call the process_podcast function to get podcast information
            podcast_info = process_podcast(podcast_url)
        
        if podcast_info is not None:
            # Create a section for outputs to the right
            output_section = st.beta_container()
            
            with output_section:
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
