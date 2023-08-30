from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.views import ObtainJSONWebToken
# from .serializers import CustomJWTSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EmailVerification
from .serializers import VerificationCodeSerializer, VerifyCodeSerializer
import random

def generate_verification_code():
    # Generate a 6-digit random verification code
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

@api_view(['POST'])
def send_verification_code(request):
    serializer = VerificationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']

    verification_code = generate_verification_code()  # Implement this function

    EmailVerification.objects.create(email=email, verification_code=verification_code)

    send_mail(
        'FreeMoney Verification Code',
        f'Your FreeMoney verification code is: {verification_code}',
        'support@httpfreemoney.com',  # Replace with your sending email
        [email],
        fail_silently=False,
    )

    return Response({'message': 'Verification code sent'})

@api_view(['POST'])
def verify_verification_code(request):
    serializer = VerifyCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']

    verification_obj = EmailVerification.objects.get(email=email)
    verification_obj.verified = True
    verification_obj.save()

    return Response({'message': 'Email verified'})

# class CustomObtainJSONWebToken(ObtainJSONWebToken):
#     serializer_class = CustomJWTSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })