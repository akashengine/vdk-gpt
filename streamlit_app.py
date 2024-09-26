import streamlit as st

# Configuration and Setup
st.set_page_config(page_title="VDK GPT", layout="wide")

# Helper Functions
def load_css():
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Main App
def main():
    load_css()

    # Initialize session state
    if 'selected_video' not in st.session_state:
        st.session_state.selected_video = None

    # Main Page
    st.title("VDK GPT")

    videos = [
        ("UvNNCdSHZ_A", "Jain Philosophy: An Introduction"),
        ("8mxDiefPrcc", "Challenges of Parenting"),
        ("fbgKj0myUOk", "The Art of Letting Go"),
        ("ALuyrcNfNRM", "Why Dr. Ambedkar is Great?"),
        ("ISRQ7djT3uw", "Sikkim Youth Convention 2023")
    ]

    if not st.session_state.selected_video:
        cols = st.columns(3)
        for idx, (video_id, title) in enumerate(videos):
            with cols[idx % 3]:
                st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
                if st.button(title, key=f"btn_{video_id}"):
                    st.session_state.selected_video = video_id
                    st.rerun()

    # Video Interaction Page
    else:
        video_id = st.session_state.selected_video
        st.video(f"https://youtu.be/{video_id}")

        tab1, tab2, tab3 = st.tabs(["Summarize", "Quiz Me", "Ask any Doubt"])

        with tab1:
            st.subheader("Summarize")
            st.text_area("Summary will appear here")

        with tab2:
            st.subheader("Quiz Me")
            st.write("Quiz questions will appear here")

        with tab3:
            st.subheader("Ask any Doubt")
            st.text_input("Enter your question")
            st.button("Ask")

        if st.button("Back to Videos"):
            st.session_state.selected_video = None
            st.rerun()

if __name__ == "__main__":
    main()
