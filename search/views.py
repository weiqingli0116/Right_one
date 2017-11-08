from django.shortcuts import render
from search.models import music, movie, hobbies, health, spend
from users.models import User, profile
# Create your views here.
def search(request):
		#boys or girls?

	gender = request.GET.get('gender','')
	if gender != 'both':
		profile_list = profile.objects.filter(gender = gender)
	else:
		profile_list = profile.objects.all() #注意缩进

	onlychild = request.GET.get('onlychild','')
	if onlychild == 'true':
		profile_list = profile_list.filter(only_child = True)

	af = request.GET.get('age_from',0)
	at = request.GET.get('age_to',0)
	if af != 0:
		profile_list = profile_list.filter(age__gte = af)
	if at != 0:
		profile_list = profile_list.filter(age__lte = at)

	wf = request.GET.get('weight_from',0)
	wt = request.GET.get('weight_to',0)
	if wf != 0:
		profile_list = profile_list.filter(weight__gte = wf)
	if wt != 0:
		profile_list = profile_list.filter(weight__lte = wt)

	hf = request.GET.get('height_from',0)
	ht = request.GET.get('height_to',0)
	if hf != 0:
		profile_list = profile_list.filter(height__gte = hf)
	if ht != 0:
		profile_list = profile_list.filter(height__lte = ht)

	eduf = request.GET.get('eduf',0)
	edut = request.GET.get('edut',0)
	if eduf != 0:
		profile_list = profile_list.filter(education__gte = eduf)
	if edut != 0:
		profile_list = profile_list.filter(education__lte = edut)
		# get users
	#params = [gender, onlychild, af, at, wf, wt, hf, ht, eduf, edut]

		#return data
        #data = {}
        #data["filter"] = params
        #data["profile"] = profile_list

	#except:
    #	print('Oops! I know nothing.' )

	return render(request, 'search/search.html', {'profile_list':profile_list})

