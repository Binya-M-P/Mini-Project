from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .models import Person,Menutbl,Category,Subcategory
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')
def menu(request):
    return render(request,'menu.html')



#@cache_control(no_cash=True,must_validate=True,no_store=True)
def loginpage(request):
    # if 'username' in request.session:
    #     print("withemailenter")
    #     return render(request,'chome')
    #     #return render(request,'chome.html')
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
                subcategory=Subcategory.objects.all()
                category=Category.objects.all()
                menu=Menutbl.objects.all()
                #return render(request,'chome.html')
                return redirect('chome')
                #return render(request,'chome.html',{'subcategory':subcategory,'category':category,'menu':menu})
            elif(p.role_id==2):
                login(request, user)
                return render(request,'staffhome.html')
            elif(p.role_id==3):
                login(request, user)
                return render(request,'adminhome.html')
            else:
                #return render(request,'chome.html')
                return render(request,'chome.html')
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
@cache_control(no_cash=True,must_validate=True,no_store=True)
def chome(request):
    #category=Category.objects.filter(status=1)
    if 'username' in request.session:
        subcategory=Subcategory.objects.all()
        category=Category.objects.all()
        menu=Menutbl.objects.all()
        #return render(request,'chome.html')
        return render(request,'chome.html',{'subcategory':subcategory,'category':category,'menu':menu})
    else :
        return render(request,'lognpage.html')
    # salads=Menutbl.objects.filter(cid=1)
    # pizza=Menutbl.objects.filter(cid=2)
    # burger=Menutbl.objects.filter(cid=3)
    # return render(request,'chome.html',{"salads":salads,"pizza":pizza,"burger":burger})



def staffhome(request):
    if 'username' in request.session:
        return render(request,'staffhome.html')
    return redirect(loginpage)

    



# def logout_user(request):
#     # if 'username' in request.session:
#     #     #session.objects.all().delete()
#     #     logout(request)
#     #     request.session.flush()
#     #     request.session.clear()
#     #     #del request.session['username']
#     #     return redirect('loginpage')
#     #     #return render(request,'loginpage.html')
#     #     #return render(request,'logout_user.html')
#     logout(request)
#     request.session.flush()
#     request.session.clear()
#     return render(request,'logout_user.html')


#from django.contrib.auth import logout

def logout_user(request):
    if request.user.is_authenticated:
        # Log the user out
        logout(request)
        # Clear the session
        request.session.flush()
        request.session.clear()
        #del request.session['username']
        return render(request,'loginpage.html')
        #return redirect('loginpage')
    else:
        logout(request)
        request.session.flush()
        # Handle the case where the user is not authenticated
        return render(request,'logout_user.html')




    #logout(request)
    #return HttpResponseRedirect(reverse('loginpage'))
    #return render(request,'loginpage.html')
    

def adminhome(request):
    #if 'username' in request.session:
    salads=Menutbl.objects.filter(pk=1)
    pizza=Menutbl.objects.filter(pk=2)
    burger=Menutbl.objects.filter(pk=3)
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
    if user_profile is None:
        return redirect('loginpage')
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
        subcategory_name = request.POST.get('subcat')
        name=request.POST.get('name')
        description=request.POST.get('description')
        image = request.FILES['image']
        price=request.POST.get('price')
        lower_name = name.lower()
        cat = Category.objects.filter(cname=categoryn).first()
        subcategory = Subcategory.objects.filter(scname=subcategory_name).first()

        
        if Menutbl.objects.filter(name__iexact=lower_name).exists():
            messages.info(request,"The item already exists")
            return redirect('a_add_items')
        else:
            item=Menutbl(cid=cat,sub_category=subcategory,name=name,description=description,image=image,price=price)
            item.save();
            return redirect('a_view_menu')
    else:
        category=Category.objects.all()
        subcategories = Subcategory.objects.all()
        return render(request, 'a_add_items.html', {"category": category, "subcategories": subcategories})
    

def a_view_menu(request):
    items=Menutbl.objects.all()
    return render(request,'a_view_menu.html',{"items":items})
def a_view_category(request):
    categories=Category.objects.all()
    #subcategory=Subcategory.objects.all()
    return render(request,'a_view_category.html',{"cat":categories})


def a_view_subcategory(request,item_id):
    category = Category.objects.get(pk=item_id)
    subcats = Subcategory.objects.filter(cid=category)
    if subcats is not None:
        return render(request,'a_view_subcategory.html',{"subcats":subcats,"category":category})
    else:
        return redirect(a_view_category)
    

