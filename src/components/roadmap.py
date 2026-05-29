import streamlit as st


def render_roadmap(missing_skills):

    st.markdown("## Personalized Learning Roadmap")

    roadmap = {
        "Foundation": [],
        "Core Engineering": [],
        "Specialization": [],
        "Cloud & Deployment": []
    }

    for skill in missing_skills:

        if skill in ["statistics", "mathematics"]:
            roadmap["Foundation"].append(skill)

        elif skill in [
            "machine learning",
            "deep learning"
        ]:
            roadmap["Core Engineering"].append(skill)

        elif skill in [
            "nlp",
            "computer vision"
        ]:
            roadmap["Specialization"].append(skill)

        else:
            roadmap["Cloud & Deployment"].append(skill)

    for phase, skills in roadmap.items():

        if skills:

            st.markdown(
                f"""
                <div style="
                    background-color:#161B22;
                    padding:20px;
                    border-radius:15px;
                    margin-bottom:15px;
                    border-left:5px solid #4F46E5;
                ">

                <h3>{phase}</h3>

                <p>{", ".join(skills)}</p>

                </div>
                """,
                unsafe_allow_html=True
            )