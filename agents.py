import os
from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
# setting up google gemini api key

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
# Creating a new agent whose role is senior blog reasearcher

blog_researcher = Agent(
    role="Senior Blog Researcher from Youtube Videos",
    goal="get the relevant video content for the topic {topic} from youtube channel",
    verboe=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

# What ever the work the blog researcher does he needs to transfer it to the blog writer so delagation is kept true

# Creating a blog writer which writes us blogs from the information fetched by the blog researcher

blog_writer = Agent(
    role = "Blog Writer",
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)

# The blog writer is no way meant to transfer his work so we kept allow delagation as False