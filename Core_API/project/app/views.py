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
       

    data=Student.objects.all()
    print(data)
    p_data=list(data.values())
    print(p_data)
    j_data=json.dumps(p_data)
    print(j_data)
    return HttpResponse(j_data,content_type='application/json')

@csrf_exempt
def single_data(req,pk):
    user=Student.objects.filter(id=pk)
    if not user:
        p_data={"msg":"Entered id not presented in our db"}
        return HttpResponse(json.dumps(p_data),content_type='application/json')
    else:
        if req.method=='PUT':
            data=req.body
            print(data)
            print(type(data))
            p_data=json.loads(data)
            print(p_data)
            print(type(p_data))
            if 'Name' in p_data and 'Age' in p_data and 'Contact' in p_data and 'City' in p_data:
                n=p_data.get('Name')
                a=p_data.get('Age')
                c=p_data.get('Contact')
                ct=p_data.get('City')
                old_data=Student.objects.get(id=pk)
                old_data.Name=n
                old_data.Age=a
                old_data.Contact=c
                old_data.City=ct
                old_data.save()
                p_data={"msg":"Data updated"}
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
                
        elif req.method=='PATCH':
            data=req.body
            print(data)
            print(type(data))
            p_data=json.loads(data)
            print(p_data)
            print(type(p_data))
            n=p_data.get("Name")
            a=p_data.get("Age")
            c=p_data.get("Contact")
            ct=p_data.get("City")
            if p_data:
                n=p_data.get("Name")
                a=p_data.get("Age")
                c=p_data.get("Contact")
                ct=p_data.get("City")
                old_data=Student.objects.get(id=pk)
                if n:
                    old_data.Name=n
                if a:
                    old_data.Age=a
                if c:
                    old_data.Contact=c
                if ct:
                    old_data.City=ct
                old_data.save()
                p_data={"msg":"Data partially updated"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            else:
                p_data={"msg":"Object values are missing"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            
        elif req.method=='DELETE':
            user=Student.objects.get(id=pk)
            user.delete()
            p_data={"msg":"Data deleted"}
            return HttpResponse(json.dumps(p_data),content_type='application/json')





                


    data=Student.objects.get(id=pk)
    print(data)
    print(type(data))
    p_data=model_to_dict(data)
    print(p_data)
    print(type(p_data))
    j_data=json.dumps(p_data)
    print(j_data)
    return HttpResponse(j_data,content_type='application/json')