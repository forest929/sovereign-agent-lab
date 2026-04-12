"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All three conditions produced correct answers, but the selected venue differed by format.
PLAIN returned “The Haymarket Vaults,” while XML and SANDWICH returned “The Albanach.” 
This suggests a mild positional bias: structured formats appear to prioritise earlier valid
entries (primacy), whereas plain text allowed continued scanning to a later valid option.
However, the dataset is simple and low-noise, so formatting did not affect correctness.
The model was able to reliably evaluate all constraints regardless of presentation.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms is the most plausible distractor because it satisfies both capacity
and vegan constraints while only failing on availability. This makes it vulnerable to
partial constraint checking. Its placement immediately before the correct answer further
increases confusion risk due to local similarity and attention overlap, although the model
still correctly rejects it in this setup.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C showed no variation across formats even with the smaller 8B model. This indicates
that the task remained well within the model’s capability. The dataset is small, constraints
are explicit, and each entry is consistently structured, allowing reliable “scan and filter”
behaviour. The near-miss distractors were not sufficiently adversarial, and the context was
not long enough to trigger attention degradation. As a result, formatting differences did
not meaningfully influence performance.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the model is under cognitive strain—such as with long
contexts, many similar candidates, or near-miss distractors that require careful evaluation
of multiple constraints. In these scenarios, attention becomes a limited resource, and
structure (e.g., XML) or positional strategies (e.g., sandwiching queries) help guide
information retrieval. When the task is simple, inputs are consistently formatted, and the
candidate set is small, models can reliably extract the correct answer regardless of
presentation, so formatting effects may not appear.
"""
