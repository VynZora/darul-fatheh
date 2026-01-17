from django import forms
from .models import (
    
    Category,
    GalleryImage,
    DonationDetails,
)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class GalleryImageForm(forms.ModelForm):  # no need
    class Meta:
        model = GalleryImage
        fields = ["category", "title", "image"]



class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationDetails
        fields = ['donor_name', 'email', 'phone', 'amount', 'payment_method', 'transaction_id', 'message']
        widgets = {
            'donor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount Donated'}),
            'payment_method': forms.Select(choices=[
                ('bank_transfer', 'Bank Transfer'), 
                ('upi', 'UPI / GPay / PhonePe'), 
                ('cash', 'Cash / Direct')
            ], attrs={'class': 'form-control'}),
            'transaction_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Transaction ID / Reference No'}),
            # 'purpose': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Purpose (e.g., Donations / General)'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any additional notes...(optional)'}),
        }