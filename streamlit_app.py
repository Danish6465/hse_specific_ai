import requests
import streamlit as st

# Page Configuration for Mobile Optimization
st.set_page_config(
    page_title="HSE JSA Generator", page_icon="🛡️", layout="centered"
)

# App Header
st.title("🛡️ Mobile JSA Generator")
st.markdown(
    "Generate field-ready Job Safety Analyses and Toolbox Talk briefs instantly."
)

# Input Form for Safety Officer / Supervisor
with st.form("jsa_form"):
  st.subheader("1. Task Details")
  task_name = st.text_input(
      "Task Description",
      placeholder="e.g., Hot work near hydrocarbon lines / Sandblasting",
  )
  location = st.text_input(
      "Work Location / Unit", placeholder="e.g., Unit-104 / Storage Tank Area"
  )

  st.subheader("2. Hazard Identification")
  hazards = st.multiselect(
      "Select Anticipated Hazards",
      [
          "Fire & Explosion",
          "Working at Heights",
          "Confined Space Entry",
          "Electrical Hazards",
          "Toxic Gas Release / H2S",
          "Moving Machinery",
          "Slip, Trip & Fall",
          "Manual Handling",
      ],
  )

  additional_notes = st.text_area(
      "Specific Site Conditions / Extra Notes",
      placeholder="Enter any specific weather, permits, or PPE requirements...",
  )

  submitted = st.form_submit_button("Generate JSA Report 🚀")

# Webhook Trigger & Response Handling
if submitted:
  if not task_name or not location:
    st.warning("⚠️ Please provide at least the Task Description and Location.")
  else:
    # Your Make.com Webhook URL
    webhook_url = "https://hook.eu1.make.com/inhegyi298f6mkvfxowd0hoq2tnq4qop"

    payload = {
        "task_name": task_name,
        "location": location,
        "hazards": hazards,
        "additional_notes": additional_notes,
    }

    with st.spinner(
        "🔄 Transmitting data to HSE processing engine & generating JSA..."
    ):
      try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
          st.success("✅ JSA Request Sent Successfully to Make.com!")
          st.info(
              "Your backend automation is now processing this via Gemini API."
          )
        else:
          st.error(
              f"❌ Failed to trigger automation. Status code:"
              f" {response.status_code}"
          )
      except Exception as e:
        st.error(f"❌ Connection error: {e}")
