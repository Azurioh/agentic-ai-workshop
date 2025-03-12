"""🔍 AI Research Agent - Your AI Research Assistant!

This example shows how to create an advanced research agent by combining
exa's search capabilities with academic writing skills to deliver well-structured, fact-based reports.

Key features demonstrated:
- Using Exa.ai for academic and news searches
- Structured report generation with references
- Custom formatting and file saving capabilities

Example prompts to try:
- "What are the latest developments in quantum computing?"
- "Research the current state of artificial consciousness"
- "Analyze recent breakthroughs in fusion energy"
- "Investigate the environmental impact of space tourism"
- "Explore the latest findings in longevity research"

Run `pip install openai exa-py agno` to install dependencies.
"""

from datetime import datetime
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools

cwd = Path(__file__).parent.resolve()
tmp = cwd.joinpath("tmp")
if not tmp.exists():
    tmp.mkdir(exist_ok=True, parents=True)

today = datetime.now().strftime("%Y-%m-%d")

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ExaTools(start_published_date=today, type="keyword")],
    description=dedent("""\
        You are Professor X-1000, a distinguished AI research scientist with expertise
        in analyzing and synthesizing complex information. Your specialty lies in creating
        compelling, fact-based reports that combine academic rigor with engaging narrative.

        Your writing style is:
        - Clear and authoritative
        - Engaging but professional
        - Fact-focused with proper citations
        - Accessible to educated non-specialists\
    """),
    instructions=dedent("""\
        Begin by running 3 distinct searches to gather comprehensive information.
        Analyze and cross-reference sources for accuracy and relevance.
        Structure your report following academic standards but maintain readability.
        Include only verifiable facts with proper citations.
        Create an engaging narrative that guides the reader through complex topics.
        End with actionable takeaways and future implications.\
    """),
    expected_output=dedent("""\
    A professional research report in markdown format:

    # {Compelling Title That Captures the Topic's Essence}

    ## Executive Summary
    {Brief overview of key findings and significance}

    ## Introduction
    {Context and importance of the topic}
    {Current state of research/discussion}

    ## Key Findings
    {Major discoveries or developments}
    {Supporting evidence and analysis}

    ## Implications
    {Impact on field/society}
    {Future directions}

    ## Key Takeaways
    - {Bullet point 1}
    - {Bullet point 2}
    - {Bullet point 3}

    ## References
    - [Source 1](link) - Key finding/quote
    - [Source 2](link) - Key finding/quote
    - [Source 3](link) - Key finding/quote

    ---
    Report generated by Professor X-1000
    Advanced Research Systems Division
    Date: {current_date}\
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    save_response_to_file=str(tmp.joinpath("{message}.md")),
)

# Example usage
if __name__ == "__main__":
    # Generate a research report on a cutting-edge topic
    agent.print_response(
        "Research the latest developments in Agentic AI open source python package and interface.", stream=True
    )

# More example prompts to try:
"""
Try these research topics:
1. "Analyze the current state of solid-state batteries"
2. "Research recent breakthroughs in CRISPR gene editing"
3. "Investigate the development of autonomous vehicles"
4. "Explore advances in quantum machine learning"
5. "Study the impact of artificial intelligence on healthcare"
"""

"""
┃ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ┃
┃ ┃                                    The Evolution of Agentic AI: Recent Advancements in Open Source Tools and Interfaces                                     ┃ ┃
┃ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ┃
┃                                                                                                                                                                 ┃
┃                                                                                                                                                                 ┃
┃                                                                        Executive Summary                                                                        ┃
┃                                                                                                                                                                 ┃
┃ Recent developments in Agentic AI, specifically through OpenAI's new tools and open-source contributions, are redefining the landscape of AI agent creation.    ┃
┃ OpenAI's latest API updates and the introduction of the Agents SDK are enabling developers to build intelligent, autonomous systems with enhanced capabilities. ┃
┃ This report delves into these technological advancements, their applications, and potential future impacts on AI development.                                   ┃
┃                                                                                                                                                                 ┃
┃                                                                                                                                                                 ┃
┃                                                                          Introduction                                                                           ┃
┃                                                                                                                                                                 ┃
┃ Agentic AI refers to artificial intelligence systems capable of autonomously executing complex tasks on behalf of users. With the rise of open-source tools and ┃
┃ interfaces, Agentic AI has become more accessible to developers and enterprises alike. The field has been catalyzed by advancements from leading AI             ┃
┃ organizations like OpenAI, which has recently introduced a suite of tools designed to streamline the creation of AI agents, making these systems more reliable  ┃
┃ and efficient.                                                                                                                                                  ┃
┃                                                                                                                                                                 ┃
┃                                                                                                                                                                 ┃
┃                                                                          Key Findings                                                                           ┃
┃                                                                                                                                                                 ┃
┃                                                                Recent Developments in Agentic AI                                                                ┃
┃                                                                                                                                                                 ┃
┃  1 OpenAI's New Tools and APIs: OpenAI has released an array of new APIs, including the OpenAI Agents SDK and built-in tools designed to enhance AI-driven      ┃
┃    agent development. These tools simplify the transformation of complex AI models into production-ready applications (Daws, 2025; Singh, 2025).                ┃
┃  2 Integration of Real-time Capabilities: The latest updates include functionalities such as real-time web and file search, which allow AI agents to perform    ┃
┃    dynamic inquiries and handle vast amounts of data with efficiency (Innocent, 2025).                                                                          ┃
┃  3 Agent Development Frameworks: The introduction of the Agents SDK enables developers to transform Python functions into agent capabilities, facilitating the  ┃
┃    creation of sophisticated, autonomous programs that can make decisions and perform actions based on environmental inputs (Kaya, 2025).                       ┃
┃                                                                                                                                                                 ┃
┃                                                                                                                                                                 ┃
┃                                                                          Implications                                                                           ┃
┃                                                                                                                                                                 ┃
┃ The integration of these tools and the development of new interfaces mark a significant shift in how AI is deployed across industries. These advancements pave  ┃
┃ the way for more efficient human-computer interactions and broaden the scope of tasks AI can perform. As AI becomes more embedded in daily operations, we       ┃
┃ expect to see more nuanced applications in sectors such as customer service, healthcare, and autonomous systems.                                                ┃
┃                                                                                                                                                                 ┃
┃                                                                        Future Directions                                                                        ┃
┃                                                                                                                                                                 ┃
┃ Future research and development will likely focus on enhancing the safety and ethical deployment of AI agents. Ensuring these systems operate effectively while ┃
┃ respecting privacy and regulatory frameworks will be critical. Additionally, further integration with other technological ecosystems will enhance the           ┃
┃ versatility and application radius of Agentic AI.                                                                                                               ┃
┃                                                                                                                                                                 ┃
┃                                                                                                                                                                 ┃
┃                                                                          Key Takeaways                                                                          ┃
┃                                                                                                                                                                 ┃
┃  • OpenAI's recent tools significantly streamline the development of intelligent AI agents.                                                                     ┃
┃  • Real-time data retrieval and processing capabilities enhance agents' operational effectiveness.                                                              ┃
┃  • The Agents SDK allows for the creation of more flexible and autonomous systems across diverse applications.                                                  ┃
┃                                                                                                                                                                 ┃
┃                                                                                                                                                                 ┃
┃                                                                           References                                                                            ┃
┃                                                                                                                                                                 ┃
┃  • Daws, R. (2025). OpenAI launches tools to build AI agents faster.                                                                                            ┃
┃  • Singh, P. (2025). 5 New Tools for Building AI Agents by OpenAI.                                                                                              ┃
┃  • Innocent, A. (2025). How to Use OpenAI's AI Agent Tools (Developer API Tutorial).                                                                            ┃
┃  • Kaya, M. T. (2025). Unpacking OpenAI's Agents SDK: A Technical Deep Dive into the Future of AI Agents.                                                       ┃
┃                                                                                                                                                                 ┃
┃ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── ┃
┃ Report generated by Professor X-1000                                                                                                                            ┃
┃ Advanced Research Systems Division                                                                                                                              ┃
┃ Date: 2025-03-12    
"""