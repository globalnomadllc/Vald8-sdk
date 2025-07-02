# Vald8-sdk
The python SDK for Valid8

Here’s a clean, professional, developer-friendly README for your public vald8-sdk repo (Apache 2.0 licensed, with focus on CI/LLM testing, open-source credibility, and SaaS upsell path).

⸻

📦 Vald8 SDK

Vald8 is a lightweight Python SDK for automated LLM evaluation in CI/CD pipelines.

Use it to register your LLM functions, run structured tests against datasets, and validate model behavior automatically on every pull request.

✅ Fully local, offline support (Free)
✅ Designed for seamless GitHub PR integration (Cloud SaaS option)
✅ Developer-first, CI-friendly

⸻

🚀 What is Vald8?

Vald8 helps LLM developers and ML engineers prevent silent model regressions by running automated tests on their LLM apps—just like unit tests for code.

You define what your LLM should produce for a given input.
Vald8 runs that evaluation every time you commit, push, or open a PR.

⸻

✨ Features (SDK)

✅ Decorator-based LLM function registration
✅ Local dataset loading (JSONL format)
✅ Built-in metric evaluation (Accuracy, JSON structure, Latency, etc.)
✅ Run tests locally or as part of CI
✅ Optional connection to the Vald8 Cloud Dashboard (for SaaS users)

⸻

🛠️ Quickstart Example (Local Run)
	1.	Install:

pip install vald8


⸻

	2.	Define your LLM function:

from vald8 import validation

@validation(
    eval_name="qa_task_accuracy",
    dataset="./vald8_datasets/qa_test.jsonl",
    eval_type="task_accuracy",
    metrics=["accuracy"],
    thresholds={"accuracy": 0.8}
)
def generate_answer(prompt: str) -> str:
    # Your real LLM inference code here
    return call_openai(prompt)


⸻

	3.	Prepare your dataset (qa_test.jsonl):

{"input_data": {"prompt": "What is 2+2?"}, "expected_output": "4"}
{"input_data": {"prompt": "Capital of France?"}, "expected_output": "Paris"}


⸻

	4.	Run Locally:

python -m vald8.cli

This will run your function against the dataset and print metric results.

⸻

✅ Supported Eval Types (MVP)

Eval Type	Description
task_accuracy	Check if output matches expected answers
json_structure	Validate JSON formatting and required fields
latency	Measure LLM response time
regex_pattern	Check if outputs match a regex

More eval types and metrics coming soon.

⸻

✅ Optional: Connect to Vald8 Cloud (SaaS)

For GitHub PR checks, web dashboards, historical run tracking, and team collaboration:
👉 https://vald8.ai

⸻

✅ License

This SDK is Apache 2.0 Licensed.
See LICENSE for details.

⸻

✅ Contributing

We welcome community contributions!

✅ File a GitHub issue
✅ Submit a PR (bug fixes, new metrics, dataset format adapters)
✅ Follow conventional commit messages

⸻

✅ Roadmap (Next Up):
	•	Async LLM function support
	•	Custom user-defined metrics
	•	Native GitHub Action runner
	•	More eval types (toxicity, hallucination, etc)

⸻

✅ Learn More

👉 Full docs: https://vald8.ai/docs
👉 Example projects: Coming soon.