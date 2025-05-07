"""
Tests for models.
"""
from core import models
from django.test import TestCase
from decimal import Decimal
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
  """test models."""
  def test_create_user_with_email_successful(self):
    """Test creating a user with email is successful"""
    email='test@example.com'
    password='testpass123'
    user=get_user_model().objects.create_user(email=email,password=password,)

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

  def test_new_user_email_normalized(self):
    """test email is normalized for new users."""
    sample_emails=[
      ['test1@EXAMPLE.com','test1@example.com'],
      ['Test2@Example.com','Test2@example.com'],
      ['TEST3@EXAMPLE.COM','TEST3@example.com'],
      ['test4@example.COM','test4@example.com'],
    ]
    for email,expected in sample_emails:
      user= get_user_model().objects.create_user(email,'sample123')
      self.assertEqual(user.email,expected)

  def test_new_user_without_email_raises_error(self):
    """test that creating a user without email raises a valueError"""
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user('','test123')

  def test_create_superuser(self):
    """Testing a superuser."""
    user = get_user_model().objects.create_superuser(
      'test@example.com',
      'test@123',
    )

    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)

  def test_create_recipe(self):
    """test creating a recipie is successful"""
    user=get_user_model().objects.create_user('test@example.com','testpass123',)
    recipie=models.Recipie.objects.create(
      user=user,
      title='sample recipie name',
      time_minutes=5,
      price=Decimal('5.50'),
      description='sample recipie description'
    )
    self.assertEqual(str(recipie),recipie.title)