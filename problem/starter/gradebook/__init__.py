# gradebook package
#
# TODO: Re-export the public API so callers can write:
#   from gradebook import RECORDS, format_report
#
# Hint:
#   from .data import RECORDS
#   from .reports import format_report
def average_per_student(records: list[dict]) -> dict[str, float]:
    student_scores = {}
    for record in records:
        student_name = record["name"]
        score = record["score"]
        if student_name not in student_scores:
            student_scores[student_name] = []
        student_scores[student_name].append(score)
    average_scores = {}
    for student_name, scores in student_scores.items():
        average = sum(scores) / len(scores)
        average_scores[student_name] = round(average, 2)
    return average_scores