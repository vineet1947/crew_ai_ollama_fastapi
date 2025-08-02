from crewai import Agent
from models.ollama_llm import create_deepseek_llm

# Get the LLM instance with specific model
llm = create_deepseek_llm()

# Define agents directly with the LLM instance
researcher_agent = Agent(
    role='Research Analyst',
    goal='Conduct thorough research on given topics and provide detailed insights',
    backstory="""You are an expert research analyst with years of experience in 
    gathering and analyzing information. You have a keen eye for detail and can 
    find relevant information from various sources. You can provide comprehensive 
    analysis based on your knowledge. Format your responses clearly with headings 
    and bullet points for easy reading.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

writer_agent = Agent(
    role='Content Writer',
    goal='Create engaging and informative content based on research findings',
    backstory="""You are a skilled content writer who can transform complex 
    information into clear, engaging content. You have a talent for making 
    technical topics accessible to various audiences. Format your content clearly 
    with good structure and easy-to-read paragraphs.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

editor_agent = Agent(
    role='Content Editor',
    goal='Review and improve content for clarity, accuracy, and quality',
    backstory="""You are an experienced editor with a strong background in 
    content quality assurance. You ensure all content meets high standards 
    for clarity, accuracy, and engagement. You maintain clear formatting 
    while improving the overall quality of the content.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
) 