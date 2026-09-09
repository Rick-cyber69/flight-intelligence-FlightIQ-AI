from django.shortcuts import render

from .services import answer_flight_question


def ai_assistant(request):
    answer = None
    question = ""
    error = None

    if request.method == "POST":
        question = request.POST.get("question", "").strip()

        if not question:
            error = "Please enter a question."

        else:
            try:
                answer = answer_flight_question(
                    None,
                    question
                )
            except Exception as e:
                error = f"Unable to process your question: {e}"

    context = {
        "answer": answer,
        "question": question,
        "error": error,
    }

    return render(
        request,
        "chatbot/ai_assistant.html",
        context
    )