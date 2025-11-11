# AutoGen Workflow - Execution Guide

## Quick Start (5 minutes)

### Step 1: Set API Key
```bash
export OPENAI_API_KEY='sk-your-actual-api-key-here'
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Workflow
```bash
# Quick demo (simplified, ~2 minutes)
python autogen_simple_demo.py

# Full workflow (comprehensive, ~3-5 minutes)
python autogen_interview_platform.py
```

---

## Detailed Execution Steps

### Prerequisites Check
Before running, ensure:
- [ ] Python 3.9+ installed (`python3 --version`)
- [ ] pip installed (`pip --version`)
- [ ] OpenAI API key available
- [ ] Internet connection (for API calls)

### Installation

1. **Navigate to autogen folder**
   ```bash
   cd /Users/pranavhharish/Desktop/IS-492/multi-agent/autogen
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

   Expected output:
   ```
   Successfully installed pyautogen-0.2.x openai-1.x.x python-dotenv-1.0.x
   ```

### Configuration

4. **Set API Key** (choose one method):

   **Method A: Environment Variable (recommended)**
   ```bash
   export OPENAI_API_KEY='sk-proj-xxxxxxxxxxxxx'
   ```

   **Method B: Using .env file**
   ```bash
   cp .env.example .env
   # Edit .env with your API key
   nano .env
   # Add: OPENAI_API_KEY=sk-your-key-here
   ```

   **Verify API Key**:
   ```bash
   echo $OPENAI_API_KEY
   # Should show your API key (starts with sk-)
   ```

### Execution

5. **Run the Simplified Demo** (for testing)
   ```bash
   python autogen_simple_demo.py
   ```

   Expected output:
   ```
   ================================================================================
   AUTOGEN INTERVIEW PLATFORM WORKFLOW - SIMPLIFIED DEMO
   ================================================================================
   Start Time: 2025-11-11 14:30:45
   Model: gpt-4-turbo-preview

   ================================================================================
   PHASE 1: MARKET RESEARCH
   ================================================================================

   [ResearchAgent Output]
   Analysis of competitors: HireVue, Pymetrics, Codility...
   ```

6. **Run Full Workflow** (for complete analysis)
   ```bash
   python autogen_interview_platform.py
   ```

   Expected output:
   ```
   ================================================================================
   AI-POWERED INTERVIEW PLATFORM - PRODUCT PLANNING WORKFLOW
   ================================================================================
   Start Time: 2025-11-11 14:30:45
   Initializing agents...
   ✓ ResearchAgent created
   ✓ AnalysisAgent created
   ✓ BlueprintAgent created
   ✓ ReviewerAgent created

   Initiating workflow...

   ================================================================================
   PHASE 1: MARKET RESEARCH
   ================================================================================
   ...
   ================================================================================
   WORKFLOW COMPLETED SUCCESSFULLY
   ================================================================================
   Full outputs saved to: /Users/pranavhharish/Desktop/IS-492/multi-agent/autogen/workflow_outputs_20251111_143045.txt
   Summary saved to: /Users/pranavhharish/Desktop/IS-492/multi-agent/autogen/summary_20251111_143045.txt
   End Time: 2025-11-11 14:30:58
   ```

---

## Understanding the Workflow

### Phase Flow

```
START
  ↓
[Phase 1: Research] ──→ Competitive analysis, market trends, gaps
  ↓
[Phase 2: Analysis] ──→ Identify 3 key opportunities
  ↓
[Phase 3: Blueprint] ──→ Product features, user journey
  ↓
[Phase 4: Review] ──→ Strategic recommendations, next steps
  ↓
END → Outputs saved to files
```

### Agent Roles

| Agent | Role | Input | Output |
|-------|------|-------|--------|
| **Research** | Market Researcher | Initial prompt | Competitive landscape |
| **Analysis** | Product Analyst | Research output | 3 market opportunities |
| **Blueprint** | Product Designer | Analysis output | Product blueprint |
| **Review** | Product Reviewer | Blueprint output | Recommendations |

### Key Outputs

The workflow generates several outputs:

1. **Competitive Summary**
   - 3-4 major competitors analyzed
   - Their features and positioning
   - Market gaps identified

2. **Market Gap Analysis**
   - 3 key opportunities identified
   - Why each matters
   - How to address them

3. **Product Blueprint**
   - 5-7 core features
   - User journey mapping
   - Target personas
   - Competitive differentiation

