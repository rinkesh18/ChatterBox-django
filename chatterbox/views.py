from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile,Banter
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import BanterForm,SignUpForm,ProfilePicForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
    
def home(request):
	if request.user.is_authenticated:
		form = BanterForm(request.POST or None)
		if request.method == "POST":
			if form.is_valid():
				banter = form.save(commit=False)
				banter.user = request.user
				banter.save()
				messages.success(request,"Banter Successfully Posted")
				return redirect("home")
				
			else:
				messages.error(request,"Banter not posted")
				return redirect("home")
		banters = Banter.objects.all().order_by("-created")
		return render(request,"home.html",{"form":form,"banters":banters})
	else:
		banters = Banter.objects.all().order_by("-created")
		return render(request,"home.html",{"banters":banters})

    
def profile(request,pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        banters = Banter.objects.filter(user_id=pk).order_by("-created")
        context = {"profile":profile,
                   "banters":banters,
                   }
        
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()
        return render(request,"profile.html",context)
    else:
        messages.error(request,"You must be logged in to view profiles")
        return redirect("home")
    
def follow_list(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        banters = Banter.objects.filter(user_id=pk).order_by("-created")
        context = {
            "profile": profile,
            "banters": banters,
            'followers_count': profile.followed_by.count(),  # Count of users following this profile
            'following_count': profile.follows.count(),
        }

        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST.get('follow')  # Use .get() to avoid KeyError
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()
            return redirect("follow_list", pk=pk)  # Redirect to refresh the page after follow/unfollow

        return render(request, "list.html", context)
    else:
        messages.error(request, "You must be logged in to view profiles")
        return redirect("home")
    
    
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ("You Have Been Logged In!  Get Bntering!"))
			return redirect('home')
		else:
			messages.error(request, ("There was an error logging in. Please Try Again..."))
			return redirect('login')

	else:
		return render(request, "login.html", {})



def logout_user(request):
    logout(request)
    messages.success(request,"You have successfully logged out")
    return redirect("home")

def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# first_name = form.cleaned_data['first_name']
			# second_name = form.cleaned_data['second_name']
			# email = form.cleaned_data['email']
			# Log in user
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ("You have successfully registered! Welcome!"))
			return redirect('home')
	
	return render(request, "register.html", {'form':form})

def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		profile_user = Profile.objects.get(user__id=request.user.id)
		# Get Forms
		user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
		profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()

			login(request, current_user)
			messages.success(request, ("Your Profile Has Been Updated!"))
			return redirect('home')

		return render(request, "update_user.html", {'user_form':user_form, 'profile_form':profile_form})
	else:
		messages.success(request, ("You Must Be Logged In To View That Page..."))
		return redirect('home')
