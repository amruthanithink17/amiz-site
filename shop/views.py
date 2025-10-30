from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from shop.models import Cart, Order, OrderItem 
from django.shortcuts import get_object_or_404
from shop.models import Product, Cart, Wishlist



# ---------- Public Pages ----------
def index(request):
    return render(request, 'index.html')

def mens(request):
    return render(request, 'mens.html')

def womens(request):
    return render(request, 'womens.html')

def kids(request):
    return render(request, 'kids.html')

def accessories(request):
    return render(request, 'accessories.html')

def sales(request):
    return render(request, 'sales.html')

def contact(request):
    return render(request, 'contact.html')

def shipping(request):
    return render(request, 'shipping.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def profile(request):
    return render(request, 'profile.html')


# ---------- Authentication ----------
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        next_page = request.POST.get('next')  # ✅ Keep the 'next' from the form

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")

            # ✅ Redirect back to 'next' page if it exists
            if next_page:
                print(f"✅ Redirecting to: {next_page}")
                return redirect(next_page)
            else:
                return redirect('account')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

    # ✅ Preserve ?next= value in the GET request
    next_page = request.GET.get('next', '')
    return render(request, 'login.html', {'next': next_page})



def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')


# ---------- Protected Pages ----------
@login_required(login_url='login')
def cart(request):
    return render(request, 'cart.html')

@login_required(login_url='login')
def orders(request):
    return render(request, 'orders.html')

@login_required(login_url='login')
def account(request):
    return render(request, 'account.html')


@login_required
def proceed_order(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)

    if not cart_items.exists():
        return redirect('cart')  # no items in cart

    total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        payment_method = request.POST.get('payment_method')

        order = Order.objects.create(
            user=user,
            full_name=full_name,
            address=address,
            phone=phone,
            email=email,
            total_price=total,
            payment_method=payment_method,
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )

        cart_items.delete()  # clear cart after ordering
        return render(request, 'shop/order_success.html', {'order': order})

    return render(request, 'shop/checkout.html', {'cart_items': cart_items, 'total': total})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-ordered_at')
    return render(request, 'shop/my_orders.html', {'orders': orders})

# ---------- CART & WISHLIST MANAGEMENT ----------

@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} added to your cart.")
    return redirect('cart')


@login_required(login_url='login')
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, f"{product.name} added to your wishlist.")
    else:
        messages.info(request, f"{product.name} is already in your wishlist.")

    return redirect('wishlist')


@login_required(login_url='login')
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Cart.objects.filter(user=request.user, product=product).delete()
    messages.success(request, f"{product.name} removed from your cart.")
    return redirect('cart')


@login_required(login_url='login')
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    messages.success(request, f"{product.name} removed from your wishlist.")
    return redirect('wishlist')
