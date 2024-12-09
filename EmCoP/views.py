from django.shortcuts import render, redirect
from django.shortcuts import redirect
from .models import Product, Order
from .forms import CreateUserForm, LoginForm
from .models import Slider, Team, Board, Product, Category, Order, OrderItem,EmergencyAlert, ContactMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .forms import ContactMessageForm

from .models import Product

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

    return render(request, 'register.html', {'form': form})

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'you are logged in successfully as {username}')
                return redirect ('homepage')
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You are logged out successfully')
    return redirect('login')

def home(request):
    sliders = Slider.objects.all()
    return render(request, 'index.html', {'sliders': sliders})

def about(request):
    teams = Team.objects.all()
    boards = Board.objects.all()
    return render(request, 'about.html', {'teams': teams, 'boards': boards})

def contact(request):
    return render(request, 'contact.html')

def join(request):
    return render(request, 'join.html')

def products(request):
    return render(request, 'product_list.html')


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(stock__gt=0)
    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(
        user=request.user,
        is_paid=False,
        defaults={'total_price': 0}
    )
    return redirect('Product_list')

    order_item, item_created = OrderItem.objects.get_or_create(
        order=order,
        product=product,
        defaults={'quantity': 1, 'price': product.price}
    )

    if not item_created:
        order_item.quantity += 1
        order_item.save()

    order.total_price += product.price
    order.save()
    return redirect('cart_view')

@login_required
def cart_view(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    return render(request, 'product_list/cart.html', {'order': order})

@login_required(login_url='/login/')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    messages.success(request, 'Product added to cart!')
    return redirect('product_list')


def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact_message = form.save()

            # Optional: Send notification based on urgency
            if contact_message.urgency in ['high', 'emergency']:
                # Here you could implement:
                # 1. Email notifications
                # 2. SMS alerts
                # 3. Push notifications
                # 4. Slack/Discord webhook notifications
                send_urgent_alert(contact_message)

            messages.success(request, 'Your message has been sent successfully. We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {'form': form})

def send_urgent_alert(contact_message):
    """
    Send urgent alerts via multiple channels
    This is a placeholder - implement your preferred notification methods
    """
    # Email notification
    send_email_notification(contact_message)

    # SMS notification (optional)
    send_sms_notification(contact_message)

    # Slack/Discord webhook (optional)
    send_webhook_notification(contact_message)

def send_email_notification(contact_message):
    from django.core.mail import send_mail

    send_mail(
        f'Urgent Message: {contact_message.subject}',
        f'''
        Urgent Message Received:
        From: {contact_message.full_name}
        Email: {contact_message.email}
        Phone: {contact_message.phone_number or 'Not provided'}
        Urgency: {contact_message.get_urgency_display()}

        Message:
        {contact_message.message}
        ''',
        'your_app_email@example.com',
        ['respondent_team@example.com'],
        fail_silently=False,
    )

    from .forms import ContactMessageForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        # Manually create ContactMessage instance
        contact_message = ContactMessage(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
            urgency=request.POST.get('urgency'),
            latitude=request.POST.get('latitude'),
            longitude=request.POST.get('longitude')
        )
        contact_message.save()
        
        # Add success message
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'contact.html')

from .forms import EmergencyAlertForm

def emergency_alert(request):
    if request.method == 'POST':
        form = EmergencyAlertForm(request.POST)
        if form.is_valid():
            alert = form.save()
            # TODO: Implement notification system to emergency services
            messages.success(
                request, 
                'Emergency alert sent! Help is on the way.'
            )
            return redirect('emergency_alert')
    else:
        form = EmergencyAlertForm()
    
    return render(request, 'emergency_alert.html', {'form': form})
