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

    # Simple CLI: support either the default behavior or a --modi flag
    # Usage examples:
    #   python app.py                    -> default student, default focus
    #   python app.py Alex systems       -> generate advice for Alex
    #   python app.py --modi              -> generate a short Modi-inspired quote
    #   python app.py --modi service      -> Modi-inspired quote on 'service'

    # If first arg is --modi, treat optional second arg as topic
    if len(argv) >= 2 and argv[1] == "--modi":
        modi_topic = argv[2] if len(argv) >= 3 else None
        try:
            client = OpenAIChatClient(model="gpt-4o-mini")
            agent = AIMotivationalQuoteAgent(client)
            advice = agent.generate_modi_quote(modi_topic)

            out_path = Path("gpt_output.txt")
            out_path.write_text(HEADER.format(ts=datetime.now()) + advice + "\n", encoding="utf-8")
            print(f"SUCCESS: Wrote Modi-inspired quote to {out_path.resolve()}")
            print(advice)
            return 0

        except Exception as ex:
            print(f"ERROR: {ex}", file=sys.stderr)
            return -1

    # Default behavior: generate motivational advice
    student_name = argv[1] if len(argv) >= 2 else "student"
    focus_area = argv[2] if len(argv) >= 3 else "DSA and System Design"

    try:
        client = OpenAIChatClient(model="gpt-4o-mini")
        agent = AIMotivationalQuoteAgent(client)
        advice = agent.generate_advice(student_name, focus_area)

        out_path = Path("gpt_output.txt")
        out_path.write_text(HEADER.format(ts=datetime.now()) + advice + "\n", encoding="utf-8")
        print(f"SUCCESS: Wrote advice to {out_path.resolve()}")
        print(" Response recived is ... ")
        print(advice)
        return 0

    except Exception as ex:
        print(f"ERROR: {ex}", file=sys.stderr)
        return -1


if __name__ == "__main__":
    sys.exit(main(sys.argv))