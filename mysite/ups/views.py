from django.shortcuts import render, get_object_or_404
from .models import Package, Product, Truck, Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    return render(request, 'ups/home.html')


def shipments(request):
    context = {
        'packages': Package.objects.all()
    }
    return render(request, 'ups/shipments.html', context)


class ShipListView(ListView):
    model = Package
    template_name = 'ups/shipments.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'packages'
    ordering = ['pkgId']


def shipdetail(request, pkgId):
    package_ = Package.objects.get(pkgId=pkgId)
    context = {
        'products': Product.objects.filter(package=package_),
        'pkgId': pkgId,
    }
    return render(request, 'ups/product_detail.html', context)


def search(request):
    return render(request, 'ups/search.html')


def searchdetail(request):
    if request.method == 'POST':
        data = request.POST
        trackingNum = data.get("trackingNum")
        context = {
            'packages': Package.objects.filter(pkgId=trackingNum),
        }
        return render(request, "ups/shipments_search.html", context)


def editdestination(request, pkgId):
    context = {
        'pkgId': pkgId,
    }
    return render(request, 'ups/editdestination.html', context)


def editdestinationResult(request):
    if request.method == 'POST':
        data = request.POST
        x = int(data.get("X"))
        y = int(data.get("Y"))
        Id = int(data.get("packageId"))
        print(x)
        print(y)
        print(Id)
        package = Package.objects.filter(pkgId=Id).first()
        if (package.productStatus == "waiting_for_pickup") or (package.productStatus == "loading_on_truck"):
            package.buyerX = x
            package.buyerY = y
            package.save()
            return render(request, 'ups/editDestSuccess.html')
        else:
            return render(request, 'ups/editDestFailure.html')


def addpackage(request, pkId):
    package = Package.objects.filter(pkgId=pkId).first()
    package.upsId = request.user.username
    package.save()
    return render(request, 'ups/addpackageSuccess.html')


def find_specialists(request):
    return render(request, 'ups/specialists.html')

# Contents for the blog


class PostListView(ListView):
    model = Post
    template_name = 'ups/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Contents for the resources


def resources(request):
    return render(request, 'ups/resource.html')
