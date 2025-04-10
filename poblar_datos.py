from biblioteca.models import Autor, Libro, Resena
import datetime

# Borrar datos existentes (opcional, para evitar duplicados)
Autor.objects.all().delete()
Libro.objects.all().delete()
Resena.objects.all().delete()

# Crear autores
autor1 = Autor.objects.create(nombre="Gabriel García Márquez", nacionalidad="Colombiana")
autor2 = Autor.objects.create(nombre="Isabel Allende", nacionalidad="Chilena")

# Crear libros
libro1 = Libro.objects.create(
    titulo="Cien años de soledad",
    autor=autor1,
    fecha_publicacion=datetime.date(1967, 6, 5),
    resumen="Novela emblemática del realismo mágico, que narra la historia de la familia Buendía durante varias generaciones."
)
libro2 = Libro.objects.create(
    titulo="El amor en los tiempos del cólera",
    autor=autor1,
    fecha_publicacion=datetime.date(1985, 9, 5),
    resumen="Una historia de amor que se desarrolla durante más de medio siglo en el Caribe."
)
libro3 = Libro.objects.create(
    titulo="La casa de los espíritus",
    autor=autor2,
    fecha_publicacion=datetime.date(1982, 1, 1),
    resumen="Una saga familiar que mezcla elementos del realismo mágico y la política latinoamericana."
)

# Crear reseñas
Resena.objects.create(libro=libro1, texto="Una obra maestra de la literatura universal.", calificacion=5)
Resena.objects.create(libro=libro2, texto="Una historia de amor profundamente conmovedora.", calificacion=4)
Resena.objects.create(libro=libro3, texto="Una novela rica en simbolismo y emociones.", calificacion=5)

print("Datos poblados exitosamente.")
