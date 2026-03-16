from django.shortcuts import render
from django.http import HttpResponse
from app.models import Student
import json
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def all_data(req):
    if req.method=="POST":
        data=req.body
        print(data)
        print(type(data))
        p_data=json.loads(data)
        print(p_data)
        print(type(p_data))
        n=p_data.get('Name')
        a=p_data.get('Age')
        c=p_data.get('Contact')
        ct=p_data.get('City')
        if 'Name' in p_data and 'Age' in p_data and 'Contact' in p_data and 'City' in p_data:
            Student.objects.create(Name=n,Age=a,Contact=c,City=ct)
            p_data={"msg":"Object created"}
            return HttpResponse(json.dumps(p_data),content_type='application/json')
        else:
            if not 'Name' in p_data:
                p_data={"msg":"Name missing"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            if not 'Age' in p_data:
                p_data={"msg":"Age missing"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            if not 'Contact' in p_data:
                p_data={"msg":"Contact missing"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            if not 'City' in p_data:
                p_data={"msg":"City missing"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
        return HttpResponse(json.dumps(p_data),content_type='application/json')
        


 



            



    # data=Student.objects.all()
    # print(data)
    # p_data=list(data.values())
    # print(p_data)
    # j_data=json.dumps(p_data)
    # print(j_data)
    # return HttpResponse(j_data,content_type='application/json')

def single_data(req,pk):
    data=Student.objects.get(id=pk)
    print(data)
    print(type(data))
    p_data=model_to_dict(data)
    print(p_data)
    print(type(p_data))
    j_data=json.dumps(p_data)
    print(j_data)
    return HttpResponse(j_data,content_type='application/json')