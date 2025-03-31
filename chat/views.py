import os
import json
import traceback
import openai
from openai import OpenAI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


def chat_page(request):
    return render(request, "chat.html")


@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message = data.get("message")

            if not message:
                return JsonResponse({"error": "Missing message"}, status=400)

            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}],
            )

            return JsonResponse({"reply": response.choices[0].message.content})

        except Exception as e:
            print("❌ Exception:", e)
            traceback.print_exc()
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)