def profile_list(request):
	if request.user.is_authenticated:
		profiles = Profile.objects.exclude(user=request.user)
		return render(request, 'profile_list.html', {"profiles":profiles})
	else:
		messages.error(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')
    
def unfollow(request, pk):
	if request.user.is_authenticated:
		# Get the profile to unfollow
		profile = Profile.objects.get(user_id=pk)
		# Unfollow the user
		request.user.profile.follows.remove(profile)
		# Save our profile
		request.user.profile.save()

		# Return message
		messages.success(request, (f"You Have Successfully Unfollowed {profile.user.username}"))
		return redirect(request.META.get("HTTP_REFERER"))

	else:
		messages.error(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')

def follow(request, pk):
	if request.user.is_authenticated:
		# Get the profile to unfollow
		profile = Profile.objects.get(user_id=pk)
		# Unfollow the user
		request.user.profile.follows.add(profile)
		# Save our profile
		request.user.profile.save()

		# Return message
		messages.success(request, (f"You Have Successfully Followed {profile.user.username}"))
		return redirect(request.META.get("HTTP_REFERER"))

	else:
		messages.error(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Banter  # Ensure Banter model is imported

def banter_like(request, pk):
    if request.user.is_authenticated:
        banter = get_object_or_404(Banter, id=pk)
        
        # Check if the user already liked the post
        if banter.likes.filter(id=request.user.id).exists():
            banter.likes.remove(request.user)
        else:
            banter.likes.add(request.user)
        
        return redirect(request.META.get("HTTP_REFERER",))
    else:
        messages.error(request, 'You must be logged in to like a post.')    
        return redirect('home')

def banter_show(request,pk):
	banter = get_object_or_404(Banter, id=pk)
	if banter:
		return render(request,"show_banter.html",{'banter':banter})
	else:
		messages.error(request, 'That Banter Does Not Exists...')    
		return redirect('home')
	
def follow(request, pk):
    if request.user.is_authenticated:
        target_profile = get_object_or_404(Profile, user__id=pk)
        current_profile = request.user.profile
        # Prevent following yourself and duplicate follows
        if target_profile != current_profile and target_profile not in current_profile.follows.all():
            current_profile.follows.add(target_profile)
            messages.success(request, f"You have followed {target_profile.user.username}")
        else:
            messages.info(request, "Already following or cannot follow yourself.")
        return redirect(request.META.get("HTTP_REFERER", "home"))
    else:
        messages.error(request, "You must be logged in to follow someone.")
        return redirect("home")

def unfollow(request, pk):
    if request.user.is_authenticated:
        target_profile = get_object_or_404(Profile, user__id=pk)
        current_profile = request.user.profile
        if target_profile in current_profile.follows.all():
            current_profile.follows.remove(target_profile)
            messages.success(request, f"You have unfollowed {target_profile.user.username}")
        else:
            messages.info(request, f"You are not following {target_profile.user.username}")
        return redirect(request.META.get("HTTP_REFERER", "home"))
    else:
        messages.error(request, "You must be logged in to unfollow someone.")
        return redirect("home")
    
def list(request,pk):
    profile = Profile.objects.get(user_id=pk)
    return render(request,'list.html',{'profile':profile})
        

def delete_banter(request,pk):
	if request.user.is_authenticated:
		banter = get_object_or_404(Banter, id=pk)
		# Check to see if you own the banter
		if request.user.username == banter.user.username:
			# Delete The banter
			banter.delete()
			
			messages.success(request, ("The Banter Has Been Deleted!"))
			return redirect(request.META.get("HTTP_REFERER"))	
		else:
			messages.error(request, ("You Don't Own That Banter!!"))
			return redirect('home')

	else:
		messages.error(request, ("Please Log In To Continue..."))
		return redirect(request.META.get("HTTP_REFERER"))

def edit_banter(request, pk):
    if request.user.is_authenticated:
        banter_instance = get_object_or_404(Banter, id=pk)
        if request.user.username == banter_instance.user.username:
            form = BanterForm(request.POST or None, instance=banter_instance)
            if request.method == "POST":
                if form.is_valid():
                    banter = form.save(commit=False)
                    banter.user = request.user
                    banter.save()
                    messages.success(request, "Banter Updated Successfully")
                    return redirect("home")
            # Fetch the latest banters to display
            banters = Banter.objects.all().order_by('-created')
            return render(request, "edit_banter.html", {
                'form': form,
                "banter": banter_instance,
                "banters": banters
            })
        else:
            messages.error(request, "You Don't Own That Banter!!")
            return redirect('home')
    else:
        messages.error(request, "Please Log In To Continue...")
        return redirect('home')

def search(request):
	if request.method =="POST":
		search =request.POST['search']

		searched = Banter.objects.filter(body__contains = search)
		return render(request,'search.html',{'search':search,'searched':searched })
	else:
		return render(request,'search.html')

def search_user(request):
	if request.method =="POST":
		search =request.POST['search']

		searched = User.objects.filter(username__contains = search)
		return render(request,'search_user.html',{'search':search,'searched':searched })
	else:
		return render(request,'search_user.html')

def followers(request, pk):
	if request.user.is_authenticated:
		if request.user.id == pk:
			profiles = Profile.objects.get(user_id=pk)
			return render(request, 'followers.html', {"profiles":profiles})
		else:
			messages.error(request, ("That's Not Your Profile Page..."))
			return redirect('home')	
	else:
		messages.error(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')


def follows(request, pk):
	if request.user.is_authenticated:
		if request.user.id == pk:
			profiles = Profile.objects.get(user_id=pk)
			return render(request, 'follows.html', {"profiles":profiles})
		else:
			messages.error(request, ("That's Not Your Profile Page..."))
			return redirect('home')	
	else:
		messages.error(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')