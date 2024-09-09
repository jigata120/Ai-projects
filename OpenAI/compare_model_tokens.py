import tiktoken


def display_tokens_gpt_4o_mini(text):
    model = "gpt-4o-mini"
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    print(f"The text contains {len(tokens)} tokens using {model}.")


def display_tokens_gpt_3_5_turbo(text):
    model = "gpt-3.5-turbo"
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    print(f"The text contains {len(tokens)} tokens using {model}.")


def display_tokens_gpt_4(text):
    model = "gpt-4"
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    print(f"The text contains {len(tokens)} tokens using {model}.")


def display_tokens_davinci(text):
    model = "text-davinci-003"
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    print(f"The text contains {len(tokens)} tokens using {model}.")


def display_tokens_curie(text):
    model = "text-curie-001"
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    print(f"The text contains {len(tokens)} tokens using {model}.")


def display_tokens_babbage(text):
    model = "text-babbage-001"
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    print(f"The text contains {len(tokens)} tokens using {model}.")


# Example business data for assistant chatbot
text = """
    Company Overview: ApexBuild Construction Group
    
    About Us
        ApexBuild Construction Group is a premier construction company specializing in residential, commercial, and industrial projects. Founded in 2010, we have built a reputation for delivering high-quality, innovative, and sustainable building solutions. With offices across the United States, our team of experienced professionals is committed to excellence in every project we undertake.
    Our Mission
        At ApexBuild Construction Group, our mission is to transform visions into reality through superior construction services. We strive to deliver projects on time, within budget, and to the highest standards of quality, ensuring client satisfaction every step of the way.
        Core Values
        1. Quality: We are committed to using the best materials, craftsmanship, and technology to ensure our projects stand the test of time.
        2. Safety: We prioritize the safety of our employees, clients, and the communities where we build, adhering to strict safety protocols and industry standards.
        3. Sustainability: We integrate eco-friendly practices and sustainable materials into our projects, minimizing environmental impact and promoting green building.
        4. Integrity: We conduct our business with transparency, honesty, and a commitment to ethical practices in all aspects of our work.
        5. Customer Focus: We work closely with clients to understand their needs and deliver customized solutions that exceed expectations.
    Services Offered
        • Residential Construction: Custom homes, townhouses, and apartment buildings.
        • Commercial Construction: Office buildings, retail centers, and hospitality projects.
        • Industrial Construction: Warehouses, manufacturing plants, and distribution centers.
        • Renovation & Remodeling: Comprehensive remodeling services for residential and commercial properties.
        • Design-Build: Integrated design and construction services that streamline the building process.
        • Project Management: End-to-end project management ensuring timely and cost-effective delivery.
        • Green Building: LEED-certified projects and energy-efficient construction solutions.
    Why Choose Us?
        • Experienced Team: Our team includes skilled architects, engineers, project managers, and construction workers with decades of experience in the industry.
        • Customer Satisfaction: We have a track record of completing projects that meet or exceed client expectations, with numerous testimonials and repeat business.
        • Innovation: We stay ahead of industry trends by adopting the latest construction technologies, including Building Information Modeling (BIM) and smart construction techniques.
        • Comprehensive Solutions: From initial design to final handover, we offer a full suite of construction services, making us a one-stop solution for all building needs.
    Safety & Compliance
        ApexBuild Construction Group places a strong emphasis on safety. We follow strict safety protocols and are fully compliant with OSHA regulations. Our safety-first approach ensures that every project is executed in a safe and controlled environment, protecting both our workers and the surrounding community.
    Sustainability Commitment
        We believe in building for the future, which is why sustainability is at the core of our operations. Our projects incorporate green building practices such as energy-efficient designs, the use of sustainable materials, and waste reduction strategies. We are also proud to offer LEED-certified buildings and consult with clients on how to reduce the carbon footprint of their projects.
    Community Engagement
        ApexBuild Construction Group is committed to giving back to the communities where we operate. We partner with local organizations to support housing initiatives, workforce development programs, and other community-focused projects. Our goal is to leave a positive impact on both the built environment and the people who live in it.
    Customer Support
        Our customer support team is available to assist clients at every stage of the project. From initial inquiries to after-project support, we ensure that our clients receive prompt and effective communication. Clients can reach us via phone, email, or through our dedicated project management portal.
"""

display_tokens_gpt_4o_mini(text)
display_tokens_gpt_3_5_turbo(text)
display_tokens_gpt_4(text)
display_tokens_davinci(text)
display_tokens_curie(text)
display_tokens_babbage(text)
