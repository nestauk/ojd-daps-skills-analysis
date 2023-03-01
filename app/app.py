import os
from pathlib import Path

import streamlit as st
from annotated_text import annotated_text

from ojd_daps_skills.pipeline.extract_skills.extract_skills import ExtractSkills

PROJECT_DIR = Path(__file__).resolve().parents[1]
app_folder = os.path.join(PROJECT_DIR, "app/")

st.set_page_config(
    page_title="Nesta Skills Extractor", page_icon=os.path.join(app_folder, "images/nesta_logo.png"),
)

def hash_config_name(es):
    # custom hash function in order to use st.cache
    return es.taxonomy_name
    
@st.cache(hash_funcs={ExtractSkills: hash_config_name})
def load_model(app_mode):
    if app_mode == esco_tax:
        es = ExtractSkills(config_name="extract_skills_esco", local=True)
    elif app_mode == lightcast_tax:
        es = ExtractSkills(config_name="extract_skills_lightcast", local=True)
    es.load()
    return es

col1, col2 = st.columns([45, 55])

with col1:
    st.image(os.path.join(app_folder, "images/nesta_escoe_logo.png"))

with col2:
    st.markdown(
        "<p class='title-font'>Skills Extractor</p>",
        unsafe_allow_html=True,
    )

# ----------------- streamlit config ------------------#

with open(os.path.join(app_folder, "style.css")) as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
This app shows how Nesta's [Skills Extractor Python Library](https://github.com/nestauk/ojd_daps_skills) can extract skills from a job advert and then match those terms to skills from a standard list or ‘skills taxonomy’. 
At present, you can choose to match extracted skills to one of two skills taxonomies that have been developed by other groups:
1. The [European Commission's ESCO taxonomy v1.1.1](https://esco.ec.europa.eu/en/classification/skill_main) which is a multilingual classification of European Skills, Competences, Qualifications and Occupations and;
2. [Lightcast's Open Skills taxonomy](https://lightcast.io/open-skills) (as of 22/11/22) which is open source library of 32,000+ skills
"""
)

st.warning(
    "As with any algorithm, our approach has limitations. As a result, we cannot guarantee the accuracy of every extracted or mapped skill. To learn more about the strengths and limitations, consult our [model cards](https://nestauk.github.io/ojd_daps_skills/build/html/model_card.html).",
    icon="🤖",
)

st.markdown(
    """
If you would like to explore how the algorithm can provide new insights on the UK skills landscape, check out this interactive blog (link pending) that analyses extracted skills from thousands of job adverts. 
"""
)


esco_tax = "ESCO"
lightcast_tax = "Lightcast"
app_mode = st.selectbox("🗺️ Choose a taxonomy to map onto", [esco_tax, lightcast_tax])
txt = st.text_area(
    "✨ Add your job advert text here ... or try out the phrase 'You must have strong communication skills.'",
    "",
)
es = load_model(app_mode)

@st.cache(allow_output_mutation=True)
def SkillsExtracted():
    return []

skills_extracted_counter=SkillsExtracted()

button = st.button("Extract Skills")

if button:
    skills_extracted_counter.append('dummy')
    txt = txt.replace("\n", ". ")
    with st.spinner("🤖 Running algorithms..."):

        extracted_skills = es.extract_skills(txt)

    if "SKILL" in extracted_skills[0].keys():
        st.success(f"{len(extracted_skills[0]['SKILL'])} skill(s) extracted!", icon="💃")
        st.markdown(f"**The extracted skills are:** ")
        annotated_text(
            *[
                highlight
                for s in extracted_skills[0]["SKILL"]
                for highlight in [(s[0], "", "#F6A4B7"), " "]
            ]
        )
        st.markdown("")  # Add a new line
        st.markdown(f"**The _{app_mode}_ taxonomy skills are**: ")
        annotated_text(
            *[
                highlight
                for s in extracted_skills[0]["SKILL"]
                for highlight in [(s[1][0], "", "#FDB633"), " "]
            ]
        )

    else:
        st.warning("No skills were found in the job advert", icon="⚠️")

st.write("#")
st.markdown("""---""")
st.markdown(
    """
<small><p>The Skills Extractor library was made possible by funding from the [Economic Statistics Centre of Excellence](https://www.escoe.ac.uk/).</p></small>

<small><p>If you have any feedback or questions about the library or app, do reach out to **dataanalytics@nesta.org.uk**.</p></small>
""",
unsafe_allow_html=True,
)

# Page views

@st.cache(allow_output_mutation=True)
def Pageviews():
    return []

pageviews=Pageviews()
pageviews.append('dummy')

st.write("#")
st.write("#")
st.write("#")

st.markdown(
    """
<style>
.tiny-font {
    font-size:14px !important;
    color: #646363;
    text-align: center;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<p class='tiny-font'>Page viewed {} times. Skills extracted {} times.</p>".format(len(pageviews), len(skills_extracted_counter)),
    unsafe_allow_html=True,
)

