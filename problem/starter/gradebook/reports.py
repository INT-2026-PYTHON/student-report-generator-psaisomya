"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass
def top_scorer(records: list[dict]) -> tuple[str, float]:
    average_scores = average_per_student(records)
    if not average_scores:
        return "", 0.0
    top_name = ""
    top_score = -1.0
    for name, score in average_scores.items():
        if score > top_score:
            top_score = score
            top_name = name
    return top_name, top_score