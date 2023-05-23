"""
URL configuration for Ecart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainApp import views as mainApp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mainApp.homePage),
    path("shop/<str:mc>/<str:sc>/<str:br>/", mainApp.shopPage),
    path("filter/<str:mc>/<str:sc>/<str:br>/<str:filter>/", mainApp.filterPage),
    path("price-filter/<str:mc>/<str:sc>/<str:br>/", mainApp.priceFilterPage),
    path("search/", mainApp.searchPage),
    path("cart/", mainApp.cartPage),
    path("add-to-cart/<int:num>/", mainApp.addToCartPage),
    path("remove-from-cart/<str:num>/", mainApp.removeFromCartPage),
    path("update-cart/<str:num>/<str:op>/", mainApp.updateCartPage),
    path("checkout/", mainApp.checkoutPage),
    path('paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>/',mainApp.paymentSuccessPage),
    path('re-payment/<str:checkid>/',mainApp.payAgainPage),
    path("place-order/", mainApp.placeOrderPage),
    path("confirmation/", mainApp.confirmationPage),
    path("single-product/<int:id>", mainApp.singleProductPage),
    path("contact/", mainApp.contactPage),
    path("login/", mainApp.loginPage),
    path("signup/", mainApp.signupPage),
    path("profile/", mainApp.profilePage),
    path("logout/", mainApp.logoutPage),
    path("update-profile/", mainApp.updateProfilePage),
    path("add-to-wishlist/<int:num>/", mainApp.addToWishlistPage),
    path("remove-from-wishlist/<int:num>/", mainApp.removeFromWishlistPage),
    path("forget-password-1/", mainApp.forgetPasswordPage1),
    path("forget-password-2/", mainApp.forgetPasswordPage2),
    path("forget-password-3/", mainApp.forgetPasswordPage3),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
