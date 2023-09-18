from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse


class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'myapp/home.html', {'candidates': candidates, 'form': form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Add a success message
            messages.success(request, 'Congratulations! Your form has been submitted successfully.')
            return HttpResponseRedirect(request.path_info)  # Redirect to the same page

        # Form is not valid, re-render the form with errors
        candidates = Resume.objects.all()
        return render(request, 'myapp/home.html', {'candidates': candidates, 'form': form})

class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html', {'candidate': candidate})
class DeleteCandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        candidate.delete()
        messages.success(request, 'Candidate has been deleted successfully.')
        return HttpResponseRedirect(reverse('home'))