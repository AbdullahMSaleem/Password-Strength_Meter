import streamlit as st
import time
import math
import string

def calculate_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    
    complexity = (has_lower + has_upper + has_digit + has_symbol) * 26
    entropy = length * math.log2(complexity)
    
    # Estimated time to crack password (rough estimate in seconds)
    seconds_to_crack = 2**entropy / 1e9  # assuming 1 billion guesses per second
    
    return entropy, seconds_to_crack

def strength_label(entropy):
    if entropy < 30:
        return "Weak", "#FF4C4C"
    elif entropy < 50:
        return "Moderate", "#FFA500"
    elif entropy < 80:
        return "Strong", "#00C853"
    else:
        return "Very Strong", "#00796B"

def format_crack_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds / 86400:.2f} days"
    elif seconds < 3.154e+7 * 100:
        return f"{seconds / 3.154e+7:.2f} years"
    else:
        return "Millions of years"

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Enter a password below to check its strength.")

password = st.text_input("Enter your password", type="password")

if password:
    entropy, crack_time = calculate_strength(password)
    strength, color = strength_label(entropy)
    
    st.markdown(f"""<h3 style='color: {color};'>{strength}</h3>""", unsafe_allow_html=True)
    st.write(f"Estimated time to crack: {format_crack_time(crack_time)}")
    
    with st.expander("Password Analysis"):
        st.write(f"**Length:** {len(password)} characters")
        st.write(f"**Contains Lowercase:** {'✅' if any(c.islower() for c in password) else '❌'}")
        st.write(f"**Contains Uppercase:** {'✅' if any(c.isupper() for c in password) else '❌'}")
        st.write(f"**Contains Numbers:** {'✅' if any(c.isdigit() for c in password) else '❌'}")
        st.write(f"**Contains Symbols:** {'✅' if any(c in string.punctuation for c in password) else '❌'}")
