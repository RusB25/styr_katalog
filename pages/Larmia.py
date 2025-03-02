import streamlit as st

st.set_page_config(page_title="W17 driftsättning", layout="wide")

from components.Footnote import footnote
from components.Styles import add_styles
from components.Divider import blue_divider

add_styles()

st.markdown(
    '<div class="section-title">DUC byte till W17</div>', unsafe_allow_html=True
)

# Instructions for the user
st.markdown(
    """
    <div class="markdown-section">
    För att utföra DUC byte till W17, vänligen följ stegen nedan:

    1. **Ladda ner mallen**:
       - Klicka på knappen nedan för att ladda ner filen.

    2. **Fyll i mallen**:
       - Öppna den nedladdade filen och bocka alla nödvändiga steg under kolumnen "Done" genom att dubbelklicka.

    3. **Skicka mallen**:
       - När du har fyllt i mallen, skicka den via e-post till den ansvariga personen.
    </div>
    """,
    unsafe_allow_html=True,
)

filepath1 = "files/W17_setup.xlsm"
with open(filepath1, "rb") as file:
    st.download_button(
        "Download File",
        data=file,
        mime="application/vnd.ms-excel.sheet.macroEnabled.12",
        file_name="W17_setup.xlsm",
        key="download1",
    )

blue_divider()

st.markdown(
    '<div class="section-title">Kopiering av grupper eller enheter mellan olika databaser/anläggningar</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="markdown-section">
    Detta dokument beskriver hur man gör och bör tänka på när man slår ihop 2st. anläggningar som varit i drift. Vid kopiering kopieras editering, bilder, anteckningar, trendkurvor och händelselistor.
    </div>
    """,
    unsafe_allow_html=True,
)

filepath2 = "files/Slå_ihop_anläggningar.pdf"
with open(filepath2, "rb") as file:
    st.download_button(
        "Download File",
        data=file,
        mime="application/pdf",
        file_name="Slå_ihop_anläggningar.pdf",
        key="download2",
    )

blue_divider()

st.markdown(
    '<div class="section-title">INSTALLATIONSANVISNING EVO SCADA</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="markdown-section">
    Detta dokument beskriver hur man installerar EVO SCADA på en dator. EVO SCADA är ett program som används för att övervaka och styra anläggningar.
    </div>
    """,
    unsafe_allow_html=True,
)

filepath3 = "files/Installationsanvisning_Evo_SCADA.pdf"
with open(filepath3, "rb") as file:
    st.download_button(
        "Download File",
        data=file,
        mime="application/pdf",
        file_name="Installationsanvisning_Evo_SCADA.pdf",
        key="download3",
    )

blue_divider()

st.markdown(
    '<div class="section-title">DRIFTSÄTTNINGINSTRUKTION AVALON ONE & W17</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="markdown-section">
    Detta dokument beskriver hur man driftsätter Avalon One & W17.
    </div>
    """,
    unsafe_allow_html=True,
)

filepath4 = "files/Avalon W17 - Driftsättningsinstruktion.pdf"
with open(filepath4, "rb") as file:
    st.download_button(
        "Download File",
        data=file,
        mime="application/pdf",
        file_name="Avalon W17 - Driftsättningsinstruktion.pdf",
        key="download4",
    )

# Add author information and bug report link at the bottom
footnote()
