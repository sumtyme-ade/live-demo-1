import streamlit as st

st.set_page_config(
    page_title="sumtyme.ai",
    page_icon="brandmark.png"
 
)

col1, col2, col3 = st.columns([1, 3, 1])

# Place the image inside the middle column
with col2:
    # We use 'use_column_width=True' here to make the image fill the width of its *containing column*.
    # Since the column itself is smaller than the page, the image will be smaller and centered.
    st.image('sumtyme_logo.png')
# --- End of the code to center the image ---

st.markdown("""
With our platform, developers and enterprises can model dynamic systems instantly, saving time and costly training runs. Our proprietary technology fundamentally changes how intelligent AI systems are built, creating models that can reason, adapt, and think beyond their training data.""")

tab1, tab2 = st.tabs(["Key Benefits", "Video Demo"])

with tab1:

    st.markdown("""
    Key Benefits:
    """)
    
    st.markdown("""
    - **Zero Training Data Dependence:** Our platform provides the core intelligence needed to model dynamic systems, removing the traditional reliance on training data.
    - **Zero Feature Engineering & Fine-Tuning:** We eliminate the complex and time-consuming process of manually creating features or adapting existing models, streamlining model development.
    - **Zero Retraining Cycles:** Our solution eliminates frequent, resource-intensive retraining, ensuring continuous model effectiveness without the need for constant updates.
    """)

with tab2:

    st.markdown("""Demonstrating our ability to model noisy, high-frequency data without training or retraining, our API was used to build a four-timeframe network (1, 2, 3, and 4-second intervals) to model the market dynamics of the SPY ETF.""")
    st.markdown("""The technology successfully anticipated a market decline 10 minutes before Trump's tariff announcement on April 2nd, 2025.""")
    
    video_bytes = "https://github.com/sumtyme-ade/live-demo-1/releases/download/v1.0.0/20252905.mp4"

    st.video(video_bytes)
