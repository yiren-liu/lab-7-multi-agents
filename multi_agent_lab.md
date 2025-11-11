# Multi-Agent System Lab: AutoGen vs. CrewAI

## Lab Overview
This lab demonstrates how AutoGen and CrewAI frameworks orchestrate multi-agent workflows. You'll implement two scenarios and compare their approaches to agent collaboration.

---

## Part 1: AutoGen Multi-Agent Demo

### Scenario
**Goal:** Create a one-page product plan for an AI-powered interview platform using four collaborative agents.

### Agent Definitions

**ResearchAgent**
- Role: Market Researcher
- Task: Find and summarize current market competitors and trends in AI-powered interview platforms
- Output: Competitive landscape summary

**AnalysisAgent**
- Role: Product Analyst
- Task: Analyze research findings and extract 3 key product opportunities or market gaps
- Output: Structured analysis with opportunities

**BlueprintAgent**
- Role: Product Designer
- Task: Create a feature list and user flow based on identified opportunities
- Output: Product blueprint with features and user journey

**ReviewerAgent**
- Role: Product Reviewer
- Task: Review the blueprint and suggest improvements or next steps
- Output: Final recommendations and enhancement suggestions

### Implementation Instructions

```python
# TODO: Implement AutoGen agents for the following workflow:

# 1. Initialize AutoGen configuration
# 2. Create four agents with the roles defined above
# 3. Define the conversation flow:
#    ResearchAgent → AnalysisAgent → BlueprintAgent → ReviewerAgent
# 4. Start with user prompt: "Build an AI-powered interview platform for startups."
# 5. Execute the workflow and capture outputs
```

### Expected Output Structure
- **Competitive Summary** (from ResearchAgent)
- **Market Gap Analysis** (from AnalysisAgent) - 3 opportunities
- **Product Blueprint** (from BlueprintAgent) - Features & user flow
- **Review & Recommendations** (from ReviewerAgent)

---

## Part 2: CrewAI Multi-Agent Demo

### Scenario
**Goal:** Form a "crew" of travel agents to collaboratively plan a 5-day trip to Iceland.

### Agent Definitions

**FlightAgent**
- Role: Flight Specialist
- Task: Research and recommend best flight options for the trip dates
- Output: List of flight options with prices and timings

**HotelAgent**
- Role: Accommodation Specialist
- Task: Suggest top-rated hotels in Reykjavik for the trip duration
- Output: Hotel recommendations with amenities and pricing

**ItineraryAgent**
- Role: Travel Planner
- Task: Create a detailed day-by-day travel plan with activities
- Output: 5-day itinerary with attractions and tours

**BudgetAgent**
- Role: Financial Advisor
- Task: Calculate total trip costs and identify cost-saving opportunities
- Output: Comprehensive budget breakdown with savings tips

### Implementation Instructions

```python
# TODO: Implement CrewAI crew for the following workflow:

# 1. Install and import CrewAI
# 2. Define four agents with roles, goals, and backstories
# 3. Create tasks for each agent
# 4. Form a crew with sequential task execution:
#    FlightAgent → HotelAgent → ItineraryAgent → BudgetAgent
# 5. Start with user input: "Plan a 5-day trip to Iceland."
# 6. Execute the crew and capture outputs
```

### Expected Output Structure
- **Flight Options** (from FlightAgent) - 2-3 options
- **Hotel Recommendations** (from HotelAgent) - 3-4 hotels
- **Daily Itinerary** (from ItineraryAgent) - Day-by-day plan
- **Budget Report** (from BudgetAgent) - Total costs and savings tips

---

## Execution Steps

### Setup
1. **Install required packages:**
   ```bash
   pip install pyautogen crewai crewai-tools
   ```

2. **Set up API keys** (if needed for web search/tools):
   ```bash
   export OPENAI_API_KEY="your-key-here"
   # or configure in your code
   ```

### Running Part 1 (AutoGen)
```bash
# Create and run autogen_demo.py
python autogen_demo.py
```

### Running Part 2 (CrewAI)
```bash
# Create and run crewai_demo.py
python crewai_demo.py
```

---

## Comparison Framework

After completing both parts, analyze the following dimensions:

### 1. **Agent Communication**
- How do agents pass information in each framework?
- Is it conversational (AutoGen) or task-based (CrewAI)?

### 2. **Workflow Control**
- How is the execution sequence defined?
- Can agents work in parallel or only sequentially?

### 3. **Output Aggregation**
- How are individual agent outputs combined?
- Is there a final synthesis step?

### 4. **Ease of Implementation**
- Which framework required less boilerplate code?
- Which was more intuitive to set up?

### 5. **Flexibility**
- How easy is it to add/remove agents?
- Can you modify the workflow dynamically?

### 6. **Use Case Fit**
- Which framework suits conversational, iterative tasks better?
- Which excels at structured, sequential workflows?

---

## Discussion Questions

1. **Agent Autonomy:** Which framework gives agents more autonomy in decision-making?

2. **Human-in-the-Loop:** How easy is it to add human feedback between agent steps?

3. **Debugging:** Which framework provides better visibility into agent reasoning?

4. **Scalability:** How would each framework handle 10+ agents?

5. **Real-World Application:** For your project needs, which framework would you choose and why?

---

## Deliverables

### For Each Implementation:
1. ✅ Complete working code (autogen_demo.py and crewai_demo.py)
2. ✅ Execution output logs
3. ✅ Screenshot or text capture of final results

### Final Report:
- 2-3 page comparison document covering:
  - Implementation experience
  - Output quality comparison
  - Framework strengths and weaknesses
  - Recommendation for specific use cases

---

## Bonus Challenges

1. **Hybrid Approach:** Can you combine AutoGen's conversation style with CrewAI's task structure?

2. **Tool Integration:** Add web search tools to ResearchAgent (AutoGen) and FlightAgent (CrewAI)

3. **Error Handling:** Implement retry logic when an agent fails to produce output

4. **Parallel Execution:** Modify CrewAI workflow so FlightAgent and HotelAgent run simultaneously

---

## Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [Multi-Agent Systems Primer](https://lilianweng.github.io/posts/2023-06-23-agent/)

---

## Notes for Claude Code Execution

When you run this lab:
1. Start with Part 1 (AutoGen) - implement each agent sequentially
2. Test and verify outputs before moving to Part 2
3. For Part 2 (CrewAI) - follow the same pattern
4. Save outputs from both runs for comparison
5. Use the comparison framework to analyze differences

**Expected Time:** 45-60 minutes for full implementation and comparison

---

## Quick Start Command for Claude Code

Simply paste this entire file into Claude Code and say:

```
"Please implement both Part 1 (AutoGen) and Part 2 (CrewAI) multi-agent demos 
as described in this lab manual. Execute both workflows and provide a comparison 
of the two frameworks."
```

Or for step-by-step execution:

```
"Let's start with Part 1. Please implement the AutoGen multi-agent workflow 
for building an AI-powered interview platform product plan."
```
