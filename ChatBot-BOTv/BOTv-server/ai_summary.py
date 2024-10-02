import tiktoken
from openai import OpenAI

client = OpenAI(api_key="API_KEY")

def ai_summary(content_list,output_tokens):
    context_text = ' '.join([msg['content'] for msg in content_list])
    messages = [
        {"role": "system",
         "content": "You are a helpful assistant who provides concise and to-the-point answers."},
        {"role": "user",
         "content": f"Summarize the following conversation flow in 2-3 sentences, focusing on the key points in the user side, actions, and any conclusions or resolutions:{context_text}"}
    ]

    encoding = tiktoken.encoding_for_model("gpt-4o-mini")
    context_tokens = len(encoding.encode(' '.join([msg['content'] for msg in messages])))

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=output_tokens
    )

    assistant_response = completion.choices[0].message.content 
    total_completion_tokens = completion.usage.total_tokens
    print(f"Summary applied {context_tokens} => {total_completion_tokens-context_tokens} tokens")
    print(f" total: {total_completion_tokens} tokens")
    return assistant_response
ex =  [
    {"role": "system", "content": "You are a helpful assistant who provides personalized insights and support. You are here to discuss someone's goals, achievements, and future plans."},
    {"role": "user", "content": "Can you tell me about Sarah's journey?"},
    {"role": "system", "content": "Sarah has had an inspiring journey. She started as a software developer with a passion for artificial intelligence. Over the past 10 years, she has worked her way up from a junior developer to a lead engineer at a top tech company."},
    {"role": "user", "content": "What are some of her key achievements?"},
    {"role": "system", "content": "Sarah has made several significant contributions. She developed an AI-powered recommendation system that increased user engagement by 35% at her company. She also led a team that successfully deployed a large-scale machine learning model used by millions of users daily."},
    {"role": "user", "content": "What are her main goals for the future?"},
    {"role": "system", "content": "Sarah's primary goal is to transition into a leadership role where she can influence company strategy on AI initiatives. She is also passionate about mentoring young women in tech and aims to establish a mentorship program in the next couple of years."},
    {"role": "user", "content": "How has she prepared for that leadership role?"},
    {"role": "system", "content": "To prepare for her leadership role, Sarah has completed several leadership development courses, including one from Harvard Business School. She’s also been taking on more management responsibilities at her current job, such as leading cross-functional teams and working closely with product managers."},
    {"role": "user", "content": "Has she faced any major challenges?"},
    {"role": "system", "content": "Yes, Sarah has faced challenges, particularly in balancing her technical expertise with managerial duties. At first, she struggled with delegating tasks, but over time, she learned to trust her team and focus on bigger picture issues. She also faced biases in a male-dominated industry, which motivated her to advocate for diversity in tech."},
    {"role": "user", "content": "That's impressive. What is she currently working on?"},
    {"role": "system", "content": "Currently, Sarah is leading the development of a new AI platform that aims to streamline data analysis for small businesses. She believes this platform can help democratize access to advanced analytics, empowering smaller companies to compete with larger organizations in data-driven decision-making."},
    {"role": "user", "content": "What does she do in her free time?"},
    {"role": "system", "content": "In her free time, Sarah enjoys hiking and photography. She often combines the two, capturing nature's beauty while exploring new trails. Additionally, she volunteers at local coding boot camps, helping young people learn programming skills."},
    {"role": "user", "content": "Has she received any awards or recognition?"},
    {"role": "system", "content": "Yes, Sarah has been recognized multiple times for her contributions. She won the 'Innovator of the Year' award at her company for her work on AI-driven solutions. She was also named one of the 'Top 50 Women in Tech' by a leading technology magazine last year."},
    {"role": "user", "content": "What's her long-term vision?"},
    {"role": "system", "content": "Sarah's long-term vision is to lead a global AI research team that develops ethical AI systems for healthcare and education. She believes AI can be a powerful tool for good, and she is committed to ensuring its applications are equitable and beneficial to all."},
    {"role": "user", "content": "How does she plan to achieve that?"},
    {"role": "system", "content": "Sarah is already laying the groundwork for her long-term vision. She’s networking with AI researchers in healthcare and education and attending global conferences to stay updated on the latest trends. She's also working on a research paper that explores the ethical implications of AI in these fields, which she plans to publish soon."},
    {"role": "user", "content": "Does she have any mentors or people who inspire her?"},
    {"role": "system", "content": "Yes, Sarah has several mentors who have guided her throughout her career. Her primary mentor is Dr. Emily Tan, a pioneer in AI research, who has been a great source of advice and support. Sarah is also deeply inspired by leaders like Sundar Pichai and Sheryl Sandberg, particularly for their leadership styles and vision."},
    {"role": "user", "content": "Does she mentor anyone herself?"},
    {"role": "system", "content": "Yes, Sarah is passionate about mentoring. She currently mentors two junior developers at her company and is also involved in a mentorship program for women in tech. She believes in giving back and helping others navigate the challenges she faced early in her career."},
    {"role": "user", "content": "What’s the biggest lesson she has learned so far?"},
    {"role": "system", "content": "The biggest lesson Sarah has learned is the importance of resilience. She realized that setbacks are inevitable, but how you respond to them determines your success. She has also learned the value of continuous learning and staying adaptable in the fast-changing tech landscape."},
    {"role": "user", "content": "What advice would she give to others looking to follow a similar path?"},
    {"role": "system", "content": "Sarah’s advice to others is to stay curious, never stop learning, and seek out mentors who can guide you. She also emphasizes the importance of networking and building relationships in the industry, as well as finding a balance between technical expertise and leadership skills."},
    {"role": "user", "content": "Thanks for the detailed info!"},
    {"role": "system", "content": "You're welcome! If you need any more information about Sarah or anything else, feel free to ask."}
]
if __name__ == "__main__":
    ai_summary(ex,100)
 