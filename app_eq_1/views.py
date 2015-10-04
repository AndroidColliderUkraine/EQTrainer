from django.shortcuts import render


def home(request):
	# locale_init(request)
	# title_user = "%s" %(request.user) 
	# user_type = request.user.profile.type_user
	# text = _("Main page  :)")
	text = "Main page  :)"
	context = {
		# "title_user": title_user,
		"text": text,
		# "user_type": user_type,
	}
	return render(request, "base.html",context)


def profile(request):
	text = "Main page  :)"
	context = {
		"text": text,
	}
	return render(request, "profile.html",context)
