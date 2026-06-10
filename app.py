
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Title
st.set_page_config(page_title="Thunder Detection FYP", layout="wide")
st.title("⚡ Cloud-to-Ground (CG) Lightning Detection")
st.subheader("Universiti Teknikal Malaysia Melaka (UTeM)")

# Sidebar
st.sidebar.header("📊 Thunder Parameters")

# Data (contoh - kau boleh ganti dengan data real)
data = {
    "Parameter": ["Peak Amplitude (dB)", "Duration (s)", "Rise Time (s)", "Peak Frequency (Hz)"],
    "CG Target": ["> -10", "< 2", "< 0.1", "< 200"],
    "Test 1 Value": [-21.76, 7.20, 1.709, 337.42],
     "Test 2 Value": [-13.911, 29.49, 25.215, 146.166],
    "Status": ["❌ Too Low", "❌ Too Long", "❌ Too Slow", "❌ Too High"]
    "Status": ["❌ Too Low", "❌ Too Long", "❌ Too Slow", "✅ Good"]
    
}
df = pd.DataFrame(data)

# Display table
st.subheader("📋 Thunder Analysis Results")
st.dataframe(df, use_container_width=True)

# Target criteria
st.subheader("🎯 CG Lightning Target Criteria")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Peak Amplitude", "> -10 dB", "Need higher")
col2.metric("Duration", "< 2 s", "Need shorter")
col3.metric("Rise Time", "< 0.1 s", "Need faster")
col4.metric("Peak Frequency", "< 200 Hz", "Need lower")

# Plot waveform example
st.subheader("📈 Thunder Waveform")
t = np.linspace(0, 7.2, 1000)
# Simulated waveform (ganti dengan data real kau nanti)
waveform = 0.15 * np.sin(2 * np.pi * 50 * t) * np.exp(-t/2)
fig, ax = plt.subplots()
ax.plot(t, waveform)
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Amplitude")
ax.set_title("Thunder Waveform (Example)")
ax.grid(True)
st.pyplot(fig)

# References
st.subheader("📚 References")
st.markdown("""
- **Hazmi et al. (2019)** - Thunder frequency: 4.88-175.78 Hz
- **Wang et al. (2023)** - Combined filtering accuracy: 93.18%
- **Lacroix et al. (2019)** - CG deposited energy: 4-60 J/cm
- **Bodhika (2019)** - Clap duration: 0.2-2 s (86% of flashes)
""")

# Methodology
with st.expander("📝 Methodology"):
    st.markdown("""
    - **Sensor:** Acoustic sensor (microphone)
    - **Software:** Audacity + Python/Streamlit
    - **Location:** UTeM faculty building
    - **Filtering:** Spectral subtraction + low-pass @ 200 Hz
    """)

st.caption("© 2025 FYP - UTeM")
