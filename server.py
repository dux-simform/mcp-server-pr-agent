import asyncio
import os
import sys
from typing import Dict, List, Any, Optional, Tuple

from mcp.server.fastmcp import FastMCP, Context, Image
from pr_agent.agent.pr_agent import PRAgent
from pr_agent.config_loader import get_settings
from pr_agent.log import get_logger, setup_logger

# Set up logging
setup_logger()
logger = get_logger()

# Create an MCP server named "PR-Agent"
mcp = FastMCP("PR-Agent", dependencies=["pr_agent"])


@mcp.tool()
async def review_pr(pr_url: str, ctx: Context) -> str:
    """
    Review a pull request and provide feedback.

    Args:
        pr_url: The URL of the pull request to review

    Returns:
        A comprehensive review of the pull request
    """
    await ctx.info(f"Reviewing PR: {pr_url}")
    await ctx.report_progress(0, 1)

    try:
        agent = PRAgent()
        result = await agent.handle_request(pr_url, "/review")
        await ctx.report_progress(1, 1)
        return result or "Review completed, but no results were returned."
    except Exception as e:
        logger.error(f"Error reviewing PR: {e}")
        return f"Error reviewing PR: {str(e)}"


# @mcp.tool()
# async def describe_pr(pr_url: str, ctx: Context) -> str:
#     """
#     Generate a description for a pull request based on its changes.
#
#     Args:
#         pr_url: The URL of the pull request to describe
#
#     Returns:
#         A detailed description suitable for the PR
#     """
#     await ctx.info(f"Generating description for PR: {pr_url}")
#     await ctx.report_progress(0, 1)
#
#     try:
#         agent = PRAgent()
#         result = await agent.handle_request(pr_url, "/describe")
#         await ctx.report_progress(1, 1)
#         return result or "Description generated, but no results were returned."
#     except Exception as e:
#         logger.error(f"Error describing PR: {e}")
#         return f"Error describing PR: {str(e)}"
#
#
# @mcp.tool()
# async def improve_pr(pr_url: str, ctx: Context) -> str:
#     """
#     Suggest improvements for a pull request.
#
#     Args:
#         pr_url: The URL of the pull request to improve
#
#     Returns:
#         Suggestions for improving the pull request code
#     """
#     await ctx.info(f"Suggesting improvements for PR: {pr_url}")
#     await ctx.report_progress(0, 1)
#
#     try:
#         agent = PRAgent()
#         result = await agent.handle_request(pr_url, "/improve")
#         await ctx.report_progress(1, 1)
#         return result or "Improvements suggested, but no results were returned."
#     except Exception as e:
#         logger.error(f"Error improving PR: {e}")
#         return f"Error improving PR: {str(e)}"
#
#
# @mcp.tool()
# async def ask_about_pr(pr_url: str, question: str, ctx: Context) -> str:
#     """
#     Ask a specific question about a pull request.
#
#     Args:
#         pr_url: The URL of the pull request
#         question: The question to ask about the PR
#
#     Returns:
#         An answer to your question about the PR
#     """
#     await ctx.info(f"Answering question about PR: {pr_url}")
#     await ctx.report_progress(0, 1)
#
#     try:
#         agent = PRAgent()
#         result = await agent.handle_request(pr_url, f"/ask {question}")
#         await ctx.report_progress(1, 1)
#         return result or "Question answered, but no results were returned."
#     except Exception as e:
#         logger.error(f"Error answering question: {e}")
#         return f"Error answering question: {str(e)}"
#
#
# @mcp.tool()
# async def reflect_on_pr(pr_url: str, ctx: Context) -> str:
#     """
#     Reflect on a pull request's purpose and implementation.
#
#     Args:
#         pr_url: The URL of the pull request to reflect on
#
#     Returns:
#         A reflection on the PR's purpose and implementation
#     """
#     await ctx.info(f"Reflecting on PR: {pr_url}")
#     await ctx.report_progress(0, 1)
#
#     try:
#         agent = PRAgent()
#         result = await agent.handle_request(pr_url, "/reflect")
#         await ctx.report_progress(1, 1)
#         return result or "Reflection completed, but no results were returned."
#     except Exception as e:
#         logger.error(f"Error reflecting on PR: {e}")
#         return f"Error reflecting on PR: {str(e)}"
#
#
# @mcp.tool()
# async def analyze_pr(pr_url: str, ctx: Context) -> str:
#     """
#     Perform a detailed code analysis of a pull request.
#
#     Args:
#         pr_url: The URL of the pull request to analyze
#
#     Returns:
#         A comprehensive analysis of the PR's code
#     """
#     await ctx.info(f"Analyzing PR: {pr_url}")
#     await ctx.report_progress(0, 1)
#
#     try:
#         agent = PRAgent()
#         result = await agent.handle_request(pr_url, "/analyze")
#         await ctx.report_progress(1, 1)
#         return result or "Analysis completed, but no results were returned."
#     except Exception as e:
#         logger.error(f"Error analyzing PR: {e}")
#         return f"Error analyzing PR: {str(e)}"
#
#
# @mcp.tool()
# async def explain_pr(pr_url: str, ctx: Context) -> str:
#     """
#     Generate a simple explanation of a pull request.
#
#     Args:
#         pr_url: The URL of the pull request to explain
#
#     Returns:
#         A simple explanation of what the PR does
#     """
#     await ctx.info(f"Explaining PR: {pr_url}")
#     await ctx.report_progress(0, 1)
#
#     try:
#         agent = PRAgent()
#         result = await agent.handle_request(pr_url, "/explain")
#         await ctx.report_progress(1, 1)
#         return result or "Explanation completed, but no results were returned."
#     except Exception as e:
#         logger.error(f"Error explaining PR: {e}")
#         return f"Error explaining PR: {str(e)}"
#
#
# @mcp.prompt()
# def pr_review_prompt(pr_url: str) -> str:
#     """Create a prompt for reviewing a pull request"""
#     return f"""
#     Please review the following pull request: {pr_url}
#
#     Some things to consider:
#     - Code correctness
#     - Performance improvements
#     - Security concerns
#     - Design issues
#     - Documentation updates needed
#     """
#
#
# @mcp.prompt()
# def pr_improvement_prompt(pr_url: str) -> str:
#     """Create a prompt for suggesting improvements to a pull request"""
#     return f"""
#     Please suggest improvements for the following pull request: {pr_url}
#
#     Focus on:
#     - Code quality
#     - Performance optimizations
#     - Better design patterns
#     - Potential edge cases
#     - Security improvements
#     """


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    get_settings().set("CONFIG.git_provider", os.getenv("CONFIG_GIT_PROVIDER"))
    # get_settings().set("CONFIG.publish_output", os.getenv("CONFIG_PUBLISH_OUTPUT"))
    get_settings().set("CONFIG.verbosity_level", int(os.getenv("CONFIG_VERBOSITY_LEVEL")))

    get_settings().set("openai.key", os.getenv("OPENAI_API_KEY"))
    get_settings().set("openai.api_type", os.getenv("OPENAI_API_TYPE"))
    get_settings().set("openai.api_version", os.getenv("OPENAI_API_VERSION"))
    get_settings().set("openai.api_base", os.getenv("OPENAI_API_BASE"))
    get_settings().set("openai.deployment_id", os.getenv("OPENAI_API_DEPLOYMENT"))

    get_settings().set("github.user_token", os.getenv("GITHUB_USER_TOKEN"))

    # Run the MCP server
    mcp.run(transport="sse")
