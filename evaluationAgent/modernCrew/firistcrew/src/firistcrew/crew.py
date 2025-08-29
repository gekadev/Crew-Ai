from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task ,before_kickoff, after_kickoff
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
from dotenv import load_dotenv
from pydantic import BaseModel ,Field

load_dotenv()



class KeywordInstruction(BaseModel) :
        main_topic: str = Field(..., description="Main topic of the story")
        keywords  : List[str] = Field(..., description="suggent key word that represent  main topic ")



@CrewBase
class Firistcrew():
    """Firistcrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    llm = LLM(
    model=os.environ['MODEL'],
    api_key=os.environ['GEMINI_API_KEY'],
    temperature=.4)


    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools




    @agent
    def keyWordGeneration(self) -> Agent:
        return Agent(
            config=self.agents_config['keyWordGeneration'], # type: ignore[index]
            verbose=True,
            llm=self.llm,
            output_pydantic=KeywordInstruction

        )
    
    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'], # type: ignore[index]
            verbose=True,
            llm=self.llm,

        )
    @agent
    def evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['evaluator'], # type: ignore[index]
            verbose=True,
            llm=self.llm,

        )
    
    @agent
    def performance (self) -> Agent:
        return Agent(
            config=self.agents_config['performance'], # type: ignore[index]
            verbose=True,
             llm=self.llm
        )  

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task


    # @task
    # def reporting_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['reporting_task'], # type: ignore[index]
    #         xpected_output="well strured article that generated from key words that represent out {topic}", 

    #         output_file='./output/finalreport.md',
    #     ) 
    
 
    
 
   
    @task
    def keyWordGeneration_task(self) -> Task:
        return Task(
            config=self.tasks_config['keyWordGeneration_task'], # type: ignore[index]
            output_json=KeywordInstruction,
            expected_output="JSON with fields: main_topic (str), keywords (list of str)", 
            output_file='./output/keywords.json',
            
        )   
    @task
    def writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['writer_task'], 
            expected_output="well strured article that generated from key words that represent out {topic}", 
            output_file='./output/{topic}-report.md',
            
        )
    @task
    def evaluator_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluator_task'], 
            expected_output="critical report about evaluated artricle ", 
            output_file='./output/evaluated_Report.md',
            
        )   
        
    @task
    def performance_task(self) -> Task:
        return Task(
            config=self.tasks_config['performance_task'], 
            expected_output="create final report for measuring performance and anlysis and accuarcy of generated reports ", 
            output_file='./output/finalReport.md',
            
        )



    @crew
    def crew(self) -> Crew:
        """Creates the Firistcrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
    
