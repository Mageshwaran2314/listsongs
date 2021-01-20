from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def home(request):
    # return HttpResponse("<h1>List songs</h1>")
    return render(request, "home.html", context={})


@csrf_exempt
def getSongs(request):
    try:
        start = request.POST.get("start", 0)
        end = request.POST.get("end", 10)
        print(start, end)
        file = open('playlist.json')
        data = json.load(file)

        # ['id', 'title', 'danceability', 'energy', 'key', 'loudness', 'mode', 
        # 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 
        # 'duration_ms', 'time_signature', 'num_bars', 'num_sections', 'num_segments', 'class']
        if int(end)>len(data["id"]):
            return JsonResponse({"success":False, "messsage":"out of range"}, status=403)
        
        data_holder = []
        for i in range(int(start), int(end)):
            key = str(i)
            data_holder.append({
                "k": i,
                "id": data["id"][key],
                "title": data["title"][key],
                "danceability": data["danceability"][key],
                "energy": data["energy"][key],
                "key": data["key"][key],
                "loudness": data["loudness"][key],
                "mode": data["mode"][key],
                "acousticness": data["acousticness"][key],
                "instrumentalness": data["instrumentalness"][key],
                "liveness": data["liveness"][key],
                "valence": data["valence"][key],
                "duration_ms": data["duration_ms"][key],
                "num_bars": data["num_bars"][key],
                "num_sections": data["num_sections"][key],
                "num_segments": data["num_segments"][key],
            })
        return JsonResponse({
            "total": len(data["id"]),
            "data":data_holder}, 
            safe=False)
    except Exception as e:
        print("Error:",e)
        return JsonResponse({"success":False}, status=500)
