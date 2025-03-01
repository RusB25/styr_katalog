import streamlit as st

st.set_page_config(page_title="W17 driftsättning", layout="wide")

# Title of the app
st.title("DUC byte till W17")

# Instructions for the user
st.markdown(
    """
    För att utföra DUC byte till W17, vänligen följ stegen nedan:

    1. **Ladda ner mallen**:
       - Klicka på knappen nedan för att ladda ner filen.

    2. **Fyll i mallen**:
       - Öppna den nedladdade filen och bocka alla nödvändiga steg under kolumnen "Done" genom att dubbelklicka.

    3. **Skicka mallen**:
       - När du har fyllt i mallen, skicka den via e-post till den ansvariga personen.
    """
)

filepath1 = "files/W17_setup.xlsm"
with open(filepath1, "rb") as file:
    st.download_button(
        "Download File",
        data=file,
        mime="application/vnd.ms-excel.sheet.macroEnabled.12",
        file_name="W17_setup.xlsm",
    )

st.markdown("---")

st.title("Kopiering av grupper eller enheter mellan olika databaser/anläggningar")

st.markdown(
    "Detta dokument beskriver hur man gör och bör tänka på när man slår ihop 2st. anläggningar som varit i drift. Vid kopiering kopieras editering, bilder, anteckningar, trendkurvor och händelselistor."
)

filepath2 = "files/Slå_ihop_anläggningar.pdf"
with open(filepath2, "rb") as file:
    st.download_button(
        "Download File",
        data=file,
        mime="application/pdf",
        file_name="Slå_ihop_anläggningar.pdf",
    )

st.markdown("---")

st.title("INSTALLATIONSANVISNING EVO SCADA")

st.markdown(
    "Detta dokument beskriver hur man installerar EVO SCADA på en dator. EVO SCADA är ett program som används för att övervaka och styra anläggningar."
)

filepath3 = "files/Installationsanvisning_Evo_SCADA.pdf"
with open(filepath3, "rb") as file:
    st.download_button(
        "Download File",
        data=file,
        mime="application/pdf",
        file_name="Installationsanvisning_Evo_SCADA.pdf",
    )

st.markdown("---")

st.title("DRIFTSÄTTNINGINSTRUKTION AVALON ONE & W17")

st.markdown("Detta dokument beskriver hur man driftsätter Avalon One & W17.")

filepath4 = "files/Avalon W17 - Driftsättningsinstruktion.pdf"
with open(filepath4, "rb") as file:
    st.download_button(
        "Download File",
        data=file,
        mime="application/pdf",
        file_name="Avalon W17 - Driftsättningsinstruktion.pdf",
    )

# Add author information and bug report link at the bottom
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            color: #333;
            z-index: 1000;
        }
    </style>
    <div class="footer">
        Created by Ruslan Bagirov © 2025 | <a href="mailto:ruslan861125@gmail.com?subject=Bug Report">Report a bug</a>
    </div>
    """,
    unsafe_allow_html=True,
)
