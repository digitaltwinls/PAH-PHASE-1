import streamlit as st


def main_home_page():
# Set the page title and favicon
    # st.set_page_config(page_title="Digital Twin Student (DTS)", page_icon=":books:")

    # Welcome Section
    st.title("Welcome to Digital Twin Student (DTS)")
    st.subheader("Empowering student learning journey")
    st.markdown('---')
    st.write("""
    In today’s fast-paced, technology-driven world, learning is a continuous journey for everyone.
    **Digital Twin Student (DTS)** is your personalized, intelligent learning coach, designed to support students' educational journeys
    through insightful analytics and dynamic engagement. DTS empowers students to achieve their goals by personalizing learning experiences
    and helping educators understand critical areas for improvement.
    """)

    # What DTS Offers Section
    st.subheader("What DTS Offers")
    st.image("src/vision.png")
    st.write("""
    - **Personalized Coaching**: DTS uses Artificial Intelligence to guide students in their learning journey, fostering deeper understanding and critical thinking skills.
    - **Enhanced Engagement**: With behavioral, emotional, and cognitive analysis, DTS provides interactive insights, helping students stay motivated and engaged.
    - **Insightful Feedback**: DTS allows educators to monitor progress and challenges, offering feedback based on cognitive frameworks like Bloom's Taxonomy and the Pedagogy-Andragogy-Heutagogy model.
    """)


    # Why Choose DTS Section
    st.subheader("Why Choose DTS?")
    st.image("src/approach.png")
    st.write("""
    Mature learners and online students often face challenges like isolation and lack of guidance, leading to high dropout rates.
    DTS addresses these issues by integrating separate systems—learning, well-being, and career services—into one cohesive platform.
    By supporting retention and improving engagement, DTS enables institutions to reduce attrition and boost student success.
    """)

    # Cognitive Analysis Tool Section
    st.subheader("Our Cognitive Analysis Tool")
    st.image("src/cognitive.jpeg",width=580)
    st.write("""
    An Innovative Approach to Self-Reflection
    Self-reflection enhances learning and accountability but can be time-consuming for educators to review.
    The DTS Cognitive Analysis Tool is designed to help students reflect deeply on their learning experiences, which has been shown to be a powerful method for understanding material and fostering personal growth. Self-reflection allows students to evaluate their strengths, identify areas for improvement, set goals, and create strategies to reach those goals. This reflective process encourages students to think critically and enhances their ability to retain information. For educators, it provides a window into each student’s thought process, helping to identify areas where guidance may be needed.

However, reviewing these reflections manually is labor-intensive, especially when dealing with large numbers of students. DTS addresses this issue by using Artificial Intelligence (AI) to automate the analysis of self-reflection texts, aligning feedback with established educational frameworks like Bloom’s Taxonomy and the Pedagogy-Andragogy-Heutagogy model. Bloom’s Taxonomy, for instance, categorizes thinking skills from basic (recalling facts) to advanced (evaluating and creating). By analyzing text within this framework, DTS can determine how deeply a student understands a topic or where they need support.

In the DTS Cognitive Analysis Tool, educational approaches are redefined to align with various levels of learner autonomy:

* Pedagogy is reframed as dependent learning, where students require structured guidance and are supported more closely by educators. This approach typically suits younger or beginner learners who benefit from a clear, structured path in their studies.

* Andragogy translates into independent learning, where learners have more autonomy and are engaged in problem-solving and self-directed exploration. It aligns with adult learners who prefer applying knowledge to real-world scenarios and require less direct guidance from instructors.

* Heutagogy represents self-determined learning, suited to advanced, highly autonomous learners. These learners are able to direct their own learning journeys, exploring and discovering new insights independently. Self-determined learners are motivated to dive deeper and can set personal goals and strategies for growth without external prompts.

The DTS tool uses this framework to assess each student’s reflection and provides feedback that aligns with their level of autonomy. This tailored feedback supports learners’ growth at every stage of their journey, from dependent to independent to fully self-directed learning. Through these insights, DTS helps educators understand each student’s unique needs and promotes a gradual progression towards self-determined, lifelong learning.
    """)

    # Footer or Additional Information
    st.markdown('---')
    st.write("##### DTS: Enhancing learning experiences and enabling lifelong success.")
