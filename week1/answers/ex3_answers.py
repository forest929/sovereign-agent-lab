"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.                                  
Is there anything else I can help you with?
""" # note that there were several timeout errors during this conversation, should the default timeout be changed to larger than 30?

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?  
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "a deposit of £500 exceeds the organiser's authorised limit of £300."   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?                                   
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.                                                              
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
After the user asked about parking, which is outside the booking scope, CALM immediately responded that it could not handle the request. 
It clarified that its functionality is limited to confirming tonight’s venue booking and directed the user to contact the event organiser for other requests. 
It then prompted the user to continue with the booking process, maintaining the conversation flow and staying on-topic.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Rasa CALM immediately recognised the parking request as out-of-scope, clearly informed the user of its limitations, and guided them back to the booking task. 
In contrast, LangGraph in Exercise 2 Scenario 3 did not properly detect the out-of-scope nature of the train times question, instead returning a generic request for more information, which could confuse users and fail to maintain the intended conversation flow. 
CALM’s approach is more structured and user-friendly, maintaining context and focus.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I tested the cutoff guard by running a conversation after 16:45 with all required slots filled: guest count, vegan count, and deposit amount. 
Once the deposit was confirmed, the action triggered the escalation message about insufficient time before 5 PM. 

"I need to check one thing with the organiser before I can confirm. The issue is: it is past 16:45 — insufficient time to process the confirmation before the 5 PM deadline. Can I call you back within 15 minutes?                                                                                                                                      
Is there anything else I can help you with?"

This confirmed the guard correctly interrupts normal booking confirmation.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
In Rasa Pro CALM, the LLM handles slot extraction from natural language directly, replacing the need for regex and multiple FormValidationAction methods. 
Python still enforces deterministic business rules, like maximum guests, deposit limits, vegan ratio, and cutoff time, which cannot rely on probabilistic LLM reasoning. 
The simplification reduces the number of classes and NLU intents needed, but you lose some transparency in slot parsing compared to explicit Python validation in the old approach.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
Rasa CALM still requires domain.yml, flows.yml, config.yml, endpoints.yml, training, and running both the Rasa and action servers. 
Unlike LangGraph, it cannot improvise responses or call tools outside defined flows. 
The setup ensures controlled, legally binding business rules are enforced by Python, which is critical for booking confirmations, even if it reduces flexibility.
"""
