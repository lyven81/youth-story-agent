# youth_story_agent.py

import streamlit as st

class YouthStoryBuilderAgent:
    def __init__(self):
        self.story_theme = None
        self.selected_idea = None
        self.story_outline = None

    def classify_story_type(self, user_input):
        genres = ["成长", "冒险", "校园", "奇幻", "家庭", "悬疑", "爱情"]
        return [g for g in genres if g in user_input]

    def generate_story_ideas(self, theme):
        ideas = [
            f"一个热心青少年发起学校清洁日，唤起大家对公共空间的责任感。",
            f"三位同学利用课余时间帮助年长邻居，建立代际交流。",
            f"一个内向的学生通过社区服务发现表达自己的勇气。",
            f"一群青少年改造被遗弃的花园，学会合作与奉献。",
            f"主角在照顾病弱邻居的过程中发现了自己未来的志向。"
        ]
        return ideas

    def build_outline(self, idea_number):
        self.story_outline = {
            "unit_1": "觉醒服务意识，组成团队，设立目标",
            "unit_2": "开展行动，面对困难，合作克服，收获成长"
        }
        return self.story_outline

    def write_chapter(self, unit):
        if unit == "unit_1":
            return ("第一章：在一次班会中，主角提出为学校服务的想法，"
                    "小组成员们开始讨论他们可以做些什么来改善校园环境。大家决定周末一起清洁校园角落，"
                    "并制定了分工计划，充满干劲地迎接挑战。")
        elif unit == "unit_2":
            return ("第二章：清洁行动当天，他们发现工具不足，天气也突然下雨。但通过互相鼓励，"
                    "大家仍坚持完成任务。过程中，他们也感染了其他同学加入，最终让校园焕然一新，"
                    "而他们的友情与信念也变得更强。")

# === Streamlit App ===
def main():
    st.title("📚 Youth Story Builder Agent")
    st.write("帮助你为青少年创作富有成长与服务精神的故事")

    agent = YouthStoryBuilderAgent()

    theme_input = st.text_input("请输入你想强调的故事主题关键词（如 服务、成长、家庭）：")
    if theme_input:
        genres = agent.classify_story_type(theme_input)
        st.write(f"识别的题材类型：{', '.join(genres)}")

        ideas = agent.generate_story_ideas(theme_input)
        selected_idea = st.selectbox("请选择一个故事创意：", ideas)

        if selected_idea:
            idea_index = ideas.index(selected_idea) + 1
            outline = agent.build_outline(idea_index)
            st.subheader("📋 故事大纲")
            st.markdown(f"**单元一：** {outline['unit_1']}\n\n**单元二：** {outline['unit_2']}")

            st.subheader("✍️ 第一章")
            chapter1 = agent.write_chapter("unit_1")
            st.text_area("第一章内容：", value=chapter1, height=150)

            st.subheader("✍️ 第二章")
            chapter2 = agent.write_chapter("unit_2")
            st.text_area("第二章内容：", value=chapter2, height=150)

if __name__ == "__main__":
    main()
