from django import forms

class ClienteForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50, required=True)
    fechadenacimiento= forms.DateField(label="Fecha de Nacimiento", required=True)
    email= forms.EmailField(label="e-mail", required=True)

class VendedorForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50, required=True)
    telefono= forms.IntegerField(label="Teléfono", required=True)
    email= forms.EmailField(label="e-mail", required=True)
    rfc=forms.CharField(label="RFC", max_length=13, required=True)

class SocioForm(forms.Form):
    empresa= forms.CharField(label="Nombre de la empresa", max_length=50, required=True)
    paisdeorigen= forms.CharField(label="País de Origen", max_length=50, required=True)

class CatalogoForm(forms.Form):
    articulo= forms.CharField(label="Nombre del artículo", max_length=50, required=True)
    cantidad= forms.IntegerField(label="Cantidad", max_value=99, required=True)
    categoria= forms.CharField(label="Categoría", max_length=50, required=True)
