"""
CLI entry for AI Motivational Quote Agent (Python).
- Optional args: student name, focus area
- Writes UTF-8 text to gpt_output.txt
- Robust error messages for beginners
"""

import os
import sys
from pathlib import Path
from datetime import datetime

from openai_client import OpenAIChatClient
from ai_motivational_agent import AIMotivationalQuoteAgent

HEADER = """\
=========================
AI Motivational Quote Agent
Timestamp: {ts}
=========================

"""

def main(argv: list[str]) -> int:
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY is not set in your environment.", file=sys.stderr)
        return 1

    student_name = argv[1] if len(argv) >= 2 else "student"
    focus_area   = argv[2] if len(argv) >= 3 else "DSA and System Design"

    try:
        # Step 1 - create a client to talk to GPT or Gen AI 
        client = OpenAIChatClient(model="gpt-4o-mini")

        # Step 2 - Create a specific agent to be invoked (motivation agent)
        agent = AIMotivationalQuoteAgent(client)

        # Step 3 - Invoke the agent to get response 
        advice = agent.generate_advice(student_name, focus_area)

        # Step 4 - If you get the resonse write it to a file 
        out_path = Path("gpt_output.txt")
        out_path.write_text(HEADER.format(ts=datetime.now()) + advice + "\n", encoding="utf-8")
        print(f"SUCCESS: Wrote advice to {out_path.resolve()}")

        # Step 5 - Print the advice on the terminal 
        print(" Response recived is ... ")
        print(advice)
        return 0

    except Exception as ex:
        # If something goes wrong, catch the exeption and show the error
        print(f"ERROR: {ex}", file=sys.stderr)
        # if there is an error you return a non zero value 
        return -1


if __name__ == "__main__":
    sys.exit(main(sys.argv))