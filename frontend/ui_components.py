# frontend/ui_components.py
import streamlit as st

def styled_button(label, key=None):
    """
    A simple styled button component.
    """
    return st.button(label, key=key, help=f"Click to {label.lower()}")

def custom_text_input(label, placeholder="", key=None):
    """
    A custom text input component.
    """
    return st.text_area(label, placeholder=placeholder, key=key, height=100) 