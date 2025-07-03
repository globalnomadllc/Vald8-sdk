from vald8.registry import register_function

def validation(
    eval_name: str,
    dataset: str = None,
    eval_type: str = "task_accuracy",
    metrics: list[str] = None,
    thresholds: dict = None,
    config: dict = None,
    mode: str = "auto"
):
    """
    Decorator to register a function for LLM evaluation with Vald8.

    Args:
        eval_name (str): Unique name for this evaluation test.
        dataset (str): Path to the JSONL dataset file (or dataset ID for cloud mode).
        eval_type (str): Type of evaluation to perform.
        metrics (list): List of metrics to apply (e.g., ["accuracy", "semantic_similarity"]).
        thresholds (dict): Optional metric thresholds for pass/fail.
        config (dict): Additional config for the eval (e.g., required fields, regex pattern).
        mode (str): Evaluation mode: "local", "cloud", or "auto" (default is "auto").
    """

    def decorator(func):
        func_entry = {
            "func": func,
            "func_name": func.__name__,
            "eval_config": {
                "eval_name": eval_name,
                "dataset": dataset,
                "eval_type": eval_type,
                "metrics": metrics or [],
                "thresholds": thresholds,
                "config": config or {},
                "mode": mode
            }
        }

        register_function(func_entry)

        return func

    return decorator