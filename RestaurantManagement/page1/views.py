from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .models import Person,Menutbl,Category
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')
def menu(request):
    return render(request,'menu.html')



#@cache_control(no_cash=True,must_validate=True,no_store=True)
def loginpage(request):
    #if 'username' in request.session:
        #return render(request,'chome')
        #return render(request,'chome.html')
    if request.method == 'POST':
        email=request.POST['username']
        password= request.POST['password']
        #user=User.objects.get(email=email)
        #pa=User.objects.get(email_address=email)
        #if pa is not None:
            #user=authenticate(request,email_address=pa.email_address,password=password)
        p=Person.objects.get(email=email)
        user=authenticate(request,username=p.name,password=password)
        #p=Person.objects.get(email=email)
        #employee = Employee.objects.get(id=id) 
        #employee = Employee.objects.all() 
        #context["data"] = GeeksModel.objects.get(id = id)
        if user is not None:
            request.session['username']=p.name
            request.session.save()
            if (p.role_id==1):
                login(request, user)
                #return render(request,'chome.html')
                return redirect('chome')
            elif(p.role_id==2):
                login(request, user)
                return render(request,'staffhome.html')
            elif(p.role_id==3):
                login(request, user)
                return render(request,'adminhome.html')
            else:
                #return render(request,'chome.html')
                return render(request,'loginpage.html')
        else:
            messages.error(request,"Invalid Username or password")
            return redirect('loginpage')
    else:
        return render(request,'loginpage.html')
def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        #role=request.POST.get('category')
        password=request.POST.get('password')
        #print(username)
        if User.objects.filter(username=username).exists():
            messages.info(request,"User already exists")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")
            return redirect('signup')
        elif username != '' and email != '' and phone != '' and password != '':
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save();
            data=Person(user_id=user,name=username,email=email,phone=phone,role_id=1,address=address,password=password)
            data.save()
            messages.info(request,"Successfully registered")
            #data2=Users(USERNAME=username,Email address=email)
            return redirect('loginpage')
        else:
            messages.info(request,"Error occur")
            return redirect('signup')
    else:
        return render(request,'signup.html')

@login_required
def chome(request):
    #category=Category.objects.filter(status=1)
    # if 'username' in request.session:
    #     salads=Menutbl.objects.filter(cid=1)
    #     pizza=Menutbl.objects.filter(cid=2)
    #     burger=Menutbl.objects.filter(cid=3)
    #     return render(request,'chome.html',{"salads":salads,"pizza":pizza,"burger":burger})
    # else :
    #     return redirect(loginpage)
    salads=Menutbl.objects.filter(cid=1)
    pizza=Menutbl.objects.filter(cid=2)
    burger=Menutbl.objects.filter(cid=3)
    return render(request,'chome.html',{"salads":salads,"pizza":pizza,"burger":burger})



def staffhome(request):
    if 'username' in request.session:
        return render(request,'staffhome.html')
    return redirect(loginpage)

    



def logout_user(request):
    if 'username' in request.session:
        #session.objects.all().delete()
        logout(request)
        request.session.flush()
        request.session.clear()
        #del request.session['username']
        return redirect('logout_user')
        #return render(request,'loginpage.html')
        #return render(request,'logout_user.html')
    return render(request,'logout_user.html')


    #logout(request)
    #return HttpResponseRedirect(reverse('loginpage'))
    #return render(request,'loginpage.html')
    

def adminhome(request):
    #if 'username' in request.session:
    salads=Menutbl.objects.filter(cid=1)
    pizza=Menutbl.objects.filter(cid=2)
    burger=Menutbl.objects.filter(cid=3)
    return render(request,'adminhome.html',{"salads":salads,"pizza":pizza,"burger":burger})
    #return redirect(loginpage)



#def customerprofile(request,):
    #user_profile = get_object_or_404(Person, username=username)
    #return render(request,'customerprofile.html')

def a_add_person(request,):
    #user_profile = get_object_or_404(Person, user__name=username)
    #return render(request,'a_add_person.html')

    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        #role=request.POST.get('category')
        password=request.POST.get('password')
        #print(username)
        if User.objects.filter(username=username).exists():
            messages.info(request,"User already exists")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")
            return redirect('signup')
        elif username != '' and email != '' and phone != '' and password != '':
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save();
            data=Person(name=username,email=email,phone=phone,role_id=2,address=address,password=password)
            data.save()
            print("data saved")
            messages.info(request,"Saved")
            #data2=Users(USERNAME=username,Email address=email)
            return render(request,'adminhome.html')
    else:
        return render(request,'a_add_person.html')


