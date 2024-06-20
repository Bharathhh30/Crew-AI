from crewai import Task
from tools import tool
from agents import news_researcher,news_writer


#  Creating the research task

research_task = Task(
  description=(
    "Identify the news/facts/informations regarding  {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points present in the news article as well the sources,"
  ),
  expected_output='A comprehensive 3 paragraphs long report on the {topic}.',
  tools=[tool],
  agent=news_researcher,
)

# Writing the blog from the researcch done

write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest news and information regarding the {topic}"
    "This article should be easy to understand, engaging, and positive also should be informative (Consider this to be mandatory)."
  ),
  expected_output='A 4 paragraph article on {topic}  formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)