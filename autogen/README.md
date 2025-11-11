# AutoGen Multi-Agent Workflow: AI-Powered Interview Platform

This directory contains a comprehensive AutoGen implementation for building a product plan for an AI-powered interview platform using a four-agent collaborative workflow.

## Overview

This workflow demonstrates how to use Microsoft's AutoGen framework to orchestrate multiple AI agents working together sequentially to solve a complex product planning problem.

### Workflow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│           ResearchAgent (Market Analysis)                    │
│  - Analyze competitors (HireVue, Pymetrics, Codility, etc)   │
│  - Identify trends in AI recruiting                          │
│  - Document market gaps                                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│        AnalysisAgent (Opportunity Identification)            │
│  - Extract 3 key market opportunities                        │
│  - Analyze competitive advantages                            │
│  - Assess market viability                                   │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         BlueprintAgent (Product Design)                      │
│  - Define core features (MVP)                                │
│  - Create user journey maps                                  │
│  - Identify user personas                                    │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│      ReviewerAgent (Strategic Review)                        │
│  - Assess feasibility                                        │
│  - Suggest business model                                    │
│  - Provide implementation roadmap                            │
│  - Define next steps and priorities                          │
└─────────────────────────────────────────────────────────────┘
```

## Agents

### 1. ResearchAgent (Market Researcher)
- **Role**: Market Researcher
- **Task**: Find and summarize current market competitors and trends
- **Output**: Competitive landscape summary with market gaps
- **Key Focus**:
  - Competitor analysis (HireVue, Pymetrics, Codility, Greenhouse, etc.)
  - Market trends in AI recruiting
  - Unmet needs and opportunities

### 2. AnalysisAgent (Product Analyst)
- **Role**: Product Analyst
- **Task**: Analyze research findings and extract key opportunities
- **Output**: Structured analysis with 3+ market opportunities
- **Key Focus**:
  - Market gap identification
  - Opportunity assessment
  - Competitive positioning

### 3. BlueprintAgent (Product Designer)
- **Role**: Product Designer
- **Task**: Create feature list and user flow based on opportunities
- **Output**: Product blueprint with features and user journey
- **Key Focus**:
  - MVP feature definition (5-7 core features)
  - User journey mapping
  - Persona definition
  - Competitive differentiation

### 4. ReviewerAgent (Product Reviewer)
- **Role**: Product Reviewer
- **Task**: Review blueprint and suggest improvements
- **Output**: Final recommendations and enhancement suggestions
- **Key Focus**:
  - Feasibility assessment
  - Business model recommendations
  - Implementation roadmap
  - Top 5 priority actions

## Setup & Installation

### Prerequisites
- Python 3.9+
- OpenAI API Key (for GPT-4 access)
- pip package manager

### Quick Start

1. **Clone/Navigate to the autogen folder**
   ```bash
   cd /path/to/autogen
   ```

2. **Run the setup script** (optional, but recommended)
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Or manual setup**:
   ```bash
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
   ```

4. **Set up API Key**
   ```bash
   export OPENAI_API_KEY='sk-your-actual-api-key-here'
   ```

   Or copy `.env.example` to `.env` and update with your key:
   ```bash
   cp .env.example .env
   # Edit .env with your API key
   ```

### Running the Workflow

```bash
# Activate virtual environment (if using)
source venv/bin/activate

# Set API key
export OPENAI_API_KEY='your-key-here'

