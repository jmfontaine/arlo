import os
import re
import subprocess
from anthropic import Anthropic

incorrect_format_message = """Your output was malformatted.
Please include exactly 1 action formatted as in the following example:

```bash-action
ls -R
```
"""


class FormatError(RuntimeError): ...


client = Anthropic()


def execute_action(command: str) -> str:
    """Execute action, return output"""
    result = subprocess.run(
        command,
        shell=True,
        text=True,
        env=os.environ,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=30,
    )
    return result.stdout


def parse_action(llm_output: str) -> str:
    """Take LLM output, return action"""
    matches = re.findall(r"```bash-action\s*\n(.*?)\n```", llm_output, re.DOTALL)

    if len(matches) == 1:
        return matches[0].strip()
    raise FormatError(incorrect_format_message)


def query_llm(messages):
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        messages=messages,
        system="You are a helpful assistant. When you want to run a command, wrap it in ```bash-action\n<command>\n```. To finish, run the exit command.",
    )
    return response.content[0].text


def run(input: str):
    messages = [
        {"role": "user", "content": input},
    ]

    while True:
        try:
            llm_output = query_llm(messages)
            print("LLM output", llm_output)
            messages.append(
                {"role": "assistant", "content": llm_output}
            )  # remember what the LLM said
            action = parse_action(llm_output)  # separate the action from output
            print("Action", action)
            if action == "exit":
                break
            output = execute_action(action)
            print("Output", output)
            messages.append(
                {"role": "user", "content": output}
            )  # send command output back
        except Exception as e:  # Let the LLM handle exceptions
            messages.append({"role": "user", "content": str(e)})
