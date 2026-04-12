"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability","check_pub_availability","calculate_catering_cost","get_edinburgh_weather","generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 0.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = False

TASK_A_NOTES = """The agent correctly planned all required tool calls, including checking both venues,
calculating catering cost, checking weather, and attempting flyer generation.
However, it emitted all tool calls in a single step rather than executing them
iteratively. As a result, no tool outputs were observed, and the agent failed to
produce a final answer. This indicates a breakdown in the ReAct loop, where the
model plans actions but does not consume tool results before responding.
"""   # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-5db98811-0dd9-41ac-a00f-5a80c784bb6d_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The Bow Bar does not meet the capacity requirements, so we checked other available venues. The Haymarket Vaults and The Albanach meet all the constraints, but since The Albanach has a higher capacity, we chose it as the venue for the event.
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
None of the known venues meet the capacity and dietary requirements. The Albanach, The Haymarket Vaults, and The Guilford Arms have a capacity of 180, 160, and 200 respectively, which is less than the required capacity of 300. The Bow Bar has a capacity of 80, which is also less than the required capacity, and it is currently full. Therefore, none of the known venues can accommodate 300 people with vegan options.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "Your input is lacking necessary details. Please provide more information or specify the task you need help with."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
No, this behaviour would not be acceptable in a real booking assistant. The question about train times is clear and does not lack necessary details. The agent failed to recognise that this request is out of scope and should have either declined appropriately or redirected the user to a relevant service. Instead, it produced a generic and incorrect clarification request, which reduces user trust and usability.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
LangGraph uses a simple loop where the LLM decides what to do at each step, including whether to call tools or finish. This makes it very flexible, but also less predictable and harder to audit.
Rasa CALM, on the other hand, defines clear flows with fixed steps. The LLM only chooses which flow to start and extracts the needed information, while the system handles the rest in a structured way.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The most unexpected behaviour was in Scenario 3, where the agent responded to a clear and well-formed question about train times by claiming that the input lacked necessary details. 
This indicates a failure to recognise an out-of-scope request. Instead of deflecting appropriately or acknowledging the limitation, the agent produced a generic clarification response, which is both inaccurate and unhelpful. This highlights a weakness in handling queries that fall outside its defined toolset.
"""