# Run the workflow
python autogen_interview_platform.py
```

## Expected Output

The workflow generates comprehensive outputs across four phases:

### Phase 1: Market Research & Competitive Analysis
```
- Analysis of 3-4 major competitors
- Key features and positioning of each
- Current trends in AI recruiting
- Market gaps identified
```

### Phase 2: Market Gap Analysis & Opportunities
```
- 3 clearly defined market opportunities
- Why each opportunity matters
- How to address each gap
- Potential market impact
```

### Phase 3: Product Blueprint
```
- 5-7 core features for MVP
- Feature descriptions and benefits
- User journey maps
- Target personas
- Competitive differentiation
```

### Phase 4: Product Review & Recommendations
```
- Feasibility assessment
- Business model suggestions
- Implementation roadmap (phases)
- Resource requirements
- Top 5 priority actions
```

## Output Files

The workflow automatically creates two output files in the autogen folder:

1. **workflow_outputs_YYYYMMDD_HHMMSS.txt**
   - Complete detailed outputs from all four agents
   - Full agent responses and analysis
   - Can be imported into product management tools

2. **summary_YYYYMMDD_HHMMSS.txt**
   - Executive summary
   - Key deliverables checklist
   - Quick reference guide

## Key Features

### Agent Communication
- Sequential conversation flow: ResearchAgent → AnalysisAgent → BlueprintAgent → ReviewerAgent
- Context passing between agents using previous outputs
- Each agent receives full previous outputs for informed decision-making

### Configuration
- LLM configuration with GPT-4 (customizable to other models)
- Temperature setting: 0.7 (balanced between creativity and consistency)
- Human-input mode: NEVER (fully autonomous agents)

### Extensibility
- Easy to modify agent roles and system messages
- Add new phases by creating new agents
- Support for tool integration (web search, databases, etc.)
- Configurable output formats

## Customization

### Modify Agent Behavior

Edit the system messages in `autogen_interview_platform.py`:

```python
def create_research_agent(self):
    system_message = """Your custom system message here..."""
    # ... rest of agent creation
```

### Add New Phases

1. Create a new agent method:
   ```python
   def create_custom_agent(self):
       system_message = """..."""
       agent = autogen.ConversableAgent(
           name="CustomAgent",
           system_message=system_message,
           llm_config={"config_list": self.config_list},
           human_input_mode="NEVER",
       )
       self.agents["custom"] = agent
       return agent
   ```

2. Add a workflow phase method:
   ```python
   def conduct_custom_phase(self, previous_output):
       # Create message with context
       # Get output from agent
       # Return output
   ```

3. Call in `execute_workflow()` method.

### Use Different LLM Models

Modify the `model` variable in `AutoGenConfig.__init__()`:

```python
self.model = "gpt-3.5-turbo"  # or "claude-3-opus" etc.
```

## Troubleshooting

### API Key Issues
```
Error: Invalid API key
Solution: Ensure OPENAI_API_KEY environment variable is set correctly
```

### Module Not Found
```
Error: ModuleNotFoundError: No module named 'autogen'
Solution: pip install pyautogen
```

### Rate Limiting
```
Error: Rate limit exceeded
Solution: Add delays between calls or use different API tier
```

## Project Structure

```
autogen/
├── autogen_interview_platform.py  # Main workflow implementation
├── requirements.txt               # Python dependencies
├── setup.sh                       # Setup script
├── .env.example                   # Environment variable template
├── README.md                      # This file
├── workflow_outputs_*.txt         # Generated outputs (created on run)
└── summary_*.txt                  # Generated summaries (created on run)
```

## Performance Notes

- **Execution Time**: Approximately 3-5 minutes for full workflow
- **API Calls**: ~4 calls to OpenAI API (one per agent)
- **Tokens**: ~2000-3000 tokens used across all calls
- **Estimated Cost**: ~$0.10-0.20 per run (GPT-4)

## Advanced Usage

### Batch Execution
Create multiple runs with different parameters:

```bash
for i in {1..5}; do
  python autogen_interview_platform.py
  sleep 60  # Wait between runs
done
```

### Integration with Other Systems
Outputs are plain text files that can be:
- Imported into Notion/Confluence
- Converted to JSON using post-processing
- Piped into other analysis tools
- Used as input for subsequent agent runs

## References

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [Agent Design Patterns](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat/)
- [Multi-Agent Systems Primer](https://lilianweng.github.io/posts/2023-06-23-agent/)

## License

This project is part of the IS-492 Multi-Agent Systems Lab at [Your Institution].

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review AutoGen documentation
3. Check API key configuration
4. Ensure all dependencies are installed

---

**Last Updated**: 2025-11-11
**Framework**: Microsoft AutoGen
**Model**: GPT-4 Turbo Preview