def a_edit_subcategory(request,item_id):
    
    subcat = Subcategory.objects.filter(pk=item_id).first()
    if request.method == 'POST':
        # print("subcat nokkan",item_id)
        sn=request.POST.get('name')

        lower_name = sn.lower()
        if Subcategory.objects.filter(scname__iexact=lower_name).exists():
            messages.info(request,"The subcategory already exists")
        else :
            Subcategory.objects.filter(pk=item_id).update(scname=sn)
            messages.info(request,"The subcategory Edited Successfully")

        
        #return redirect(a_view_subcategory)
    if subcat is not None :
        return render(request,'a_edit_subcategory.html',{"subcat":subcat})
    else :
        return redirect(a_view_subcategory)

def a_add_category(request):
    
    if request.method == 'POST':
        name=request.POST.get('name')
        lower_name = name.lower()
        if Category.objects.filter(cname__iexact=lower_name).exists():
            messages.info(request,"The item already exists")
            return redirect('a_add_category')
        else:
            item=Category(cname=name)
            item.save();
            return redirect('a_view_category')
    return render(request,'a_add_category.html')



def a_edit_menu_item(request, item_id):
    item = Menutbl.objects.get(pk=item_id)
    category=Category.objects.all()
    subcategory = Subcategory.objects.all()
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
    return render(request, 'a_edit_menu_item.html', {'item': item,'category':category, 'subcategory': subcategory})



def get_category_subcategory_data(request):
    # Query your database to get the category-subcategory data
    category_subcategory_data = {}
    categories = Category.objects.all()

    for category in categories:
        subcategories = Subcategory.objects.filter(cid=category)
        subcategory_names = [subcategory.scname for subcategory in subcategories]
        category_subcategory_data[category.cname] = subcategory_names

    return JsonResponse(category_subcategory_data)

def a_add_subcategory(request, item_id):
    cat = Category.objects.filter(pk=item_id).first()
    cid=cat.cid
    if request.method == 'POST':
        name=request.POST.get('name')
        lower_name = name.lower()
        cat = Category.objects.filter(pk=item_id).first()
        if Subcategory.objects.filter(scname__iexact=lower_name,cid=cat).exists():
            messages.info(request,"The subcategory already exists")
            #return redirect(a_add_subcategory)
            return render(request,'a_add_subcategory.html',{"item_id":item_id})
        else:
            itm=Subcategory(scname=name,cid=cat)
            itm.save();
            messages.info(request,"The subcategory is added successfully ")
            return redirect(a_view_category)
            #return render(request,'a_view_subcategory.html',{"item_id":cid})
    else :
        return render(request,'a_add_subcategory.html',{"item_id":item_id})

def get_subcategories(request):
    if request.method == 'GET':
        category_name = request.GET.get('category')
        subcategories = []

        if category_name:
            # Query your database to get subcategories based on the selected category
            # Replace this with the actual query to retrieve subcategories
            subcategories = [subcat.scname for subcat in Subcategory.objects.filter(cid__cname=category_name)]

        return JsonResponse({'subcategories': subcategories})
    

def a_status_menu(request,item_id):
    item = Menutbl.objects.get(pk=item_id)
    if item.status == True:
        Menutbl.objects.filter(pk=item_id).update(status=False)
    else :
        Menutbl.objects.filter(pk=item_id).update(status=True)
    return redirect('a_view_menu')


def a_edit_category(request,item_id):
    category = Category.objects.get(cid=item_id)
    if request.method == 'POST':
        # print("subcat nokkan",item_id)
        name=request.POST.get('name')
        lower_name = name.lower()
        if name is not None:
            
        
            if Category.objects.filter(cname__iexact=lower_name).exists():
                messages.info(request,"The Category already exists")
            else:
                Category.objects.filter(cid=item_id).update(cname=name)
                messages.info(request,"The category name edited successfully")
                return redirect('a_view_category')
        #return redirect(a_view_subcategory)
    return render(request,'a_edit_category.html',{'category':category})

def a_status_category(request,item_id):
    item = Category.objects.get(pk=item_id)
    if item.status == True:
        Category.objects.filter(pk=item_id).update(status=False)
    else :
        Category.objects.filter(pk=item_id).update(status=True)
    return redirect('a_view_category')