4. **Strategic Recommendations**
   - Feasibility assessment
   - Business model suggestions
   - Implementation roadmap
   - Top 5 priorities

---

## Output Files

After execution, find these files in the autogen folder:

### 1. workflow_outputs_YYYYMMDD_HHMMSS.txt
**Contains**: Full detailed outputs from all four agents
**Size**: ~2000-4000 words
**Use**: Detailed analysis, product planning document
**Example filename**: `workflow_outputs_20251111_143045.txt`

### 2. summary_YYYYMMDD_HHMMSS.txt
**Contains**: Executive summary with key deliverables
**Size**: ~500 words
**Use**: Quick reference, presentation prep
**Example filename**: `summary_20251111_143045.txt`

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'autogen'"
```
Solution: pip install pyautogen
Check: pip list | grep autogen
```

### Issue: "Error: Invalid API key"
```
Solution 1: Check API key is set: echo $OPENAI_API_KEY
Solution 2: Verify key starts with "sk-" (not "sk-test")
Solution 3: Generate new key at: https://platform.openai.com/account/api-keys
```

### Issue: "Error: Model 'gpt-4-turbo-preview' not found"
```
Solution 1: Use valid model: gpt-4, gpt-4-turbo, gpt-3.5-turbo
Solution 2: Check API key has access to GPT-4
Solution 3: Edit config.py, change model to "gpt-3.5-turbo"
```

### Issue: "Rate limit exceeded"
```
Solution 1: Wait 60 seconds before retrying
Solution 2: Use gpt-3.5-turbo (cheaper, faster)
Solution 3: Check API usage: https://platform.openai.com/account/usage
```

### Issue: "Workflow runs but outputs are empty"
```
Solution 1: Check API key is valid
Solution 2: Check API quota and usage
Solution 3: Try simple demo first: python autogen_simple_demo.py
```

---

## Performance Metrics

### Typical Execution Times
- **Simple Demo**: 60-90 seconds
- **Full Workflow**: 180-300 seconds (3-5 minutes)

### API Usage
- **API Calls**: 4 (one per agent)
- **Tokens per run**: 2000-3000
- **Estimated cost**: $0.10-0.20 per full workflow

### Output Quality Factors
- **Model**: GPT-4 > GPT-4-Turbo > GPT-3.5-Turbo (quality-wise)
- **Temperature**: 0.7 (balanced)
- **Context**: Previous agent outputs included for better results

---

## Advanced Usage

### Run with Custom Model
```bash
# Edit config.py
OPENAI_MODEL = "gpt-3.5-turbo"

# Or set environment variable
export OPENAI_MODEL="gpt-3.5-turbo"
```

### Run Multiple Times for Comparison
```bash
for i in {1..3}; do
  echo "Run #$i"
  python autogen_simple_demo.py
  sleep 30  # Wait between runs
done
```

### Extract Specific Output
```bash
# Get just research phase
grep -A 50 "PHASE 1" workflow_outputs_*.txt

# Get just recommendations
grep -A 20 "PHASE 4" workflow_outputs_*.txt
```

### Convert Output to JSON
```python
# Use parse_outputs.py (optional utility)
python parse_outputs.py workflow_outputs_*.txt > output.json
```

---

## Next Steps

After running the workflow:

1. **Review Outputs**
   - Read the full workflow_outputs file
   - Review the summary document

2. **Extract Key Insights**
   - 3 identified opportunities
   - 5-7 product features
   - Strategic recommendations

3. **Use for Planning**
   - Import into product management tool
   - Create user stories from features
   - Plan development roadmap

4. **Iterate**
   - Modify prompts in code for different focus areas
   - Run multiple times for different product angles
   - Compare outputs from different model versions

5. **Document Findings**
   - Create product requirements document (PRD)
   - Build feature specifications
   - Develop go-to-market strategy

---

## Testing Checklist

- [ ] Python 3.9+ installed
- [ ] pip dependencies installed
- [ ] OPENAI_API_KEY set and valid
- [ ] Simple demo runs successfully
- [ ] Full workflow completes
- [ ] Output files created
- [ ] Can read workflow outputs
- [ ] Outputs contain all 4 phases

---

## Support Resources

- **AutoGen Docs**: https://microsoft.github.io/autogen/
- **OpenAI API**: https://platform.openai.com/docs/
- **Multi-Agent Systems**: https://lilianweng.github.io/posts/2023-06-23-agent/

---

**Need Help?** Check README.md for detailed configuration and customization options.