def a_view_person(request):
    person=Person.objects.all()
    return render(request,'a_view_person.html',{"person":person})



def customerprofile(request):
    user_profile = Person.objects.get(name=request.user)
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        #role=request.POST.get('category')
        #password=request.POST.get('password')
        #print(username)
        if username != '' and email != '' and phone != '':
            user_profile.name=username
            user_profile.phone=phone
            user_profile.address=address
            user_profile.email=email
            #user_profile.save()
            Person.objects.filter(pk=user_profile.pk).update(address=address)
            #data2=Users(USERNAME=username,Email address=email)
            messages.success(request,"Changes are saved successfully !")
            
            return redirect('customerprofile')
        else:
            messages.error(request,"Updation failed !")
    else: 
        return render(request, 'customerprofile.html', {'user_profile': user_profile})
    


def changepassword(request):
    user_profile = Person.objects.get(name=request.user)
    u=User.objects.get(username=user_profile)
    if request.method == 'POST':
        password=request.POST.get('password')
        #print(username)
        if password != '':
            user_profile.password=password
            u.password=password
            u.save()
            user_profile.save()
            #data2=Users(USERNAME=username,Email address=email)
            messages.info(request,"Password Changed")
            
            return redirect('chome')
    else:
        
        return render(request, 'changepassword.html', {'user_profile': user_profile})
    


def delete_user(request,pk):
    
    if pk!=3:
        #records_to_delete = Person.objects.filter(pk=pk)
        # Delete the records that match the criteria
        #records_to_delete.delete()
        messages.success(request,"Changes are saved successfully !")
            
    return redirect('a_view_person')


def a_add_items(request):
    if request.method == 'POST':
        categoryn=request.POST.get('cat')
        name=request.POST.get('name')
        description=request.POST.get('description')
        image = request.FILES['image']
        price=request.POST.get('price')
        cat = Category.objects.filter(cname=categoryn).first()
        
        if Menutbl.objects.filter(name=name).exists():
            messages.info(request,"The item already exists")
            return redirect('a_add_items')
        else:
            item=Menutbl(cid=cat,name=name,description=description,image=image,price=price)
            item.save();
            return redirect('a_view_menu')
    else:
        category=Category.objects.all()
        return render(request,'a_add_items.html',{"category":category})

def a_view_menu(request):
    items=Menutbl.objects.all()
    return render(request,'a_view_menu.html',{"items":items})
def a_view_category(request):
    categories=Category.objects.all()
    return render(request,'a_view_category.html',{"cat":categories})
def a_add_category(request):
    return render(request,'a_add_category.html')


def a_edit_menu_item(request, item_id):
    item = Menutbl.objects.get(pk=item_id)
    category=Category.objects.all()
    
    if request.method == 'POST':
        categoryn=request.POST.get('catn')
        if categoryn == "" :
            categoryn=item.cid
        if categoryn is None:
            categoryn=item.cid
        name=request.POST.get('name')
        if name is None:
            name=item.name
        #print("name",name)
        description=request.POST.get('description')
        if description is None:
            description=item.description
        if 'eimage' in request.FILES:
            print("image bin",request.FILES) 
            #image = request.FILES['eimage']
            image = request.FILES.get('eimage', item.image)
            #image = media/images/image;
        else:
            image = item.image
        price=request.POST.get('price')
        if price is None:
            price=item.price
        cat = Category.objects.filter(cname=categoryn).first()
        if categoryn != ''and name != '' and description !='' and image !='' and price != '':
            Menutbl.objects.filter(pk=item.pk).update(cid=cat,name=name,description=description,image=image,price=price)
            messages.success(request,"Changes are saved successfully !")
            return redirect('a_edit_menu_item',item.pk)
        else:
            return redirect('adminhome')
        # if form.is_valid():
        #     form.save()
        #     return redirect('a_view_menu')
    # else:
    #     form = MenutblEditForm(instance=item)
    return render(request, 'a_edit_menu_item.html', {'item': item,'category':category})

