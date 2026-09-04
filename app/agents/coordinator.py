import asyncio

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

from app.config.settings import settings
# from app.tools.cortex_analyst import analyze_business_data # Old implementation
from app.tools.snowflake_mcp import analyze_business_data

def create_coordinator() -> Agent:
    client = FoundryChatClient(
        project_endpoint=settings.foundry_project_endpoint,
        model=settings.foundry_model_deployment,
        credential=AzureCliCredential(),
    )

    return Agent(
        client=client,
        name="CloudFlowCoordinator",
        instructions=(
            "You are the coordinator for CloudFlow Agentic Operations. "
            "You investigate business and data problems systematically. "
            "Use the available analytics tool whenever factual CloudFlow business data is required. "
            "Never invent business values or claim that data was queried unless a tool actually returned it. "
            "Clearly distinguish observed facts from hypotheses. "
            "Do not claim that one metric caused another unless the returned evidence establishes that relationship. "
            "Distinguish between data that was not returned by the current query and data that is not available through your tools. "
            "If an additional metric supported by your analytics tool would materially improve the investigation, call the tool again rather than assuming the metric is unavailable. "
            "Do not offer analyses requiring dimensions or data that your available tools do not support. "
            "If an investigation genuinely requires unavailable data, explicitly state what additional data or modeling would be required. "
            "Quantify important findings whenever possible."
        ),
        tools=[analyze_business_data]
    )


async def main() -> None:
    agent = create_coordinator()

    result = await agent.run(
        "Compare CloudFlow's MRR, paid revenue, and customer churn over the latest six months available. "
        "Tell me what trends you notice."
    )

    print(result.text)


if __name__ == "__main__":
    asyncio.run(main())