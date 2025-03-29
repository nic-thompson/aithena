from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import os
import openai
import traceback

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message = data.get("message")

            print("🟡 Incoming message:", message)

            if not message:
                return JsonResponse({"error": "Missing 'message' in request body"}, status=400)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}],
            )

            reply = response.choices[0].message.content
            return JsonResponse({"reply": reply})

        except Exception as e:
            print("❌ Exception:", str(e))
            traceback.print_exc()
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def chat_page(request):
    return render(request, "chat.html")
