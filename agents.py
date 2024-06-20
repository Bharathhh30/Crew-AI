from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from tools import tool
load_dotenv()
import os

# Using Gemini Model
llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Creating senior research agent
news_researcher=Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking facts and information in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world and want to make the news go wide and make meaning."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating writer agent with custom tools responsible in writing news blog
news_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "informations and facts to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)