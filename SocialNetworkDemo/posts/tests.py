from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from posts.models import Post
from posts.services import PostsServices


class PostsServiceTestCase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(
            username='test_user',
            password='test_password',
        )
        post = Post.objects.create(
            text='test post',
            user=user,
            photo=SimpleUploadedFile(
                name='test_image.jpg',
                content=open('media/test/ava.jpg', 'rb').read(),
            )
        )
        self.user = user
        self.post = post
        self.post_services = PostsServices()

    def test_add_post(self):
        post_data = {
            'text': self.post.text,
            'photo': self.post.photo
        }
        post = self.post_services.add_post(post_data=post_data, user=self.user)
        self.assertEqual(post.text, self.post.text)
        self.assertEqual(post.user, self.post.user)
        self.assertEqual(post.photo, self.post.photo)

    def test_get_post(self):
        post = self.post_services.get_post(post_id=self.post.id)
        self.assertEqual(self.post, post)

