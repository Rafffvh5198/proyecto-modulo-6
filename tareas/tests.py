from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Proyecto

class ProyectoTest(TestCase):

    def setUp(self):
        # crear usuario
        self.user = User.objects.create_user(username='test', password='1234')
        
        # login
        self.client.login(username='test', password='1234')

        # crear proyecto
        self.proyecto = Proyecto.objects.create(
            nombre='Proyecto Test',
            usuario=self.user
        )

    def test_ver_proyectos(self):
        response = self.client.get(reverse('proyectos'))
        self.assertEqual(response.status_code, 200)

    def test_crear_proyecto(self):
        response = self.client.post(reverse('crear_proyecto'), {
            'nombre': 'Nuevo Proyecto',
            'descripcion': 'Texto'
        })
        self.assertEqual(Proyecto.objects.count(), 2)

    def test_eliminar_proyecto(self):
        response = self.client.post(
            reverse('eliminar_proyecto', args=[self.proyecto.id])
        )
        self.assertEqual(Proyecto.objects.count(), 0)
# Create your tests here.
