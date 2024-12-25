from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Post  # Adjust this import based on your project structure

class PostAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Obtain JWT token for this user
        url = reverse('token_obtain_pair')  # URL to obtain token
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, HTTP_200_OK)
        
        # Set the token in the Authorization header for subsequent requests
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_post(self):
        url = reverse('post-list')  # Assumes the viewset route is named `post-list`
        data = {'title': 'Test Post', 'content': 'Test Content'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_get_post(self):
        # Create a post to retrieve
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        url = reverse('post-detail', args=[post.id])  # Assumes the viewset route is named `post-detail`
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['title'], post.title)
        self.assertEqual(response.data['content'], post.content)

    def test_update_post(self):
        # Create a post to update
        post = Post.objects.create(title='Old Title', content='Old Content', author=self.user)
        url = reverse('post-detail', args=[post.id])
        data = {'title': 'Updated Title', 'content': 'Updated Content'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        
        # Refresh from the database to check updates
        post.refresh_from_db()
        self.assertEqual(post.title, 'Updated Title')
        self.assertEqual(post.content, 'Updated Content')

    def test_delete_post(self):
        # Create a post to delete
        post = Post.objects.create(title='Title to Delete', content='Content to Delete', author=self.user)
        url = reverse('post-detail', args=[post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=post.id).exists())

    def test_unauthorized_access(self):
        # Remove credentials to simulate unauthorized access
        self.client.credentials()  # Clear the authorization header
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)