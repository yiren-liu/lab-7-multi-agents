"""
Simplified AutoGen Demo - Interview Platform Product Planning

This is a lightweight version for quick testing and understanding the workflow.
It uses the same four-agent architecture but with simplified prompts.
"""

import os
from datetime import datetime
from config import Config, WorkflowConfig

# Check if autogen is available, provide helpful message if not
try:
    import autogen
except ImportError:
    print("ERROR: pyautogen is not installed!")
    print("Please run: pip install pyautogen")
    exit(1)


class SimpleInterviewPlatformWorkflow:
    """Simplified workflow for interview platform planning"""

    def __init__(self):
        """Initialize the workflow"""
        if not Config.validate_setup():
            print("ERROR: Configuration validation failed!")
            exit(1)

        self.config_list = Config.get_config_list()
        self.outputs = {}

    def run(self):
        """Execute the complete workflow"""
        print("\n" + "="*80)
        print("AUTOGEN INTERVIEW PLATFORM WORKFLOW - SIMPLIFIED DEMO")
        print("="*80)
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Model: {Config.OPENAI_MODEL}\n")

        # Phase 1: Research
        self.phase_research()

        # Phase 2: Analysis
        self.phase_analysis()

        # Phase 3: Blueprint
        self.phase_blueprint()

        # Phase 4: Review
        self.phase_review()

        # Summary
        self.print_summary()

    def phase_research(self):
        """Phase 1: Market Research"""
        print("\n" + "="*80)
        print("PHASE 1: MARKET RESEARCH")
        print("="*80)

        agent = autogen.ConversableAgent(
            name="ResearchAgent",
            system_message="""You are a market research analyst. Provide a brief
            analysis of 3 competitors in AI interview platforms (HireVue, Pymetrics, Codility).
            List their key features and identify market gaps in 200 words.""",
            llm_config={"config_list": self.config_list, "temperature": 0.7},
            human_input_mode="NEVER",
        )

        message = "Analyze the current market for AI-powered interview platforms."
        self.outputs["research"] = agent.generate_reply(messages=[{"content": message, "role": "user"}])

        print("\n[ResearchAgent Output]")
        print(self.outputs["research"][:500] + "..." if len(self.outputs["research"]) > 500 else self.outputs["research"])

    def phase_analysis(self):
        """Phase 2: Opportunity Analysis"""
        print("\n" + "="*80)
        print("PHASE 2: OPPORTUNITY ANALYSIS")
        print("="*80)

        agent = autogen.ConversableAgent(
            name="AnalysisAgent",
            system_message="""You are a product analyst. Based on market research,
            identify 3 key opportunities for an AI interview platform startup.
            For each, explain the gap and why it matters in 150 words.""",
            llm_config={"config_list": self.config_list, "temperature": 0.7},
            human_input_mode="NEVER",
        )

        message = f"""Based on this research, identify 3 market opportunities:
        {self.outputs["research"][:300]}..."""
        self.outputs["analysis"] = agent.generate_reply(messages=[{"content": message, "role": "user"}])

        print("\n[AnalysisAgent Output]")
        print(self.outputs["analysis"][:500] + "..." if len(self.outputs["analysis"]) > 500 else self.outputs["analysis"])

    def phase_blueprint(self):
        """Phase 3: Product Blueprint"""
        print("\n" + "="*80)
        print("PHASE 3: PRODUCT BLUEPRINT")
        print("="*80)

        agent = autogen.ConversableAgent(
            name="BlueprintAgent",
            system_message="""You are a product designer. Create a brief product blueprint
            with 5 core features for an AI interview platform and a simple user journey
            in 200 words.""",
            llm_config={"config_list": self.config_list, "temperature": 0.7},
            human_input_mode="NEVER",
        )

        message = f"""Based on these opportunities, design the product:
        {self.outputs["analysis"][:300]}..."""
        self.outputs["blueprint"] = agent.generate_reply(messages=[{"content": message, "role": "user"}])

        print("\n[BlueprintAgent Output]")
        print(self.outputs["blueprint"][:500] + "..." if len(self.outputs["blueprint"]) > 500 else self.outputs["blueprint"])

    def phase_review(self):
        """Phase 4: Strategic Review"""
        print("\n" + "="*80)
        print("PHASE 4: STRATEGIC REVIEW")
        print("="*80)

        agent = autogen.ConversableAgent(
            name="ReviewerAgent",
            system_message="""You are a product executive. Review the product blueprint
            and provide 3-4 strategic recommendations for success and implementation priorities
            in 200 words.""",
            llm_config={"config_list": self.config_list, "temperature": 0.7},
            human_input_mode="NEVER",
        )

        message = f"""Review this product blueprint and provide recommendations:
        {self.outputs["blueprint"][:300]}..."""
        self.outputs["review"] = agent.generate_reply(messages=[{"content": message, "role": "user"}])

        print("\n[ReviewerAgent Output]")
        print(self.outputs["review"][:500] + "..." if len(self.outputs["review"]) > 500 else self.outputs["review"])

    def print_summary(self):
        """Print workflow summary"""
        print("\n" + "="*80)
        print("WORKFLOW COMPLETED")
        print("="*80)
        print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nPhases Completed:")
        print("✓ Market Research & Competitive Analysis")
        print("✓ Opportunity Identification & Analysis")
        print("✓ Product Blueprint Creation")
        print("✓ Strategic Review & Recommendations")
        print("\nFor detailed outputs, run: python autogen_interview_platform.py")


def main():
    """Main execution"""
    try:
        workflow = SimpleInterviewPlatformWorkflow()
        workflow.run()
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Ensure OPENAI_API_KEY is set: export OPENAI_API_KEY='your-key'")
        print("2. Install dependencies: pip install -r requirements.txt")
        print("3. Check your API key is valid and has sufficient quota")


if __name__ == "__main__":
    main()
