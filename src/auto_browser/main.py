from crew import create_form_crew
from tools.form_tools import cleanup

if __name__ == "__main__":
    try:
        form_crew = create_form_crew()
        result = form_crew.kickoff()
        print("\n\nForm filling results:")
        print(result)
    finally:
        # Add a delay before closing to see the final state
        import time
        time.sleep(3)
        cleanup()