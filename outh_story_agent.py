# youth_story_agent.py

import streamlit as st

class YouthStoryBuilderAgent:
    def __init__(self):
        self.story_theme = None
        self.selected_idea = None
        self.story_outline = None

    def classify_story_type(self, user_input):
        genres = [
            "成长故事：主要讲述青少年在成长过程中的心理变化、人生选择和成长困惑，关注青少年的自我发现与成长。",
            "冒险故事：青少年角色在探索未知的世界、面对挑战时发生的故事，通常充满刺激和冒险。",
            "校园故事：围绕青少年在学校的生活展开，描绘他们与同学、老师之间的关系，解决问题，成长与变化。",
            "科幻/奇幻故事：青少年主角参与虚构的、超现实的世界，可能涉及外星、时间旅行、魔法等元素。",
            "家庭故事：关注青少年与家庭成员之间的关系，可能探讨家庭矛盾、亲情和成长等话题。",
            "悬疑/侦探故事：以青少年为主角，解决谜题或揭开悬疑。",
            "爱情故事：青少年在成长过程中经历的爱情故事，可能是初恋、暗恋等，描绘他们的情感体验。"
        ]
        return [g for g in genres if any(t in user_input for t in g.split("：")[0])]

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
            "unit_1": "第一单元：觉醒服务意识，组成团队，设立目标。侧重思想力的提升和小组协作。",
            "unit_2": "第二单元：开展真实服务行动，面对挑战，合作成长，体现社会贡献与自我发展统一。"
        }
        return self.story_outline

    def write_chapter(self, unit):
        if unit == "unit_1":
            return (
                "第一章：阳光洒进教室，班主任在黑板上写下“校园改变行动”。主角小杰灵光一闪，提出了清洁校园的想法。"
                "他的提议立刻引发了热烈讨论。班上的几个好友志强、小慧、阿芳加入了小杰的计划。"
                "他们组成了“校园服务小队”，分工合作，制定了一个周末清洁校园的初步计划。每个人都热血沸腾，跃跃欲试。"
            )
        elif unit == "unit_2":
            return (
                "第二章：到了周末，小队一早来到学校，却发现扫帚和垃圾袋不够用，天色也阴沉下来。"
                "但没有人退缩，小杰灵机一动，向看门的老王借来了备用工具。清扫过程中，他们彼此鼓励，还吸引了其他同学加入。"
                "当阳光再次露面时，整个校园焕然一新。校长经过时投来赞许的目光，而小队成员也从服务中获得了前所未有的满足与成长。"
            )

# === Streamlit App ===
def main():
    st.title("📚 Youth Story Builder Agent")
    st.write("帮助你为青少年创作富有成长与服务精神的故事")

    agent = YouthStoryBuilderAgent()

    theme_input = st.text_input("请输入你想强调的故事主题关键词（如 服务、成长、家庭）：")
    if theme_input:
        genres = agent.classify_story_type(theme_input)
        st.write(f"识别的题材类型：\n- " + "\n- ".join(genres))

        ideas = agent.generate_story_ideas(theme_input)
        selected_idea = st.selectbox("请选择一个故事创意：", ideas)

        if selected_idea:
            idea_index = ideas.index(selected_idea) + 1
            outline = agent.build_outline(idea_index)
            st.subheader("📋 故事大纲")
            st.markdown(f"**单元一：** {outline['unit_1']}\n\n**单元二：** {outline['unit_2']}")

            st.subheader("✍️ 第一章：内在觉醒与行动启动")
            chapter1 = agent.write_chapter("unit_1")
            st.text_area("第一章内容：", value=chapter1, height=200)

            st.subheader("✍️ 第二章：深化成长与社会贡献")
            chapter2 = agent.write_chapter("unit_2")
            st.text_area("第二章内容：", value=chapter2, height=200)

if __name__ == "__main__":
    main()
