"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "This function call will return a list of venues in Edinburgh that can accommodate at least 300 people and have vegan options. The response will include the names of the venues that match these criteria."
# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
After changing The Albanach’s status from 'available' to 'full', the search_venues tool returned only one match instead of two. Specifically, The Albanach was removed from the results and only The Haymarket Vaults remained. No changes were required in exercise4_mcp_client.py or the agent code, demonstrating that the agent automatically picked up updated data from the MCP server. This confirms that all business logic and data live in mcp_venue_server.py, and modifying that single file propagates to all connected clients without requiring any downstream code changes.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 10   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP decouples tool implementation from agent logic, enabling dynamic tool discovery and centralized control over data and business rules. Unlike hardcoded tools, where every change requires modifying the agent code, MCP allows updates to propagate automatically by modifying only the server. This also enables multiple clients, such as LangGraph agents and Rasa actions, to share the same tool layer consistently. As observed in the experiment, changing venue availability required no changes to the client code, demonstrating improved maintainability, scalability, and separation of concerns.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- A LangGraph research agent is responsible for reasoning over user queries and deciding which tools to call, ensuring flexible and interpretable decision-making.
- An MCP server hosts all business logic and data access functions, acting as a single source of truth so that updates propagate across all clients without duplication.
- A Rasa conversational agent handles real-time user interactions, managing dialogue state and delegating complex queries to the research agent when needed.
- A tool abstraction layer using StructuredTool ensures that all tools have well-defined schemas, preventing argument mismatches and enabling reliable execution.
- A shared data layer or database backs the MCP server, allowing persistent storage and scalable retrieval of venue or domain-specific information.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The LangGraph agent is better suited for research tasks because it can iteratively call tools, combine results, and produce structured answers, as seen in Query 1 where it first called search_venues and then get_venue_details before producing a final answer. In contrast, a Rasa agent is better suited for handling user interactions and dialogue flow, especially in real-time settings. Swapping them feels wrong because the Rasa agent lacks the reasoning loop needed for multi-step tool use, while the LangGraph agent does not manage conversational context as effectively. This separation became clear during the run, where the research agent handled tool orchestration while relying entirely on the MCP server for data.
"""
