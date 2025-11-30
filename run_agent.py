
import uuid
import asyncio
import warnings
import sys
from dotenv import load_dotenv
from google.adk.runners import Runner
from github_agent.tools.tools import github_tools
from google.adk.sessions import InMemorySessionService
from google.genai import types
from github_agent.agent import root_agent

load_dotenv()

# Suppress the experimental warnings
warnings.filterwarnings('ignore', category=UserWarning, module='google.adk.tools.mcp_tool.mcp_tool')


async def main():
    # Configuration
    APP_NAME = "Brandon Bot"
    USER_ID = "brandon_hancock"
    SESSION_ID = str(uuid.uuid4())
    
    print("CREATED NEW SESSION:")
    print(f"\tSession ID: {SESSION_ID}\n")

    # Create session service
    session_service = InMemorySessionService()
    
    # Create session FIRST before creating runner
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    # Create runner with the agent
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    # Your query
    new_message = types.Content(
        role="user", 
        parts=[types.Part(text="Provide the code review in the latest PR in the repo https://github.com/MohdZaheen123/Agent-Test")]
    )

    print("=== AGENT RESPONSE ===\n")
    
    try:
        async for event in runner.run_async(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=new_message,
        ):
            # Handle different event types
            if event.content and event.content.parts:
                for part in event.content.parts:
                    # Check if it's text
                    if hasattr(part, 'text') and part.text:
                        print(part.text, end='', flush=True)
                    
                    # Check if it's a function call
                    elif hasattr(part, 'function_call') and part.function_call:
                        func_call = part.function_call
                        if func_call and hasattr(func_call, 'name'):
                            print(f"\n[Tool Call: {func_call.name}]", flush=True)
                        else:
                            print(f"\n[Tool Call]", flush=True)
                    
                    # Check if it's a function response
                    elif hasattr(part, 'function_response') and part.function_response:
                        print(f"\n[Tool Response Received]", flush=True)
                    
            if event.is_final_response():
                print("\n\n[Response Complete]")
        await github_tools.close()
    except KeyboardInterrupt:
        print("\n\n[Interrupted by user]")
    except Exception as e:
        print(f"\n\nError during agent execution: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # Suppress the async generator cleanup warning
    import warnings
    warnings.filterwarnings('ignore', message='.*async_generator.*')
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
    # except Exception as e:
    #     pass  # Ignore cleanup errors