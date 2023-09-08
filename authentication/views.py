from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EmailVerification
from .serializers import VerificationCodeSerializer
import random
import smtplib
from email.mime.text import MIMEText

def generate_verification_code():
    # Generate a 6-digit random verification code
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])


@api_view(['GET', 'POST'])
def email_verification(request):
    if request.method == 'POST':
        # Create a new EmailVerification record and send a verification code
        serializer = VerificationCodeSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            verification_code = generate_verification_code()
            
            # Save the verification code in the database
            email_verification, created = EmailVerification.objects.get_or_create(email=email)
            email_verification.verification_code = verification_code
            email_verification.save()

            # Send the verification email
            email = EmailMessage(
                subject='FreeMoney Verification Code',
                 body= f'Your FreeMoney verification code is: {verification_code}',
                 from_email ='support@httpfreemoney.com',
                to=[email],
                headers={'Content-Type': 'text/plain'},
            )
            email.send()
            send_mail(
                'FreeMoney Verification Code',
                f'Your FreeMoney verification code is: {verification_code}',
                'support@httpfreemoney.com',
                [email],
                fail_silently=False,
            )
            sender = 'support@httpfreemoney.com'
            recipient = email

            msg = MIMEText("Your FreeMoney verification code is: {verification_code}")
            msg['Subject'] = "Testing MIME Text"
            msg['From'] = sender
            msg['To'] = recipient

            # Create server object with SSL option
            server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

            # Perform operations via server
            server.login('support@httpfreemoney.com', 'abdou0792A*')
            server.sendmail(sender, [recipient], msg.as_string())
            server.quit()

            return Response({'message': 'Verification code sent'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        # Check if the provided verification code is correct
        email = request.query_params.get('email')
        verification_code = request.query_params.get('verification_code')

        try:
            email_verification = EmailVerification.objects.get(email=email)

            if email_verification.verification_code == verification_code:
                # Mark the email as verified
                email_verification.verified = True
                email_verification.save()
                return Response({'message': 'Email verified'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)
        except EmailVerification.DoesNotExist:
            return Response({'error': 'Email not found'}, status=status.HTTP_400_BAD_REQUEST)


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