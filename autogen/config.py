"""
Configuration module for AutoGen Interview Platform Workflow

This module manages all configuration settings including API keys,
model selection, and agent parameters.
"""

import os
from typing import List, Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class"""

    # OpenAI API Settings
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-test-key")
    OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4-turbo-preview")

    # Agent Parameters
    AGENT_TEMPERATURE = 0.7  # Balance between creativity and consistency
    AGENT_MAX_TOKENS = 2000  # Maximum tokens per response
    HUMAN_INPUT_MODE = "NEVER"  # Agents operate autonomously

    # Workflow Settings
    TIMEOUT_SECONDS = 300  # Timeout for API calls
    MAX_RETRIES = 2  # Retry failed API calls
    VERBOSE_MODE = True  # Print detailed logging

    # Output Settings
    OUTPUT_DIR = "/Users/pranavhharish/Desktop/IS-492/multi-agent/autogen"
    SAVE_OUTPUTS = True
    CREATE_SUMMARY = True

    @classmethod
    def get_config_list(cls) -> List[Dict[str, Any]]:
        """Get LLM configuration list for AutoGen"""
        return [
            {
                "model": cls.OPENAI_MODEL,
                "api_key": cls.OPENAI_API_KEY,
                "api_base": cls.OPENAI_API_BASE,
                "api_type": "openai",
                "request_timeout": cls.TIMEOUT_SECONDS,
                "temperature": cls.AGENT_TEMPERATURE,
                "max_tokens": cls.AGENT_MAX_TOKENS,
            }
        ]

    @classmethod
    def validate_setup(cls) -> bool:
        """Validate that all required configurations are set"""
        if cls.OPENAI_API_KEY == "sk-test-key":
            print("WARNING: OPENAI_API_KEY is not configured properly!")
            print("Please set the OPENAI_API_KEY environment variable.")
            return False

        if cls.VERBOSE_MODE:
            print(f"Configuration loaded: {cls.OPENAI_MODEL}")

        return True

    @classmethod
    def get_summary(cls) -> str:
        """Get a summary of current configuration"""
        return f"""
Configuration Summary:
- Model: {cls.OPENAI_MODEL}
- Temperature: {cls.AGENT_TEMPERATURE}
- Output Directory: {cls.OUTPUT_DIR}
- Verbose Mode: {cls.VERBOSE_MODE}
- API Base: {cls.OPENAI_API_BASE}
"""


class AgentConfig:
    """Configuration for individual agents"""

    RESEARCH_AGENT = {
        "name": "ResearchAgent",
        "role": "Market Researcher",
        "temperature": 0.7,
    }

    ANALYSIS_AGENT = {
        "name": "AnalysisAgent",
        "role": "Product Analyst",
        "temperature": 0.7,
    }

    BLUEPRINT_AGENT = {
        "name": "BlueprintAgent",
        "role": "Product Designer",
        "temperature": 0.7,
    }

    REVIEWER_AGENT = {
        "name": "ReviewerAgent",
        "role": "Product Reviewer",
        "temperature": 0.7,
    }

    @classmethod
    def get_agent_config(cls, agent_type: str) -> Dict[str, Any]:
        """Get configuration for a specific agent type"""
        agents = {
            "research": cls.RESEARCH_AGENT,
            "analysis": cls.ANALYSIS_AGENT,
            "blueprint": cls.BLUEPRINT_AGENT,
            "reviewer": cls.REVIEWER_AGENT,
        }
        return agents.get(agent_type, {})


class WorkflowConfig:
    """Configuration for workflow parameters"""

    # Workflow phases
    PHASES = [
        "research",
        "analysis",
        "blueprint",
        "review",
    ]

    # Phase descriptions
    PHASE_DESCRIPTIONS = {
        "research": "Market Research & Competitive Analysis",
        "analysis": "Market Gap Analysis & Opportunities",
        "blueprint": "Product Blueprint Creation",
        "review": "Strategic Review & Recommendations",
    }

    # Task descriptions
    TASK_DESCRIPTIONS = {
        "research": "Conduct market analysis for AI-powered interview platforms",
        "analysis": "Identify 3 key market opportunities and gaps",
        "blueprint": "Create product blueprint with features and user flows",
        "review": "Review blueprint and provide strategic recommendations",
    }

    @classmethod
    def get_phase_description(cls, phase: str) -> str:
        """Get description for a specific phase"""
        return cls.PHASE_DESCRIPTIONS.get(phase, "Unknown Phase")

    @classmethod
    def get_task_description(cls, phase: str) -> str:
        """Get task description for a specific phase"""
        return cls.TASK_DESCRIPTIONS.get(phase, "Unknown Task")
