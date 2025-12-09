# =============================================================================
# File:         chatbot.py
# Author:       Cédric P. Legendre
# Created:      December 2025
# Description:  Local Coding Assistant.
# License:      MIT License
#
# Copyright (c) 2025 Intellmaps s.r.o.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================
import streamlit as st
import ollama

# === Page config ===
st.set_page_config(
    page_title="Local Coding Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("Local Coding Assistant")
st.markdown("—")

# === Initialize session state (must come BEFORE any use of st.session_state) ===
if "messages" not in st.session_state:
    st.session_state.messages = []

# === Add system prompt (only once, at the very beginning) ===
system_prompt = {
    "role": "system",
    "content": "You are an expert programmer and software architect. Always provide clean, efficient, well-commented code. "
               "Explain your reasoning step by step. Use modern best practices. When suggesting architecture or strategy, "
               "be opinionated and practical. Support Python, JavaScript, Rust, Go, Bash, and any other language requested."
}

# Insert system prompt as the very first message if it's not already there
if not st.session_state.messages or st.session_state.messages[0]["role"] != "system":
    st.session_state.messages.insert(0, system_prompt)

# === Display chat history ===
for message in st.session_state.messages:
    # Skip the hidden system message from being displayed
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# === User input ===
if prompt := st.chat_input("Ask me anything about code, architecture, debugging…"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            stream = ollama.chat(
                model="coder-r1:latest",        # ← your best coding model
                messages=st.session_state.messages,   # includes the system prompt automatically
                stream=True,
            )
            response = st.write_stream(chunk["message"]["content"] for chunk in stream)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
