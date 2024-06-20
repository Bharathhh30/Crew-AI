from crewai import Crew,Process
from agents import news_writer,news_researcher
from tasks import research_task,write_task


crew = Crew(
  agents=[news_researcher,news_writer],
  tasks=[research_task, write_task],
  process=Process.sequential
)
result=crew.kickoff(inputs={'topic':'USA Cricket team performance in World T20 2024'})
print(result)