from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Post

class PublicacionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Post.objects.create(author = author, title = 'Titulo publicacionn',
                                   text = 'Texto de prueba de la publicación')
        pass


    def test_titulo_label(self):
        publicacion=Post.objects.get(id=1)
        field_label = publicacion._meta.get_field('texto').verbose_name
        self.assertEquals(field_label,'texto')

    def test_titulo_max_length(self):
        publicacion=Post.objects.get(id=1)
        max_length = Post._meta.get_field('titulo').max_length
        self.assertEquals(max_length,100)

    def test_fecha_creacion_label (self):
        publicacion = Publicacion.objects.get(id=1)
        field_label = publicacion._meta.get_field('fecha_creacion').verbose_name
        self.assertEquals(field_label,'Creado')
