from crewai import Task
from typing import List

def create_research_task(researcher, topic: str) -> Task:
    """Create a research task"""
    return Task(
        description=f"""Research the topic: {topic}
        
        Your research should include:
        1. Current trends and developments
        2. Key facts and statistics
        3. Different perspectives on the topic
        4. Recent news or events related to the topic
        
        Format your response with:
        - Clear headings
        - Bullet points for lists
        - Easy to read paragraphs
        
        Provide comprehensive findings that can be used to create engaging content.""",
        agent=researcher,
        expected_output="A detailed research report with key findings, statistics, and insights about the topic."
    )

def create_writing_task(writer, topic: str, research_task: Task) -> Task:
    """Create a writing task"""
    return Task(
        description=f"""Based on the research findings, create engaging content about: {topic}
        
        The content should:
        1. Be informative and well-structured
        2. Include relevant facts and statistics
        3. Be engaging for the target audience
        4. Be between 500-800 words
        5. Be clearly formatted and easy to read
        
        Format with:
        - Clear headings
        - Good paragraph structure
        - Bullet points where helpful
        - A conclusion section
        
        Use the research provided by the Research Analyst to create compelling content.""",
        agent=writer,
        expected_output="A well-written article about the topic, incorporating research findings.",
        context=[research_task]
    )

def create_editing_task(editor, writing_task: Task) -> Task:
    """Create an editing task"""
    return Task(
        description="""Review and improve the content created by the Content Writer.
        
        Focus on:
        1. Grammar and spelling
        2. Clarity and readability
        3. Logical flow and structure
        4. Fact-checking and accuracy
        5. Overall quality and engagement
        
        Ensure the final output is:
        - Well-structured and easy to read
        - Free of errors
        - Engaging and informative
        - Properly formatted
        
        Provide the final polished version of the content.""",
        agent=editor,
        expected_output="A polished, error-free version of the content that maintains engagement while ensuring accuracy.",
        context=[writing_task]
    )

def create_research_workflow_tasks(researcher, writer, editor, topic: str) -> List[Task]:
    """Create all tasks for the research workflow"""
    research_task = create_research_task(researcher, topic)
    writing_task = create_writing_task(writer, topic, research_task)
    editing_task = create_editing_task(editor, writing_task)
    
    return [research_task, writing_task, editing_task] 